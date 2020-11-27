import random
import string

n = random.randint(50, 100) #Tạo ngẫu nhiên số phần tử ditionary có trong list
print('Số phần tử trong mỗi list hiện tại:',n)

list1 = []

for i in range(n):
    
    #Tạo giá trị ngẫu nhiên cho name: (chữ cái đầu tiên in hoa)
    n = random.randint(1,15)
    name = random.choice(string.ascii_uppercase) 
    for i in range(n):
        name += random.choice(string.ascii_lowercase)
        
    n = random.randint(0, 150)  #Tạo giá trị ngẫu nhiên cho age
    
    dic = {'name':name,'age':n} #Tạo dictionary từ 2 giá trị name và age vừa tạo
    list1.append(dic)         #Thêm phần tử dictionary vừa tạo vào list
    
print('List =',list1)
