from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<h1>Top Five Web Application Frameworks</h1>
<h2>1.Django</h2>
</body>
</html>
'''


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my web server")
server_address =('',80)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever() 