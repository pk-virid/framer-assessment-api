#!/usr/bin/env node
/**
 * Local development server for the Vercel serverless functions in `api/`.
 *
 * Vercel's Node runtime augments the native request/response objects with a few
 * helpers (`req.body`, `res.status()`, `res.json()`, ...). This harness mounts
 * each `api/*.js` handler over Node's built-in HTTP server and reproduces those
 * helpers so the functions can be exercised locally exactly as they run on
 * Vercel. It exists only for local development and testing; production continues
 * to run on Vercel.
 */

const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 3000;
const HOST = process.env.HOST || "0.0.0.0";
const API_DIR = path.join(__dirname, "..", "api");

function loadRoutes() {
  const routes = new Map();
  for (const file of fs.readdirSync(API_DIR)) {
    if (!file.endsWith(".js")) continue;
    const name = file.replace(/\.js$/, "");
    // eslint-disable-next-line global-require, import/no-dynamic-require
    const handler = require(path.join(API_DIR, file));
    routes.set(`/api/${name}`, handler);
  }
  return routes;
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on("data", (chunk) => chunks.push(chunk));
    req.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
    req.on("error", reject);
  });
}

function parseBody(raw, contentType) {
  if (!raw) return undefined;
  if (contentType && contentType.includes("application/json")) {
    try {
      return JSON.parse(raw);
    } catch (err) {
      return raw;
    }
  }
  return raw;
}

function decorateResponse(res) {
  res.status = (code) => {
    res.statusCode = code;
    return res;
  };
  res.json = (payload) => {
    if (!res.getHeader("Content-Type")) {
      res.setHeader("Content-Type", "application/json; charset=utf-8");
    }
    res.end(JSON.stringify(payload));
    return res;
  };
  res.send = (payload) => {
    if (payload === undefined || payload === null) {
      res.end();
    } else if (typeof payload === "object") {
      res.json(payload);
    } else {
      res.end(String(payload));
    }
    return res;
  };
  return res;
}

const routes = loadRoutes();

const server = http.createServer(async (req, res) => {
  decorateResponse(res);

  const url = new URL(req.url, `http://${req.headers.host || "localhost"}`);
  const handler = routes.get(url.pathname);

  if (!handler) {
    res.status(404).json({
      error: "Not found",
      availableRoutes: [...routes.keys()],
    });
    return;
  }

  try {
    const raw = await readBody(req);
    req.body = parseBody(raw, req.headers["content-type"]);
    req.query = Object.fromEntries(url.searchParams.entries());
    await handler(req, res);
  } catch (err) {
    // eslint-disable-next-line no-console
    console.error("Unhandled error in handler:", err);
    if (!res.headersSent) {
      res.status(500).json({ error: "Internal server error", message: err.message });
    }
  }
});

server.listen(PORT, HOST, () => {
  // eslint-disable-next-line no-console
  console.log(`Dev server listening on http://${HOST}:${PORT}`);
  // eslint-disable-next-line no-console
  console.log(`Mounted routes: ${[...routes.keys()].join(", ")}`);
  if (!process.env.ANTHROPIC_API_KEY) {
    // eslint-disable-next-line no-console
    console.warn(
      "Warning: ANTHROPIC_API_KEY is not set. The /api/assess endpoint will fail when calling Anthropic."
    );
  }
});
