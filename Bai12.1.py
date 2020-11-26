import random

n = random.randint(50, 1000) #Tạo ngẫu nhiên số phần tử có trong mỗi list
print('Số phần tử trong mỗi list hiện tại:',n)
print('''
            ''')
list1 = []
list2 = []
for i in range(n):
    i = random.randint(-1000, 1000) #Tạo phần tử mang giá trị ngẫu nhiên
    list1.append(i)         #Thêm phần tử vừa tạo vào list
for i in range(n):
    i = random.uniform(-1000.0, 1000.0) #Tạo phần tử mang giá trị ngẫu nhiên
    list2.append(i)         #Thêm phần tử vừa tạo vào list
print('List1 =',list1)
print('''
            ''')
print('List2 =',list2)
