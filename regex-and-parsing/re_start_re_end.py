# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == '__main__':
    S = input()
    k = input()
    pattern = fr'(?=({k}))'
    matches = list(re.finditer(pattern, S))
    if matches:
        for match in matches:
            print((match.start(1), match.end(1) - 1))
    else:
        print((-1, -1))