# Python CGI Server Framework.
# cgi — Common Gateway Interface support. 
# Support module for Common Gateway Interface (CGI) scripts.
# This module defines a number of utilities for use by CGI scripts written in Python.
#
# A CGI script is invoked by an HTTP server, usually to process user input submitted through an HTML <FORM> or <ISINDEX> element.
# 
# Most often, CGI scripts live in the server’s special cgi-bin directory. The HTTP server places all sorts of information about the request
# (such as the client’s hostname, the requested URL, the query string, and lots of other goodies) in the script’s shell environment, executes
# the script, and sends the script’s output back to the client.
#
# If you need to load modules from a directory which is not on Python’s default module search path, you can change the path in your script, before
# importing other modules.
#
# For example:
# 

import sys

sys.path.insert(0, "/usr/home/joe/lib/python")

sys.path.insert(0, "/usr/local/lib/python")
