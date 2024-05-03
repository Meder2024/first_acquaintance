# numbers = [1,'2',3,'4',5,'6',8,'8']

# for i in range(-5,5):
#     if int(i) % 2 == 0:
#         print(numbers[8]/i)

# numbers = [1, '2', 3, '4', 5, '6a', 7, '8']

# # for i in range(-5, 5):
# #     if i != 0 and int(i) % 2 == 0:  # Проверка, что i не равно 0
# #         print(numbers[7] / int(i))  # Используем индекс 7, так как индексация начинается с 0


# try:
#     for i in range(-5.5):
#      if int(i) % 2==0:
#         print(numbers[8]/i)
# except:
#     print("Найдена Ошибка!")

# try:
# #    a = 12/0
#    o = int('sdf')
# #    print(a)
#    print(o)
# except IndexError:
#    print("erroe")

# numbers_set = set()
# try:
#     for i in range(5):
#         num = int(input("Введённое число: "))
#         numbers_set.add(num)
#     min_number = min(numbers_set)
#     print("Самое маленькое число, которое вы ввели:", min_number)
# except ValueError:
#     print("Вы ввели некорректные данные. Пожалуйста, введите целое число.")

# def execute_python_function(func_name):
#     try:    
#         func = globals()[func_name]
#     except KeyError:
#         return f"В Python нет функции с именем '{func_name}'"

#     try:
#         result = func()
#         return f"Результат выполнения функции '{func_name}': {result}"
#     except Exception as e:
#         return f"При выполнении функции '{func_name}' произошла ошибка: {str(e)}"


# def example_function():
#     return "Пример выполнения функции"

# function_name = input("Введите имя функции Python: ")

# print(execute_python_function(function_name))


# values = [1, '2', 3, '4', 5, '6', 8, '8']

# convertibility_check = []

# for item in values:
#     try:
#         int(item)
#         convertibility_check.append(True)
#     except ValueError:
#         convertibility_check.append(False)

# can_convert_to_set = all(convertibility_check)

# print("Можно ли конвертировать values в set?", can_convert_to_set)