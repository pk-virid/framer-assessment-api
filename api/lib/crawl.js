const MAX_PAGES = 18;
const FETCH_TIMEOUT_MS = 12000;
const MAX_HTML_CHARS = 14000;

function isProbablyFramer(html, finalUrl) {
  const hay = `${finalUrl}\n${html}`.toLowerCase();
  return (
    hay.includes("framerusercontent.com") ||
    hay.includes("framer.com") ||
    hay.includes("framer-website") ||
    hay.includes("__framer") ||
    /\.framer\.(website|app|wiki)/.test(hay)
  );
}

async function fetchText(url) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
  try {
    const res = await fetch(url, {
      redirect: "follow",
      signal: controller.signal,
      headers: {
        "user-agent":
          "FramerTemplateReviewer/1.0 (+https://github.com/pk-virid/framer-assessment-api)",
        accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      },
    });
    const text = await res.text();
    return {
      ok: res.ok,
      status: res.status,
      url: res.url || url,
      text,
      contentType: res.headers.get("content-type") || "",
    };
  } finally {
    clearTimeout(timer);
  }
}

function extractLinks(html, baseUrl) {
  const links = new Set();
  const re = /href\s*=\s*["']([^"']+)["']/gi;
  let m;
  while ((m = re.exec(html))) {
    const raw = m[1].trim();
    if (!raw || raw.startsWith("#") || raw.startsWith("mailto:") || raw.startsWith("tel:") || raw.startsWith("javascript:")) {
      continue;
    }
    try {
      const abs = new URL(raw, baseUrl);
      if (abs.origin === new URL(baseUrl).origin) {
        abs.hash = "";
        links.add(abs.toString());
      }
    } catch {
      // ignore invalid
    }
  }
  return [...links];
}

function extractSitemapLocs(xml) {
  const locs = [];
  const re = /<loc>\s*([^<\s]+)\s*<\/loc>/gi;
  let m;
  while ((m = re.exec(xml))) locs.push(m[1].trim());
  return locs;
}

function summarizePage(html, pageUrl) {
  const title = (html.match(/<title[^>]*>([\s\S]*?)<\/title>/i) || [,""])[1]
    .replace(/\s+/g, " ")
    .trim();
  const metaDesc = (
    html.match(
      /<meta[^>]+name=["']description["'][^>]+content=["']([^"']*)["'][^>]*>/i
    ) ||
    html.match(
      /<meta[^>]+content=["']([^"']*)["'][^>]+name=["']description["'][^>]*>/i
    ) || [,""]
  )[1];
  const ogTitle = (
    html.match(
      /<meta[^>]+property=["']og:title["'][^>]+content=["']([^"']*)["']/i
    ) || [,""]
  )[1];
  const hasViewport = /name=["']viewport["']/i.test(html);
  const htmlLang = (html.match(/<html[^>]+lang=["']([^"']+)["']/i) || [,""])[1];
  const h1s = [...html.matchAll(/<h1[^>]*>([\s\S]*?)<\/h1>/gi)].map((x) =>
    x[1].replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim()
  );
  const imgs = [...html.matchAll(/<img[^>]+>/gi)].slice(0, 40).map((tag) => {
    const t = tag[0];
    const src = (t.match(/src=["']([^"']+)["']/i) || [,""])[1];
    const alt = (t.match(/alt=["']([^"']*)["']/i) || [, null])[1];
    const width = (t.match(/\bwidth=["']?(\d+)/i) || [,""])[1];
    const height = (t.match(/\bheight=["']?(\d+)/i) || [,""])[1];
    return { src, alt, width, height };
  });
  const text = html
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, MAX_HTML_CHARS);

  const placeholderHits = [];
  const patterns = [
    /lorem ipsum/gi,
    /your text here/gi,
    /click to edit/gi,
    /add any disclaimer/gi,
    /placeholder/gi,
    /here is a short chat message/gi,
    /\[insert[^\]]*\]/gi,
  ];
  for (const p of patterns) {
    const found = text.match(p);
    if (found) placeholderHits.push(...found.slice(0, 3));
  }

  return {
    url: pageUrl,
    title,
    metaDescription: metaDesc,
    ogTitle,
    hasViewport,
    htmlLang,
    h1s,
    imageCount: imgs.length,
    imagesMissingAlt: imgs.filter((i) => i.alt === null || i.alt === "").length,
    imagesSample: imgs.slice(0, 8),
    placeholderHits: [...new Set(placeholderHits)].slice(0, 10),
    textExcerpt: text,
  };
}

async function crawlTemplate(templateUrl) {
  const start = await fetchText(templateUrl);
  if (!start.ok && start.status >= 400) {
    throw new Error(`Failed to fetch template URL (${start.status})`);
  }

  const base = start.url;
  const framer = isProbablyFramer(start.text, base);

  let sitemapUrls = [];
  let robots = "";
  try {
    const sm = await fetchText(new URL("/sitemap.xml", base).toString());
    if (sm.ok) sitemapUrls = extractSitemapLocs(sm.text);
  } catch {
    // optional
  }
  try {
    const rb = await fetchText(new URL("/robots.txt", base).toString());
    if (rb.ok) robots = rb.text.slice(0, 2000);
  } catch {
    // optional
  }

  const discovered = new Set([base, ...extractLinks(start.text, base), ...sitemapUrls]);
  const priorityPaths = [
    "/",
    "/about",
    "/contact",
    "/pricing",
    "/blog",
    "/privacy",
    "/terms",
    "/terms-of-service",
    "/privacy-policy",
    "/instructions",
    "/getting-started",
    "/style-guide",
    "/licenses",
    "/changelog",
    "/404",
  ];
  for (const path of priorityPaths) {
    discovered.add(new URL(path, base).toString());
  }

  const queue = [...discovered];
  const pages = [];
  const seen = new Set();

  for (const url of queue) {
    if (pages.length >= MAX_PAGES) break;
    const key = url.replace(/\/$/, "") || url;
    if (seen.has(key)) continue;
    seen.add(key);
    try {
      const res = await fetchText(url);
      if (!res.ok || !/text\/html|application\/xhtml/i.test(res.contentType || "text/html")) {
        if (!res.ok) continue;
      }
      pages.push(summarizePage(res.text, res.url));
      for (const link of extractLinks(res.text, res.url)) {
        if (!seen.has(link.replace(/\/$/, ""))) queue.push(link);
      }
    } catch {
      // skip failed page
    }
  }

  return {
    startUrl: templateUrl,
    finalUrl: base,
    isFramer: framer,
    sitemapUrlCount: sitemapUrls.length,
    robots,
    pages,
  };
}

module.exports = { crawlTemplate, isProbablyFramer };
