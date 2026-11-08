# Video Insight Digest

> Intelligent video analysis with context-efficient summaries

Analyze videos without flooding your context. Subagent reads frames, returns structured text. **Saves 97% context** vs direct viewing.

## Features

- **Subagent Isolation**: Images stay out of main context
- **Structured Summaries**: Tech stack, workflow, timeline, insights
- **Memory Integration**: Auto-saves to project memory
- **Smart Naming**: `watch-20261109-233045-BV1xFnt6zE3K`
- **On-Demand Refinement**: Extract specific frames when needed

## Performance

| Metric | Direct (100 frames) | This Skill |
|--------|---------------------|------------|
| Main context | ~85K tokens | ~1.5K tokens |
| Savings | - | **97%** |
| Quality | High | High |

## Installation

```bash
# Clone into Claude skills directory
cd ~/.claude/skills
git clone https://github.com/buzhonger/video-insight-digest

# Or download and extract
```

### Requirements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp): `pip install yt-dlp` or `brew install yt-dlp`
- [ffmpeg](https://ffmpeg.org/): `brew install ffmpeg` or `winget install ffmpeg`
- [claude-video](https://github.com/bradautomates/claude-video): This skill extends it

Optional:
- WhisperX for local transcription (no API key needed)

## Usage

### Basic Analysis

```
/video-insight-digest https://www.bilibili.com/video/BV1xFnt6zE3K/
```

Returns:

```markdown
# BV1xFnt6zE3K - AI Animation Production

**Duration**: 32:08
**Topic**: Complete AI video workflow

## Tech Stack
- Claude (Opus 5.5): Code generation
- Gemini: TTS + images
...

## Workflow
1. Script in Obsidian
2. Visual style selection
...

## Key Timestamps
- 00:29 - Cost analysis
- 01:57 - Blender demo
...

## Core Insights
1. $0.3/30s cost
2. Multi-model collaboration
...
```

### With Question

```
/video-insight-digest https://youtube.com/watch?v=xyz --question "What animation tools are mentioned?"
```

### Refine Timestamp

After seeing summary:

```
/video-insight-digest --refine BV1xFnt6zE3K 3:24
```

Extracts that frame, describes details (text only).

## How It Works

```
┌─────────────┐
│ Main Agent  │  (Your context)
│  ≈ 1.5K tok │
└──────┬──────┘
       │ spawn
       ├──────────────────┐
       │                  ▼
       │         ┌─────────────────┐
       │         │  Subagent       │
       │         │  - Download     │
       │         │  - Extract 100  │
       │         │    frames       │
       │         │  - Read images  │
       │         │    (≈85K tokens)│
       │         │  - Transcribe   │
       │         └────────┬────────┘
       │                  │
       ▼                  │
  ┌────────────┐         │
  │ Text Only  │ ◄───────┘
  │ Summary    │
  └────────────┘
```

Images never enter main context.

## Configuration

Uses `~/.config/watch/.env`:

```bash
# Engine
WATCH_ENGINE=local  # or gemini (needs API key)

# WhisperX (local transcription)
WATCH_WHISPERX_DEVICE=cuda  # or cpu
WATCH_WHISPERX_MODEL=small  # or large-v3
WATCH_WHISPER_BACKEND=whisperx
```

## Directory Structure

```
watch-20261109-233045-BV1xFnt6zE3K/
├── video.mp4
├── frames/
│   ├── frame_0001.jpg
│   └── ...
├── audio.mp3
└── transcript.json
```

Timestamped for easy sorting and cleanup.

## When to Use

**Use this skill when:**
- Learning from tutorials
- Analyzing long videos (30min+)
- Building knowledge base
- Context budget is tight

**Use direct `watch` when:**
- Short clips (<5min)
- Need pixel-perfect details
- Code screenshots analysis

## Comparison

| Tool | Context Cost | Use Case |
|------|--------------|----------|
| `watch` (direct) | 85K/100 frames | Short, precise |
| `watch --engine gemini` | 0 (Gemini watches) | Best quality, needs key |
| **This skill** | 1.5K (summary) | Long videos, local, memory |

## Example: 4-Video Analysis

Analyze these Opus 5.5 tutorials:

```bash
/video-insight-digest BV1xFnt6zE3K
/video-insight-digest BV1M2sf6VETm
/video-insight-digest BV1VMnk68E9Q
/video-insight-digest BV1bqx76wEUM
```

**Total context**: ~6K tokens (summaries)  
**vs Direct**: ~340K tokens (4×85K frames)

**Savings**: 98%

All summaries saved to memory, queryable later.

## Memory Integration

Auto-creates:

```markdown
~/.claude/projects/your-project/memory/video-BV1xFnt6zE3K.md
```

With frontmatter:

```yaml
---
name: video-BV1xFnt6zE3K
description: AI animation workflow, $12/46min
metadata:
  type: reference
  video_id: BV1xFnt6zE3K
  duration: "32:08"
  analyzed: 2026-11-09
---
```

Query later: "What did that Opus video say about costs?"

## Limitations

- **Sparse sampling**: 100 frames from 30min = ~1 frame/18s
  - Fast demos may be missed
  - Use `--refine` for specific moments
- **Text-only**: No visual verification
  - Subagent describes what it sees
  - Trust summary, or refine timestamps
- **First analysis takes time**: Download + transcription
  - ~3-5min for 30min video
  - Cached summaries instant

## Roadmap

- Configurable frame count (`--max-frames 300`)
- Multi-video comparison mode
- Export summaries (PDF, HTML)
- Integration with note-taking tools

## Credits

Built on [claude-video](https://github.com/bradautomates/claude-video) by [@bradautomates](https://github.com/bradautomates).

## License

MIT © 2026 buzhonger
