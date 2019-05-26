# Python Web Server Framework
# wsgiref — WSGI Utilities and Reference Implementation
# The Web Server Gateway Interface (WSGI) is a standard interface between web server software and web applications written in Python.
# Having a standard interface makes it easy to use an application that supports WSGI with a number of different web servers.
# class wsgiref.util.FileWrapper(filelike, blksize=8192) 
# A wrapper to convert a file-like object to an iterator. The resulting objects support both __getitem__() and __iter__() iteration styles, for
# compatibility with Python 2.1 and Jython. As the object is iterated over, the optional blksize parameter will be repeatedly passed to the filelike
# object’s read() method to obtain bytestrings to yield. When read() returns an empty bytestring, iteration is ended and is not resumable.
# If filelike has a close() method, the returned object will also have a close() method, and it will invoke the filelike object’s close() method when
# called.
# 
# Example usage:
# 

from io import StringIO
from wsgiref.util import FileWrapper

# We're using a StringIO-buffer for as the file-like object

filelike = StringIO("This is an example file-like object"*10)
wrapper = FileWrapper(filelike, blksize=5)

for chunk in wrapper:
    print(chunk)
