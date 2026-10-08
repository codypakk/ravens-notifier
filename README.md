# 🏈 Baltimore Ravens News Notifier

A lightweight, serverless automated script that checks for the latest Baltimore Ravens news via ESPN RSS and delivers push notifications directly to your phone using [ntfy.sh](https://ntfy.sh/).

Managed with [`uv`](https://github.com/astral-sh/uv) and automatically executed every hour via **GitHub Actions**.

---

## ✨ Features

- 📰 **RSS Fetching:** Parses ESPN's Baltimore Ravens feed for up-to-date headlines.
- 📱 **Mobile Push Alerts:** Delivers real-time notifications via the free, open-source `ntfy` app (iOS & Android).
- 🧠 **Duplicate Protection:** Tracks previously seen links in `seen_news.txt` to avoid duplicate alerts.
- ⚡ **Ultra-Fast Environment:** Managed using `uv` for instant dependency resolution.
- ☁️ **Serverless Execution:** Runs automatically on an hourly schedule using GitHub Actions without requiring local server uptime.

---

## 🛠️ Setup & Installation

### 1. Mobile App Setup

1. Download the **ntfy** app on your phone ([iOS App Store](https://apps.apple.com/us/app/ntfy/id1625396386) or [Google Play Store](https://play.google.com/store/apps/details?id=io.heckel.ntfy)).
2. Open the app and tap **Subscribe to topic** (`+`).
3. Enter the secret topic string (e.g., `ravens-notifier`) and tap **Subscribe**.
