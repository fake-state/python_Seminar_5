# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

number = int(input('Введите число > '))
degree_of_number = int(input('Введите степень > '))

def number_degree(num, deegree):
    if deegree == 1:
        return num
    else:
        num = num * number_degree(num ,deegree - 1)
        return num

print(number_degree(number, degree_of_number))


