# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    s = input()

    result = sorted(s, key=lambda x: (
        x.isdigit(), 
        x.isupper(), 
        x.isdigit() and int(x) % 2 == 0,
        x
    ))
    
    print("".join(result))