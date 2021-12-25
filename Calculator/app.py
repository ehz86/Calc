#Программа, которая может сложить или вычесть два неотрицательных числа
from calc import calc
try:

    Num1 = int(input('Введите первое число: '))
    Num2 = int(input('Введите второе число: '))


except ValueError as message:

    print(message)

else:
    znak = input('Введите знак(+ или -): ')
    calc(Num1, Num2, znak)


