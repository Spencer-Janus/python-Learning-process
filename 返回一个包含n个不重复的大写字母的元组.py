import random
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list1=[]
def fn(n):
    for i in range(0,n):
        x=random.choice(letter)             #随机选择列表中一个元素
        while x in list1:
            x=random.choice(letter)
        list1.append(x)
    a=tuple(list1)
    return a
print(fn(4))
