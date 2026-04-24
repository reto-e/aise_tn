#!/usr/bin/env bash
set -e

echo "==> Checking if Ollama is installed..."
if ! command -v ollama &> /dev/null; then
    echo "==> Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "==> Ollama already installed."
fi

echo "==> Checking if gemma4:e2b model is pulled..."
if ! ollama list | grep -q "gemma4:e2b"; then
    echo "==> Pulling gemma4:e2b model..."
    OLLAMA_NUM_CTX=65536 ollama serve &
    OLLAMA_PID=$!
    until ollama list > /dev/null 2>&1; do sleep 1; done
    ollama pull gemma4:e2b
    kill $OLLAMA_PID
else
    echo "==> gemma4:e2b model already pulled."
fi

echo "==> Ollama setup complete."
