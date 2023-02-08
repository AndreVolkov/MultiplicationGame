# Multiplication game for kids - version 2
import random
n = 10
v = 0
nv = 0
for i in range(1, n+1):
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    result = x1 * x2
    print('\nQ', i,':', x1,'x',x2,'= ?')
    try:
        x3 = int(input("Student Answer: "))
    except ValueError:
        x3 = None
    if result == x3:
        v = v + 1
        print('Answer:',result,'Status: CORRECT')
        
    else:
        nv = nv + 1
        print('Answer:',result,'Status: WRONG')
if v >= 7:
    print("Test PASS!")
else:
    print("Test FAIL!")
print(f"Correct answer {v} out of {n}")
