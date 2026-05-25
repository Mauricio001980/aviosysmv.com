"""AvioSysMV website — local dev server.  python3 serve.py"""
import http.server, socketserver, os, socket

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def free_port(start=8082, end=8099):
    for p in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", p)); return p
            except OSError:
                continue
    raise RuntimeError("No free port found in range 8082-8099")

PORT = free_port()

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as s:
    s.allow_reuse_address = True
    url = f"http://localhost:{PORT}/index.html"
    print(f"\n  AvioSysMV website → {url}")
    print(f"  Ctrl+C to stop.\n")
    try:
        s.serve_forever()
    except KeyboardInterrupt:
        print("Stopped.")
