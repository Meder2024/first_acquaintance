# import datetime
# while True:
#     year_of_birth = input("Введите ваш год рождения: ")
#     if year_of_birth.isdigit() and len(year_of_birth) == 4:
#         year_of_birth = int(year_of_birth)
#         current_year = datetime.datetime.now().year
#         age = current_year - year_of_birth 
#         if age < 0 or age > 110:
#             print("Вы неверно указали год рождения")
#         else:
#             break
#     else:
#         print("Вы ввели некорректно ваш год рождения. Пожалуйста, введите год рождения цифрами и не более чем 4 цифры.")
# if age in range(0, 5):
#     print("Вы ребёнок")
# elif age >= 18:
#     print("Вы совершеннолетний")
# else:
#     print("Вы несовершеннолетний")

# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# num3 = float(input("Введите третье число: "))

# max_num = max(num1, num2, num3)
# min_num = min(num1, num2, num3)
# print("Самое большое число:", max_num)
# print("Самое маленькое число:", min_num)


# numbers = [17391, 546, 934]
# remainders = [number % 17 for number in numbers]
# min_remainder = min(remainders)
# index = remainders.index(min_remainder)
# print(f"Число {numbers[index]} имеет наименьший остаток от деления на 17, который составляет {min_remainder}.")

# x = 13
# while x ** 2 < 172:
#     x = x ** 2
# print("Итоговое значение x:", x)