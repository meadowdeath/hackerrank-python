# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validate_credit_card(card_number):
    credit_card_pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    
    if not re.match(credit_card_pattern, card_number):
        return False
    
    cleaned_number = card_number.replace('-', '')

    if re.search(r'(\d)\1{3,}', cleaned_number):
        return False
    
    return True

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        card_number = input().strip()
        if validate_credit_card(card_number):
            print("Valid")
        else:
            print("Invalid")