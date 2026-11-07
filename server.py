import http.server
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        path = self.path.split("?", 1)[0].rstrip("/")
        if path == "/app":
            self.path = "/app.html"
        return super().do_GET()

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    os.chdir(ROOT)
    http.server.ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
