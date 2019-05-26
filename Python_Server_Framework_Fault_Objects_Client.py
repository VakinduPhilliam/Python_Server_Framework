# Python Server Framework.
# xmlrpc.client — XML-RPC client access.
# XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport.
# With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
# This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and
# XML on the wire.
#
# Fault Objects:
# class xmlrpc.client.Fault 
# A Fault object encapsulates the content of an XML-RPC fault tag. Fault objects have the following attributes:
#
# faultCode: 
# A string indicating the fault type.
#
# faultString: 
# A string containing a diagnostic message associated with the fault.
# 
# In the following example we’re going to intentionally cause a Fault by returning a complex type object.
#
# The Client code:
# 
# The client code for the preceding server:
# 

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

try:
    proxy.add(2, 5)

except xmlrpc.client.Fault as err:
    print("A fault occurred")

    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)

