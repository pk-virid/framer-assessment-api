const Anthropic = require("@anthropic-ai/sdk");

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

module.exports = async (req, res) => {
  // CORS
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

  if (req.method === "OPTIONS") {
    res.status(200).end();
    return;
  }

  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  try {
    const { templateUrl } = req.body;

    if (!templateUrl) {
      return res.status(400).json({ error: "Missing templateUrl" });
    }

    const prompt = `You are a Framer marketplace expert. Quickly assess this template:

URL: ${templateUrl}

Check these 5 critical items:
1. No placeholder text (Lorem ipsum, "Click to edit")? PASS/FAIL
2. Has Home, Terms, Privacy pages? PASS/FAIL
3. All links working? PASS/FAIL
4. Mobile responsive? PASS/FAIL
5. No major accessibility issues? PASS/FAIL

Respond with ONLY this JSON (no other text):
{
  "overallScore": 0-100,
  "grade": "A/B/C/D/F",
  "readyForMarketplace": true/false,
  "summary": "One sentence summary",
  "checks": {
    "placeholderContent": { "status": "PASS/FAIL", "issues": [] },
    "requiredPages": { "status": "PASS/FAIL", "issues": [] },
    "workingLinks": { "status": "PASS/FAIL", "issues": [] },
    "mobileResponsive": { "status": "PASS/FAIL", "issues": [] },
    "accessibility": { "status": "PASS/FAIL", "issues": [] }
  },
  "recommendations": ["rec1", "rec2"]
}`;

    const response = await client.messages.create({
      model: "claude-opus-4-20250805",
      max_tokens: 1000,
      messages: [
        {
          role: "user",
          content: prompt,
        },
      ],
    });

    const text = response.content[0].text;
    const jsonMatch = text.match(/\{[\s\S]*\}/);

    if (!jsonMatch) {
      return res.status(500).json({ error: "Invalid response format" });
    }

    const result = JSON.parse(jsonMatch[0]);
    res.status(200).json(result);
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: "Assessment failed",
      message: error.message,
    });
  }
};
