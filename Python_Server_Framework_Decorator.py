# Python Server Framework
# Python xmlrpc.server — Basic XML-RPC servers
# The xmlrpc.server module provides a basic server framework for XML-RPC servers written in Python.
# Servers can either be free standing, using SimpleXMLRPCServer, or embedded in a CGI environment, using CGIXMLRPCRequestHandler.
# SimpleXMLRPCRequestHandler.rpc_paths. 
# An attribute value that must be a tuple listing valid path portions of the URL for receiving XML-RPC requests.
# Requests posted to other paths will result in a 404 “no such page” HTTP error. If this tuple is empty, all paths will be considered valid.
# The default value is ('/', '/RPC2').
#
# register_function() can also be used as a decorator. 
#
# A server framework can register functions in a decorator way:
# 

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.

    server.register_function(pow)

    # Register a function under a different name, using
    # register_function as a decorator. *name* can only be given
    # as a keyword argument.

    @server.register_function(name='add')

    def adder_function(x, y):
        return x + y

    # Register a function under function.__name__.

    @server.register_function

    def mul(x, y):
        return x * y

    server.serve_forever()
