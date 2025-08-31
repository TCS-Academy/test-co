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
q = 12345
q = 'string again'
unused_var = None
for k in range(2):
    x = k * 2
    print('loop', x)
def bad_func():
    global x
    x = 999
    print('bad_func', x)
bad_func()
try:
    x = x / 0
except:
    pass
random_list = [q, x, y, z]
for item in random_list:
    print(item)
if x == 'now a string':
    y = 'changed again'
else:
    y = 0
def another_func():
    return y + 1
another_func()
del x
x = [1,2,3]
y = {'a': 1}
z = (1,2,3)
print(x, y, z)
