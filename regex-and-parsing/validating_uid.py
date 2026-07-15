# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validate_uid(uid):

    if len(uid) != 10:
        return False
    
    if len(set(uid)) != 10:
        return False
    
    if not re.match(r'^[A-Za-z0-9]+$', uid):
        return False
    
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    
    if len(re.findall(r'[0-9]', uid)) < 3:
        return False
    
    if len(re.findall(r'[^A-Za-z0-9]', uid)) > 0:
        return False
    
    return True

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        uid = input().strip()
        if validate_uid(uid):
            print("Valid")
        else:
            print("Invalid")