list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]

#List2 gồm 4 Tuple
#Tuple gồm 2 Dic
#Dic gồm 2 key: name , age

for index,tup in enumerate(list2,1):
    print(index,tup)
    for dic in tup:           
        print(dic)
        print(dic['name'],dic['age'])
        
"""
Thầy ơi nếu những Key của dic biến đổi không có quy luật (hoặc quá nhiều để liệt kê hết)
 và mình không xác định được
thì có cách nào gõ lệnh để python tự động điền Key không ạ?
"""
