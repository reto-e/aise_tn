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

## Mistral Vibe

Mistral Vibe is a CLI coding agent built by Mistral AI.

### Install

1. Install Mistral Vibe via pip:
   ```bash
   pip install mistral-vibe
   ```

2. start vibe and log in:
   ```bash
   vibe --setup
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

## Atlassion CLI

Create an API Token at https://id.atlassian.com/manage-profile/security/api-tokens

1. Install it and make it executable

   ```bash
   sudo apt-get install -y wget gnupg2
   ```
2. Setup APT repo:
   ```bash
   sudo mkdir -p -m 755 /etc/apt/keyrings
   wget -nv -O- https://acli.atlassian.com/gpg/public-key.asc | sudo gpg --dearmor -o /etc/apt/keyrings/acli-archive-keyring.gpg
   sudo chmod go+r /etc/apt/keyrings/acli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/acli-archive-keyring.gpg] https://acli.atlassian.com/linux/deb stable main" | sudo tee /etc/apt/sources.list.d/acli.list > /dev/null
   ```
3. Install ACLI

   ```bash
   sudo apt update
   sudo apt install -y acli
   ```

4. Log in 

   ```bash
   $ echo ATATT...1rko=63D0F137 | acli jira auth login --site "aise-fhnw.atlassian.net" --email "reto.eichholzer@bluewin.ch" --token

   ```