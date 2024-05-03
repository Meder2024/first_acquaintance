count = 0
while count < 5:
    print(count)
    count += 1

for num in range(12, 65, 3):
    print(num)

for i in 'meder':
    print(i)

mylist = [12,45,56,7]
# for num in mylist:
#     print(num)

newlist = [i for i in mylist if i%2==1]
print(newlist)

string = 'python - best'
for i in string:
    if i == '-':
        break
    print((i))

c = ["kochebaev"]
for i in c:
    if i == "kochebaev":
        c += ["meder"]
    if i == "meder":
        c += ["baktybekovich"]
print(c)

a = ['отбивные', 'пельмени', 'яйца', 'орехи']

for food in a:
    if food == 'пельмени':
        print("я не ем пельмени!")
    else: 
        print("отлично, вкусные ", food)
else:
    print("хорошо, что не было пельменей!")
print("ужин окончен.")

for num in range(1,11):
    print(num)


for num in range(1,21,2):
    print(num)

count = 0
while count < 100:
   count += 1
   print(count)


count = 0
for i in range(1,101):
    count=+1
    print(i)

for i in range(1,11):
    print('6 x', i, '=', 6 * i)


a = [1,2,3,4,5]
for i in a:
    print(i)

for i in range(1,6):
    print(i**2)