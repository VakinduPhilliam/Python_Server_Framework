# Python Server Framework.
# xmlrpc.client — XML-RPC client access.
# XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport.
# With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
# This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and
# XML on the wire.
#
# The client code for the preceding server:
# 

import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:

    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))
