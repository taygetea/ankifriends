from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
import urlparse

def serverrunner():
    server_address = ('', 4545)
    httpd = BaseHTTPServer.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print httpd.socket.getsockname()[:2]
    httpd.handle_request()
    print httpd.__dict__.keys()
    # return HandlerClass.GetQueryParams()
if __name__ == '__main__':
    serverrunner()
