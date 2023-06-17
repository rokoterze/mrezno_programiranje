from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()
        
        self.wfile.write(b"<html><head><title>Student Info</title></head>")
        self.wfile.write(b"<body><h1>Student Info</h1>")
        self.wfile.write(b"<form>")
        self.wfile.write(b"<label>Ime: <input type='text' name='ime'></label>")
        self.wfile.write(b"<label>Prezime: <input type='text' name='prezime'></label>")
        self.wfile.write(b"<label>Datum Rodenja: <input type='text' name='datum_rodenja'></label>")
        self.wfile.write(b"</form>")
        self.wfile.write(b"</body></html>")
        return


try:
    server = HTTPServer(('', PORT), Handler)
    print('Started http server on port ', PORT)
    
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, exiting and shutting down the web server!')
    server.socket.close()