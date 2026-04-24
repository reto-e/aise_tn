#!/usr/bin/env bash
set -e

echo "==> Checking if Playwright CLI is installed..."
if ! command -v playwright &> /dev/null; then
    echo "==> Installing Playwright CLI..."
    npm install -g @playwright/cli
else
    echo "==> Playwright CLI already installed."
fi

echo "==> Installing Chromium browser..."
npx playwright install chromium

echo "==> Installing Playwright skills..."
playwright-cli install --skills

echo "==> Playwright setup complete."
