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
# If the submitted form data contains more than one field with the same name, the object retrieved by form[key] is not a FieldStorage or MiniFieldStorage
# instance but a list of such instances. Similarly, in this situation, form.getvalue(key) would return a list of strings.
# If you expect this possibility (when your HTML form contains multiple fields with the same name), use the getlist() method, which always returns a list
# of values (so that you do not need to special-case the single item case). For example, this code concatenates any number of username fields, separated by
# commas:
# 

value = form.getlist("username")
usernames = ",".join(value)

# 
# If a field represents an uploaded file, accessing the value via the value attribute or the getvalue() method reads the entire file in memory as bytes.
# This may not be what you want. You can test for an uploaded file by testing either the filename attribute or the file attribute.
# You can then read the data from the file attribute before it is automatically closed as part of the garbage collection of the FieldStorage instance
# (the read() and readline() methods will return bytes):
# 

fileitem = form["userfile"]

if fileitem.file:

    # It's an uploaded file; count lines

    linecount = 0

    while True:
        line = fileitem.file.readline()

        if not line: break
        linecount = linecount + 1
 
#
# FieldStorage objects also support being used in a with statement, which will automatically close them when done.
#
