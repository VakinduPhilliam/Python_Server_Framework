# Python Web Server Framework
# wsgiref — WSGI Utilities and Reference Implementation
# The Web Server Gateway Interface (WSGI) is a standard interface between web server software and web applications written in Python.
# Having a standard interface makes it easy to use an application that supports WSGI with a number of different web servers.
#
# wsgiref.simple_server – a simple WSGI HTTP server.
# 
# This module implements a simple HTTP server (based on http.server) that serves WSGI applications.
# Each server instance serves a single WSGI application on a given host and port. If you want to serve multiple applications on a single host
# and port, you should create a WSGI application that parses PATH_INFO to select which application to invoke for each request. (E.g., using the
# shift_path_info() function from wsgiref.util.)
# wsgiref.simple_server.make_server(host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler).
# Create a new WSGI server listening on host and port, accepting connections for app. The return value is an instance of the supplied server_class, and
# will process requests using the specified handler_class. app must be a WSGI application object, as defined by PEP 3333.
# 
# Example usage:
# 

from wsgiref.simple_server import make_server, demo_app

with make_server('', 8000, demo_app) as httpd:
    print("Serving HTTP on port 8000...")

    # Respond to requests until process is killed

    httpd.serve_forever()

    # Alternative: serve one request, then exit

    httpd.handle_request()
