# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

if __name__ == '__main__':
    parser = MyHTMLParser()
    n = int(input())
    html_lines = []
    
    for _ in range(n):
        html_lines.append(input())

    html_content = "\n".join(html_lines)
    parser.feed(html_content)   