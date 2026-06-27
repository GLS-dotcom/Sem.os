const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json({ limit: "1mb" }));
app.use(express.static(path.join(__dirname, "public")));

app.post("/api/lucky", async (req, res) => {
  try {
    const apiKey = process.env.OPENROUTER_API_KEY || process.env.OPENAI_API_KEY;
    const endpoint =
      process.env.LUCKY_API_ENDPOINT ||
      "https://openrouter.ai/api/v1/chat/completions";
    const defaultModel = process.env.LUCKY_MODEL || "openrouter/auto";
    const model = (req.body && req.body.model) || defaultModel;
    const userMessage = (req.body && req.body.message || "").toString().trim();

    if (!userMessage) {
      return res.status(400).json({ error: "Mensagem vazia." });
    }

    if (!apiKey) {
      return res.status(500).json({
        error: "Configure OPENROUTER_API_KEY no arquivo .env antes de usar a Lucky."
      });
    }

    const payload = {
      model,
      messages: [
        {
          role: "system",
          content:
            "Você é Lucky, a assistente do SEM FIM OS. Responda em português, de forma amigável, curta e útil."
        },
        { role: "user", content: userMessage }
      ]
    };

    const apiRes = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${apiKey}`,
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "SEM FIM OS"
      },
      body: JSON.stringify(payload)
    });

    const data = await apiRes.json().catch(() => ({}));

    if (!apiRes.ok) {
      return res.status(apiRes.status).json({
        error: data.error?.message || data.error || "Erro ao consultar a IA."
      });
    }

    const reply = data?.choices?.[0]?.message?.content;
    if (!reply) {
      return res.status(500).json({ error: "A IA não retornou resposta." });
    }

    res.json({ reply });
  } catch (error) {
    res.status(500).json({ error: error.message || "Erro interno no servidor." });
  }
});

app.listen(PORT, () => {
  console.log(`SEM FIM OS rodando em http://localhost:${PORT}`);
});