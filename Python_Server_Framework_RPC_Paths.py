# Python Server Framework
# Python xmlrpc.server — Basic XML-RPC servers
# The xmlrpc.server module provides a basic server framework for XML-RPC servers written in Python.
# Servers can either be free standing, using SimpleXMLRPCServer, or embedded in a CGI environment, using CGIXMLRPCRequestHandler.
# SimpleXMLRPCRequestHandler.rpc_paths. 
# An attribute value that must be a tuple listing valid path portions of the URL for receiving XML-RPC requests.
# Requests posted to other paths will result in a 404 “no such page” HTTP error. If this tuple is empty, all paths will be considered valid.
# The default value is ('/', '/RPC2').
#
# The following example included in the Lib/xmlrpc/server.py module shows a server allowing dotted names and registering a multicall function.
# 
# Warning:
# 
# Enabling the allow_dotted_names option allows intruders to access your module’s global variables and may allow intruders to execute arbitrary
# code on your machine. Only use this example only within a secure, closed network.
# 

import datetime

class ExampleService:

    def getData(self):
        return '42'

    class currentTime:

        @staticmethod

        def getCurrentTime():
            return datetime.datetime.now()

with SimpleXMLRPCServer(("localhost", 8000)) as server:

    server.register_function(pow)
    server.register_function(lambda x,y: x+y, 'add')

    server.register_instance(ExampleService(), allow_dotted_names=True)
    server.register_multicall_functions()

    print('Serving XML-RPC on localhost port 8000')

    try:
        server.serve_forever()

    except KeyboardInterrupt:

        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)
