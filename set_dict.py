# my_set = {1, 2, 3}
# print(my_set)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict)

# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_set = set(my_list)
# unique_list = list(unique_set)
# print(unique_list)

# my_list = [1, 2, 3 ,4, 5]
# is_unique = len(my_list) == len(set(my_list))
# print(is_unique)

# user_info = {'username': 'meder', 'age': 37, 'city': 'Osh'}
# print(user_info['username'])

# my_set = {1, 2, 3, 4 ,5}
# my_set1 = {0, 2, 3, 4 ,5}
# my_set.add(6) 
# print(my_set)

# my_set.update([7, 8]) # list
# print(my_set)

# my_set.remove(1)
# print(my_set)

# my_set.discard(2)
# print(my_set)

# inter = my_set.intersection(my_set1)
# print(inter)

# my_set1.intersection_update(my_set)
# print(my_set1)

# popped = my_set.pop()
# print(popped)
# print(my_set)

# popped = my_set.pop()
# print(popped)
# print(my_set, f'удалено {popped}')

# a = {'a', 'i', 'o', 'e', 'u', 'y'}
# b = input('any letter: ')
# if b.lower()in a:
#     print(True)
# else:
#     print(False)


# a = {'a', 'i', 'o', 'e', 'u', 'y'}
# b = input('Введите одну букву: ')

# if len(b) == 1 and b.lower() in a:
#     print(True)
# else:
#     print(False)

# a = {'a', 'i', 'o', 'e', 'u', 'y'}
# b = input('Введите одну букву: ')
# c = 1
# if b.lower() in a:
#     print(True)
# elif len(b) > c:   
#     print('не больше 1 буквы')
# else:
#     print(False)

# my_set = {1, 2, 3, 4 ,7} 
# my_set.remove(7)
# print(my_set) # первое задание

# my_set = {1, 2, 3, 4 ,7}
# my_set1 = {0, 2, 3, 4 ,5}
# inter = my_set.intersection(my_set1)
# print(inter) # второе задание

# my_set = {1, 2, 3, 4 ,7}
# my_set1 = {0, 2, 3, 4 ,5}
# diff = my_set.difference(my_set1)
# print(my_set, my_set1, f'между ними ' f'разница {diff}') # третье задание

# my_set = {0, 2, 3, 4 ,5}
# my_set.add(6)
# popped = my_set.pop()
# print(my_set, f'удалено {popped}') # четвёртое задание

# dict = {
#     #key : value
#     'kyrgyzstan':'bishek'
# }
# print(dict['kyrgyzstan'])
# dict['usa'] = 'washigton' # добавление в словарь
# print(dict)

# value = dict.get('kyrgyzstan') # полусить значение по ключу
# print(value)


# menu = {
#     "besh_barmak": 130}, {"lagman": 120}, {"borshch": 120
# }
# menu["lagman"][120] = 135       
# print(menu)