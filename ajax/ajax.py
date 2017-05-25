from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SimpleHTTPServer

PORT = 10114

class AjaxHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Access-Control-Allow-Original','*')
        self.end_headers()
        self.wfile.write("Arturs Nikulins, 161REB114")
        return
try:
    server = HTTPServer(('',PORT), AjaxHandler)
    print'Startet Ajax handler porta', PORT
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
