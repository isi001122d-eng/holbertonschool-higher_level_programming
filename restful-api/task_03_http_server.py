#!/usr/bin/python3
"""
Standart http.server modulu ilə sadə API serveri
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """HTTP sorğularını idarə edən sinif"""

    def do_GET(self):
        """GET sorğularını emal edir"""
        
        # 1. Ana səhifə endpoint-i
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. JSON data endpoint-i
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # 3. Status endpoint-i
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. Info endpoint-i (Expected Output-da qeyd olunub)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # 5. 404 Error Handling
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Serveri işə salan funksiya"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server {port} portunda işləyir...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
