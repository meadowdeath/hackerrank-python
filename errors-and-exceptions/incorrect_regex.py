# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def is_valid_regex(regex):
    
    if '*+' in regex or '++' in regex or '?+' in regex or '}{' in regex:
            return False
            
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


queries = int(input())
for _ in range(queries):
    regex = input()
    print(is_valid_regex(regex))
