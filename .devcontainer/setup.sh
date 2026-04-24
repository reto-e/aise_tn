#!/usr/bin/env bash
set -e

echo "==> Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

echo "==> Installing OpenCode..."
curl -fsSL https://opencode.ai/install | bash

echo "==> Installing Pi coding agent..."
npm install -g @mariozechner/pi-coding-agent

echo "==> Pulling gemma4:e2b model..."
OLLAMA_NUM_CTX=65536 ollama serve &
OLLAMA_PID=$!
# Wait for the server to be ready
until ollama list > /dev/null 2>&1; do sleep 1; done
ollama pull gemma4:e2b
kill $OLLAMA_PID

echo "==> Setup complete."
