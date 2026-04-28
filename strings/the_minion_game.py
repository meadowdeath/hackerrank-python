def minion_game(string):
    # your code goes here
    kevin, stuart = 0, 0
    n = len(string)
    vowels = "AEIOU"

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)