import os
import errno

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from datetime import datetime

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()

        now = datetime.now()
        date = now.strftime('%Y-%m-%d-%H:%M:%S')
        filename = '/home/pi/http/' + self.client_address[0] + '/' + date + '.csv'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(body.decode("utf-8"))

        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
