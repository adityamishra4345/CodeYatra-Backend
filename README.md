📌 What is QR Shield?
QR Shield is a browser-based security web app that protects users from modern phishing attacks — suspicious messages, malicious URLs, and dangerous QR codes — all without installing anything. Just open the browser and you're protected.
Phishing has evolved. Beyond emails, attackers now use:

SMS phishing — fake texts impersonating banks or services
Malicious links — credential-stealing URLs disguised as real websites
Quishing — QR codes that silently redirect to harmful sites or trigger downloads

QR Shield fights all three.

✨ Features
1. 📝 Text Analyser
Paste any SMS, email, or message and get an instant verdict.

Detects OTP harvesting — messages trying to steal one-time passwords
Flags social engineering — urgency tactics and fake authority impersonation
Catches brand spoofing — fake messages from banks, retailers, or government agencies
Returns verdict: Safe / Suspicious / Phishing

2. 🔗 URL Detector
Never click a suspicious link blindly again.

Domain verification — checks if the site is real, fake, or a known scam
Typosquatting detection — catches domains mimicking real brands (e.g. paypa1.com)
SSL & WHOIS checks — flags missing certificates and freshly registered domains
Redirect tracing — follows link chains to reveal the true destination

3. 📷 Secure QR Scanner ⭐ Main Feature
This is what sets QR Shield apart from every other QR scanner.
The problem with standard QR scanners:
The moment you scan, your device immediately connects to the encoded URL — you're already at the malicious site before you even know what you scanned.
How QR Shield is different:

You scan the QR code in the app
QR decoded → URL extracted
Our server sends the request — your device never connects
Every redirect hop is followed and inspected
App-install attempts and malicious payloads are detected
Verdict returned: Safe / Risky / Block


🔒 Your device is never exposed. All scanning happens server-side in an isolated environment.


🌐 The WebApp Advantage
FeatureTraditional AppsQR ShieldInstallation required✅ Yes❌ NoStorage used✅ Yes❌ ZeroThreat updatesManual✅ AutomaticWorks on all devicesVaries✅ Mobile, tablet, desktopQR device exposure✅ Exposed❌ Server-side only

🚀 Getting Started
No installation needed. Just visit:
https://action-kamen-frontend.vercel.app
Or run locally:
Prerequisites

Node.js v18+
Python 3.10+

Installation
bash# Clone the repository
git clone https://github.com/CodeYatra/qr-shield.git
cd qr-shield

# Install frontend dependencies
cd frontend
npm install
npm run dev

# Install backend dependencies
cd ../backend
pip install -r requirements.txt
python app.py

🛠️ Tech Stack
LayerTechnologyFrontendReact, Tailwind CSS, Camera APIBackendNode.js / Python FastAPIAnalysis EngineNLP Model, URL Crawler, Sandbox RunnerDatabase & CacheMongoDB, RedisDeploymentVercel (frontend)

🎯 Real-World Use Cases

Suspicious bank email? → Paste into Text Analyser to detect OTP harvesting before responding
Got a link from a hacked account? → Run it through URL Detector before clicking
Scanning a public QR code (restaurant, parking meter, flyer)? → Use Secure QR Scanner with zero device exposure


🆚 QR Shield vs Traditional Tools
FeatureTraditional ScannersQR ShieldText phishing detectionPartial (keyword only)✅ Full NLP analysisURL reputation checkBasic✅ Live + redirect-awareQR code scanningJust opens URL✅ Full sandbox crawlRedirect chain inspection❌ No✅ All hops scannedDevice protection (QR)❌ Device exposed✅ Server-side onlyApp install detection❌ No✅ YesOTP harvest detection❌ No✅ Yes

👥 Team
CodeYatra
Built with ❤️ as part of a hackathon project focused on making everyday digital interactions safer for everyone.
