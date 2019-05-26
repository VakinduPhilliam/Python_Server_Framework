# Python Server Framework
# Python xmlrpc.server — Basic XML-RPC servers
# The xmlrpc.server module provides a basic server framework for XML-RPC servers written in Python.
# Servers can either be free standing, using SimpleXMLRPCServer, or embedded in a CGI environment, using CGIXMLRPCRequestHandler.
# SimpleXMLRPCRequestHandler.rpc_paths. 
# An attribute value that must be a tuple listing valid path portions of the URL for receiving XML-RPC requests.
# Requests posted to other paths will result in a 404 “no such page” HTTP error. If this tuple is empty, all paths will be considered valid.
# The default value is ('/', '/RPC2').
#
# CGIXMLRPCRequestHandler.handle_request(request_text=None) .
# Handle an XML-RPC request.
# If request_text is given, it should be the POST data provided by the HTTP server, otherwise the contents of stdin will be used.
# 
#
# Example:
# 

class MyFuncs:

    def mul(self, x, y):
        return x * y

handler = CGIXMLRPCRequestHandler()
handler.register_function(pow)

handler.register_function(lambda x,y: x+y, 'add')
handler.register_introspection_functions()

handler.register_instance(MyFuncs())
handler.handle_request()
