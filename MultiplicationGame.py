# Multiplication game for kids
import random
n = 10
v = 0
nv = 0
for i in range(1, n+1):
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    result = x1 * x2
    print('\nQuestion', i,':', x1,'x',x2,'= ?')
    try:
        x3 = int(input("Result: "))
    except ValueError:
        x3 = None
    if result == x3:
        v = v + 1
        print('Right!')
        
    else:
        nv = nv + 1
        print('Wrong! The right answer is', result)
if v >= 8:
    print("You WIN!")
else:
    print("You LOSE!")
print(f"Correct answer {v} out of {n}")
