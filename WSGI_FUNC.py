from wsgiref.simple_server import make_server
from hello import application


httpd=make_server('',6666,application)
print "Serving HTTP on port 6666..."
httpd.serve_forever()
