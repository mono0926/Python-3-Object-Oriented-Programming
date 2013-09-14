from xml.etree.ElementTree import (Element, SubElement,
        tostring)

root = Element("html")
head = Element("head")
root.append(head)
title = SubElement(head, "title")
title.text = "my page"
link = SubElement(head, "link")
link.attrib['rel'] = "stylesheet"
link.attrib['href'] = "styles.css"
body = Element("body")
body.text = "This is my website."
root.append(body)

print(tostring(root))
