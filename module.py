# # # import math
# # import os
# # import sys
# # # print(math.sqrt(16))
# # # print(math.factorial(5))
# # # print(math.tan(16))

# # # import datetime as d
# # # print(d.datetime.now())

# # print(os.name)
# # print(sys.version)
# # print(sys.platform)
# # # print(sys.argv)

# # # from my_module import a
# # # print(a)

# # # import my_module
# # # print(my_module)

# # import random
# # names = ["aibek", "joomart", "adinai", "ermek", "atai", "aslan", "lyazat", "salavat", "daniyar", "bolotbek", "alymbek", "dastan", "maksat"]
# # random_names = random.sample(names, 4)
# # print(random_names)

# # import sys
# # print(sys.platform)

# # a = input("Любое слово: ")
# # print(a)

# # import sys
# # arguments = sys.argv[1:]
# # print(arguments)

# # import sys
# # a = str(input("Любое слово: "))
# # b = str(input("Ещё вариант: "))
# # size1 = sys.getsizeof(a)
# # size2 = sys.getsizeof(b)
# # print(size1,"размер памяти первого слова",size2, "размер памяти вторго слова")

# import random
# import string

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# def main():
#     n = int(input("Введите количество символов для пароля: "))
    
#     # Проверяем, чтобы n было положительным числом
#     if n <= 0:
#         print("Количество символов должно быть положительным числом.")
#         return
    
#     password = generate_password(n)
#     print("Ваш пароль:", password)

# if __name__ == "__main__":
#     main()