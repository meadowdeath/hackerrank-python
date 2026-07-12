import re

if __name__ == '__main__':
    
    N = int(input())
    regex_pattern = r"^[789]\d{9}$"	# Do not delete 'r'.
    
    for _ in range(N):
        if bool(re.match(regex_pattern, input())):
            print("YES")
        else:
            print("NO")