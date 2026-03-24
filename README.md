# 🖥️ IT HelpDesk AI

An intelligent, fully automated IT support chatbot powered by [Claude (Anthropic)](https://anthropic.com). Describe any IT issue and get an instant, accurate diagnosis with step-by-step solutions — built for companies, teams, or anyone who wants a smart IT assistant on-demand.

![IT HelpDesk AI Screenshot](https://via.placeholder.com/900x500/0d1117/2f81f7?text=IT+HelpDesk+AI)

---

## ✨ Features

- 🔍 **Smart Issue Assessment** — Accurately diagnoses IT problems based on your description
- ⚠️ **Priority Triage** — Labels issues as 🔴 Critical / 🟡 Medium / 🟢 Low
- 🛠️ **Step-by-Step Solutions** — Clear, numbered instructions anyone can follow
- 📞 **Escalation Guidance** — Tells you exactly when to contact a human IT admin
- 💡 **Prevention Tips** — Helps prevent issues from recurring
- 💬 **Multi-turn Conversations** — Ask follow-up questions naturally
- ⚡ **Streaming Responses** — Real-time text streaming for fast, responsive feel
- 📱 **Fully Responsive** — Works on desktop, tablet, and mobile
- 🎯 **Quick-Action Chips** — One-click common issue templates

## 🧠 IT Knowledge Coverage

| Category | Examples |
|---|---|
| **Operating Systems** | Windows, macOS, Linux |
| **Microsoft 365** | Outlook, Teams, SharePoint, OneDrive, Office Suite |
| **Networking** | Wi-Fi, VPN, DNS, DHCP, TCP/IP, proxy |
| **Hardware** | Printers, monitors, peripherals, laptops, desktops |
| **Cloud Services** | Azure, AWS, Google Workspace, Dropbox |
| **Security** | Phishing, malware, MFA, password policies |
| **User Accounts** | Active Directory, permissions, locked accounts |
| **Email** | Configuration, sync issues, rules, signatures |
| **Browsers** | Chrome, Edge, Firefox, Safari issues |
| **Mobile** | iOS, Android, MDM, device enrollment |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- An Anthropic API key ([get one free at console.anthropic.com](https://console.anthropic.com))

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/it-helpdesk-ai.git
cd it-helpdesk-ai
```

### 2. Create a virtual environment

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

```bash
# Copy the example env file
cp .env.example .env
```

Open `.env` in any text editor and replace `your_anthropic_api_key_here` with your real API key:

```
ANTHROPIC_API_KEY=sk-ant-...
```

### 5. Run the app

```bash
python app.py
```

Open your browser and go to **http://localhost:5000** 🎉

---

## 📁 Project Structure

```
it-helpdesk-ai/
├── app.py                 # Flask backend + Anthropic API integration
├── templates/
│   └── index.html         # Full frontend (HTML/CSS/JS — single file)
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

---

## 🔧 Configuration

All configuration is done via the `.env` file:

| Variable | Required | Default | Description |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | ✅ Yes | — | Your Anthropic API key |
| `FLASK_DEBUG` | No | `false` | Enable debug mode |
| `PORT` | No | `5000` | Port to run on |

---

## 🌐 Deploying for Your Team

### Option A — Run on a local server or VM

Run `python app.py` on any machine your team can reach on the network. Access via the machine's IP address:

```
http://192.168.1.X:5000
```

### Option B — Deploy to Railway (free tier available)

1. Push your repo to GitHub
2. Go to [railway.app](https://railway.app) and connect your repo
3. Add `ANTHROPIC_API_KEY` in the Railway environment variables panel
4. Done — Railway auto-deploys on every push

### Option C — Deploy to Render (free tier available)

1. Push your repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service → Connect repo
3. Set **Build Command**: `pip install -r requirements.txt`
4. Set **Start Command**: `python app.py`
5. Add `ANTHROPIC_API_KEY` in Environment Variables
6. Deploy

### Option D — Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

```bash
docker build -t it-helpdesk-ai .
docker run -p 5000:5000 -e ANTHROPIC_API_KEY=your_key it-helpdesk-ai
```

---

## 💡 Example Use Cases

**User types:**
> "My Outlook stopped receiving emails this morning but I can still send them."

**IT HelpDesk AI responds:**
> 🔍 **Issue Assessment:** This is likely a mailbox sync issue, a stuck email rule, or a server-side filtering problem...
>
> ⚠️ **Priority Level:** 🟡 Medium
>
> 🛠️ **Solution Steps:**
> 1. Open Outlook → File → Account Settings...
> ...

---

## 🔒 Security Notes

- **Never commit your `.env` file** — it contains your API key
- The `.gitignore` already excludes it, but double-check before pushing
- For production deployments, use environment variables in your hosting platform rather than a `.env` file
- Consider adding authentication (login page) if deploying for a company

---

## 🛠️ Customization

### Change the AI's personality or knowledge scope

Edit the `SYSTEM_PROMPT` variable in `app.py`. You can:
- Restrict it to specific software your company uses
- Add company-specific procedures and policies
- Change the response format
- Add your company name and branding to responses

### Change the model

In `app.py`, change the model string:
```python
model="claude-sonnet-4-20250514"   # Fast and capable (default)
model="claude-opus-4-20250514"     # Most capable, slower
model="claude-haiku-4-5-20251001"  # Fastest, most affordable
```

### Add authentication

To restrict access to your team, add Flask-Login or a simple password check before serving the index route.

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `anthropic` | ≥0.40.0 | Claude API client |
| `flask` | ≥3.0.0 | Web framework |
| `python-dotenv` | ≥1.0.0 | Load `.env` file |

---

## 🤝 Contributing

Pull requests are welcome! To contribute:

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## ⭐ Support

If this helped you, please give the repo a star on GitHub — it helps others find it!

Built with ❤️ using [Claude by Anthropic](https://anthropic.com)
