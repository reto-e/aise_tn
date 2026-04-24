#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "$SCRIPT_DIR/setup_ollama.sh"
bash "$SCRIPT_DIR/setup_opencode.sh"
bash "$SCRIPT_DIR/setup_pi.sh"

echo "==> Setup complete."
