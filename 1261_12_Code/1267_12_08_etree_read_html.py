from xml.etree.ElementTree import fromstring

with open("1267_12_07_html_document.html") as file:
    root = fromstring(file.read())

print("ROOT NODE")
print("\ttag:", root.tag)
print("\tnumber of children:", len(root))
print("\tchildren:", [c.tag for c in root.getchildren()])
head = root[0]
print("HEAD NODE")
print("\tfirst child:", head[0].tag)
print("\tsecond_child:", head[1].tag)
print("\tlink attributes:", head[1].attrib)
article = root[1][1]
print("ARTICLE NODE")
print("\ttag:", article.tag)
print("\ttext:", article.text)
print("\tfirst child:", article[0].tag, article[0].text)
print("\t\tem's tail:", article[0].tail)
print("\tsecond child:", article[1].tag, article[1].text)
print("\tstrong's tail:", article[1].tail)

# XPath Selection
print('search for child tag:', root.find('head'))
print('search children recursively:', root.findall('.//em'))
print('build path:', root.findtext('./body/article/em'))
