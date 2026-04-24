#!/usr/bin/env bash
set -e

echo "==> Checking if Ollama is installed..."
if ! command -v ollama &> /dev/null; then
    echo "==> Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "==> Ollama already installed."
fi

echo "==> Checking if OpenCode is installed..."
if ! command -v opencode &> /dev/null; then
    echo "==> Installing OpenCode..."
    curl -fsSL https://opencode.ai/install | bash || echo "==> OpenCode installation failed, continuing..."
else
    echo "==> OpenCode already installed."
fi

echo "==> Checking if Pi coding agent is installed..."
if ! command -v pi &> /dev/null; then
    echo "==> Installing Pi coding agent..."
    npm install -g @mariozechner/pi-coding-agent
else
    echo "==> Pi coding agent already installed."
fi

echo "==> Checking if gemma4:e2b model is pulled..."
if ! ollama list | grep -q "gemma4:e2b"; then
    echo "==> Pulling gemma4:e2b model..."
    OLLAMA_NUM_CTX=65536 ollama serve &
    OLLAMA_PID=$!
    # Wait for the server to be ready
    until ollama list > /dev/null 2>&1; do sleep 1; done
    ollama pull gemma4:e2b
    kill $OLLAMA_PID
else
    echo "==> gemma4:e2b model already pulled."
fi

echo "==> Setup complete."