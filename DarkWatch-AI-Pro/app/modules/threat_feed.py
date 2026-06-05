import os
import requests
from datetime import datetime

DEMO_FEED = [
    {"type": "Malicious IP", "indicator": "185.220.101.42", "source": "Demo OTX", "severity": "High", "first_seen": "2026-06-01"},
    {"type": "Phishing Domain", "indicator": "secure-login-alert.example", "source": "Demo Feed", "severity": "Critical", "first_seen": "2026-06-02"},
    {"type": "Malware Hash", "indicator": "44d88612fea8a8f36de82e1278abb02f", "source": "Demo Malware Bazaar", "severity": "Medium", "first_seen": "2026-05-29"},
    {"type": "C2 Domain", "indicator": "update-service-check.example", "source": "Demo TI", "severity": "High", "first_seen": "2026-06-03"},
    {"type": "Suspicious URL", "indicator": "http://example.test/reset", "source": "Demo URLHaus", "severity": "Medium", "first_seen": "2026-06-04"},
    {"type": "Botnet IP", "indicator": "45.155.205.233", "source": "Demo AbuseIPDB", "severity": "High", "first_seen": "2026-06-05"}
]

def get_threat_feed(limit=10):
    """
    Uses safe/public threat-intelligence style data by default.
    You can extend this with OTX, AbuseIPDB, URLHaus, or MISP APIs.
    """
    otx_key = os.getenv("OTX_API_KEY")
    if not otx_key:
        return DEMO_FEED[:limit]

    try:
        url = "https://otx.alienvault.com/api/v1/pulses/subscribed"
        headers = {"X-OTX-API-KEY": otx_key}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        pulses = response.json().get("results", [])
        feed = []
        for pulse in pulses:
            for ioc in pulse.get("indicators", [])[:3]:
                feed.append({
                    "type": ioc.get("type", "Indicator"),
                    "indicator": ioc.get("indicator", ""),
                    "source": "AlienVault OTX",
                    "severity": "Medium",
                    "first_seen": pulse.get("created", datetime.utcnow().date().isoformat())[:10]
                })
        return feed[:limit] or DEMO_FEED[:limit]
    except Exception:
        return DEMO_FEED[:limit]
