#chapter 8  python类的特殊方法
'''
Python是一门尽量简单的语言，它不像某些语言(如Java)需要让类实现接口，:并实现接口中的方法。
Python采用的是一种“约定”的机制，Python 按照约定，以特│殊名字的方法、属性来提供特殊的功能。

Python类中的特殊方法、特殊属性有些需要开发者重写，有些则可以直接调用，
掌握这些常见的特殊方法、特殊属性也是非常重要的。

'''

#8.1.1 重写__repr__方法
class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
im=Item('鼠标',29.8)
print(im)
'''
输出内存中的一个对象，
实际上输出的是Item对象的_repr_()方法的返回值。也就是说，下面两行代码的效果完全一样。
print(im)
'''
print(im.__repr__)#__repr__方法是object类提供的
#__repr__并不能实现真正的“自我描述”功能，需要重写
class Apple:
    def __init__(self,color,weight):
        self.color=color
        self.weight=weight
    def __repr__(self):
        return "Apple [color=" +self.color+"weight= "+str(self.weight)+']'
a=Apple("红色",5.56)
print(a)
#8.1.2 析构方法__del__

#__init__方法用于初始化对象，而__del__则用于销毁python对象，在任何python对象将要被系统回收之时，系统都会自动调用
#该对象的__del__方法
'''
当程序不再需要一个 Python对象时，系统必须把该对象所占用的内存空间释放出来，这个过程被称为垃圾回收，
Python会自动回收所有对象所占用的内存空间，因此开发者无须关心对象垃圾回收的过程。
Python采用自动引用计数(ARC）方式来回收对象所占用的空间，当程序中有一个变量引用该Python对象时，
Python会自动保证该对象引用计数为1;当程序中有两个变量引用该Python对象时，Python会自动保证该对象引用计数为2……
依此类推，如果一个对象的引用计数变成了0，则说明程序中不再有变量引用该对象，表明程序不再需要该对象，因此 Python 就会回收该对象。

当一个对象被垃圾回收时，python就会自动调用该对象的__del__方法
需要说明的是 对一个变量执行del操作不一定回收变量所引用的对象，只有当计数为0时，该对象才会被回收

因此，如果一个对象如果有多个变量引用，del其中一个变量是不会回收该对象的
'''
class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __del__(self):
        print('删除对象')
im=Item('陈锐',0.00001)
x=im
del im
print('------------------')
#可以看到----------在删除对象之前出现，说明del im系统并不会回收Item对象，如果注释掉x=im,则会回收
#最后需要说明的是，如果父类提供了_del ()方法，则系统重写_del_()方法时必须显式调用父类的 del_()方法，
# 这样才能保证合理地回收父类实例的部分属性。

# 8.1.3 __dir__方法
#对象__dir__方法用于列出对象内部的所有属性（包括方法）名，该方法会返回包含所有属性（方法）的序列
#当程序执行dir(obejct)函数时，实际上就是将该对象的__dir__（）方法返回值进行排序，然后包装成列表
class Item2:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def info(self):
        pass
Im=Item2("鼠标",20)
print(Im.__dir__())
print(dir(Im))


#8.1.4   __dict__属性
#该属性用于查看对象内部存储的所有属性名和属性值组成的字典，通常程序直接使用该属性即可。程序使用__dict__属性即可
#查看对象的所有内部状态，也可以通过字典语法来访问或修改指定属性的值
class Item2:
    def __init__(self,name,price):
        self.name=name
        self.price=price
Im=Item2("鼠标",20)
print(Im.__dict__)
print(Im.__dict__['name'])
print(Im.__dict__['price'])
print(Im.price)
print(Im.name)

#8.1.5 __getattr__, __setattr__
'''
当程序操作（包括访问，设置，删除）对象的属性时，Python系统同样会执行该对象特定的方法
__getattribute__(self, name):当程序访问对象的name属性时被自动调用。
__getattr__(self, name):当程序访问对象的name属性且该属性不存在时被自动调用。
__setattr__(self, name, value):当程序对对象的name属性赋值时被自动调用。
__delattr__(self, name):当程序删除对象的name属性时被自动调用。
python可以通过重写这些方法来“合成”属性，例如如下程序
'''
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def __setattr__(self,name,value):
        print('---设置%s属性---'%name)
        if name=='size':
            self.width,self.height=value   #value此刻是一个元组
        else:
            self.__dict__[name]=value
    def __getattr__(self, name):
        print('---读取%s属性---'%name)
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError
    def __delattr__(self, name):
        print('---删除%s属性---'%name)
        if name=='size':
            self.__dict__['width']=0
            self.__dict__['height']=0
rect=Rectangle(3,4)
print(rect.size)
rect.size=6,8  #6，8被包装为元组

print(rect.width)
print(rect.height)
del rect.size
print(rect.size)

#8.2与反射相关的属性和方法
#如果程序在运行过程中要动态判断是否包含某个属性(包括方法)，甚至要动态设置某个属性值，则通过python的反射来实现
'''
8.2.1
在动态检查对象是否包含某些属性（包括方法）相关的函数有如下几个。
hasattr(obj, name):检查obj对象是否包含名为name的属性或方法。
getattr(object, name[ , default]):获取object对象中名为name的属性的属性值。
setattr(obj, name, value, /):将obj对象的name属性设为value。
'''
class Comment:
    def __init__(self,detail,view_times):
        self.detail=detail
        self.view_times=view_times
    def info(self):
        print('一条简单的评论，内容是%s'% self.detail)
c=Comment("陈锐真不错",20)
print(hasattr(c,'detail'))
print(hasattr(c,'view_times'))
print(hasattr(c,'info'))

print(getattr(c,'detail'))
print(getattr(c,'view_times'))

setattr(c,'detail','陈锐锐')  #如果设置不存在的方法，使用setattr()函数 即为对象添加新的属性
setattr(c,'view_times',32)
#setattr还可设置对象，比如：
def bar():
    print('一个简单的bar')
setattr(c,'info',bar)  #注意bar的格式，如果写成 'bar' info就被设置为字符串bar
c.info()

#8.2.2 __call__属性     函数含有这个属性
#hasattr()只能判断属性或方法是否存在，但到底是属性还是方法，需要进一步判断是否可以调用，程序可以通过是否包含__call__属性来确定
class User:
    def __init__(self,name,passwd):
        self.name=name
        self.passwd=passwd
    def validLogin(self):
        print("验证%s的登陆"% self.name)
u=User('crazyit','leegang')
print(hasattr(u.name,'__call__')) #FALSE
print(hasattr(u.passwd,'__call__'))#FALSE
print(hasattr(u.validLogin,'__call__'))#TRUE

#我们也可以定义__call__方法，使得类的实例也可以调用
class Role:
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('执行Role对象')
r=Role('chenrui')
r()

#对程序中的函数，同样既可以用函数的语法来调用它，也可以把函数当对象，调用它的__call__方法
def foo():
    print('foo函数')
foo()
foo.__call__()

#8.3与序列相关的特殊方法
'''
__len__(self):该方法返回值决定序列中元素的个数
__getitem__(self,key):获取指定索引对应的元素，该方法的key应该是整数或者slice对象，否则发生KeyError
__contains__(self,item):该方法判断序列是否包含指定元素
__setitem__(self.key,value):  该方法设置指定索引对应的元素。该方法的key应该是整数值，或slice对象，否则引发KeyError
__delitem__(self,key):该方法删除指定索引对应的元素
如果程序要实现不可变序列（只能获取，不能修改），只要实现上面前三个方法就行了，如果可变序列，则要实现5个方法
下面程序实现一个字符串序列，默认每个字符串的长度都是3，该序列按 AAA，AAB,AAC这种格式排列
'''
def check_key(key):
    '''
该函数将会负责检查序列的索引，该索引必须是整数值，否则引发TypeError异常
且程序要求索引必须为非负整数值，否则引发工ndexError异常
    '''
    if not isinstance(key,int):raise TypeError("索引值必须是整数")
    if key<0:raise IndexError("索引值必须是非负整数")
    if key >=26**3: raise IndexError("索引值不能超过%d"%26**3)
class StringSeq:
    def __init__(self):
        #用于存储被修改的数据
        self.__changed={}
        #用于存储已经删除元素的索引
        self.__deleted=[]
    def __len__(self):
        return 26**3
    def __getitem__(self, item):
        check_key(item)
        if item in self.__changed:
            return self.__changed[item]
        if item in self.__deleted:
            return None
        #否则根据计算规则返回序列元素
        three=item//(26*26)#整数除法
        two=(item-three*26*26)//26
        one=item%26
        return chr(65 + three) + chr(65 + two) + chr(65 + one)
    def __setitem__(self, key, value):
        check_key(key)
        self.__changed[key]=value
    def __delitem__(self, key):
        check_key(key)
        if key not in self.__deleted: self.__deleted.append(key)
        if key in self.__changed: del self.__changed[key]
sq=StringSeq()
print(len(sq))   #实际上就是返回__len__的返回值
print(sq[26*26])
print(sq[1])
sq[1]='fkit'
print(sq[1])
del sq[1]
print(sq[1])
sq[1]='crazyit'
print(sq[1])
#8.3.2实现迭代器
'''
前面介绍了使用for 循环遍历列表、元组和字典等，这些对象都是可迭代的，因此它们都属迭代器。
如果开发者需要实现迭代器，只要实现如下两个方法即可。
__iter__ (self):该方法返回一个迭代器（iterator)，迭代器必须包含一个_next_()方法 该方法返回迭代器的下一个元素。
__reversed__ (self):该方法主要为内建的reversed()反转函数提供支持,当程序调用reversed()
函数对指定迭代器执行反转时，实际上是由该方法实现的。
从上面介绍不难看出，如果程序不需要让迭代器反转迭代，其实只需要实现第一个方法即下面程序将会定义一个代表斐波那契数列(数列的元素等于前两个元素之和: f(n+2)=f(n+1)+f(n)的迭代器。
'''
class Fibs:
    def __init__(self,len):
        self.first=0
        self.sec=1
        self.__len=len
    def __next__(self):
        if self.__len==0:
            raise StopIteration
        self.first,self.sec=self.sec,        self.first+self.sec
        self.__len-=1
        return self.first
    def __iter__(self):
        return self
fibs=Fibs(10)
print("斐波那契数列")
for el in fibs:
    print(el,end=' ')
print('')
#此外，程序可使用内置的 iter()函数将列表、元组等转换成迭代器，例如如下代码。
my_list=iter([2,'xyz',4])
print(my_list.__next__())
print(my_list.__next__())
#8.3.3 扩展列表、元组和字典
#如果程序明确需要一个特殊的列表，元组或字典类，我们可以扩展系统已经有的列表元组或字典
#下面这个字典类可以根据value来获取key，由于字典中value是可以重复的，因此该方法会返回指定value对应的全部key组成的列表
class ValueDict(dict):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def getkeys(self,val):
        result=[]
        for key,value in self.items():
            if value==val:result.append(key)
        return  result
my_dict=ValueDict(语文=92,数学=89,英语=92)
print(my_dict.getkeys(92))
