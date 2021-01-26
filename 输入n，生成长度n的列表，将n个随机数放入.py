import random
a=int(input('请输入列表的长度'))
list_1=[]
for i in range(1,a+1):
    list_1.append(random.randint(0,9))    #随机生成0-9（包括后者)的一个数
print(list_1)
