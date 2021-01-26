#if分支语句
'''
if:
    A
else：
    b
if：
    
elif：
    
else：

'''
#需要特别注意的是：执行if语句python会判断条件的真假，if条件可以是任意类型，当下面的值作为bool表达式的时候，会被当作false：False，None，0，"",(),{},[]
#也就是说0，空字符串，空元组，空列表都会被当成false处理
#判断年龄
age=70
if 20<age<40:
    print('中青年人')
elif 40<age<60:
    print('中年人')
else :
    print('老年人')

#书上版本：   if else语句的基本规则：把范围小的优先处理掉
age=45
if age>60:
    print('old man ')
if age>40 and not(age>60):
    print('mid man')
if age>20 and not (age>60) and not (age>40 and not(age>60)):
    print('yong man')
#pass语句：占一个位置但是又不做任何事情
s=5
if s>5:
    print('大于5')
elif s<5:
    pass                              #什么都不做
else:
    print('等于5')
#断言
#assert断言的执行逻辑:  if false :引发AssertionError错误
#循环结构
#1.while循环
'''
while expression:
    body statements.
只有循环条件为真的时候
'''
#需要注意：while循环条件必须要有假的时候，否则会变成死循环
#使用while遍历列表和元组
a_tuple=('fkit','zz','naobaihao')
i=0
while i<len(a_tuple):
    print(a_tuple[i])
    i+=1
#对一个列表的元素进行分类，能整除3的放入一个列表，余数为1放入一个列表，余数为2放入另一个列表
initial_list=[12,45,34,13,100,24,56,74,109]
a_list=[]
b_list=[]
c_list=[]
i=0
while i<len(initial_list):
    if (initial_list[i])%3==0:
        a_list.append(initial_list[i])
    elif(initial_list[i])%3==1:
        b_list.append(initial_list[i])
    elif(initial_list[i])%3==2:
        c_list.append(initial_list[i])
    i+=1
print(a_list,b_list,c_list)
#for-in循环
'''
for 变量 in 字符串【范围】集合等：
    body statements
'''
#for in循环中的变量受循环控制，会自动赋值，因此在循环里不需要对该变量赋值
#计算6的阶乘
s=6
result=1
for num in range(1,s+1):
    result*=num
print(result)
#for循环遍历列表和元组，有多少个元素，循环体就执行多少次
tuple_1=('liunanren','shabi','yige')
for name in tuple_1:
    print(name)
#例：计算所有数值元素的总和and平均值
num_list=[12,45,3.4,13,'a',4,56,'liunanren',109.5]
sum=0
count=0
for ele in num_list:
    if isinstance(ele,int) or isinstance(ele,float):               #isinstance(element,type)判断数据是不是指定类型，返回bool
        sum+=ele
        count+=1
print('the sum:',sum)
print('average:',sum/count)
#for循环遍历字典
dict_1={'liujiayao':'gaiwa','guoyifan':'gaiwa','gaiwa':'gaiwa'}
for key,value in dict_1.items():
    print('key:',key)
    print('value',value)
#统计列表各元素出现的次数
list_2=[12,45,3.4,12,'fuck',45,3.4,'fuck',45,3.4]
statistics={}
for element in list_2:
    if element in statistics:
        statistics[element]+=1
    else:                               #若没有出现过，将出现次数设为1
        statistics[element]=1
for key,value in statistics.items():
    print('元素：',key)
    print('出现次数：',value)
#循环使用else：python的循环都可以定义else代码块，当循环条件为False的时候，程序会执行else代码块（并没有太大的价值，但能使得代码更加美观）
count_i=0
while count_i<5:
    print('counti小于5:',count_i)
    count_i+=1
else:
    print('count_i大于等于5：',count_i)
a_list=[330,1.4,50,666]
for ele in a_list:
    print('元素',ele)
else:                     #在else代码中，循环计数器的值仍然等于最后一个元素的值
    print('else:',ele)
#循环的嵌套：
for i in range(0,5):
    j=0
    while j<3:
        print('i的值为：%d,j的值为%d'%(i,j))
        j+=1
#for表达式用于利用区间/元组/列表、字符串！！等可迭代对象创建新的列表。  重点：创建列表
#[表达式 for 循环计数器 in 可迭代对象]
#表达式包含循环计数器，for表达式没有循环体，不需要冒号，可迭代对象有几个，就会对表达式执行几次循环。并将每次执行的值收集起来作为新的列表元素：for表达式返回的是列表，因此也被称为列表推导式
a_range=range(10)
a_list=[x*x for x in a_range]
print(a_list)
print([x*x for x in a_range])
b_list=[x*x for x in a_range if x%2==0]#表达式后可加条件
print(b_list)
#将for表达式方括号改为圆括号，for表达式不再生成列表，而生成一个生成器（generator），该生成器可以使用for循环迭代
c_generator=(x*x for x in a_range if x%2==0)
for i in c_generator:
    print(i,end='\t')#!!!
print()
#for表达式可以有多个循环
d_list=[(x,y)for x in range(5)for y in range(4)]
print(d_list)
'''
相当于：
d_list=[]
for x in range(5):
    for y in range(4):
        d_list.append((x,y))
'''
#三层循环嵌套的for表达式
e_list=[[x,y,z]for x in range(5)for y in range(4)for z in range(6)]
print(e_list)
#相当于三层for循环的嵌套
#多个循环的for 表达式也可指定if条件。例如：将数值按照能否整除配对
list_a=[30,12,66,34,39,78,36,57,121]
list_b=[3,5,7,11]
result=[(x,y)for x in list_a for y in list_b if x%y==0]
print(result)
#常用工具函数
#zip()函数，把两个列表压缩成一个zip对象（可迭代），这样就可以用一个循环遍历两个列表，也可以压缩3个列表zip(a,b,c)
a=[4,5,2,16,1]
b=[656,5,454,5]
list_c=[x for x in zip(a,b)]
print(list_c)#由结果可以看出来：压缩得到的可迭代对象为元组（x,x）
books=['java','python','go']
prices=[100,100,100]
for book,price in zip(books,prices):
    print('%s的价格是%d'%(book,price))
#reversed()函数该函数可以接受元组，列表，区间，（字符串）返回一个反序序列，但对参数本身不会产生任何影响！！！
a=range(10)
list_d=[x for x in reversed(a)]
print(list_d,list(a))
str_a='fxacc'
list_e=[x for x in reversed(str_a)]#字符串会被拆分成单个元素
print(list_e)
#sorted()与reversed类似对参数本身不会产生任何影响sorted（a，revese=）若不输入reverse为False，默认从小到大排列;True为从大到小sorted（a，key=len）,根据长短字符串排序4/
a=[1,1,2,1,16,15,6165,16,51,651,5646,546,816]
list_f=[x for x in sorted(a,reverse=True)]
print(list_f)
b=['asdas','dsad','s','gaiwa','fxac','c']
list_g=[x for x in sorted(b,key=len,reverse=True)]
print(list_g)
for s in sorted(b,key=len):
    print(s)
for s in zip(b,a):
    print(s)
#控制循环结构：1.使用break结束循环（完全结束，跳出循环体），只能结束所在的循环，不可以结束嵌套循环外层的外层循环
for i in range(0,10):
    print('i的值是：',i)
    break
for i in range(0,10):
    if i==2:             #对于带else板块的for循环，如果使用break强行终止，则不会执行else快
        break
    else:
        print('else块',i)
#为了能够跳出外层循环，可先定义，bool类的变量来标志是否需要跳出，然后在内外两层分别使用两条break语句
exit_flag=False
for i in range(0,5):
    for j in range(0,3):
        print('i的值为：%d，j的值为%d'%(i,j))
        if j==1:
            exit_flag=True
            break
    if exit_flag:
        break
#使用continue忽略本次循环剩下的语句
for i in range(0,3):
    print('i的值是：',i)
    if i==1:
        continue
    print('continue后的输出语句：')
#使用return结束方法：return后跟变量，常量，表达式，一旦在循环体内执行到return，return就会自动结束该函数或者方法，循环也就随之结束
def test():
    for i in range(10):
        for j in range(10):
            print('i为：%d，j为：%d'%(i,j))
            if j==1:
                return
            print('return后的语句')
test()


#python生成随机数的方法
#import random
#random.random()会返回[0.0,1.0)之间的浮点数
#random.randint(a,b)生成一个[a,b]之间的随机整数 .randrange不包括b
#random.uniform(a,b)生成[a,b]之间的随机浮点数
#ret_list = random.sample(letter_list,n)#随机把前者的n个元素放入retlist
