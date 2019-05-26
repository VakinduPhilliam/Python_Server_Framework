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
# The following code (which assumes that the Content-Type header and blank line have already been printed) checks that the fields name and addr are
# both set to a non-empty string:
# 

form = cgi.FieldStorage()

if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")

    print("Please fill in the name and addr fields.")

    return
print("<p>name:", form["name"].value)
print("<p>addr:", form["addr"].value)

# ...further form processing here...
