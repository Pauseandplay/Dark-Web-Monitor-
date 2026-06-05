import os
import requests

def check_email_breaches(email: str):
    """
    Legal breach-monitoring helper.

    Production option:
    - Add HIBP_API_KEY in .env.
    - Respect the Have I Been Pwned API terms.
    - Do not scrape leaked databases or illegal dark-web marketplaces.
    """
    if not email:
        return []

    api_key = os.getenv("HIBP_API_KEY")

    if not api_key:
        return [
            {
                "name": "DemoBreach Cloud",
                "domain": "example.com",
                "breach_date": "2024-11-18",
                "data_classes": ["Email addresses", "Passwords", "IP addresses"],
                "verified": True,
                "description": "Demo result. Add HIBP_API_KEY to enable live breach checks."
            },
            {
                "name": "Demo Forum Leak",
                "domain": "forum.example",
                "breach_date": "2023-06-02",
                "data_classes": ["Usernames", "Email addresses"],
                "verified": False,
                "description": "Synthetic portfolio data for safe local testing."
            }
        ]

    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": api_key,
        "user-agent": "DarkWatch-AI-Pro"
    }

    response = requests.get(url, headers=headers, params={"truncateResponse": "false"}, timeout=15)

    if response.status_code == 404:
        return []
    if response.status_code != 200:
        return [{
            "name": "API Error",
            "domain": "hibp",
            "breach_date": "N/A",
            "data_classes": [],
            "verified": False,
            "description": f"HIBP request failed with status {response.status_code}."
        }]

    data = response.json()
    return [
        {
            "name": item.get("Name"),
            "domain": item.get("Domain"),
            "breach_date": item.get("BreachDate"),
            "data_classes": item.get("DataClasses", []),
            "verified": item.get("IsVerified"),
            "description": item.get("Description", "")
        }
        for item in data
    ]
