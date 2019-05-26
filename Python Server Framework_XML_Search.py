# Python Server Framework.
# xml.etree.ElementTree � The ElementTree XML API.
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#
# Parsing XML with Namespaces:
# 
# If the XML input has namespaces, tags and attributes with prefixes in the form prefix:sometag get expanded to {uri}sometag where the prefix
# is replaced by the full URI. Also, if there is a default namespace, that full URI gets prepended to all of the non-prefixed tags.
# 
# An XML example that incorporates two namespaces, one with the prefix �fictional� and the other serving as the default namespace:
# 

# <?xml version="1.0"?>
#
# <actors xmlns:fictional="http://characters.example.com"
#        xmlns="http://people.example.com">
#    <actor>
#        <name>John Cleese</name>
#        <fictional:character>Lancelot</fictional:character>
#        <fictional:character>Archie Leach</fictional:character>
#    </actor>
#    <actor>
#        <name>Eric Idle</name>
#        <fictional:character>Sir Robin</fictional:character>
#        <fictional:character>Gunther</fictional:character>
#        <fictional:character>Commander Clement</fictional:character>
#    </actor>
# </actors>
 
#
# One way to search and explore this XML example is to manually add the URI to every tag or attribute in the xpath of a find() or findall():
# 

root = fromstring(xml_text)

for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')

    print(name.text)

    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)

# 
# A better way to search the namespaced XML example is to create a dictionary with your own prefixes and use those in the search functions:
# 

ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)

    print(name.text)

    for char in actor.findall('role:character', ns):
        print(' |-->', char.text)


