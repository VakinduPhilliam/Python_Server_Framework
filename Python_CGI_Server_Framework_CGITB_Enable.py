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
# Fortunately, once you have managed to get your script to execute some code, you can easily send tracebacks to the Web browser using the cgitb module.
# If you haven’t done so already, just add the lines: to the top of your script.
# Then try running it again; when a problem occurs, you should see a detailed report that will likely make apparent the cause of the crash.
 
import cgitb

cgitb.enable()
 
#
# If you suspect that there may be a problem in importing the cgitb module, you can use an even more robust approach (which only uses built-in modules):
# 

import sys

sys.stderr = sys.stdout

print("Content-Type: text/plain")
print()

# ...your code here...
