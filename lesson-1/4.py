'''
Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
'''

n = int(input('Введите целое полодительное число '))

max = 0
while n > 0:
    m = n % 10
    if m > max:
        max = m
    n = n // 10
        
print("Максимальное цифра в числе ", max) 