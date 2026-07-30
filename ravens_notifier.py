import os
import requests
import feedparser

# RSS Feed for Baltimore Ravens (ESPN)
RSS_URL = "https://www.espn.com/espn/rss/nfl/news?team=bal"

NTFY_TOPIC = "ravens-notifier"
NTFY_URL = f"https://ntfy.sh/{NTFY_TOPIC}"

CACHE_FILE = "seen_news.txt"

def load_seen_links():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_seen_link(link):
    with open(CACHE_FILE, "a") as f:
        f.write(f"{link}\n")

def check_and_notify():
    seen_links = load_seen_links()
    feed = feedparser.parse(RSS_URL)

    # Get the latest 5 news articles
    for entry in reversed(feed.entries[:5]):
        link = entry.link
        title = entry.title
        summary = getattr(entry, "summary", "Click to read full article.")

        if link not in seen_links:
            response = requests.post(
                NTFY_URL,
                data=summary.encode("utf-8"),
                headers={
                    "Title": f"Ravens News: {title}",
                    "Click": link,
                    "Tags": "football,baltimore",
                    "Priority": "high",
                }
            )

            if response.status_code == 200:
                print(f"Sent notification: {title}")
                save_seen_link(link)
            else:
                print(f"Failed to send alert. Status: {response.status_code}")

if __name__ == "__main__":
    check_and_notify()