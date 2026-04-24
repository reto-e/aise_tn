# Tool Installation Guide

This guide walks you through setting up your environment for this AI training class using **GitHub Codespaces** — no local installation required.

---

## Step 1: Open the repo in a Codespace

1. Go to [https://github.com/reto-e/aise_tn](https://github.com/reto-e/aise_tn)
2. Log in with your GitHub account (create a free account at [github.com](https://github.com) if you don't have one)
3. Click the green **Code** button
4. Select the **Codespaces** tab
5. Click **Create codespace on main**

GitHub will provision a cloud-based development environment and open it in your browser. All subsequent steps are run inside this Codespace.

---

## Ollama

Ollama lets you run large language models locally (or in your Codespace).

### Install Ollama

Run the official install script in your Codespace terminal:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the installation:

```bash
ollama --version
```

### Start the Ollama server

Ollama needs its background service running before you can pull or use models:

```bash
OLLAMA_NUM_CTX=65536 ollama serve &
```

> The `&` runs it in the background. You can also open a second terminal and run `ollama serve` there without `&`.

### Pull the Gemma 4 model

Once the server is running, download the `gemma3:4b` model (the instruction-tuned 4-billion-parameter variant):

```bash
ollama pull gemma3:4b
```

> This download is several gigabytes. GitHub Codespaces has sufficient disk space, but it may take a few minutes depending on network speed.

### Verify the model works

Run a quick test prompt:

```bash
ollama run gemma3:4b "Hello, who are you?"
```

Type `/bye` to exit the interactive session.

---

## OpenCode

OpenCode is a terminal-based AI coding assistant.

### Install OpenCode

```bash
curl -fsSL https://opencode.ai/install | bash
```

Verify the installation:

```bash
opencode --version
```

---

## Pi (picode)

Pi is a terminal coding agent by pi.dev.

### Install Pi

Node.js is pre-installed in GitHub Codespaces, so you can install Pi directly via npm:

```bash
npm install -g @mariozechner/pi-coding-agent
```

Verify the installation:

```bash
pi --version
```

---

