import random
import string
n = random.randint(1,20)
name = random.choice(string.ascii_uppercase)
for i in range(n):
    name += random.choice(string.ascii_lowercase)
n = random.randint(0, 150)
dic = {'name':name,'age':n}
print(dic)