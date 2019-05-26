# Python XML DOM Tree
# DOMEventStream Objects:
# class xml.dom.pulldom.DOMEventStream(stream, parser, bufsize) getEvent() 
# Return a tuple containing event and the current node as xml.dom.minidom.Document if event equals START_DOCUMENT, xml.dom.minidom.Element if event
# equals START_ELEMENT or END_ELEMENT or xml.dom.minidom.Text if event equals CHARACTERS. The current node does not contain information about its
# children, unless expandNode() is called.
# expandNode(node). 
# Expands all children of node into node. Example:
 
from xml.dom import pulldom

xml = '<html><title>Foo</title> <p>Some text <div>and more</div></p> </html>'
doc = pulldom.parseString(xml)

for event, node in doc:

    if event == pulldom.START_ELEMENT and node.tagName == 'p':

        # Following statement only prints '<p/>'

        print(node.toxml())

        doc.expandNode(node)

        # Following statement prints node with all its children '<p>Some text <div>and more</div></p>'

        print(node.toxml())
