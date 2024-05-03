# import builtins
# # print(dir(builtins))

# builtin_functions = [func for func in dir(builtins) if callable(getattr(builtins, func))]
# print(builtin_functions)

# def hello():
#     print('oyboy')
# hello()

# def name1(a, b):
#     return a+b
# result = name1(12, 5)
# print(result)

# def division(a, b):
#     return a//b
# result = division(10, 2)
# print(result)

# def multiplication(a, b):
#     return a*b
# result = multiplication(10, 2)
# print(result)

# def multiplication(a, b):
#     return a-b
# result = multiplication(10, 2)
# print(result)

# list_1 = ['name', 'age', '1', '19']
# def split_and_reverse(list_1):
#     middle = len(list_1) // 2
#     first_half = list_1[:middle]
#     second_half = list_1[middle:]
#     first_half_reversed = first_half[::-1]
#     second_half_reversed = second_half[::-1]
#     return first_half_reversed + second_half_reversed
# result = split_and_reverse(list_1)
# print(result)


# def square(a):
#     return a ** 2
# so = square(222)
# print(so) 


# def even(x):
#     return x % 2 == 0

# for i in range(1, 11):
#     print(i, even(i))

# x = int(input('Введите число до ста: '))
# def even(x):
#     return x + 1
# print(even(x))

# def bolshe(num):
#     if num <= 100:
#         return num
#     else:
#         return 'Вы ввели цифры больше ста!'
# print(bolshe(even(x)))
    

# def pay(salary):
#     to_pay = salary * 1.12
#     if to_pay > salary:
#         print("Итого: ")
#         print("\t{0}".format(to_pay))
#     else:
#         print("Вы уволены!")
# pay(0)
# pay(21000)
# pay(120000)

# def const(salary, persent=12):
#     print(salary*persent)
# const(15000)
# const(17000, persent=15)

# a,*b,c = [1,2,3,4,5,6,7,8]
# print(a,b,c)

# def func(*nums):
#     res = 0
#     for num in nums:
#         res += num
#     return res
# print(func(1,2,3,4,5,6))

# def student(name, **lessons):
#     print(f'hello, {name}')
#     for names, times in lessons.items():
#         print(f'{names} : {times}')
# student('Meder', chemistry=4, math=7, kyrgyzlang=1)

# def add(a, b):
#     return a+b
# result = add(12, 5)
# print(result)

# def substract(a, b):
#     return a-b
# result = substract(10, 2)
# print(result)

# def division(a, b):
#     return a//b
# result = division(10, 2)
# print(result)

# def multiply(a, b):
#     return a*b
# result = multiply(10, 2)
# print(result)


# def count(string):
#     count = 0
#     for i in string:
#         count+=1
#     return count
# x = input('Введите слово: ')
# count1 = count(x)
# print("Вы ввели", count1, "символов")

