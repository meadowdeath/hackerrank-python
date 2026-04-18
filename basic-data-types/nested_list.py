if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    lowest = float('inf')
    second_lowest = float('inf')
       
    for name, score in records:
        if score < lowest:
            second_lowest = lowest
            lowest = score
        elif lowest < score < second_lowest:
            second_lowest = score
    
    names = sorted([name for name, score in records if score == second_lowest])
    
    for n in names:
        print(n)



    
    