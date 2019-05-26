# Python Server Framework.
# xml.etree.ElementTree — The ElementTree XML API.
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#
# Finding interesting elements. 
# Element has some useful methods that help iterate recursively over all the sub-tree below it (its children, their children, and so on).
# For example, Element.iter():
 
for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)

# OUTPUT:
#
# {'name': 'Austria', 'direction': 'E'}
# {'name': 'Switzerland', 'direction': 'W'}
# {'name': 'Malaysia', 'direction': 'N'}
# {'name': 'Costa Rica', 'direction': 'W'}
# {'name': 'Colombia', 'direction': 'E'}
#

