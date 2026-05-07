# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = input()
    english_subbed = set(map(int, input().split()))
    b = input()
    french_subbed = set(map(int, input().split()))
    
    difference_subbed = english_subbed.difference(french_subbed)
    
    print(len(difference_subbed))