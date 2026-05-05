# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = input()
    english_subbed = set(map(int, input().split()))
    b = input()
    french_subbed = set(map(int, input().split()))
    
    one_subbed = english_subbed.union(french_subbed)
    
    print(len(one_subbed))