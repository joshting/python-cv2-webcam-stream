import threading
import http.server
import socketserver

class HttpServer:

    def singleStaticPage(self):
        self.handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", 8080), self.handler) as httpd:
            self.httpd = httpd
            self.httpd.serve_forever()

    def __init__(self):
        self.httpserver = None

    def __del__(self):
        self.httpd.shutdown()

    def start(self):
        if self.httpserver is None:
            self.httpserver = threading.Thread(target=self.singleStaticPage)
            self.httpserver.start()

    def stop(self):
        if(self.httpd != None):
            self.httpd.shutdown()
        self.httpserver.join()
        self.httpserver = None


