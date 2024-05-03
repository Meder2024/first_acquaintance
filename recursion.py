# def func(x):
#     if x < 10:
#         print(x)
#         func(x+1)
#         print(x)
# func(1)

# def main(number):
#     print(number)
#     if number == 0:
#         return number
#     else:
#         main(number+1)
# main(-20)

# def main(number):
#     print(number)
#     if number == 0:
#         return number
#     else:
#         main(number-1)
# main(10)


# l = lambda b, o: b+o
# print(l(11,12))

# p = lambda num: True if num > 5 else False
# print(p(20))

# def sum(a,c):
#     return a+c

# print(sum(12,2))

# def compare(n):
#     if n>5:
#         return True
#     else:
#         return False
# print(compare(12))


# l = (lambda weight,height: {(height-110) - weight})
# print(l(50,167))

# p=lambda a,b,c: a*b*c
# print(p(100,50,10))

# k=lambda a: 365-a
# print(k(50))


# def odd_num(n):
#     if n<1:
#         return odd_num
#     if n % 2 !=0:
#         print(n)
#     odd_num(n-1)
# print(odd_num(11))

# def set(g):
#     if not g:
#         return g
#     else:
#         print("удалённый элемент: ", g.pop())
#         return set(g)
# my_set = {1,2,3,4,5,6,7,8,9,0}
# print("Итого: ",my_set)