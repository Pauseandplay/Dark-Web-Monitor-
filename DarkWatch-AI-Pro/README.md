# DarkWatch AI Pro

A professional, legal, portfolio-grade cybersecurity project for breach monitoring, threat intelligence, IOC lookup, AI-style risk scoring, and PDF security reports.

## Features

- Dark cybersecurity dashboard UI
- Email breach monitoring module
- Threat intelligence feed module
- IOC lookup for IPs, domains, URLs, and hashes
- Risk scoring engine
- PDF exposure report generator
- Demo mode with safe synthetic data
- Optional integrations:
  - Have I Been Pwned
  - AlienVault OTX
  - AbuseIPDB
  - URLHaus
  - MISP

## Legal and Ethical Use

This project does **not** scrape illegal dark-web marketplaces, leaked password dumps, or private systems.  
It is designed for legal OSINT, public threat intelligence, and authorized security monitoring.

## Quick Start

```bash
git clone https://github.com/your-username/DarkWatch-AI-Pro.git
cd DarkWatch-AI-Pro
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Environment Variables

Copy `.env.example` to `.env` and add your API keys.

```bash
cp .env.example .env
```

## Pages

- `/` Dashboard
- `/breach` Email breach monitor
- `/threats` Threat intelligence feed
- `/ioc` IOC lookup
- `/api/threats` JSON API

## Resume Description

**DarkWatch AI Pro** — Built a Flask-based cyber threat intelligence dashboard that monitors email breach exposure, aggregates threat indicators, performs IOC lookup, generates risk scores, and exports PDF security reports using modular Python components and a modern dark UI.

## GitHub Topics

`cybersecurity` `threat-intelligence` `osint` `flask` `python` `breach-monitoring` `ioc-lookup` `security-dashboard`
