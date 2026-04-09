#!/bin/bash

# ENOLA SEO — Installer
# by Enola Revenue — free, forever
# Usage: curl -fsSL [raw-github-url]/install.sh | bash

set -e

SKILL_NAME="enola-seo"
REPO_URL="https://github.com/enola-revenue/enola-seo"

# ── Detect OS ────────────────────────────────────────────────
OS="$(uname -s)"
case "$OS" in
  Darwin)  PLATFORM="macOS" ;;
  Linux)   PLATFORM="Linux" ;;
  *)
    echo ""
    echo "Windows detected."
    echo "Manual install: copy the enola-seo/ folder to %APPDATA%\\Claude\\skills\\"
    echo "Then open Claude Code and say: run my SEO audit"
    exit 0
    ;;
esac

echo ""
echo "ENOLA SEO Installer"
echo "Platform: $PLATFORM"
echo "───────────────────────────────────────"

# ── Find Claude Code skills directory ────────────────────────
SKILLS_DIR="$HOME/.claude/skills"

if [ ! -d "$HOME/.claude" ]; then
  echo ""
  echo "Error: Claude Code not found at ~/.claude"
  echo "Install Claude Code first: https://claude.ai/download"
  exit 1
fi

mkdir -p "$SKILLS_DIR"

# ── Find enola-seo source ────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -d "$SCRIPT_DIR/enola-seo" ]; then
  # Running from inside the repo
  SOURCE_DIR="$SCRIPT_DIR/enola-seo"
elif [ -d "$SCRIPT_DIR/SKILL.md" ] || [ -f "$SCRIPT_DIR/SKILL.md" ]; then
  # Running from inside the enola-seo folder itself
  SOURCE_DIR="$SCRIPT_DIR"
else
  # Curl install — download from GitHub
  echo "Downloading enola-seo from GitHub..."
  TMP_DIR="$(mktemp -d)"
  trap 'rm -rf "$TMP_DIR"' EXIT

  if command -v curl &>/dev/null; then
    curl -fsSL "$REPO_URL/archive/refs/heads/main.tar.gz" | tar -xz -C "$TMP_DIR"
  elif command -v wget &>/dev/null; then
    wget -qO- "$REPO_URL/archive/refs/heads/main.tar.gz" | tar -xz -C "$TMP_DIR"
  else
    echo "Error: curl or wget required."
    exit 1
  fi

  SOURCE_DIR="$(find "$TMP_DIR" -name "SKILL.md" -maxdepth 3 | head -1 | xargs dirname)"

  if [ -z "$SOURCE_DIR" ]; then
    echo "Error: Could not find SKILL.md in downloaded archive."
    exit 1
  fi
fi

# ── Install ───────────────────────────────────────────────────
TARGET_DIR="$SKILLS_DIR/$SKILL_NAME"

if [ -d "$TARGET_DIR" ]; then
  echo "Existing install found at $TARGET_DIR"
  echo "Updating..."
  rm -rf "$TARGET_DIR"
fi

cp -r "$SOURCE_DIR" "$TARGET_DIR"

# ── Verify ────────────────────────────────────────────────────
if [ ! -f "$TARGET_DIR/SKILL.md" ]; then
  echo "Error: Install failed — SKILL.md not found at $TARGET_DIR"
  exit 1
fi

# ── Done ─────────────────────────────────────────────────────
echo ""
echo "───────────────────────────────────────"
echo "Enola SEO installed."
echo "Location: $TARGET_DIR"
echo ""
echo "Open Claude Code and say:"
echo "  run my SEO audit"
echo ""
echo "Or use a slash command:"
echo "  /enola audit [your-url]"
echo "  /enola fix [your-url]"
echo "  /enola geo [your-url]"
echo "───────────────────────────────────────"
