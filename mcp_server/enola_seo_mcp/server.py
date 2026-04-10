"""
ENOLA SEO MCP Server
© Sean Gal | enolarevenu.com

Exposes all 26 ENOLA SEO audits and preset workflows as MCP tools.
Install: uvx --from git+https://github.com/sean1gal/enola-seo enola-seo-mcp
"""

import json
import re
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("enola-seo")

# Resolve paths relative to this file (works wherever it's installed from)
ROOT = Path(__file__).parent.parent.parent  # → enola-seo repo root
REFS = ROOT / "references"
PRESETS_DIR = ROOT / "presets"
CONTEXT_FILE = Path.home() / ".enola-seo" / "context.json"

CONTEXT_FILE.parent.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# Skill parsing
# ---------------------------------------------------------------------------

def _parse_audits() -> dict[str, str]:
    """Parse references/audits.md and references/advanced.md into a dict of
    audit_id -> prompt_text. Handles the ## NN — TITLE / ``` blocks format."""
    audits: dict[str, str] = {}

    for ref_file in [REFS / "audits.md", REFS / "advanced.md"]:
        if not ref_file.exists():
            continue
        text = ref_file.read_text()
        # Split on section headers: ## 01 — TITLE
        sections = re.split(r"\n## (\d+) — ([^\n]+)", text)
        # sections = [preamble, num, title, body, num, title, body, ...]
        i = 1
        while i < len(sections) - 2:
            num = sections[i].strip().zfill(2)
            title = sections[i + 1].strip()
            body = sections[i + 2].strip()
            # Extract the code block content (the actual prompt)
            code_match = re.search(r"```\n(.*?)```", body, re.DOTALL)
            prompt_text = code_match.group(1).strip() if code_match else body
            key = f"{num}-{title.lower().replace(' ', '-').replace('/', '-')}"
            audits[key] = {
                "id": int(num),
                "title": title,
                "prompt": prompt_text,
                "context": body[:200].replace(prompt_text, "").strip()
            }
            i += 3

    return audits


def _parse_presets() -> dict[str, dict]:
    """Parse preset markdown files into structured dicts."""
    presets: dict[str, dict] = {}
    if not PRESETS_DIR.exists():
        return presets
    for f in sorted(PRESETS_DIR.glob("*.md")):
        text = f.read_text()
        # Extract frontmatter
        fm_match = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not fm_match:
            continue
        fm_lines = fm_match.group(1).strip().splitlines()
        meta: dict = {}
        for line in fm_lines:
            if ":" in line:
                k, _, v = line.partition(":")
                meta[k.strip()] = v.strip()
        # Get body (after frontmatter)
        body = text[fm_match.end():].strip()
        name = meta.get("name", f.stem)
        presets[name] = {
            "name": name,
            "goal": meta.get("goal", ""),
            "time": meta.get("time", ""),
            "sequence": meta.get("sequence", "[]"),
            "applies_to": meta.get("applies_to", "[all]"),
            "body": body
        }
    return presets


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

@mcp.tool()
def list_skills() -> str:
    """List all 26 ENOLA SEO audit skills with their IDs and one-line descriptions."""
    audits = _parse_audits()
    if not audits:
        return "Skill files not found. Ensure the enola-seo repo is intact."
    lines = ["ENOLA SEO — 26 Audit Skills\n"]
    for key, audit in sorted(audits.items(), key=lambda x: x[1]["id"]):
        lines.append(f"  {audit['id']:02d}. {audit['title']} → load_skill('{key}')")
    lines.append("\nUse load_skill(name) to get the full prompt for any audit.")
    return "\n".join(lines)


@mcp.tool()
def load_skill(name: str) -> str:
    """Load the full prompt for a named ENOLA SEO audit.

    Args:
        name: Skill key from list_skills (e.g. '01-gbp-categories') or
              a plain number (e.g. '1' or '01') or partial title match.
    """
    audits = _parse_audits()
    if not audits:
        return "Skill files not found."

    # Exact match
    if name in audits:
        a = audits[name]
        return f"PROMPT {a['id']:02d} — {a['title']}\n\n{a['prompt']}"

    # Match by number
    try:
        num = int(name)
        for key, a in audits.items():
            if a["id"] == num:
                return f"PROMPT {a['id']:02d} — {a['title']}\n\n{a['prompt']}"
    except ValueError:
        pass

    # Partial title match
    name_lower = name.lower()
    matches = [(k, a) for k, a in audits.items()
               if name_lower in a["title"].lower() or name_lower in k]
    if len(matches) == 1:
        a = matches[0][1]
        return f"PROMPT {a['id']:02d} — {a['title']}\n\n{a['prompt']}"
    if len(matches) > 1:
        options = "\n".join(f"  - {k}" for k, _ in matches)
        return f"Multiple matches for '{name}':\n{options}\n\nBe more specific."

    return (f"Skill '{name}' not found. Run list_skills() to see available audits.")


@mcp.tool()
def list_presets() -> str:
    """List all ENOLA SEO preset workflows with their goals and prompt sequences."""
    presets = _parse_presets()
    if not presets:
        return "No presets found."
    lines = ["ENOLA SEO — Preset Workflows\n"]
    for name, p in presets.items():
        lines.append(f"  {name}")
        lines.append(f"    goal: {p['goal']}")
        lines.append(f"    time: {p['time']}")
        lines.append(f"    sequence: {p['sequence']}")
        lines.append("")
    lines.append("Use load_preset(name) to get the full workflow with rationale.")
    return "\n".join(lines)


@mcp.tool()
def load_preset(name: str) -> str:
    """Load a named ENOLA SEO preset workflow.

    Args:
        name: Preset name from list_presets (e.g. 'local-quick-start')
    """
    presets = _parse_presets()
    if name not in presets:
        available = ", ".join(presets.keys())
        return f"Preset '{name}' not found. Available: {available}"
    p = presets[name]
    return (
        f"PRESET — {p['name'].upper().replace('-', ' ')}\n\n"
        f"Goal: {p['goal']}\n"
        f"Time: {p['time']}\n"
        f"Sequence: {p['sequence']}\n"
        f"Applies to: {p['applies_to']}\n\n"
        f"{p['body']}"
    )


@mcp.tool()
def run_diagnostic() -> str:
    """Return the ENOLA SEO diagnostic interview prompt.
    Paste this into Claude to start a one-question-at-a-time interview
    that identifies your business type and builds your custom audit path.
    """
    return """ENOLA SEO — DIAGNOSTIC INTERVIEW

I want to run an SEO audit on my business using the ENOLA SEO system.

Interview me to understand my business before we start.

Ask me one question at a time. Wait for my answer before asking the next one.
Cover: what I do, who I serve, my website, my competitors, my current SEO situation,
and what's not working.

When you have enough context:
- Identify my business type
- Tell me which of the 26 prompts apply to me (and which to skip, and why)
- Give me my recommended order based on highest impact first
- Tell me the one thing I should do in the next 48 hours

Start with your first question now."""


@mcp.tool()
def set_context(data: str) -> str:
    """Save business context for this session so audits use your specific details.

    Args:
        data: Business context as plain text or JSON string.
    """
    CONTEXT_FILE.parent.mkdir(exist_ok=True)
    try:
        parsed = json.loads(data)
        CONTEXT_FILE.write_text(json.dumps(parsed, indent=2))
        return "Context saved. All subsequent audits will use your business details."
    except json.JSONDecodeError:
        # Store as plain text wrapped in JSON
        CONTEXT_FILE.write_text(json.dumps({"raw": data}))
        return "Context saved as plain text. All subsequent audits will use your business details."


@mcp.tool()
def get_context() -> str:
    """Retrieve the saved business context for this session."""
    if not CONTEXT_FILE.exists():
        return (
            "No context saved yet. Run run_diagnostic() to set up your business context, "
            "or use set_context(data) to save it directly."
        )
    data = json.loads(CONTEXT_FILE.read_text())
    if "raw" in data:
        return data["raw"]
    return json.dumps(data, indent=2)


@mcp.tool()
def clear_context() -> str:
    """Clear the saved business context (use when switching to a different business)."""
    if CONTEXT_FILE.exists():
        CONTEXT_FILE.unlink()
        return "Context cleared."
    return "No context was saved."


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
