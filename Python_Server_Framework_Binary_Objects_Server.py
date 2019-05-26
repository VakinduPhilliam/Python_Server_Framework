# Python Server Framework.
# xmlrpc.client — XML-RPC client access.
# XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport.
# With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
# This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and
# XML on the wire.
#
# Binary Objects
# class xmlrpc.client.Binary 
# This class may be initialized from bytes data (which may include NULs). The primary access to the content of a Binary object is provided
# by an attribute:
# data 
# The binary data encapsulated by the Binary instance. The data is provided as a bytes object.
# 
# Binary objects have the following methods, supported mainly for internal use by the marshalling/unmarshalling code:
# decode(bytes) 
# Accept a base64 bytes object and decode it as the instance’s new data.
# encode(out) 
# Write the XML-RPC base 64 encoding of this binary item to the out stream object.
# 
# The encoded data will have newlines every 76 characters as per RFC 2045 section 6.8, which was the de facto standard base64 specification
# when the XML-RPC spec was written.
# 
# It also supports certain of Python’s built-in operators through __eq__() and __ne__() methods.
# 
# Example usage of the binary objects. We’re going to transfer an image over XMLRPC:
# 
# Server Code:
#

from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def python_logo():

    with open("python_logo.jpg", "rb") as handle:

        return xmlrpc.client.Binary(handle.read())

server = SimpleXMLRPCServer(("localhost", 8000))

print("Listening on port 8000...")

server.register_function(python_logo, 'python_logo')

server.serve_forever()
