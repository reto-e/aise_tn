#!/usr/bin/env bash
set -e

echo "==> Checking if OpenCode is installed..."
if ! command -v opencode &> /dev/null; then
    echo "==> Installing OpenCode..."
    curl -fsSL https://opencode.ai/install | bash || echo "==> OpenCode installation failed, continuing..."
else
    echo "==> OpenCode already installed."
fi

echo "==> OpenCode setup complete."
