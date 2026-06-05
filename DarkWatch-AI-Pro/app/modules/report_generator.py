from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_report(email, breaches, risk):
    report_dir = Path("app/reports")
    report_dir.mkdir(exist_ok=True)

    safe_email = email.replace("@", "_at_").replace(".", "_")
    path = report_dir / f"darkwatch_report_{safe_email}.pdf"

    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4

    y = height - 60
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "DarkWatch AI - Security Exposure Report")

    y -= 35
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    y -= 20
    c.drawString(50, y, f"Asset: {email}")

    y -= 35
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, f"Risk Score: {risk['score']} / 100 ({risk['level']})")

    y -= 25
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Recommendation: {risk['recommendation'][:95]}")

    y -= 35
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Breach Findings")

    c.setFont("Helvetica", 10)
    y -= 20

    if not breaches:
        c.drawString(50, y, "No breach findings from configured source.")
    else:
        for breach in breaches:
            if y < 80:
                c.showPage()
                y = height - 60
            c.drawString(50, y, f"- {breach.get('name')} | {breach.get('domain')} | {breach.get('breach_date')}")
            y -= 16
            data_classes = ", ".join(breach.get("data_classes", []))
            c.drawString(70, y, f"Data: {data_classes[:90]}")
            y -= 20

    c.save()
    return str(path)
