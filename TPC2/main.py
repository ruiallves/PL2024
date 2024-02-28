import re
import sys

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

def main(args):

    input_file = args[1]
    output_file = args[2]

    with open(input_file, 'r') as f:
        markdown_content = f.read()

    markdown_content = convertHeader(markdown_content)
    markdown_content = convertBold(markdown_content)
    markdown_content = convertItalic(markdown_content)
    markdown_content = convertImage(markdown_content)
    markdown_content = convertLink(markdown_content)
    markdown_content = convertNumberedList(markdown_content)
    markdown_content = addSpaceToLi(markdown_content)

    with open(output_file, 'w') as f:
        f.write(markdown_content)

    print("Arquivo HTML gerado com sucesso:", output_file)
    return 0

if __name__ == "__main__":
    main(sys.argv)
