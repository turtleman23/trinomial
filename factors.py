import math
z = 1
f = input("what is the first number? ")
f = int(f)
s = input("what is the second number? ")
s = int(s)
n = input("what is the third number? ")
n = int(n)
x = 1
while x <= math.sqrt(abs(n*f)):
    if n * f % x == 0:
        if x + n*f//x == s:
            print(x, "+", n*f//x)
            z = 1
        elif x - n*f//x == s:
            print(x, "-", n*f//x)
            z = 1
        elif n*f//x - x == s:
            print(n*f//x, "-", x)
            z = 1
        elif n*f//x + x ==s:
            print(n*f//x, "+", x)
            z = 1
        elif -n*f//x + x == s:
            print(-n*f//x, "+", x)
            z = 1
        elif -n*f//x - x == s:
            print(-n*f//x, "-", x)
            z = 1
    x += 1
if z != 1:
    print("this can't be solved")
