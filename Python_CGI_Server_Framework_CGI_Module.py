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
# Using the cgi module
# 
# Begin by writing import cgi.
# 
# When you write a new script, consider adding these lines:
# 

import cgitb

cgitb.enable()

# 
# This activates a special exception handler that will display detailed reports in the Web browser if any errors occur.
# If you’d rather not show the guts of your program to users of your script, you can have the reports saved to files instead, with code like this:
# 

import cgitb

cgitb.enable(display=0, logdir="/path/to/logdir")
