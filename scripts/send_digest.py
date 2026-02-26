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
    "product": "Product",
    "engineering": "Engineering",
    "data": "Data",
    "design": "Design",
    "everyone": "Everyone",
}

FORMATS = [
    {
        "name": "The 5 Lessons",
        "instruction": (
            "For each point: write a headline as a single bold declarative sentence — "
            "make it specific, not generic. Then write exactly 3 sentences of substance: "
            "unpack the insight with rigor, connect it to real practice, and where relevant "
            "tie it to building tools that touch people's inner lives. "
            "End with just the guest's name on its own line — no label, no italics, no 'source:'. "
            "Use this exact structure for each of the 5 sections:\n\n"
            "## [Bucket Name]\n\n"
            "**[Headline]**\n\n"
            "[Sentence 1. Sentence 2. Sentence 3.]\n\n"
            "[Guest Name]\n\n"
            "---"
        ),
    },
    {
        "name": "The 5 Contrarian Takes",
        "instruction": (
            "For each point: write a headline that names what conventional wisdom gets wrong — "
            "sharp, specific, slightly uncomfortable. Then write exactly 3 sentences: "
            "what the default thinking misses, what to do instead with enough detail to act on, "
            "and why this matters specifically for a team building behavioral science products. "
            "End with just the guest's name on its own line. "
            "Use this exact structure:\n\n"
            "## [Bucket Name]\n\n"
            "**[Contrarian headline]**\n\n"
            "[Sentence 1. Sentence 2. Sentence 3.]\n\n"
            "[Guest Name]\n\n"
            "---"
        ),
    },
    {
        "name": "The 5 Frameworks",
        "instruction": (
            "For each point: give the framework a sharp, memorable name as the headline. "
            "Then write exactly 3 sentences: a clean one-sentence definition, "
            "how it works in practice with a concrete example, "
            "and when to reach for it — including the conditions where it breaks. "
            "End with just the guest's name on its own line. "
            "Use this exact structure:\n\n"
            "## [Bucket Name]\n\n"
            "**[Framework Name]**\n\n"
            "[Sentence 1. Sentence 2. Sentence 3.]\n\n"
            "[Guest Name]\n\n"
            "---"
        ),
    },
    {
        "name": "The 5 Mistakes",
        "instruction": (
            "For each point: name the mistake in one sharp, specific headline — "
            "not a category, an actual mistake teams make. "
            "Then write exactly 3 sentences: what it looks like in practice so people recognize it, "
            "why it happens (the real reason, not the surface one), "
            "and how to avoid it with something concrete enough to do next week. "
            "End with just the guest's name on its own line. "
            "Use this exact structure:\n\n"
            "## [Bucket Name]\n\n"
            "**[Mistake headline]**\n\n"
            "[Sentence 1. Sentence 2. Sentence 3.]\n\n"
            "[Guest Name]\n\n"
            "---"
        ),
    },
    {
        "name": "The 5 What-Ifs",
        "instruction": (
            "For each point: pose a speculative future-facing provocation as the headline — "
            "grounded in the episode content but pushed forward. Make it genuinely unsettling. "
            "Then write exactly 3 sentences: what would have to be true for this to happen, "
            "what it would change about how we build, "
            "and why a team working on self-discovery tools should be thinking about it now. "
            "End with just the guest's name on its own line. "
            "Use this exact structure:\n\n"
            "## [Bucket Name]\n\n"
            "**[What-if provocation]**\n\n"
            "[Sentence 1. Sentence 2. Sentence 3.]\n\n"
            "[Guest Name]\n\n"
            "---"
        ),
    },
    {
        "name": "The 5 This Week In...",
        "instruction": (
            "For each point: surface an evergreen insight from the episode and frame it "
            "with a headline that creates fresh urgency — not timeless wisdom, a live wire. "
            "Then write exactly 3 sentences: what the insight actually is, "
            "why it has teeth right now specifically, "
            "and what the team should do with it this week — concrete, not inspirational. "
            "End with just the guest's name on its own line. "
            "Use this exact structure:\n\n"
            "## [Bucket Name]\n\n"
            "**[Urgent headline]**\n\n"
            "[Sentence 1. Sentence 2. Sentence 3.]\n\n"
            "[Guest Name]\n\n"
            "---"
        ),
    },
    {
        "name": "The 5 Playbooks",
        "instruction": (
            "For each point: give the playbook a name that makes someone want to run it. "
            "Then write exactly 3 sentences: what the play is and what problem it solves, "
            "the 3-4 steps to execute it in order, "
            "and what outcome to expect and how you know it worked. "
            "End with just the guest's name on its own line. "
            "Use this exact structure:\n\n"
            "## [Bucket Name]\n\n"
            "**[Playbook Name]**\n\n"
            "[Sentence 1. Sentence 2. Sentence 3.]\n\n"
            "[Guest Name]\n\n"
            "---"
        ),
    },
]

REPO_ROOT = Path(__file__).parent.parent
HISTORY_FILE = REPO_ROOT / "digest_history.json"
INDEX_DIR = REPO_ROOT / "index"

SYSTEM_PROMPT = """You are the voice behind a weekly digest for the full technology team at a \
behavioral science startup — product, engineering, data, and design. You write \
like the love child of Peter Thiel, Nassim Taleb, Nir Eyal, and Lenny Rachitsky: \
singular and uncomfortable when the truth demands it, blunt and anti-fragile when \
conventional wisdom deserves a fight, behavioral and tactical when the team needs \
to act, and always warm and no-BS so people actually read it.

Your writing principles:
- Never say what everyone already knows. If it's obvious, flip it or skip it.
- Every insight should create a tiny moment of productive discomfort.
- Be tactical enough that someone can use it in a meeting today.
- Be intellectual enough that someone feels proud their company thinks this way.
- Short sentences. No filler. No corporate warmth. Real warmth.
- Always cite the guest name — the source is part of the credibility.
- Write for builders, not managers. This team ships things.
- Each point should feel like something worth screenshotting and sending to a friend.

The team builds AI-native tools for self-discovery. \
When relevant, connect insights back to the human side of building — \
behavior change, identity, what makes people trust a product with their inner life."""


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
        available = [f for f in candidates if (INDEX_DIR / f).exists()]
    if not available:
        raise ValueError(f"No index files found for bucket '{bucket}'")
    return random.choice(available)


def build_user_prompt(format_info, bucket_files):
    lines = [
        f"Write this week's digest in the {format_info['name']} format.",
        "",
        f"Format instructions: {format_info['instruction']}",
        "",
        "Produce exactly 5 points in this order: Product, Engineering, Data, Design, Everyone.",
        "Follow the structure exactly — ## header, bold headline, 3 sentences, guest name, ---",
        "No preamble. No meta-commentary. No extra formatting. Start directly with ## Product.",
        "Never repeat insights or framings from previous digests.",
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
    header = f"BYL Tech Digest — {format_name} | Week of {today}"
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
