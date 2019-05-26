# Python Server Framework.
# xmlrpc.client — XML-RPC client access.
# XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport.
# With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
# This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and
# XML on the wire.
#
# ProtocolError Objects
# class xmlrpc.client.ProtocolError 
# A ProtocolError object describes a protocol error in the underlying transport layer (such as a 404 ‘not found’ error if the server named
# by the URI does not exist). It has the following attributes:
# url 
# The URI or URL that triggered the error.
# errcode 
# The error code.
# errmsg 
# The error message or diagnostic string.
# headers 
# A dict containing the headers of the HTTP/HTTPS request that triggered the error.
# 
# In the following example we’re going to intentionally cause a ProtocolError by providing an invalid URI:
# 

import xmlrpc.client

# create a ServerProxy with a URI that doesn't respond to XMLRPC requests

proxy = xmlrpc.client.ServerProxy("http://google.com/")

try:
    proxy.some_method()

except xmlrpc.client.ProtocolError as err:

    print("A protocol error occurred")
    print("URL: %s" % err.url)

    print("HTTP/HTTPS headers: %s" % err.headers)
    print("Error code: %d" % err.errcode)

    print("Error message: %s" % err.errmsg)
