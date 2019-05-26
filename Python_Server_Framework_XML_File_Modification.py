# Python Server Framework.
# xml.etree.ElementTree � The ElementTree XML API.
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#
# Modifying an XML File. 
# ElementTree provides a simple way to build XML documents and write them to files. The ElementTree.write() method serves this purpose.
# 
# Once created, an Element object may be manipulated by directly changing its fields (such as Element.text), adding and modifying attributes
# (Element.set() method), as well as adding new children (for example with Element.append()).
# 
# Let�s say we want to add one to each country�s rank, and add an updated attribute to the rank element:
# 

for rank in root.iter('rank'):
        new_rank = int(rank.text) + 1

        rank.text = str(new_rank)
        rank.set('updated', 'yes')

tree.write('output.xml')

#
# 
# Our XML now looks like this:
# 

# <?xml version="1.0"?>
#
# <data>
#    <country name="Liechtenstein">
#        <rank updated="yes">2</rank>
#        <year>2008</year>
#        <gdppc>141100</gdppc>
#        <neighbor name="Austria" direction="E"/>
#        <neighbor name="Switzerland" direction="W"/>
#    </country>
#    <country name="Singapore">
#        <rank updated="yes">5</rank>
#        <year>2011</year>
#        <gdppc>59900</gdppc>
#        <neighbor name="Malaysia" direction="N"/>
#    </country>
#    <country name="Panama">
#        <rank updated="yes">69</rank>
#        <year>2011</year>
#        <gdppc>13600</gdppc>
#        <neighbor name="Costa Rica" direction="W"/>
#        <neighbor name="Colombia" direction="E"/>
#    </country>
# </data>

# 
# We can remove elements using Element.remove(). Let�s say we want to remove all countries with a rank higher than 50:
# 

for country in root.findall('country'):
        rank = int(country.find('rank').text)

        if rank > 50:
            root.remove(country)

tree.write('output.xml')

# 
# Our XML now looks like this:
# 

# <?xml version="1.0"?>
#
# <data>
#    <country name="Liechtenstein">
#        <rank updated="yes">2</rank>
#        <year>2008</year>
#        <gdppc>141100</gdppc>
#        <neighbor name="Austria" direction="E"/>
#        <neighbor name="Switzerland" direction="W"/>
#    </country>
#    <country name="Singapore">
#        <rank updated="yes">5</rank>
#        <year>2011</year>
#        <gdppc>59900</gdppc>
#        <neighbor name="Malaysia" direction="N"/>
#    </country>
# </data>
