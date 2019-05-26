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
# Using the methods getfirst() and getlist() provided by this higher level interface.
# FieldStorage.getfirst(name, default=None) 
# This method always returns only one value associated with form field name. The method returns only the first value in case that more values were posted
# under such name. Please note that the order in which the values are received may vary from browser to browser and should not be counted on. 
# If no such form field or value exists then the method returns the value specified by the optional parameter default.
# This parameter defaults to None if not specified.
# FieldStorage.getlist(name) 
# This method always returns a list of values associated with form field name. The method returns an empty list if no such form field or value exists for 
# name. It returns a list consisting of one item if only one such value exists.
# 
# Using these methods you can write nice compact code:
# 

import cgi

form = cgi.FieldStorage()

user = form.getfirst("user", "").upper()    # This way it's safe.

for item in form.getlist("item"):
    do_something(item)
