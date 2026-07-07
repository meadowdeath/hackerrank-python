# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == '__main__':
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    pattern = fr'(?<=[{consonants}])[aeiouAEIOU]{{2,}}(?=[{consonants}])'
    matches = list(re.finditer(pattern, input()))
    if matches:
        print(*[match.group(0) for match in matches], sep='\n')
    else:
        print(-1)