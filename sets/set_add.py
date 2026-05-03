# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    country_quantity = int(input())
    countries = set()
    for country in range(country_quantity):
        countries.add(input())
    
    print(len(countries))