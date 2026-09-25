FROM mcr.microsoft.com/devcontainers/javascript-node:22

ARG OPENCODE_VERSION=2.0.6
# Shared location for Playwright browsers, so they're usable by the non-root user
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# --- OpenCode -------------------------------------------------------------
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "$arch" in \
      amd64) oc_arch="x64" ;; \
      arm64) oc_arch="arm64" ;; \
      *) echo "Unsupported architecture: $arch"; exit 1 ;; \
    esac; \
    mkdir -p /tmp/opencode; \
    curl -fsSL "https://opencode.ai/files/bin/${OPENCODE_VERSION}/opencode-linux-${oc_arch}.tar.gz" \
      | tar -xz -C /tmp/opencode; \
    install -m 0755 "$(find /tmp/opencode -type f -name opencode | head -n1)" /usr/local/bin/opencode; \
    rm -rf /tmp/opencode; \
    opencode --version

# --- Atlassian CLI (acli) ---------------------------------------------------
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends wget gnupg2; \
    mkdir -p -m 755 /etc/apt/keyrings; \
    wget -nv -O- https://acli.atlassian.com/gpg/public-key.asc \
      | gpg --dearmor -o /etc/apt/keyrings/acli-archive-keyring.gpg; \
    chmod go+r /etc/apt/keyrings/acli-archive-keyring.gpg; \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/acli-archive-keyring.gpg] https://acli.atlassian.com/linux/deb stable main" \
      > /etc/apt/sources.list.d/acli.list; \
    apt-get update; \
    apt-get install -y acli; \
    rm -rf /var/lib/apt/lists/*

# --- Playwright CLI + browser ----------------------------------------------
RUN set -eux; \
    npm install -g @playwright/cli@latest; \
    playwright-cli install-browser --with-deps; \
    if [ -d /ms-playwright ]; then chmod -R a+rX /ms-playwright; fi; \
    rm -rf /var/lib/apt/lists/*