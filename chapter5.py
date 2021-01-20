'''
定义函数和调用函数   格式：
def 函数名（形参表）
    函数体
'''
def my_max(x,y):
    z=x if x>y else y
    return z
'''
上面的函数也可以写为：
def my_max(x,y):
    return x if x>y else y


'''
def sai_hi(name):
    return name+"您好"  #return  既可以返回有值的变量，也可以是一个表达式
a=6
b=9
result=my_max(a,b)
print("result:",result)
print(sai_hi('chenrui'))
#help()可以查看函数的说明文档 ，也可以通过函数的__doc__属性访问函数的说明文档 例如：
help(len)
#为函数编写说明文档
def my_max(x,y):
    '''
    获取两个数值之间较大的那个函数
    my_max(x,y)
        返回x，y两个之间较大的那个数
    '''
    z=x if x>y else y
    #返回z的值
    return z
help(my_max)
print(my_max.__doc__) #与上一句等价
#多个返回值
def sum_and_avg(list):
    sum=0
    count=0
    for e in list:
        if isinstance(e,int) or isinstance(e,float):     #isinstance(x,int)判断数据的类型 返回bool
            count+=1
            sum+=e
    return sum,sum/count
my_list=[20,15,2.8,'a',35,5.9,-1.8]
tp=sum_and_avg(my_list)
print(tp)
s,avg=sum_and_avg(my_list)
print(s)
print(avg)
#递归函数
def fn(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fn(n-1)
print(fn(2))
#5.2函数的参数
def girth(width,height):
    print("width:",width)
    print("height:",height)
    return  2*(width+height)
print(girth(3.5,4.8))
#根据关键字传参数
print(girth(width=3.5,height=4.8))
#根据关键字参数时可以交换位置
print(girth(height=4.8,width=3.5))
#部分使用关键字参数
print(girth(3.5,height=4.8))
'''
!!!!!在混用关键字参数和位置参数时，关键字参数必须在位置参数后面
print(width=3.5,4.8)错误
print(girth(4.8,width=3.5))  顺序错误,两个值都会传送给width
'''
#5.2.2参数默认值
def say_hi(name="孙悟空",message="欢迎来到疯狂软件"):
    print(name,"您好")
    print("消息是：",message)
say_hi()
say_hi("皮皮")#自动给name
say_hi('贝贝','欢迎您来到德莱联盟')
say_hi(message="欢迎")#给message，name使用默认
#say_hi(name='陈锐',"欢迎")  关键字参数后面只能是关键字参数
#say_hi('欢迎',name="陈锐") 错误 两个值都给了name
def printTriangle(char,height=5):
    for i in range(1,height+1):
        for j in range(height-i):
            print(' ',end='')
        for j in range(2*i-1):
            print(char,end='')
        print()
printTriangle("@",6)
printTriangle('#',height=7)
printTriangle(char='*' )
#5.2.3参数收集(个数可变的参数 )
#python允许在形参前添加一个 * ，多个参数之被当成元组传入
def test(a,*books):
    print(books)
    for b in books:
        print(b)
    print(a)
test(5,"陈锐社朱",'车贝瑞狗')
#参数收集的本质：元组 python允许个数可变的形参可以处于列表的任意位置，但（每个函数只能带一个）
def test(*books,num):
    print(books)
    for b in books:
        print(b)
    print(num)
test("疯狂的陈锐",'狗狗陈锐',num=20)#num必须使用关键字参数，否则将被*books收集完
'''
python还可以收集关键字参数，此时python会将关键字参数收集成字典，为了让python能收集关键字参数，需要在参数前加两个
星号，在这种情况下，一个函数可以包含一个支持*参数收集 和**参数收集
'''
def test(x,y,z=3,*books,**scores):
    print(x,y,z)
    print(books)
    print(scores)
test(1,2,3,"crsx","crdsx",'crddddsx',语文=20,数学=10)
#123对应xyz，*books收集三个字符串，**scores收集关键字参数
test(1,2,3,语文=20,数学=10)#books空元组
#5.2.4逆向参数收集
#逆向参数收集，在程序有列表，元组，字典的前提下，把它们的元素拆开后传给函数的参数，列表元组*，字典**，如：
def test(name,message):
    print("用户是：",name)
    print("欢迎消息",message)
my_list=['陈锐','大猩猩']
test(*my_list)#列表的长度必须是2，与参数个数一直，不然报错
def foo(name,*nums):
    print('name:',name)
    print("nums:",nums)
my_tuple=(1,2,3)
foo('fkit',*my_tuple)
print()
#如果不加*，整个元组或列表将会作为一个参数传给函数
foo(my_tuple)
def bar(book,price,desc):
    print(book,'价格是:',price)
    print('描述信息',desc)
my_dict={'price':89,'book':'陈锐是猩猩','desc':'这是锐哥的自传'}
bar(**my_dict)#根据key-value匹配参数，根据key把value给参数
#5.2.5函数的参数传递机制
'''
Python的参数值是如何传入函数的呢?这是由 Python函数的参数传递机制来控制的。
Python中函数的参数传递机制都是“值传递”。所谓值传递，就是将实际参数值的副本（复制品）传入函数，
而参数本身不会受到任何影响。
如:
'''
def swap(a,b):
    a,b=b,a
    print('a是：',a,'b是:',b)
a=6
b=9
swap(a,b)
print(a,b)
def swap(dw):
    dw['a'],dw['b']=dw['b'],dw['a']
    print('a元素',dw['a'],'b元素',dw['b'])
dw={'a':6,'b':9}
swap(dw)#传入的是字典的复制品，但是操作的还是字典本身，所以这两个元素成功交换，但swap的dw和外部dw是两个dw
print(dw)
'''
“不管什么类型的参数，在Python函数中对参数直接使用”=“符号赋值是没用的，直接使用“=”符号赋值并不能改变参数。
如果需要让函数修改某些数据，则可以通过把这些数据包装成列表、字典等可变对象，然后把列表、字典
等可变对象作为参数传入函数，在函数中通过列表、字典的方法修改它们，这样才能改变这些数据.
'''
#5.2.6 变量作用域
'''
》局部变量。在函数中定义的变量，包括参数，都被称为局部变量。
>全局变量。在函数外面、全局范围内定义的变量，被称为全局变量。
每个函数在执行时，系统都会为该函数分配一块“临时内存空间”，所有的局部变量都被保存 在这块临时内存空间内.
当函数执行完成后,这块内存空间就被释放了,这些局部变量也就失效了， 因此离开函数之后就不能再访问局部变量了.
全局变量意味着它们可以在所有函数内被访问。
'''
'''
实际上，Python提供了如下三个工具函数来获取指定范围内的“变量字典”。
globals():该函数返回全局范围内所有变量组成的“变量字典”。
locals():该函数返回当前局部范围内所有变量组成的“变量字典”。
vars(object):获取在指定对象范围内所有变量组成的“变量字典”。如果不传入 object参
数，vars(和locals(的作用完全相同。
globals()和 locals()看似完全不同，但它们实际上也是有联系的，关于这两个函数的区别和联系 嫄致有以下两点。
locals()总是获取当前局部范围内所有变量组成的“变量字典”，因此，如果在全局范围内(在函数之外）调用locals()函数，同样会获取全局范围内所有变量组成的“变量字典;而
globals()无论在哪里执行，总是获取全局范围内所有变量组成的“变量字典”。
一般来说，使用locals()和globals()获取的“变量字典”只应该被访问，不应该被修改。但 实际上，不管是使用globals()还是使用locals()获取的全局范围内的“变量字典”，都可以
被修改，而这种修改会真正改变全局变量本身;但通过locals()获取的局部范围内的“变量
字典”，即使对它修改也不会影响局部变量。
下面程序示范了如何使用locals()、globals()函数访问局部范围和全局范围内的“变量字典”.
'''
def test():
    age=20
    print(age)
    print(locals())
    print(locals()['age'])
    locals()['age']=12
    print(age)#仍然输出20
    globals()['x']=19
test()
name='charlie'
def test():
    print(name)
test()
print(name)
#如果在print后加 name=‘陈锐’，就会报错name未定义 原因：重新定义了name，全局变量name被遮蔽
#1.访问被遮蔽的全局变量
name='charlie'
def test():
    print(globals()['name'])
    name='孙悟空'
test()
print(name)
#2.在函数中声明全局变量
name='charlie'
def test():
    global name
    print(name)  #global之后程序会把name当全局变量，后面对name赋值也是对全局变量赋值
test()
print(name)
#5.3局部函数：函数体内定义的函数
def get_math_func(type,nn):
    def square(n):
        return n*n
    def cube(n):
        return n*n*n
    def fac(n):
        result =1
        for index in range(2,n+1):
            result*=index
        return result
    if type=="sqiare":
        return  square(nn)
    elif type=='cube':
        return  cube(nn)
    else:
        return fac(nn)
#如果没有返回局部函数，那么只能在函数体内使用，返回后可以当全局函数使用
print(get_math_func('square',2))
print(get_math_func('cube',2))
print(get_math_func('fac',3))
'''
def foo:
    name='chenrui'
    def bar():
        print(name)
        name='陈锐锐'
    bar()
foo()
'''
#报错：运行局部函数，导致局部变量（小）遮蔽了局部变量（大）
#  @@@  nonlocal关键字：声明访问该局部函数所在函数内的局部变量  和global类似
def foo():
    name='chenrui'
    def bar():
        nonlocal name
        print(name)
        name='sunsun'
    bar()
foo()
#高级应用
#5.4.1 使用函数变量
def pow(base,exp):
    result=1
    for i in range(1,exp+1):
        result*=base
    return result
my_fun=pow   #接收函数，把函数名赋给变量
print(my_fun(2,2))
#5.4.2函数名当形参
def map(data,fn):
    result=[]
    for e in data:
        result.append(fn(e))
    return result
def square(n):
    return n*n
def cube(n):
    return  n*n*n
def fac(n):
    result=1
    for index in range(2,n+1):
        result *=index
    return result
data=[3,4,9,5,8]
print("原数据：",data)
print(map(data,square))
print(map(data,cube))
print(map(data,fac))
#5.4.3使用函数作为返回值
def get_math_func(type):
    def square(n):
        return n*n
    def cube(n):
        return n*n*n
    def fac(n):
        result=1
        for i in range(2,n+1):
            result *=index
        return result
    if type=="square": #只返回函数名
        return  square
    if type=="cube":
        return cube
    if type=="fac":
        return fac
a=get_math_func('square')
print(a(2))
#5.5lambda表达式
#5.5.2使用lambda表达式代替局部函数
def get_math_func(type):
    result=1
    if type=='square':
        return lambda n: n*n
    if type=='cube':
        return lambda n:n*n*n
a=get_math_func('cube')
print(a(2))
'''
lambda表达式只能是单行
lambda 形参 ： 函数体
在lambda关键字之后，冒号左边是参数列表，也可以没有参数，冒号右边是返回值
'''
#用法：
b=lambda x,y:x+y  #lambda表达式直接赋给变量 此时相当于变量名
print(b(1,2))
'''
python内置的map()函数
map(函数，序列)  例如：
map(lambda x:x*x,[1,2,3])
'''


