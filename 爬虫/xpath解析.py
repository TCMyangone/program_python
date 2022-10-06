from lxml import etree
parser = etree.HTMLParser(encoding="utf-8")
tree = etree.parse('sogou.html', parser=parser)
r = tree.xpath('/html/head/title/text()')[0]
print(r)

