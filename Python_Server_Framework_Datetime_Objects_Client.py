# Python Server Framework.
# xmlrpc.client — XML-RPC client access.
# XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport.
# With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
# This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and
# XML on the wire.
#
# DateTime Objects
# class xmlrpc.client.DateTime 
# This class may be initialized with seconds since the epoch, a time tuple, an ISO 8601 time/date string, or a datetime.datetime instance.
# It has the following methods, supported mainly for internal use by the marshalling/unmarshalling code:
# decode(string) 
# Accept a string as the instance’s new time value.
# encode(out) 
# Write the XML-RPC encoding of this DateTime item to the out stream object.
# It also supports certain of Python’s built-in operators through rich comparison and __repr__() methods.
# 
# The Client code:
# 
# The client code for the preceding server:
# 

import xmlrpc.client
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

today = proxy.today()

# convert the ISO8601 string to a datetime object

converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")

print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M"))
