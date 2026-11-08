---
name: video-insight-digest
description: Analyze videos with subagent isolation - extracts frames, transcribes audio, generates structured text summary while keeping images out of main context. Saves 97% context vs direct frame viewing.
license: MIT
allowed-tools: Agent, Bash, Read, Write
metadata:
  version: "1.0.0"
  author: buzhonger
  repository: https://github.com/buzhonger/video-insight-digest
---

# Video Insight Digest

Intelligent video analysis that generates structured summaries while preserving context.

## Quick Start

```bash
/video-insight-digest https://www.bilibili.com/video/BV1xFnt6zE3K/
```

Returns organized summary: tech stack, workflow, timeline, insights.

## Performance

- **97% context savings**: 1.5K tokens (summary) vs 85K tokens (100 frames)
- **Same quality**: Subagent reads all frames, returns structured text
- **Memory integration**: Auto-saves to `~/.claude/projects/.../memory/`

## How It Works

1. Spawn background agent
2. Agent downloads video, extracts frames, transcribes
3. Agent reads images (in its own context)
4. Agent returns text summary
5. Main context stays clean

## Requirements

- `yt-dlp`, `ffmpeg` (video processing)
- WhisperX optional (local transcription)

Built on [claude-video](https://github.com/bradautomates/claude-video).

See full docs: [README.md](README.md)

## License

MIT
