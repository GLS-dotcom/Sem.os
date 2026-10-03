# SEM FIM OS v3 — Lucky Universal AI

Versão 100% navegador do SEM FIM OS. Não requer Node.js, npm ou instalação de dependências.

## Lucky Universal AI

A Lucky agora usa uma arquitetura de **adaptadores de API**. A interface suporta:

- OpenRouter
- OpenAI
- Groq
- Google Gemini via endpoint OpenAI-compatible
- DeepSeek
- xAI / Grok
- Mistral
- Anthropic (Messages API)
- qualquer outro endpoint OpenAI-compatible
- qualquer endpoint compatível com o formato de mensagens da Anthropic

### Configuração

Abra a Lucky → ⚙ → escolha o provedor → informe a API key → endpoint → modelo → `Salvar e testar`.

Para provedores OpenAI-compatible, `Carregar modelos` tenta consultar `<endpoint-base>/models`.

## Importante sobre "qualquer API"

Não existe um formato universal que torne literalmente toda API de IA intercambiável. Alguns provedores usam formatos e autenticação diferentes. Por isso o SEM FIM OS usa adaptadores. APIs novas que adotem um dos protocolos suportados podem ser configuradas sem alterar o código.

Se uma API bloquear chamadas diretas do navegador por CORS, o projeto não consegue contornar isso sem um proxy/backend/serverless. O erro é informado pela Lucky.

## Segurança

A chave fica apenas em `sessionStorage` nesta versão. Isso evita gravá-la permanentemente no código do projeto, mas **não a torna secreta**: uma aplicação 100% navegador sempre expõe a chave ao ambiente do cliente. Não publique uma chave pessoal compartilhada no ZIP.
