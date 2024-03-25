from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Read the length of the data
        content_length = int(self.headers['Content-Length'])
        # Read the data
        post_data = self.rfile.read(content_length)

        # Try to parse the JSON data
        try:
            data = json.loads(post_data.decode())
            print(json.dumps(data, indent=4))  # Pretty print the received JSON data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        # Send a simple response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=12345):
    server_address = ('10.42.0.53', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
