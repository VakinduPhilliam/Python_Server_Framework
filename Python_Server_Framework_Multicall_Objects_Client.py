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
# The Client code:
# 
# The client code for the preceding server:
# 

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

multicall = xmlrpc.client.MultiCall(proxy)
multicall.add(7, 3)

multicall.subtract(7, 3)
multicall.multiply(7, 3)

multicall.divide(7, 3)

result = multicall()

print("7+3=%d, 7-3=%d, 7*3=%d, 7//3=%d" % tuple(result))
