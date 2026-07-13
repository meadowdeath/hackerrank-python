# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

if __name__ == '__main__':
    n = int(input())
    regex_pattern = r"^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"  # Do not delete 'r'.

    for _ in range(n):
        name, email_address = email.utils.parseaddr(input())
        if bool(re.match(regex_pattern, email_address)):
            print(email.utils.formataddr((name, email_address)))