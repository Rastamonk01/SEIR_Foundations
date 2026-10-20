#!/bin/bash
# =====================================================================
#  SEIR Foundations - Custom Website User Data (Amazon Linux 2023)
#  Paste this ENTIRE file into: EC2 > Advanced details > User data
#
#  What it builds:
#    /             Home page
#    /about        About page
#    /calculator   DYNAMIC page - the server does the maths you submit
#    /server       DYNAMIC page - live info about this EC2 instance
#
#  Needs: security group inbound rule HTTP (TCP 80) from your IP
#  No packages to install - uses the Python 3 already on AL2023.
# =====================================================================
set -euo pipefail

mkdir -p /opt/seir_foundations

cat > /opt/seir_foundations/app.py <<'PY'
#!/usr/bin/env python3
"""Tiny 4-page website using only the Python standard library."""
import html
import os
import socket
import urllib.request
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs

PORT = int(os.environ.get("PORT", "80"))

CSS = """
:root{--bg:#0f172a;--card:#1e293b;--text:#e2e8f0;--muted:#94a3b8;--accent:#38bdf8}
*{box-sizing:border-box}
body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
nav{background:var(--card);padding:14px 20px;display:flex;gap:18px;flex-wrap:wrap;align-items:center}
nav b{color:var(--accent);margin-right:auto}
nav a{color:var(--text);text-decoration:none}
nav a:hover,nav a.on{color:var(--accent)}
main{max-width:760px;margin:32px auto;padding:0 16px}
.card{background:var(--card);border-radius:12px;padding:20px 24px;margin:16px 0}
h1{margin-top:0}
.muted{color:var(--muted)}
input,select,button{font-size:1rem;padding:8px 10px;border-radius:8px;border:1px solid #475569;background:#0b1220;color:var(--text)}
button{background:var(--accent);color:#0f172a;border:0;font-weight:600;cursor:pointer}
form{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.result{font-size:1.6rem;color:var(--accent);font-weight:700}
.error{color:#f87171}
table{width:100%;border-collapse:collapse}
td{padding:6px 0;border-bottom:1px solid #334155}
td:first-child{color:var(--muted);width:40%}
footer{text-align:center;color:var(--muted);font-size:.85rem;margin:40px 0}
"""

PAGES = [("/", "Home"), ("/about", "About"), ("/calculator", "Calculator"), ("/server", "Server Info")]


def layout(path, title, body):
    links = "".join(
        f'<a href="{p}" class="{"on" if p == path else ""}">{n}</a>' for p, n in PAGES
    )
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | My EC2 Site</title><style>{CSS}</style></head><body>
<nav><b>&#9729; My EC2 Site</b>{links}</nav>
<main>{body}</main>
<footer>Served by <b>{html.escape(socket.gethostname())}</b> on Amazon EC2</footer>
</body></html>"""


def imds(path):
    """Read EC2 instance metadata using IMDSv2. Returns 'unavailable' off-EC2."""
    try:
        req = urllib.request.Request(
            "http://169.254.169.254/latest/api/token", method="PUT",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "60"})
        token = urllib.request.urlopen(req, timeout=1).read().decode()
        req = urllib.request.Request(
            f"http://169.254.169.254/latest/meta-data/{path}",
            headers={"X-aws-ec2-metadata-token": token})
        return urllib.request.urlopen(req, timeout=1).read().decode()
    except Exception:
        return "unavailable"


def home():
    return """<div class="card"><h1>Hello from the cloud!</h1>
<p>This website is running on an <b>Amazon EC2</b> virtual server. It was set up
automatically by a <b>User Data</b> startup script the very first time the server booted &mdash;
nobody logged in to install anything.</p></div>
<div class="card"><h2>Try it out</h2><ul>
<li><a href="/calculator">Calculator</a> &ndash; the server does the maths for you (dynamic page)</li>
<li><a href="/server">Server Info</a> &ndash; live details about this exact EC2 instance</li>
<li><a href="/about">About</a> &ndash; how this site was built</li></ul></div>"""


def about():
    return """<div class="card"><h1>About this site</h1>
<p>Built for <b>SEIR Foundations, Module 1</b>.</p>
<table>
<tr><td>Server</td><td>Amazon EC2, Amazon Linux 2023</td></tr>
<tr><td>Web server</td><td>Python 3 standard library (no extra installs)</td></tr>
<tr><td>Kept running by</td><td>a systemd service called <code>seir_foundations</code></td></tr>
<tr><td>Installed by</td><td>an EC2 User Data script at first boot</td></tr>
</table></div>
<div class="card"><h2>Static vs dynamic</h2>
<p>A <b>static</b> page (like this one) sends the same HTML to everyone.
A <b>dynamic</b> page is built by the server at the moment you ask for it &mdash;
the Calculator and Server Info pages produce different output depending on what you type
or which server answers.</p></div>"""


OPS = {
    "add": ("+", lambda a, b: a + b),
    "sub": ("&minus;", lambda a, b: a - b),
    "mul": ("&times;", lambda a, b: a * b),
    "div": ("&divide;", lambda a, b: a / b),
}


def calculator(form=None):
    form = form or {}
    a = form.get("a", [""])[0]
    b = form.get("b", [""])[0]
    op = form.get("op", ["add"])[0]
    out = ""
    if form:
        try:
            x, y = float(a), float(b)
            if op not in OPS:
                raise ValueError("Unknown operation")
            sym, fn = OPS[op]
            if op == "div" and y == 0:
                raise ZeroDivisionError
            r = fn(x, y)
            r = int(r) if float(r).is_integer() else round(r, 6)
            fmt = lambda n: int(n) if n.is_integer() else n
            out = f'<p class="result">{fmt(x)} {sym} {fmt(y)} = {r}</p>'
        except ZeroDivisionError:
            out = '<p class="error">You can\'t divide by zero.</p>'
        except ValueError:
            out = '<p class="error">Please enter two valid numbers.</p>'
    opts = "".join(
        f'<option value="{k}" {"selected" if k == op else ""}>{s}</option>'
        for k, (s, _) in OPS.items())
    return f"""<div class="card"><h1>Calculator</h1>
<p class="muted">Your numbers are sent to the EC2 server, which works out the answer
and builds this page for you.</p>
<form method="post" action="/calculator">
<input name="a" inputmode="decimal" placeholder="First number" value="{html.escape(a)}" required>
<select name="op">{opts}</select>
<input name="b" inputmode="decimal" placeholder="Second number" value="{html.escape(b)}" required>
<button type="submit">Calculate</button></form>{out}</div>"""


def server_info():
    up = float(open("/proc/uptime").read().split()[0]) if os.path.exists("/proc/uptime") else 0
    h, m = int(up // 3600), int(up % 3600 // 60)
    rows = {
        "Hostname": socket.gethostname(),
        "Instance ID": imds("instance-id"),
        "Instance type": imds("instance-type"),
        "Availability Zone": imds("placement/availability-zone"),
        "Public IPv4": imds("public-ipv4"),
        "Server time (UTC)": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "Uptime": f"{h}h {m}m",
    }
    trs = "".join(f"<tr><td>{k}</td><td>{html.escape(v)}</td></tr>" for k, v in rows.items())
    return f"""<div class="card"><h1>Server Info</h1>
<p class="muted">Generated live each time you load the page. Refresh to see the time change.</p>
<table>{trs}</table></div>"""


ROUTES = {"/": ("Home", home), "/about": ("About", about),
          "/calculator": ("Calculator", calculator), "/server": ("Server Info", server_info)}


class Handler(BaseHTTPRequestHandler):
    def send_page(self, status, path, title, body):
        data = layout(path, title, body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/") or "/"
        if path in ROUTES:
            title, fn = ROUTES[path]
            self.send_page(200, path, title, fn())
        else:
            self.send_page(404, path, "Not found",
                           '<div class="card"><h1>404</h1><p>That page doesn\'t exist. '
                           '<a href="/">Go home</a></p></div>')

    def do_POST(self):
        if self.path.rstrip("/") != "/calculator":
            return self.do_GET()
        length = min(int(self.headers.get("Content-Length", 0) or 0), 10_000)
        form = parse_qs(self.rfile.read(length).decode(errors="replace"))
        self.send_page(200, "/calculator", "Calculator", calculator(form or {"a": [""]}))


if __name__ == "__main__":
    print(f"Serving on port {PORT}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
PY

# Run it as a service so it starts on every boot and restarts if it crashes.
cat > /etc/systemd/system/seir_foundations.service <<'UNIT'
[Unit]
Description=SEIR Foundations custom website
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/python3 /opt/seir_foundations/app.py
Restart=always
DynamicUser=yes
AmbientCapabilities=CAP_NET_BIND_SERVICE

[Install]
WantedBy=multi-user.target
UNIT

systemctl daemon-reload
systemctl enable --now seir_foundations.service

echo "SEIR website installed. Visit http://<public-ip>/"
