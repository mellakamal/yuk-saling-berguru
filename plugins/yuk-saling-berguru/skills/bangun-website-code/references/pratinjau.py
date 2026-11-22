#!/usr/bin/env python3
"""Pratinjau lokal web statis dengan alamat tanpa .html, seperti setelah tayang.
Pakai: python3 -I references/pratinjau.py FOLDER_WEB [PORT]
Hanya memakai pustaka bawaan Python. Hentikan dengan Ctrl+C."""
import functools, http.server, io, os, sys

root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        local = self.translate_path(path)
        if not os.path.exists(local):
            alt = local.rstrip(os.sep) + ".html"
            if os.path.isfile(alt):
                self.path = path.rstrip("/") + ".html"
            else:
                page = os.path.join(root, "404.html")
                body = open(page, "rb").read() if os.path.isfile(page) else b"404"
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                return io.BytesIO(body)
        return super().send_head()


handler = functools.partial(Handler, directory=root)
with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as server:
    print("Pratinjau: http://localhost:%d/" % port)
    server.serve_forever()
