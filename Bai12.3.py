import random
import string
n = random.randint(50, 100) #Tạo ngẫu nhiên số phần tử có trong mỗi list
print('Số phần tử trong mỗi list hiện tại:',n)
print('''
            ''')
list1 = []
dic = {}
for i in range(n):
    n = random.randint(1,15)
    name = random.choice(string.ascii_uppercase)
    for i in range(n):
        name += random.choice(string.ascii_lowercase)
    n = random.randint(0, 150)
    dic = {'name':name,'age':n}
    list1.append(dic)         #Thêm phần tử vừa tạo vào list
print(list1)
