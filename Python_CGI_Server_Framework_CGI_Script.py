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

# The output of a CGI script should consist of two sections, separated by a blank line.
# The first section contains a number of headers, telling the client what kind of data is following. Python code to generate a minimal header
# section looks like this:
# 

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

# 
# The second section is usually HTML, which allows the client software to display nicely formatted text with header, in-line images, etc.
# Here’s Python code that prints a simple piece of HTML:
# 

print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")

print("Hello, world!")
