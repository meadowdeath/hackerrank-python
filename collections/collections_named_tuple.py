# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
fields = input().split()
Student = namedtuple('Student', fields)
total_marks = sum(int(Student(*input().split()).MARKS) for _ in range(N))

print(f'{total_marks / N:.2f}')