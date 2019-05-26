# Python Web Server Framework
# wsgiref � WSGI Utilities and Reference Implementation
# The Web Server Gateway Interface (WSGI) is a standard interface between web server software and web applications written in Python.
# Having a standard interface makes it easy to use an application that supports WSGI with a number of different web servers.
#
# wsgiref.validate.validator(application). 
# Wrap application and return a new WSGI application object. The returned application will forward all requests to the original application, and will
# check that both the application and the server invoking it are conforming to the WSGI specification and to RFC 2616.
# Any detected nonconformance results in an AssertionError being raised; note, however, that how these errors are handled is server-dependent.
# For example, wsgiref.simple_server and other servers based on wsgiref.handlers (that don�t override the error handling methods to do something else) will
# simply output a message that an error has occurred, and dump the traceback to sys.stderr or some other error stream.
# 
# This wrapper may also generate output using the warnings module to indicate behaviors that are questionable but which may not actually be prohibited by
# PEP 3333. Unless they are suppressed using Python command-line options or the warnings API, any such warnings will be written to sys.stderr
# (not wsgi.errors, unless they happen to be the same object).
# 
# Example usage:
# 

from wsgiref.validate import validator
from wsgiref.simple_server import make_server

# Our callable object which is intentionally not compliant to the
# standard, so the validator is going to break

def simple_app(environ, start_response):
    status = '200 OK'  # HTTP Status

    headers = [('Content-type', 'text/plain')]  # HTTP Headers
    start_response(status, headers)

    # This is going to break because we need to return a list, and
    # the validator is going to inform us

    return b"Hello World"

# This is the application wrapped in a validator

validator_app = validator(simple_app)

with make_server('', 8000, validator_app) as httpd:
    print("Listening on port 8000....")

    httpd.serve_forever()
