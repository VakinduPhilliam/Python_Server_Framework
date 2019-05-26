# Python Server Framework.
# xmlrpc.client — XML-RPC client access.
# XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport.
# With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
# This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and
# XML on the wire.
#
# Convenience Functions:
# xmlrpc.client.dumps(params, methodname=None, methodresponse=None, encoding=None, allow_none=False)
# Convert params into an XML-RPC request. or into a response if methodresponse is true. params can be either a tuple of arguments or an
# instance of the Fault exception class. If methodresponse is true, only a single value can be returned, meaning that params must be of
# length 1. encoding, if supplied, is the encoding to use in the generated XML; the default is UTF-8.
# Python’s None value cannot be used in standard XML-RPC; to allow using it via an extension, provide a true value for allow_none.
# xmlrpc.client.loads(data, use_datetime=False, use_builtin_types=False) 
# Convert an XML-RPC request or response into Python objects, a (params, methodname). params is a tuple of argument; methodname is a string, or
# None if no method name is present in the packet. If the XML-RPC packet represents a fault condition, this function will raise a Fault exception.
# The use_builtin_types flag can be used to cause date/time values to be presented as datetime.datetime objects and binary data to be presented as
# bytes objects; this flag is false by default.
# 
# The obsolete use_datetime flag is similar to use_builtin_types but it applies only to date/time values.
# 
# Example of Client Usage
# 

# simple test program (from the XML-RPC specification)

from xmlrpc.client import ServerProxy, Error

# server = ServerProxy("http://localhost:8000") # local server

with ServerProxy("http://betty.userland.com") as proxy:

    print(proxy)

    try:
        print(proxy.examples.getStateName(41))

    except Error as v:
        print("ERROR", v)

