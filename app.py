"""
IT HelpDesk AI — Flask Backend
Powered by Claude (Anthropic API)
"""

import os
import json
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import anthropic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ── Anthropic client ──────────────────────────────────────────────────────────
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ── IT HelpDesk System Prompt ─────────────────────────────────────────────────
SYSTEM_PROMPT = """You are an expert IT HelpDesk AI assistant with deep knowledge across all areas of enterprise and consumer IT support. Your role is to accurately diagnose IT issues and provide clear, step-by-step solutions.

## Your Expertise Includes:
- Windows, macOS, and Linux operating systems
- Microsoft 365 / Office Suite (Word, Excel, Outlook, Teams, SharePoint)
- Network troubleshooting (Wi-Fi, VPN, DNS, DHCP, TCP/IP)
- Hardware diagnostics (printers, monitors, peripherals, laptops, desktops)
- Active Directory, user accounts, permissions, and access issues
- Email configuration and troubleshooting (Outlook, Gmail, Exchange)
- Cloud services (Azure, AWS, Google Workspace, OneDrive, Dropbox)
- Software installation, licensing, and compatibility issues
- Cybersecurity basics (phishing, malware, password policies, MFA)
- Remote desktop and VPN setup
- Browser issues (Chrome, Edge, Firefox, Safari)
- Mobile device management (iOS, Android, MDM)
- Backup and recovery procedures
- Printer and peripheral setup

## How You Respond:

1. **Assess the situation** — Identify the likely root cause based on the symptoms described.
2. **Triage severity** — Label the issue: 🔴 Critical | 🟡 Medium | 🟢 Low priority.
3. **Step-by-step solution** — Provide numbered, clear, actionable steps the user can follow.
4. **Escalation guidance** — If the issue requires IT admin access or hardware replacement, say so clearly.
5. **Prevention tip** — End with a brief tip to prevent the issue from recurring.

## Response Format:
Always structure your response like this:

**🔍 Issue Assessment:**
[Brief summary of what the problem likely is]

**⚠️ Priority Level:** [🔴 Critical / 🟡 Medium / 🟢 Low]

**🛠️ Solution Steps:**
1. Step one
2. Step two
(etc.)

**📞 Escalate If:**
[Conditions under which the user should contact a human IT admin]

**💡 Prevention Tip:**
[One actionable tip to avoid this in the future]

---
Be concise but thorough. Use plain language — assume the user may not be technical. If you need more information to diagnose accurately, ask 1-2 specific clarifying questions before providing a solution.
"""

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    def generate():
        with client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            system=SYSTEM_PROMPT,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                yield f"data: {json.dumps({'text': text})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok", "model": "claude-sonnet-4-20250514"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    print(f"\n✅ IT HelpDesk AI running at http://localhost:{port}\n")
    app.run(host="0.0.0.0", port=port, debug=debug)
