from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
import urlparse

class CallStash:
    def __init__(self, c):
        self.c = c
        self.rv = None
    def __call__(self, *args, **kwargs):
        self.rv = rv = self.c(*args, **kwargs)
        return rv

def serverrunner():
    chrh_builder = CallStash(SimpleHTTPRequestHandler)
    rh = chrh_builder.rv
    server_address = ('', 4545)
    httpd = BaseHTTPServer.HTTPServer(server_address, chrh_builder)
    print "name: ", httpd.socket.getsockname()[:2]
    httpd.handle_request()
    print "keys: ", httpd.__dict__.keys()
    return rh.GetQueryParams()
if __name__ == '__main__':
    serverrunner()
