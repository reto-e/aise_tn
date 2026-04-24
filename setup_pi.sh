#!/usr/bin/env bash
set -e

echo "==> Checking if Pi coding agent is installed..."
if ! command -v pi &> /dev/null; then
    echo "==> Installing Pi coding agent..."
    npm install -g @mariozechner/pi-coding-agent
else
    echo "==> Pi coding agent already installed."
fi

echo "==> Configuring Pi coding agent with Ollama..."
mkdir -p ~/.pi/agent
cat > ~/.pi/agent/models.json << 'EOF'
{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [
        { "id": "gemma4:e2b" }
      ],
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false
      }
    }
  }
}
EOF

echo "==> Pi setup complete."
