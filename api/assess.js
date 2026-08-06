const Anthropic = require("@anthropic-ai/sdk");
const { crawlTemplate } = require("./lib/crawl");
const { SYSTEM_PROMPT } = require("./lib/reviewPrompt");

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

function setCors(res) {
  res.setHeader("Access-Control-Allow-Credentials", "true");
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET,OPTIONS,PATCH,DELETE,POST,PUT"
  );
  res.setHeader(
    "Access-Control-Allow-Headers",
    "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version"
  );
}

function extractJson(text) {
  const fenced = text.match(/```(?:json)?\s*([\s\S]*?)```/i);
  const raw = fenced ? fenced[1] : text;
  const match = raw.match(/\{[\s\S]*\}/);
  if (!match) throw new Error("Invalid response format");
  return JSON.parse(match[0]);
}

module.exports = async (req, res) => {
  setCors(res);

  if (req.method === "OPTIONS") {
    res.status(200).end();
    return;
  }

  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  try {
    const { templateUrl, strictStudioGate } = req.body || {};

    if (!templateUrl) {
      return res.status(400).json({ error: "Missing templateUrl" });
    }

    if (!process.env.ANTHROPIC_API_KEY) {
      return res.status(500).json({ error: "ANTHROPIC_API_KEY is not configured" });
    }

    const crawl = await crawlTemplate(templateUrl);

    if (!crawl.isFramer) {
      return res.status(200).json({
        url: templateUrl,
        isFramer: false,
        marketplaceReady: false,
        studioShipReady: false,
        status: "NOT_READY",
        overallScore: 0,
        grade: "F",
        summary:
          "This URL does not appear to be a Framer-hosted site. Provide a published Framer preview (*.framer.website / *.framer.app) or a Framer custom domain.",
        pagesCrawled: crawl.pages.length,
        priorityFixes: [
          {
            severity: "CRITICAL",
            title: "Not a Framer site",
            pages: [templateUrl],
            detail: "Re-run against a published Framer template preview URL.",
          },
        ],
        recommendations: [],
      });
    }

    const userPayload = {
      templateUrl,
      finalUrl: crawl.finalUrl,
      sitemapUrlCount: crawl.sitemapUrlCount,
      robotsTxt: crawl.robots,
      pagesCrawled: crawl.pages.length,
      pages: crawl.pages,
      strictStudioGate: Boolean(strictStudioGate),
      note: "Score only from evidence in pages[]. Mark missing signals UNVERIFIABLE.",
    };

    const response = await client.messages.create({
      model: process.env.ANTHROPIC_MODEL || "claude-opus-4-20250805",
      max_tokens: 4500,
      system: SYSTEM_PROMPT,
      messages: [
        {
          role: "user",
          content: `Audit this crawled Framer template and return JSON only.\n\n${JSON.stringify(
            userPayload
          )}`,
        },
      ],
    });

    const text = response.content[0].text;
    const result = extractJson(text);

    result.url = result.url || crawl.finalUrl;
    result.pagesCrawled = result.pagesCrawled || crawl.pages.length;
    result.isFramer = true;
    result.crawledAt = new Date().toISOString();

    if (strictStudioGate && result.studioShipReady !== true) {
      result.status = result.status || "NOT_READY";
    }

    res.status(200).json(result);
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: "Assessment failed",
      message: error.message,
    });
  }
};
