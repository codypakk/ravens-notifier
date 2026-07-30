import os
import re
import requests
import feedparser

# RSS Feed
RSS_URL = "https://www.baltimoreravens.com/c2j/rss/news"

NTFY_TOPIC = "ravens-notifier"
NTFY_URL = f"https://ntfy.sh/{NTFY_TOPIC}"

CACHE_FILE = "seen_news.txt"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def load_seen_links():
    """Loads previously processed article links from the cache file."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_seen_link(link):
    """Appends a new article link to the cache file."""
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{link}\n")

def clean_html(raw_html):
    """Strips HTML tags (<p>, <a>, etc.) from RSS summaries using regex."""
    clean_text = re.sub(r'<[^>]+>', '', raw_html)
    return clean_text.strip()

def sanitize_header(text):
    """
    Strips non-ASCII characters (curly quotes, em-dashes) from the title 
    to prevent Python requests header encoding crashes.
    """
    return text.encode('ascii', 'ignore').decode('ascii')

def check_and_notify():
    seen_links = load_seen_links()
    
    # Fetch feed via requests with custom headers to prevent 403 blocks
    try:
        response = requests.get(RSS_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        feed = feedparser.parse(response.content)
    except Exception as e:
        print(f"Error fetching RSS feed: {e}")
        return

    # Process top 5 articles from oldest to newest
    for entry in reversed(feed.entries[:5]):
        link = entry.link
        title = getattr(entry, "title", "New Ravens Article")
        summary_raw = getattr(entry, "summary", "Click to read full article.")
        summary = clean_html(summary_raw)

        if link not in seen_links:
            # Sanitize the title header to avoid Unicode header errors
            safe_title = sanitize_header(f"Ravens News: {title}")

            ntfy_headers = {
                "Title": safe_title,
                "Click": link,
                "Tags": "football,baltimore",
                "Priority": "high",
            }

            res = requests.post(
                NTFY_URL,
                data=summary.encode("utf-8"),
                headers=ntfy_headers,
                timeout=10
            )

            if res.status_code == 200:
                print(f"Sent notification: {title}")
                save_seen_link(link)
            else:
                print(f"Failed to send alert for '{title}'. Status: {res.status_code}")

if __name__ == "__main__":
    check_and_notify()