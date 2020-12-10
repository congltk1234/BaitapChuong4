import string , random , os

def randomstr(): #Tạo hàm để sinh ngẫu nhiên nội dung trong file
    name = random.choice(string.ascii_letters)
    for i in range(999999):
        name += random.choice(string.ascii_letters)
    return name
path = input('Nhập đường dẫn nơi bạn muốn tạo thư mục')+'\\'
path = path + input('Tên thư mục bạn muốn tạo:')
os.mkdir(path)
os.chdir(path)
#Dung lượng dữ liệu giới hạn:    
size = float(input('Nhập dung lượng dữ liệu (1MB-1024MB):'))
size = size * 1000000 #Đổi sang byte

n =int(size // 1000000) #Số lượng file trong folder
m =int(size % 1000000)  #Số byte còn dư 
for i in range(1,n):
    f = 'file'+str(i)+'.txt'
    f = open(f, mode= 'w')
    f.write(randomstr())
    f.close()
#Tạo 1 file với số byte dư
if m != 0:
    f = 'file'+ str(n + 1) +'.txt'
    f = open(f, mode= 'w')
    name = random.choice(string.ascii_letters)
    for i in range(m - 1):
        name += random.choice(string.ascii_letters)
        f.write(randomstr())
        f.close()
print('Đã tạo:', (n+1),'file!')