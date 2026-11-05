<!--
Project: OpenCLAW SEED — Complete Autonomous AI Ecosystem
Copyright (c) 2026 Francisco Angulo de Lafuente
Author: Francisco Angulo de Lafuente
ORCID: https://orcid.org/0009-0001-1634-7063
Attribution recorded: 2026-11-05
SPDX-License-Identifier: Apache-2.0
-->

# 🚀 OpenCLAW Agent — Deployment Guide

## ✅ Already Deployed: HuggingFace Spaces

**The agent is LIVE at:** https://huggingface.co/spaces/Agnuxo/OpenCLAW-Agent  
**Direct URL:** https://agnuxo-openclaw-agent.hf.space

This runs 24/7 on HuggingFace's free infrastructure with:
- 🧠 NVIDIA LLM for intelligent content generation
- 📚 ArXiv paper fetching
- 📱 Moltbook posting (when account unsuspended ~Feb 17)
- 🔄 Background loop every hour
- 📊 Gradio dashboard for monitoring

All secrets configured securely in HF Space settings.

---

## 📦 Push to GitHub Repository

To push this code to your GitHub repo:

```bash
# 1. Clone your empty repo
git clone https://github.com/Agnuxo1/OpenCLAW-2-Autonomous-Multi-Agent-Scientific-Research-Platform.git
cd OpenCLAW-2-Autonomous-Multi-Agent-Scientific-Research-Platform

# 2. Extract the agent code
# (download openclaw-agent-deploy.tar.gz from Claude)
tar xzf openclaw-agent-deploy.tar.gz --strip-components=1

# 3. Push
git add .
git commit -m "🤖 OpenCLAW Autonomous Agent v1.0 - Full deployment"
git push origin main
```

## 🔐 GitHub Secrets Setup

Go to: **Settings → Secrets → Actions** and add:

| Secret Name | Value |
|---|---|
| `NVIDIA_API_KEY` | Your NVIDIA API keys (comma-separated) |
| `MOLTBOOK_API_KEY` | Your Moltbook API key |
| `HF_TOKEN` | Your HuggingFace token |
| `BRAVE_API_KEY` | Your Brave Search API key |

Then go to **Actions** → Enable the workflow. It runs every 4 hours automatically.

## 🌐 Alternative: Deploy on Render.com

1. Connect GitHub repo at https://render.com
2. Render detects `render.yaml` automatically
3. Add secrets in Render dashboard
4. Free web server + agent at `https://your-app.onrender.com`

---

## 📅 Moltbook Suspension

The Moltbook account (`OpenCLAW-Neuromorphic`) is currently suspended until ~Feb 17, 2026.
The agent will automatically retry and post successfully once the suspension lifts.

## ⚠️ Security Reminder

- **Rotate all API keys** that were shared in plain text
- All secrets are stored in environment variables, never in code
- The `.gitignore` protects `.env` files from being committed
