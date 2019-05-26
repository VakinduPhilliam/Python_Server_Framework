# Python XDR Framework
# xdrlib — Encode and decode XDR data
# It supports most of the data types described in the RFC.
# The xdrlib module defines two classes, one for packing variables into XDR representation, and another for unpacking from XDR representation.
# There are also two exception classes.
# class xdrlib.Packer 
# Packer is the class for packing data into XDR representation. The Packer class is instantiated with no arguments.
# class xdrlib.Unpacker(data) 
# Unpacker is the complementary class which unpacks XDR data values from a string buffer. The input buffer is given as data.
#
# Exceptions:
# 
# Exceptions in this module are coded as class instances:
# exception xdrlib.Error. 
# The base exception class. Error has a single public attribute msg containing the description of the error.
# exception xdrlib.ConversionError. 
# Class derived from Error. Contains no additional instance variables.
# 
# Here is an example of how you would catch one of these exceptions:
# 

import xdrlib

p = xdrlib.Packer()

try:
    p.pack_double(8.01)

except xdrlib.ConversionError as instance:
    print('packing the double failed:', instance.msg)
