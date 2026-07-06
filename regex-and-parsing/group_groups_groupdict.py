# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == '__main__':
    coincidence = re.search(r'([a-zA-Z0-9])\1+', input())

    if coincidence:
        print(coincidence.group(1))
    else:
        print(-1)