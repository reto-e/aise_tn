# AISE Setup Guide


## Step 1: Open the repo in a Codespace

1. Go to [https://github.com/reto-e/aise_tn](https://github.com/reto-e/aise_tn)
2. Log in with your GitHub account (create a free account at [github.com](https://github.com) if you don't have one)
3. Click the green **Code** button
4. Select the **Codespaces** tab
5. Click **Create codespace on main**

GitHub will provision a cloud-based development environment and open it in your browser.


## OpenCode

OpenCode is a terminal-based AI coding assistant.

### Install

```bash
curl -fsSL https://opencode.ai/install | bash
```

Open a new terminal after installation to reload `PATH`, then start it with:

```bash
opencode
```

### Select a model

Inside OpenCode, type `/connect` to add a provider. Select **GitHub (Public)** as the provider, then choose the **Claude Haiku** model. Or set it as the default in your `opencode.json`:

```json
{
  "model": "github/claude-haiku"
}
```

---

## Playwright CLI

Playwright CLI is a browser automation tool used for AI-assisted web interactions.

### Install

1. Install the Playwright CLI globally:

   ```bash
   npm install -g @playwright/cli
   ```

2. Install the Chromium browser:

   ```bash
   npx playwright install chromium
   ```
