#!/usr/bin/env python3
"""A simple API built with http.server."""

import http.server
import json

class SimpleServer(http.server.BaseHTTPRequestHandler):
    """Handles HTTP requests"""

    def do_GET(self):
        """called when server gets GET requests"""
        if self.path =="/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run():
    """Start the server on port 8000"""
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleServer)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
