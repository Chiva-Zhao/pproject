from xml.etree import ElementTree

import xmltodict

tree = ElementTree.parse('sample_xml.xml')
root = tree.getroot()
print(root.tag, root.attrib)
for child in root:
    print("{0}tag:{1}, attribute:{2}".format(
        "\t",
        child.tag,
        child.attrib))
    print("{0}tag data:{1}".format("\t", child.text))
# xmltodict
xml_filedata = open('sample_xml.xml').read()
ordered_dict = xmltodict.parse(xml_filedata)
print(ordered_dict)