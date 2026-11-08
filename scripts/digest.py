#!/usr/bin/env python3
"""
Video Insight Digest - Context-efficient video analysis

Spawns subagent to read frames, returns text summary only.
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime

SKILL_DIR = Path(__file__).parent.parent
WATCH_SKILL = Path.home() / ".claude/skills/claude-video/skills/watch"


def main():
    if len(sys.argv) < 2:
        print("Usage: digest.py <video-url> [--question 'your question']")
        print("   or: digest.py --refine <video-id> <timestamp>")
        sys.exit(1)

    # TODO: Implement actual logic
    # For now, this is a placeholder showing the intended architecture

    print("Video Insight Digest v1.0.0")
    print("This skill requires integration with Claude Code Agent tool.")
    print("")
    print("Current implementation: Call from Claude Code with /video-insight-digest")
    sys.exit(0)


if __name__ == "__main__":
    main()
