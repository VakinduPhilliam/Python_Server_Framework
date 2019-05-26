# Python Server Framework
# Python xmlrpc.server — Basic XML-RPC servers
# The xmlrpc.server module provides a basic server framework for XML-RPC servers written in Python.
# Servers can either be free standing, using SimpleXMLRPCServer, or embedded in a CGI environment, using CGIXMLRPCRequestHandler.
# SimpleXMLRPCRequestHandler.rpc_paths. 
# An attribute value that must be a tuple listing valid path portions of the URL for receiving XML-RPC requests.
# Requests posted to other paths will result in a 404 “no such page” HTTP error. If this tuple is empty, all paths will be considered valid.
# The default value is ('/', '/RPC2').
#
# Client Code
#
# The following client code will call the methods made available by the preceding server:
# 

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

print(s.pow(2,3))  # Returns 2**3 = 8

print(s.add(2,3))  # Returns 5
print(s.mul(5,2))  # Returns 5*2 = 10

# Print list of available methods

print(s.system.listMethods())
