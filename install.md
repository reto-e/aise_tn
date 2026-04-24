# Setup Guide

This guide walks you through setting up your environment for this AI training class using **GitHub Codespaces** — no local installation required.

---

## Step 1: Open the repo in a Codespace

1. Go to [https://github.com/reto-e/aise_tn](https://github.com/reto-e/aise_tn)
2. Log in with your GitHub account (create a free account at [github.com](https://github.com) if you don't have one)
3. Click the green **Code** button
4. Select the **Codespaces** tab
5. Click **Create codespace on main**

GitHub will provision a cloud-based development environment and open it in your browser.

---

## Step 2: Run the setup script

Once the Codespace has loaded, open the terminal and run:

```bash
chmod +x setup.sh
./setup.sh
```

The script will automatically install and configure the following tools (skipping anything already installed):

- **Ollama** — local LLM runtime
- **OpenCode** — terminal-based AI coding assistant
- **Pi** — terminal coding agent ([pi.dev](https://pi.dev))
- **gemma4:e2b** model — pulled and ready to use via Ollama with a 64K token context window

The setup may take a few minutes, mainly due to the model download.

---

## Step 3: Configure OpenCode

Start OpenCode in the terminal:

```bash
opencode
```

### Select the Big Pickle model

Big Pickle is OpenCode's stealth model, currently available for free. Inside OpenCode, type:

```
/models
```

Search for `big-pickle` and select it. Alternatively, set it as the default in your `opencode.json` config:

```json
{
  "model": "opencode/big-pickle"
}
```

> Big Pickle is a free preview model. Usage data may be collected for model improvement.

---

## Step 4: Configure Pi with Ollama

Pi needs to be told to use Ollama as its model provider. Create or edit `~/.pi/agent/models.json`:

```bash
mkdir -p ~/.pi/agent
nano ~/.pi/agent/models.json
```

Paste the following content:

```json
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
```

Save the file, then make sure Ollama is running:

```bash
OLLAMA_NUM_CTX=65536 ollama serve &
```

Start Pi and select the model with `/model`:

```bash
pi
```

> The `models.json` file reloads automatically, so you can edit it without restarting Pi.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `Permission denied` when running `./setup.sh` | Run `chmod +x setup.sh` first |
| `ollama: command not found` after install | Open a new terminal to reload `PATH`, then re-run `./setup.sh` |
| `opencode: command not found` after install | Open a new terminal to reload `PATH` |
| Model download fails or is very slow | Check disk quota with `df -h`; re-run `./setup.sh` to resume |

## Links

https://aise-fhnw.atlassian.net/jira/software/projects/KAN/list
