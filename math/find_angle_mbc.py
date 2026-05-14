# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())

    theta = round(math.degrees(math.atan2(ab, bc)))

    print(f"{theta}{chr(176)}")
