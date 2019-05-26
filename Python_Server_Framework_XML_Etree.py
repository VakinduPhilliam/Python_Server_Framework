# Python Server Framework.
# xml.etree.ElementTree — The ElementTree XML API.
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
# Element.findall() finds only elements with a tag which are direct children of the current element.
# Element.find() finds the first child with a particular tag, and Element.text accesses the element’s text content.
# Element.get() accesses the element’s attributes:
 
for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')

        print(name, rank)

#
# OUTPUT:
#
# Liechtenstein 1
# Singapore 4
# Panama 68
#

