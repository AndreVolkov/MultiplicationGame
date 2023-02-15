# Multiplication game for kids
import random
n = 10
correct = 0
list_x1 = []
list_x2 = []
list_student_answer = []
list_answer = []
list_status = []
for i in range(1, n+1):
    x1 = random.randint(1, 10)
    list_x1.append(x1)
    x2 = random.randint(1, 10)
    list_x2.append(x2)
    result = x1 * x2
    list_answer.append(result)
    print('\nQuestion', i,':', x1,'x',x2,'=', end=' ')
    
    try:
        x3 = int(input())
        list_student_answer.append(x3)
    except ValueError:
        x3 = None
    if result == x3:
        correct = correct + 1
        print('Right!')
        list_status.append('CORRECT')
        
    else:
        print('Wrong! The right answer is', result)
        list_status.append('WRONG')
print()
print('*'*15, 'SUMMARY', '*'*15)
print()
for i in range(0, n):
    print('Q',i+1,': ', list_x1[i],'x',list_x2[i],'=?; Student Answer: ', list_student_answer[i],' Answer:', list_answer[i], ' Status: ', list_status[i], sep='')
print(f"Correct answer {correct} out of {n}")
if correct >= 7:
    print("Test PASS!")
else:
    print("Test FAIL!")

    

