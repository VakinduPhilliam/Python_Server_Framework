# Python XDR Framework
# xdrlib — Encode and decode XDR data
# It supports most of the data types described in the RFC.
# The xdrlib module defines two classes, one for packing variables into XDR representation, and another for unpacking from XDR representation.
# There are also two exception classes.
# class xdrlib.Packer 
# Packer is the class for packing data into XDR representation. The Packer class is instantiated with no arguments.
# class xdrlib.Unpacker(data) 
# Unpacker is the complementary class which unpacks XDR data values from a string buffer. The input buffer is given as data.
# Packer.pack_list(list, pack_item) 
# Packs a list of homogeneous items. This method is useful for lists with an indeterminate size; i.e. the size is not available until the entire
# list has been walked. For each item in the list, an unsigned integer 1 is packed first, followed by the data value from the list. pack_item is
# the function that is called to pack the individual item. At the end of the list, an unsigned integer 0 is packed.
# 
# For example, to pack a list of integers, the code might appear like this:
# 

import xdrlib

p = xdrlib.Packer()
p.pack_list([1, 2, 3], p.pack_int)
