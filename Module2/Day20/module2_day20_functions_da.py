def hello():
    return "Hello World!"

print (hello())

def even(a):
    while a % 2 != 0:
        a *= 2
    return a

for x in [3, 35, 2, 107, 254]:
    if x == even(x):
         print(f"x{x} is an even number.")
    else:
        print(f"{x} first becomes an even number when it's multiplied by 2 to become {even(x)}.")

for x in [3, 35, 2, 107, 254]:
    if x % 2 == 0:
        print(f"{x} is an even number.")
    else: 
        y = x * 2
        print(f"{x} first becomes an even number when it's multiplied by 2 to become {y}.")    

def pythag(a):
    c = (a ** 2 + even(a) ** 2) ** .5
    return c  
print (pythag)

x = int(input("Please provide an integer."))
print(f"Function output: {pythag(x)}.")

if x % 2 == 0:
    man_a = x
    man_b = x
else:
    man_a = x
    man_b = x * 2
print(f"Manual Calculation: a = {man_a}, b = {man_b}, c = {(man_a ** 2 + man_b ** 2) ** .5}")

def matrix_add(m1, m2):
    if len(m1) != len(m2):
        raise ValueError("Given matrices are not the same size.")
    for i in range(0, len(m1)):
        if len(m1[i]) != len(m2[i]):
            raise ValueError("Given matrices are not the same size.")
        for j in range(0, len(m1[0])):
            m1[i][j] = (m1[i][j] + m2[i][j])
    return m1

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(matrix_add(matrix1, matrix2))

def matrix_mult(m1, m2):
    if len(m1) != len(m2):
        raise ValueError("Given matrices are not the same size.")
    for i in range(0, len(m1)):
        if len(m1[i]) != len(m2[i]):
            raise ValueError("Given matrices are not the same size.")
        for j in range(0, len(m1[0])):
            m1[i][j] = (m1[i][j] * m2[i][j])
    return m1

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(matrix_mult(matrix1, matrix2))

# print(matrix_mult.__doc__)
# print(help(matrix_mult))
