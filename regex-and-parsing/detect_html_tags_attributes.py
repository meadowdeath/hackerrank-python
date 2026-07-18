# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

if __name__ == '__main__':
    html = ""       
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
        
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()