from flask import Blueprint, render_template, request, jsonify, send_file
from .modules.breach_checker import check_email_breaches
from .modules.threat_feed import get_threat_feed
from .modules.risk_engine import calculate_risk
from .modules.report_generator import generate_report
from .modules.ioc_lookup import lookup_ioc

main = Blueprint("main", __name__)

@main.route("/")
def index():
    feed = get_threat_feed(limit=6)
    stats = {
        "monitored_assets": 18,
        "alerts": 7,
        "risk_score": 68,
        "feeds": 4
    }
    return render_template("index.html", feed=feed, stats=stats)

@main.route("/breach", methods=["GET", "POST"])
def breach():
    result = None
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        breaches = check_email_breaches(email)
        risk = calculate_risk(breaches)
        result = {"email": email, "breaches": breaches, "risk": risk}
    return render_template("breach.html", result=result)

@main.route("/threats")
def threats():
    feed = get_threat_feed(limit=20)
    return render_template("threats.html", feed=feed)

@main.route("/ioc", methods=["GET", "POST"])
def ioc():
    result = None
    if request.method == "POST":
        query = request.form.get("query", "").strip()
        result = lookup_ioc(query)
    return render_template("ioc.html", result=result)

@main.route("/api/threats")
def api_threats():
    return jsonify(get_threat_feed(limit=20))

@main.route("/report", methods=["POST"])
def report():
    email = request.form.get("email", "demo@example.com")
    breaches = check_email_breaches(email)
    risk = calculate_risk(breaches)
    path = generate_report(email, breaches, risk)
    return send_file(path, as_attachment=True)
