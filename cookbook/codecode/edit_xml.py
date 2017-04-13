# 解析和修改 XML
# 使用 xml.etree.ElementTree 模块可以很容易的处理这些任务。第一步是以通常
# 的方式来解析这个文档。例如，假设你有一个名为 pred.xml 的文档
from xml.etree.ElementTree import parse, Element, tostring

doc = parse('pred.xml')
root = doc.getroot()
print(tostring(root))
# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))
# Insert a new element after <nm>...</nm>
idx = root.getchildren().index(root.find('nm'))
print(idx)
e = Element('spam')
e.text = "this is a test"
root.insert(2, e)
# Write back to a file
doc.write('newpred.xml', xml_declaration=True)
# 修改一个 XML 文档结构是很容易的，但是你必须牢记的是所有的修改都是针对父
# 节点元素，将它作为一个列表来处理。例如，如果你删除某个元素，通过调用父节点
# 的 remove() 方法从它的直接父节点中删除。如果你插入或增加新的元素，你同样使
# 用父节点元素的 insert() 和 append() 方法。还能对元素使用索引和切片操作，比如
# element[i] 或 element[i:j]
