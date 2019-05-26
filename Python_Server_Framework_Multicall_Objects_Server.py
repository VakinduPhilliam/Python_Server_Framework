# Python Server Framework.
# xmlrpc.client — XML-RPC client access.
# XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport.
# With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
# This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and
# XML on the wire.
#
# MultiCall Objects:
# 
# The MultiCall object provides a way to encapsulate multiple calls to a remote server into a single request [1].
# class xmlrpc.client.MultiCall(server) 
# Create an object used to boxcar method calls. server is the eventual target of the call. Calls can be made to the result object, but
# they will immediately return None, and only store the call name and parameters in the MultiCall object. Calling the object itself causes
# all stored calls to be transmitted as a single system.multicall request. The result of this call is a generator; iterating over this generator
# yields the individual results.
#
# The server code:
# 

from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

# A simple server with simple arithmetic functions

server = SimpleXMLRPCServer(("localhost", 8000))

print("Listening on port 8000...")

server.register_multicall_functions()
server.register_function(add, 'add')

server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')

server.register_function(divide, 'divide')
server.serve_forever()
