# Python Server Framework.
# xml.etree.ElementTree — The ElementTree XML API.
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#
# XML elements with no subelements will test as False. This behavior will change in future versions. Use specific len(elem) or elem is
# None test instead.
# 

element = root.find('foo')

if not element:  # careful!
    print("element not found, or element has no subelements")

if element is None:
    print("element not found")
