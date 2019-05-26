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
# Higher Level Interface:
# 
# This section describes a higher level interface which was added to this class to allow one to do it in a more readable and intuitive way.
# The interface doesn’t make the techniques described in previous sections obsolete — they are still useful to process file uploads efficiently, for
# example.
# 
# The interface consists of two simple methods. Using the methods you can process form data in a generic way, without the need to worry whether only one
# or more values were posted under one name.
# 

item = form.getvalue("item")

if isinstance(item, list):

    # The user is requesting more than one item.

else:

    # The user is requesting only one item.
 
#
# This situation is common for example when a form contains a group of multiple checkboxes with the same name:
# 

# <input type="checkbox" name="item" value="1" />
# <input type="checkbox" name="item" value="2" />
 
#
# In most situations, however, there’s only one form control with a particular name in a form and then you expect and need only one value associated with
# this name. So you write a script containing for example this code:
# 

user = form.getvalue("user").upper()
