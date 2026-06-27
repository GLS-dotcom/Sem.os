# SEM FIM OS com Lucky AI

## 1. Instalar
```bash
npm install
```

## 2. Configurar a chave
Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:
```env
PORT=3000
OPENROUTER_API_KEY=sua_chave_aqui
LUCKY_API_ENDPOINT=https://openrouter.ai/api/v1/chat/completions
LUCKY_MODEL=openrouter/auto
```

## 3. Rodar
```bash
node -r dotenv/config server.js
```

## 4. Abrir
Abra no navegador:
```txt
http://localhost:3000
```

## Arquivos de mídia
Deixe estes arquivos dentro da pasta `public`:
- lucky.png
- lucky2.png
- lucky2.mp4