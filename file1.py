# file1.py
x = 10
y = 'hello'
z = [1, 2, 3]

# Technical debt: unused variables, bad naming, magic numbers, no functions
abc = 999
foo = 'bar'
for i in range(5):
    print(x + i)

# More technical debt: inconsistent types
x = 'now a string'
y = 42
z = None

# No comments, no error handling
result = x + y
print(result)
