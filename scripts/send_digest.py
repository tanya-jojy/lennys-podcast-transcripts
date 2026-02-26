#!/usr/bin/env python3
import json
import os
import random
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

import anthropic
import requests

TOPIC_BUCKETS = {
    "product": [
        "product-strategy.md", "product-management.md", "product-market-fit.md",
        "product-development.md", "product-led-growth.md", "product-leadership.md",
        "prioritization.md", "experimentation.md", "ab-testing.md", "user-experience.md",
        "customer-research.md", "customer-experience.md", "feedback.md", "retention.md",
        "growth-strategy.md", "startup-growth.md", "innovation.md", "creativity.md",
        "storytelling.md", "branding.md", "brand-building.md", "marketing.md",
        "word-of-mouth.md", "community-building.md", "agile.md", "strategy.md",
        "ai.md", "chatgpt.md", "openai.md",
    ],
    "engineering": [
        "engineering.md", "open-source.md", "machine-learning.md",
        "ab-testing.md", "experimentation.md", "ai.md", "chatgpt.md", "openai.md",
    ],
    "data": [
        "analytics.md", "data-analytics.md", "decision-making.md", "okrs.md",
        "network-effects.md", "neuroscience.md", "psychology.md", "experimentation.md",
        "growth-strategy.md", "ab-testing.md", "ai.md",
    ],
    "design": [
        "design.md", "user-experience.md", "creativity.md", "storytelling.md",
        "customer-experience.md", "personal-branding.md", "branding.md",
        "communication.md", "ai.md",
    ],
    "everyone": [
        "leadership.md", "management.md", "company-culture.md",
        "startup-culture.md", "hiring.md", "recruiting.md", "team-building.md",
        "mentorship.md", "founder-mode.md", "entrepreneurship.md", "bootstrapping.md",
        "business-strategy.md", "organizational-design.md", "career-development.md",
        "career-growth.md", "skill-building.md", "personal-development.md",
        "personal-transformation.md", "focus.md", "productivity.md",
        "time-management.md", "work-life-balance.md", "mental-health.md",
        "stress-management.md", "anxiety-management.md", "networking.md",
        "influence.md", "power.md", "remote-work.md", "venture-capital.md",
        "media-relations.md", "enterprise-sales.md", "sales.md", "linkedin.md",
        "facebook.md", "google.md", "meta.md", "microsoft.md", "uber.md", "stripe.md",
        "airbnb.md", "executive-coaching.md", "executive-search.md",
    ],
}

BUCKET_ORDER = ["product", "engineering", "data", "design", "everyone"]

BUCKET_LABELS = {
    "product": "🧠 Product",
    "engineering": "⚙️ Engineering",
    "data": "📊 Data",
    "design": "🎨 Design",
    "everyone": "🌀 Everyone",
}

FORMATS = [
    {
        "name": "The 5 Lessons",
        "instruction": (
            "For each point: write a bold insight headline, then 3 sentences of substance "
            "that unpack the lesson with specificity, then cite the guest name and episode source in italics."
        ),
    },
    {
        "name": "The 5 Contrarian Takes",
        "instruction": (
            "For each point: clearly state what conventional wisdom gets wrong, "
            "then state what to do instead with a concrete explanation, "
            "then cite the guest name and episode source in italics."
        ),
    },
    {
        "name": "The 5 Frameworks",
        "instruction": (
            "For each point: give the framework a sharp memorable name, "
            "provide a one-sentence definition, explain how and when to use it, "
            "then cite the guest name and episode source in italics."
        ),
    },
    {
        "name": "The 5 Mistakes",
        "instruction": (
            "For each point: name the mistake in one sharp sentence, "
            "describe what happened or what it looks like in practice, "
            "explain why it happens, explain how to avoid it, "
            "then cite the guest name and episode source in italics."
        ),
    },
    {
        "name": "The 5 What-Ifs",
        "instruction": (
            "For each point: pose a speculative future-facing provocation grounded in the episode content, "
            "explain why it matters and what it would change, "
            "then cite the guest name and episode source in italics."
        ),
    },
    {
        "name": "The 5 This Week In...",
        "instruction": (
            "For each point: surface an evergreen topic from the episode and frame it with fresh urgency "
            "relevant to the current moment, explain why it matters right now specifically, "
            "then cite the guest name and episode source in italics."
        ),
    },
    {
        "name": "The 5 Playbooks",
        "instruction": (
            "For each point: give the playbook a name, break it into 3-4 concrete tactical steps, "
            "explain when to run this play and what outcome to expect, "
            "then cite the guest name and episode source in italics."
        ),
    },
]

REPO_ROOT = Path(__file__).parent.parent
HISTORY_FILE = REPO_ROOT / "digest_history.json"
INDEX_DIR = REPO_ROOT / "index"

SYSTEM_PROMPT = (
    "You are the voice behind a weekly digest for the full technology team at a 
behavioral science startup — product, engineering, data, and design. You write 
like the love child of Peter Thiel, Nassim Taleb, Nir Eyal, and Lenny Rachitsky: 
singular and uncomfortable when the truth demands it, blunt and anti-fragile when 
conventional wisdom deserves a fight, behavioral and tactical when the team needs 
to act, and always warm and no-BS so people actually read it.

Your writing principles:
- Never say what everyone already knows. If it's obvious, flip it or skip it.
- Every insight should create a tiny moment of productive discomfort.
- Be tactical enough that someone can use it in a meeting today.
- Be intellectual enough that someone feels proud their company thinks this way.
- Short sentences. No filler. No corporate warmth. Real warmth.
- Always cite the guest name and episode — the source is part of the credibility.
- Write for builders, not managers. This team ships things.
- Each point should feel like something worth screenshotting and sending to a friend.

The team builds AI-native tools for self-discovery. 
When relevant, connect insights back to the human side of building — 
behavior change, identity, what makes people trust a product with their inner life."
)


def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return {"format_rotation": 0, "topic_history": {}}


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
        f.write("\n")


def is_recently_used(filename, topic_history, weeks=8):
    if filename not in topic_history:
        return False
    last_used = datetime.fromisoformat(topic_history[filename])
    cutoff = datetime.now() - timedelta(weeks=weeks)
    return last_used > cutoff


def pick_topic_file(bucket, topic_history):
    candidates = TOPIC_BUCKETS[bucket]
    available = [
        f for f in candidates
        if (INDEX_DIR / f).exists() and not is_recently_used(f, topic_history)
    ]
    if not available:
        # Fall back to all existing files if everything has been recently used
        available = [f for f in candidates if (INDEX_DIR / f).exists()]
    if not available:
        raise ValueError(f"No index files found for bucket '{bucket}'")
    return random.choice(available)


def build_user_prompt(format_info, bucket_files):
    lines = [
        f"Write this week's digest in the *{format_info['name']}* format.",
        "",
        f"Format instructions: {format_info['instruction']}",
        "",
        "Produce exactly 5 points in this order: 🧠 Product, ⚙️ Engineering, 📊 Data, 🎨 Design, 🌀 Everyone.",
        "Start each point with its emoji label and bucket name as a header.",
        "Use *bold* for headlines and _italic_ for episode sources.",
        "Separate each point with a blank line.",
        "Never repeat insights or framings from previous digests.",
        "Return only the 5 formatted digest points — no preamble, no meta-commentary.",
        "",
        "Source material for each section:",
        "",
    ]
    for bucket in BUCKET_ORDER:
        filename = bucket_files[bucket]
        label = BUCKET_LABELS[bucket]
        content = (INDEX_DIR / filename).read_text()
        lines.append(f"--- {label} (source: {filename}) ---")
        lines.append(content.strip())
        lines.append("")
    return "\n".join(lines)


def call_claude(user_prompt):
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return message.content[0].text


def post_to_slack(format_name, digest_content):
    webhook_url = os.environ["SLACK_WEBHOOK_URL"]
    today = datetime.now().strftime("%B %d, %Y")
    header = f"*📬 BYL Tech Digest — {format_name}* | Week of {today}"
    full_message = f"{header}\n\n{digest_content}"
    response = requests.post(webhook_url, json={"text": full_message}, timeout=10)
    response.raise_for_status()


def git_commit_and_push():
    today = datetime.now().strftime("%Y-%m-%d")
    subprocess.run(["git", "add", "digest_history.json"], cwd=REPO_ROOT, check=True)
    subprocess.run(
        ["git", "commit", "-m", f"digest: update history [{today}]"],
        cwd=REPO_ROOT,
        check=True,
    )
    subprocess.run(["git", "push"], cwd=REPO_ROOT, check=True)


def main():
    history = load_history()
    format_index = history.get("format_rotation", 0) % 7
    topic_history = history.get("topic_history", {})

    format_info = FORMATS[format_index]
    print(f"Format #{format_index}: {format_info['name']}")

    bucket_files = {bucket: pick_topic_file(bucket, topic_history) for bucket in BUCKET_ORDER}
    print("Selected files:", bucket_files)

    user_prompt = build_user_prompt(format_info, bucket_files)
    digest_content = call_claude(user_prompt)

    post_to_slack(format_info["name"], digest_content)
    print("Posted to Slack.")

    today_str = datetime.now().isoformat()
    for filename in bucket_files.values():
        topic_history[filename] = today_str
    history["format_rotation"] = (format_index + 1) % 7
    history["topic_history"] = topic_history

    save_history(history)
    git_commit_and_push()
    print("History committed and pushed.")


if __name__ == "__main__":
    main()
