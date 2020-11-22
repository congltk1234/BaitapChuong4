import random
while True: #Xét điều kiện nhập
  n = int(input('Số lượng phần tử trong dãy:'))   #Nhập số lượng phần tử trong dãy
  list = [] #Tạo list rỗng
  if n == 0:
    print(list, 'Dãy không có phần tử nào. Không có giá trị nhỏ nhất.')
  elif n > 0:
    for i in range(n):
      list.append(random.random())   #Thêm phần tử vào list
    min = list[0]                    #Tạo biến phụ để so sánh
    for i in range(n):
      if min > list[i]:              #So sánh min với từng phần tử được thêm vào, nếu bé hơn min thì gán giá trị phần tử đó cho min
        min = float(list[i])
    print(list) 
    print('Phần tử nhỏ nhất trong dãy trên là:' , min) 
  print('*Vui lòng nhập số nguyên dương.*')
  #Tiếp tục vòng lặp nếu người dùng muốn nhập tiếp 
  option = input("-Bạn có muốn tiếp tục không?(y/n) ")
  if option == 'n' or option == 'N':
      print('Finish!')
      break  