import re

def convertHeader(markdown):
    markdown = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^## (.+)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^### (.+)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
    return markdown

def convertBold(markdown):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown)

def convertItalic(markdown):
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdown)

def convertLink(markdown):
    return re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', markdown)

def convertImage(markdown):
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)

def convertNumberedList(markdown):
    markdown = re.sub(r'^(\d+)\. (.+)$', r'<li>\2</li>', markdown, flags=re.MULTILINE)
    return re.sub(r'(<li>.+</li>)', r'<ol>\n\1\n</ol>', markdown, flags=re.DOTALL)

def addSpaceToLi(markdown):
    return re.sub(r'<li>(.+?)</li>',r'  <li>\1</li>', markdown)



#teste
test = """
# H1
## H2
### H3

**bold text**

*italicized text*

1. First item
2. Second item
3. Third item

[title](https://www.example.com)

![alt text](image.jpg)
"""

html_output = convertLink(convertImage(addSpaceToLi(convertNumberedList(convertItalic(convertBold(convertHeader(test)))))))
print(html_output)