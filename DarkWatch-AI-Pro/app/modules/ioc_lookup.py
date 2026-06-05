import re
from .threat_feed import get_threat_feed

def lookup_ioc(query):
    if not query:
        return {"query": query, "type": "Unknown", "status": "No input", "matches": []}

    if re.match(r"^(?:\d{1,3}\.){3}\d{1,3}$", query):
        ioc_type = "IPv4"
    elif re.match(r"^[a-fA-F0-9]{32,64}$", query):
        ioc_type = "Hash"
    elif "." in query:
        ioc_type = "Domain/URL"
    else:
        ioc_type = "Keyword"

    feed = get_threat_feed(limit=50)
    matches = [item for item in feed if query.lower() in item["indicator"].lower()]

    return {
        "query": query,
        "type": ioc_type,
        "status": "Found" if matches else "Not found in local/demo feed",
        "matches": matches
    }
