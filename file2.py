# file2.py
# Technical debt: global variables, bad structure, no encapsulation
A = 123
B = 'debt'
C = [A, B]

# Unused imports
import math
import sys

# Random variable assignments
A = 'oops'
B = 3.14
C = {'A': A, 'B': B}

# No function definitions, just code
for j in range(3):
    print(B * j)

# More technical debt: shadowing built-ins
list = [1, 2, 3]
dict = {'x': 1}

# No docstrings, no structure
print(list, dict)
