# Python Server Framework.
# xml.etree.ElementTree — The ElementTree XML API.
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#
# Parsing XML:
# 
# We’ll be using the following XML document as the sample data for this section:
# 

# <?xml version="1.0"?>
#
# <data>
#    <country name="Liechtenstein">
#        <rank>1</rank>
#        <year>2008</year>
#        <gdppc>141100</gdppc>
#        <neighbor name="Austria" direction="E"/>
#        <neighbor name="Switzerland" direction="W"/>
#    </country>
#    <country name="Singapore">
#        <rank>4</rank>
#        <year>2011</year>
#        <gdppc>59900</gdppc>
#        <neighbor name="Malaysia" direction="N"/>
#    </country>
#    <country name="Panama">
#        <rank>68</rank>
#        <year>2011</year>
#        <gdppc>13600</gdppc>
#        <neighbor name="Costa Rica" direction="W"/>
#        <neighbor name="Colombia" direction="E"/>
#    </country>
# </data>
 
#
# We can import this data by reading from a file:
# 

import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()
 
#
# Or directly from a string:
# 

root = ET.fromstring(country_data_as_string)

#
#
# fromstring() parses XML from a string directly into an Element, which is the root element of the parsed tree.
# Other parsing functions may create an ElementTree.
#
#
 
# As an Element, root has a tag and a dictionary of attributes:
 
root.tag

# OUTPUTS: 'data'

root.attrib

# OUTPUTS: '{}'
 
#
# It also has children nodes over which we can iterate:
# 

for child in root:
        print(child.tag, child.attrib)


#
# OUTPUTS:
#
# country {'name': 'Liechtenstein'}
# country {'name': 'Singapore'}
# country {'name': 'Panama'}
#

# 
# Children are nested, and we can access specific child nodes by index:
# 

root[0][1].text

# OUTPUTS: '2008'
