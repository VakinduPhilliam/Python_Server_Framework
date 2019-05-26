# Python Web Server Framework
# wsgiref � WSGI Utilities and Reference Implementation
# The Web Server Gateway Interface (WSGI) is a standard interface between web server software and web applications written in Python.
# Having a standard interface makes it easy to use an application that supports WSGI with a number of different web servers.
#
# A working �Hello World� WSGI application:
# 

from wsgiref.simple_server import make_server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object (see PEP 333).

def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status

    headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers

    start_response(status, headers)

    # The returned object is going to be printed

    return [b"Hello World"]

with make_server('', 8000, hello_world_app) as httpd:
    print("Serving on port 8000...")

    # Serve until process is killed

    httpd.serve_forever()
