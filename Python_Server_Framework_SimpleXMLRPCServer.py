# Python Server Framework.
# xmlrpc.client — XML-RPC client access.
# XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport.
# With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
# This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and
# XML on the wire.
#
# ServerProxy Objects:
# 
# A ServerProxy instance has a method corresponding to each remote procedure call accepted by the XML-RPC server.
# Calling the method performs an RPC, dispatched by both name and argument signature (e.g. the same method name can be overloaded with
# multiple argument signatures). The RPC finishes by returning a value, which may be either returned data in a conformant type or a Fault
# or ProtocolError object indicating an error.
#
# The server code:
# 

from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n % 2 == 0

server = SimpleXMLRPCServer(("localhost", 8000))

print("Listening on port 8000...")

server.register_function(is_even, "is_even")
server.serve_forever()
