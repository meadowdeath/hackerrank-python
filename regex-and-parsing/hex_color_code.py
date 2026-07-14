# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    color_pattern = r'(?<=[:,\s])#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b'

    N = int(input())
    for _ in range(N):
        line = input()
        for elem in re.finditer(color_pattern, line):
            print(line[elem.start(): elem.end()] 
            if elem is not None else '')
