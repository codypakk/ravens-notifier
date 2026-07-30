# 🏈 Baltimore Ravens News Notifier

A lightweight, serverless automated script that checks for the latest Baltimore Ravens news via ESPN RSS and delivers push notifications directly to your phone using [ntfy.sh](https://ntfy.sh/).

Managed with [`uv`](https://github.com/astral-sh/uv) and automatically executed every 30 minutes via **GitHub Actions**.

---

## ✨ Features

- 📰 **RSS Fetching:** Parses ESPN's Baltimore Ravens feed for up-to-date headlines.
- 📱 **Mobile Push Alerts:** Delivers real-time notifications via the free, open-source `ntfy` app (iOS & Android).
- 🧠 **Duplicate Protection:** Tracks previously seen links in `seen_news.txt` to avoid duplicate alerts.
- ⚡ **Ultra-Fast Environment:** Managed using `uv` for instant dependency resolution.
- ☁️ **Serverless Execution:** Runs automatically on a 30-minute schedule using GitHub Actions without requiring local server uptime.

---

## 🛠️ Setup & Installation

### 1. Mobile App Setup

1. Download the **ntfy** app on your phone ([iOS App Store](https://apps.apple.com/us/app/ntfy/id1625396386) or [Google Play Store](https://play.google.com/store/apps/details?id=io.heckel.ntfy)).
2. Open the app and tap **Subscribe to topic** (`+`).
3. Enter your secret topic string (e.g., `ravens-notifier`) and tap **Subscribe**.

### 2. Local Machine Setup

Ensure `uv` is installed on your local development environment (WSL / Linux / macOS):

```bash
# Install uv package manager
curl -sSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh

# Clone the repository
git clone git@github.com:YOUR_USERNAME/ravens-notifier.git
cd ravens-notifier

# Sync and set up virtual environment
uv sync
```
