# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def changer (match):
    if match.group(0) == ' && ':
        return ' and '
    elif match.group(0) == ' || ':
        return ' or '

if __name__ == '__main__':
    N = int(input())
    pattern = r' (&&|\|\|) '
    
    for _ in range(N):
        line = input()

        modified_line = re.sub(pattern, changer, line)
        modified_line = re.sub(pattern, changer, modified_line)
        print(modified_line)