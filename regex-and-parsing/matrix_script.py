#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_chars = []

for i in range(m):
    for j in range(n):
        try:
            decoded_chars.append(matrix[j][i])
        except IndexError:
            decoded_chars.append(' ')

decoded_string = ''.join(decoded_chars)

cleaned_string = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_string)

print(cleaned_string)