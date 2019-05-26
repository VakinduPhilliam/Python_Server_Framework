# Python Server Framework
# Python xmlrpc.server — Basic XML-RPC servers
# The xmlrpc.server module provides a basic server framework for XML-RPC servers written in Python.
# Servers can either be free standing, using SimpleXMLRPCServer, or embedded in a CGI environment, using CGIXMLRPCRequestHandler.
# SimpleXMLRPCRequestHandler.rpc_paths. 
# An attribute value that must be a tuple listing valid path portions of the URL for receiving XML-RPC requests.
# Requests posted to other paths will result in a 404 “no such page” HTTP error. If this tuple is empty, all paths will be considered valid.
# The default value is ('/', '/RPC2').
#
# The client that interacts with the above server is included in Lib/xmlrpc/client.py:
# 

server = ServerProxy("http://localhost:8000")

try:
    print(server.currentTime.getCurrentTime())

except Error as v:
    print("ERROR", v)

multi = MultiCall(server)
multi.getData()

multi.pow(2,9)
multi.add(1,2)

try:
    for response in multi():
        print(response)

except Error as v:
    print("ERROR", v)

#
#
# This client which interacts with the demo XMLRPC server can be invoked as:
#
# 

python -m xmlrpc.client
