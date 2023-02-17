"""XML demo to parse a simple ctalog file."""
from lxml import etree


tree = etree.parse(r"files/catalog.xml")  # Get the whole document as the root element
# Récupérer les éléments de la racine CATALOG qui ont le nom CD
items = tree.xpath("//CATALOG/CD")

for cd in items:
    for attribute in cd:
        print(attribute.tag, attribute.attrib)  # afficher le nom et les attributs
        print(attribute.text)
