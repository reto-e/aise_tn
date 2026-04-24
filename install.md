# Tool Installation Guide

This guide walks you through installing the required tools for this AI training class. All steps are designed to run inside a **GitHub Codespace**.

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

## Troubleshooting

| Problem | Fix |
|---|---|
| `ollama: command not found` | Re-run the install script or open a new terminal to reload `PATH` |
| `Error: could not connect to ollama app` | Run `ollama serve &` first, then retry |
| Download fails or is very slow | Check Codespace disk quota with `df -h`; free space if needed |
