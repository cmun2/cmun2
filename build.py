"""
프로필 README 의 자동 갱신 구간을 다시 쓴다.

블로그 RSS 와 GitHub 공개 활동에서 읽어오므로, 여기 나타나는 줄은 전부
실제로 일어난 일이다. 내용이 바뀌지 않으면 워크플로는 커밋하지 않는다.
"""
import json
import os
import pathlib
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

BLOG_RSS = "https://cmun2.inblog.io/rss"
EVENTS = "https://api.github.com/users/cmun2/events/public?per_page=100"
README = pathlib.Path("README.md")


def get(url, as_json=False):
    headers = {"user-agent": "cmun2-profile"}
    token = os.environ.get("GITHUB_TOKEN")
    if token and "api.github.com" in url:
        headers["authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
    return json.loads(raw) if as_json else raw


def fmt_date(value):
    for pattern in ("%a, %d %b %Y %H:%M:%S %Z", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            return datetime.strptime(value, pattern).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return value[:10]


def blog_section(limit=5):
    root = ET.fromstring(get(BLOG_RSS))
    out = []
    for item in root.findall(".//item")[:limit]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        date = fmt_date((item.findtext("pubDate") or "").strip())
        out.append(f"[{title}]({link}) — {date}")
    return "\n\n".join(out)


def fetch_title(api_url):
    """이벤트 payload 에 제목이 없을 때만 호출한다. 실패하면 조용히 포기한다."""
    if not api_url:
        return ""
    try:
        return get(api_url, as_json=True).get("title", "")
    except Exception:
        return ""


def activity_section(limit=6):
    """푸시·PR·이슈만 남긴다. 이벤트 API 는 PR 제목을 주지 않아 따로 받아온다."""
    lines, seen = [], set()
    events = get(EVENTS, as_json=True)
    # 업스트림에 PR·이슈를 낸 저장소 이름. 같은 이름의 내 포크 push 는 접는다.
    upstream_names = {
        ev["repo"]["name"].split("/")[-1]
        for ev in events
        if ev["type"] in ("PullRequestEvent", "IssuesEvent")
    }
    for ev in events:
        repo = ev["repo"]["name"]
        date = fmt_date(ev["created_at"])
        kind = ev["type"]

        if kind == "PullRequestEvent" and ev["payload"].get("action") == "opened":
            pr = ev["payload"]["pull_request"]
            url = f"https://github.com/{repo}/pull/{pr['number']}"
            if url in seen:
                continue
            seen.add(url)
            title = pr.get("title") or fetch_title(pr.get("url"))
            label = f" {title}" if title else ""
            lines.append(f"PR [{repo}#{pr['number']}]({url}){label} — {date}")

        elif kind == "IssuesEvent" and ev["payload"].get("action") == "opened":
            issue = ev["payload"]["issue"]
            url = issue["html_url"]
            if url in seen:
                continue
            seen.add(url)
            lines.append(f"Issue [{repo}#{issue['number']}]({url}) {issue['title']} — {date}")

        elif kind == "PushEvent":
            # 프로필 저장소 자체는 이 스크립트가 매일 커밋하므로 항상 잡힌다.
            # PR 용 포크도 위에 업스트림 PR 이 이미 있어 중복이다.
            name = repo.split("/")[-1]
            if repo == "cmun2/cmun2" or name in upstream_names:
                continue
            key = f"push:{repo}"
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"Pushed to [{repo}](https://github.com/{repo}) — {date}")

        if len(lines) >= limit:
            break
    return "\n\n".join(lines) if lines else "_Nothing public in the last 90 days._"


def replace(text, marker, body):
    pattern = re.compile(
        rf"(<!-- {marker} starts -->).*?(<!-- {marker} ends -->)", re.DOTALL
    )
    if not pattern.search(text):
        raise SystemExit(f"marker not found: {marker}")
    return pattern.sub(rf"\1\n{body}\n\2", text)


text = README.read_text()
for marker, body in (("blog", blog_section()), ("activity", activity_section())):
    text = replace(text, marker, body)
README.write_text(text)
print("README updated")
