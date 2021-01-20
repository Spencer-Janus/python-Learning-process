#方法的调用者：self   程序可以通过del 语句删除已有对象的实例变量
'''
定义和使用
'''
class person:
    'this is a class'
    hair='black'
    def __init__(self,name='kate',age=8):
        self.name=name
        self.age=age
    def say(self,content):
        print(self.name+content)
#python类大致有如下的作用
#定义变量  创建对象  派生子类
p=person()
print(p.name)
p.name='陈锐王八蛋'  #可以直接为实例变量赋值
p.say("是真的")
p.skills = ['aa','bb'] #可以为对象增加实例变量
del p.name
#    运行print(p.name)会报错  因为name实例已经被删除

#python也可以为对象动态增加方法  但python不会自动将调用者自动绑定到第一个参数上（即使参数名为self）
def info(self):
    print('info 函数',self)
p.foo=info
p.foo(p)    #需要手动绑定self参数
p.bar=lambda self:print('lambda',self)
p.bar(p)
#可以使用types模块下的MethodType进行包装。
def intro_fuc(self,content):
    print("我是一个人，信息为:%s"%content)
from types import MethodType
p.intro=MethodType(intro_fuc,p)
p.intro('陈锐老王八')
#self对于在类体中定义的实例方法，Python会自动绑定方法的第一个参数（通常命名为self）总是指向调用方法的对象
#由于实例方法（包括构造方法）self自动绑定，因此程序在调用普通实例方法，构造方法时不需要为一个参数传值
#self最大的作用是引用当前方法的调用者，也可以在一个实例方法中访问另一个实例方法 例如：
class Dog:
    def jump(self):
        print('正在执行jump')
    def run(self):
        self.jump()    #此处self可以省略
        print("正在执行run")
chenrui=Dog()
#chenrui.run()
oppo=chenrui.run   #自动绑定的self不依赖调用方式，方法调用函数调用均可
oppo()
class ReturnSelf :  #self可以作为返回值
    def grow(self):
        if hasattr(self,'age'):   #hasattr() 函数用于判断对象是否包含对应的属性。
            self.age+=1
        else:
            self.age=1
        return self
rs=ReturnSelf()
rs.grow().grow().grow()  #self返回值时候，可以多次重复调用函数
print("rs的age是",rs.age)
'''
6.2方法
'''
def foo():
    print("全局变量foo方法：")
bar=20
class Bird:
    def foo(self):
        print("bird类的foo")
    bar=200
foo()
print(bar)
'''
Bird.foo()     通过类来调用实例方法,报错 原因：通过类调用，Pyhton不会自动绑定self
print(Bird.bar)
'''
#解决办法：删掉foo的self函数  或者手动为方法第一个参数传入参数值如下
b=Bird()
Bird.foo(b)
#等效于 b.foo   或者：
Bird.foo('哇哇')#不推荐
'''
一、先是在语法上面的区别:
1、静态方法不需要传入self参数，类成员方法需要传入代表本类的cls参数；
2、静态方法是无法访问实例变量和类变量的，类成员方法无法访问实例变量但是可以访问类变量
二、使用的区别：由于静态方法无法访问类属性，实例属性，相当于一个相对独立的方法，跟类其实并没有什么关系。
这样说来，静态方法就是在类的作用域里的函数而已。
Python会自动绑定类方法的第一个参数，类方法的第一个参数会自动绑定到类本身，但静态方法则不会
'''
class Bird:
    @classmethod    #修饰的是类方法   参数会被自动绑定到类本身
    def fly(cls):
        print("这是类方法Fly：",cls)
    @staticmethod  #静态方法
    def info(p):
        print("这是静态方法info",p)

Bird.fly()   #调用类方法，Bird类会自动绑定到第一个参数
Bird.info("陈瑞王八蛋")   #静态方法需要手动绑定参数
b=Bird()
b.fly()
b.info("陈锐王八蛋")
#一般不会使用类方法和静态方法   但在特殊场景下需要使用（工厂模式）
'''
函数装饰器
格式@函数名
使用@函数A来装饰另外一个函数B的时候，完成两步：
1.将被修饰的函数B作为参数传给函数A
2.将函数B替换成函数A的返回值
'''
def funcA(fn):
    print('A')
    fn()
    return 'fxacc'
@funcA
def funB():
    print('B')
print(funB)
'''
在全局空间，类空间内定义了两个lambda表达式 全局空间的相当于一个普通函数
在类空间的lambda表达式，相当于在类里定义了一个函数，这个函数就是实例方法
程序必须用调用方法的方式调用这个lambda表达式，python同样会为此方法绑定self函数
'''
global_fn=lambda p:print("执行lambda表达式p参数",p)
class Category:
    cate_fn=lambda p:print("执行lambda表达式p参数",p)
global_fn('fkit')
c=Category()
c.cate_fn()
#6.3成员变量
#在类空间内定义的变量属于类变量，可以使用类来读取修改类变量
class Address:
    detail='广州'
    post_code='745000'
    def info(self):
        print(Address.detail)
        print(Address.post_code)
print(Address.detail)   #用类来访问
addr=Address()
addr.info()
Address.detail='西安' #改变类变量
Address.post_code='未知'
addr.info()
#同样，也允许使用对象来访问该对象所属类的类变量（推荐使用类访问类变量）
class Record:
    item='鼠标'
    date='2016-06-10'
    def info(self):
        print("info方法中：",self.item)
        print('info方法中:',self.date)
rc=Record()
print(rc.date)  #同样可以用Record.date
rc.info()
#通过实例访问类变量的本质还是通过类命在访问
class Inventory:
    item='鼠标'
    quartity=2000
    def change(self,item,quantity):
        '''
        这里的赋值语句不是对类变量赋值，而是定义新的实例变量
        '''
        self.item=item
        self.quartity=quantity
iv=Inventory()
iv.change('显示器',500)
print(iv.item)
print(iv.quartity) #500
print(Inventory.item)
print(Inventory.quartity)  #2000   这里访问的是类变量

Inventory.item='类变量item'          #修改类变量对实例变量不产生影响
Inventory.quartity='实例变量quantity'
print(Inventory.item)
print(Inventory.quartity)
print(iv.item)#不影响
#修改实例变量也不会对类变量产生影响
iv.item='实例变量item'
print(Inventory.item)
#使用property函数定义属性
'''
property(fget=None,fset=None,fdel=None,doc=None)
'''
#四个参数分别代表 读 写 删 说明文字
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getsize(self):
        return self.width,self.height
    def setsize(self,size):
        self.width,self.height=size,size
    def delsize(self):
        self.width,self.height=0,0
    size=property(getsize,setsize,delsize,'用来描述矩形的大小')
print(Rectangle.size.__doc__)  #访问size的doc
help(Rectangle.size)           #同上
rect=Rectangle(4,3)
print(rect.size)                     #对size属性读
print(rect.height)
print(rect.width)
rect.size=6                          #对size属性写
print(rect.height)
del rect.size    #对size属性删
print(rect.width)
print(rect.height)
#property也可以传入少量参数
class User:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def getfullname(self):
        return self.first+'.'+self.last
    def setfullname(self,fullname):
        first_last=fullname.rsplit(',')
        self.first=first_last[0]
        self.last=first_last[1]
    fullname=property(getfullname,setfullname)
u=User('悟空','孙')
print(u.fullname)
u.fullname='chen,rui'
print(u.first)
print(u.last)

#@property装饰器来修饰方法，使之成为属性。
class Cell:
    @property
    def state(self):   #修饰成了state属性的get方法
        return self._state
    @state.setter       #修饰state属性的set方法
    def state(self,value):
        if 'alive' in value.lower():
            self._state='alive'
        else:
            self._state='dead'
    @property
    def is_dead(self):       #修饰成了_stead方法的get方法  没有写is_dead.setter故只读不可写
        return not self._state.lower()=='alive'
c=Cell()
c.state='Alive'
print(c.state)
print(c.is_dead)

#6.4  面向对象三大特征 继承 多态 封装
#封装指的是将对象的信息隐藏在对象内部，不允许外部程序访问对象内部信息，而是通过该类所提供的方法实现对内部信息操作和访问
#Python没有private修饰符，因此不支持真正的隐藏
#python的做法：将Python类成员命名为双下划线开头的，python就会把他们隐藏
class User:
    def __hide(self):
        print('示范隐藏的hide方法')
    def getname(self):
        return self.__name
    def setname(self,name):
        if len(name)<3 or len(name)>8:
            raise VaueError('用户名长度必须在3-8之间')
        self.__name=name
    name=property(getname,setname)
    def setage(self,age):
        if age<18 or age>70:
            raise ValueError('用户年龄必须在18-70之间')
        self.__age=age
    def getage(self):
        return self.__age
    age=property(getage,setage)
u=User()
u.name='chenrui'
print(u.name)
#u.__hide()  报错
u._User__hide()   #可以调用隐藏，但不建议这么干
#类似地u._User__name='fk'可以直接绕过setname给__name赋值
#6.5   继承
'''
继承 父类放在子类的圆括号里
class SubClass(SuperClass1,SuperClass2):
    #类体
如果一个类没有定义父类，那么这个类默认继承object类
'''
#object类是所有类的父类
class Fruit:
    def info(self):
        print("我是一个水果")
class Food:
    def taste(self):
        print("我是一种食物")
class Apple(Fruit,Food):
    pass
a=Apple()
a.info()  #子类可以继承得到父类定义的方法
a.taste()
#除了c++和python，别的语言只支持单继承，但多继承会导致一些莫名其妙的错误
'''
如果一个子类有多个父类，父类中包含了同名的方法
排在前面的方法会遮蔽排在后面的同名方法
'''
class item:
    def info(self):
        print("item类")
class Product:
    def info(self):
        print("Product类")
class Mouse(item,Product):
    pass
moucse=Mouse()
moucse.info()     #Product里面的info方法被遮盖，如果item和Product的继承顺序改变，那么item的info方法被遮盖
'''
重写父类的方法：
'''
class Bird:
    def fly(self):
        print("我在天空自由自在飞行")
class Ostrich(Bird):
    def fly(self):
        print("我不能飞")
os=Ostrich()
os.fly()   #可以看到运行的是子类的Fly，所以只要在子类里重写方法即可完成覆盖
'''
重新调用父类被覆盖的方法
'''
class BaseClass:
    def foo(self):
        print('父类中定义的foo')
class SubClass(BaseClass):
    def foo(self):
        print('子类的foo')
    def bar(self):
        print("执行bar")
        self.foo()
        BaseClass.foo(self)  #需要为第一个参数self绑定参数值
sc=SubClass()
sc.bar()
'''
使用super函数调用父类的构造方法
python子类也会继承得到父类的构造方法，如果子类有多个直接父类，那么排在前面的父类的构造方法也会被优先使用
'''
class Employee:
    def __init__(self,salary):
        self.salary=salary
    def work(self):
        print("普通员工正在写代码，工资是：",self.salary)
class Cusomer:
    def __init__(self,favorite,address):
        self.favorite=favorite
        self.address=address
    def info(self):
        print('我是一个顾客，我的爱好是：%s,地址是%s'%(self.favorite,self.address))
class Manager(Employee,Cusomer):
    pass
m=Manager(25000)
m.work()
#m.info() 不能运行，程序使用的是Employee的构造方法创建的manager对象，并没有初始化Customer对象需要的favorite和adress
class Manager(Cusomer,Employee):
    pass
m=Manager('IT','南京')
#m.work() 不能运行理由同上
m.info()
'''
为了同时初始化两个父类的实例变量，Manager应该定义自己的构造方法，python要求：
如果重写了父类的构造方法，那么子类的构造方法必须吊桶父类的构造方法
构造方法两种：
1.使用未绑定方法
2.使用super()函数
通过supper对象的方法既可以调用父类的实例方法，也可调用父类的类方法
1.调用实例方法，会完成第一个参数self的绑定
2.调用类方法，程序会完成第一个参数clas的自动绑定
'''
class Manager(Employee,Cusomer):
    def __init__(self,salary,favorite,address):
        print('manage的构造方法')
        super().__init__(salary)  #2.使用super函数构造，不需要绑定self
        Cusomer.__init__(self,favorite,address)#使用未绑定方法构造
m=Manager(25000,'IT','南京')
m.work()
m.info()
#6.6  Python的动态性
'''
之前介绍了为对象动态添加方法，但是所添加的方法只对当前对象有效，如果希望所有实例添加
则可以为类添加方法，如下：
'''
class Cat:
    def __init__(self,name):
        self.name=name
def walk_func(self):
    print('%s 慢慢走过一片草地'%self.name)
d1=Cat('chenrui')
d2=Cat('kitty')
Cat.walk=walk_func #第一个参数自动绑定,为Cat动态添加了walk方法，不需要MethodType包装，第一个参数自动绑定
d1.walk()
d2.walk()
'''
动态添加方法虽然方便，但有隐患，有可能被其它程序修改，如果要限制某个类动态添加属性和方法，则通过__slots__指定
__slots__属性的值是一个元组，该元组的所有元素列出了该类的实例允许动态添加的所有属性名和方法名
'''
class Dog:
    __slots__ = ('walk','age','name')#只允许实例变量添加walk age name
    def __init__(self,name):
        self.name=name
    def text(self):
        print('预先定义的test')
d=Dog('snoopy')
from types import MethodType
d.walk=MethodType(lambda self:print('%s 正在慢慢走' %self.name),d)
d.age=5
d.walk()
#程序只允许为Dog动态实例添加walk age name 三个属性或实例方法，但不限制通过类动态添加属性或方法,因此下列语句合法
Dog.bar=lambda self:print('abc')
d.bar()
#需要说明的是__slots__指定的限制只对当前类的实例起作用，对派生出来的子类不起作用，若要限制，重新定义
'''
使用type（）函数定义类，type()函数可以查看变量的类型，如何查看类的类型?
'''
class Role:
    pass
r=Role()
print(type(r))
print(type(Role))
#从输出结果可以看到Role类本身是类型是Type,因此程序使用class定义的类都是type类的实例
#python允许用type()创建type对象，因此可以用type()来动态创建类
def fn(self):
    print('fn函数')
Dog=type('Dog',(object,),dict(walk=fn,age=6))
'''
参数一：创建的类名  参数二：该类继承的父类集合，因此此处使用元组指定它的多个父类，即使一个父类，也需要使用元组
参数三：该字典对象为该类绑定的类变量和方法。key是类变量或方法名，如果value是普通值，那就代表变量，如果value是函数
        则代表方法
'''
d=Dog()
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)
#总结:无论通过那种方式创建类，程序最终是type的实例
'''
如果希望创建某一批类全部具有某种特征，通过metaclass来实现，使用metaclass可以在创建类时动态修改类定义
为了使用metaclass，程序需要先定义metaclass，metaclass应该继承type类，并重写__new__方法。
'''
class ItemMetaClass(type):
    def __new__(cls,name,bases,attrs):
        '''
        cls代表被动态修改的类
        name代表被动态修改的类名
        bases代表被修改类的所有父亲
        attr代表被修改类的所有属性和方法
        '''
        attrs['cal_price']=lambda self: self.price *self.discount
        return type.__new__(cls,name,bases,attrs)
#metaclass类的方法作用是：当程序使用class定义新类时，如果指定了metaclass，那么metaclass的__new__方法会自动执行
class Book(metaclass=ItemMetaClass):
    __slots__ = ('name','price','_discount')
    def __init__(self,name,price):
        self.name=name
        self.price=price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self,discount):
        self._discount=discount
class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price','_discount')
    def __init__(self,price):
        self.price=price
    @property
    def discount(self):
        return  self._discount
    @discount.setter
    def discount(self,discount):
        self._discount=discount
#定义Class 和 CellPhone时，都指向了metaclass，因此创建这两个类,itemMetaclass的__new__会被调用
'''
__new__方法会为目标类动态添加cal_price方法，因此，虽然在定义Book类和cellphone两类没有定义call_price
但这两个类依然有cal_price()，如下
'''
b=Book("疯狂的陈锐",89)
b.discount=0.76
#创建book的calprice方法
print(b.cal_price())
cp=CellPhone(239)
cp.discount=0.85
#创建cellphone的callprice方法
print(cp.cal_price())
'''
6.7多态：当同一个变量在调用同一个方法时，完全可能出现多种行为
同一个变量可以在不同的时间引用不用的对象
'''
class Bird:
    def move(self,field):
        print("鸟在%s上自由的飞翔"%field)
class Dog:
    def move(self,field):
        print("狗在%s上自由的奔跑" % field)
x=Bird()
x.move("天上")
x=Dog()
x.move("地上")
#同一个变量x在执行同一个move()方法时，x指向的对象不同，呈现不同的特征，这就是多态
class Canvas:
    def draw_pic(self,shape):
        print('开始画图')
        shape.draw(self)
class Rectangle:
    def draw(self,canvas):
        print("在%s上画矩形" % canvas)
class Triangle:
    def draw(self,cancas):
        print('在%s上画三角形' % cancas)
c=Canvas()
c.draw_pic(Rectangle())
c.draw_pic(Triangle())
#以上为python多态的优势
'''
6.7.2 检查类型
issubclass(cls,class_or_tuple):检查clas是否为后一个类或元组包含个多个类中任意的子类
isinstance(obj,class_or_tuple):检查obj是否为后一个类或元组包含多个类及其子类中任意类的对象
'''
#例如
hello='Hello'
print('hello 是否为str类的实例：',isinstance(hello,str))
print('hello是否为object类的实例：',isinstance(hello,object))
print('str是否为object类的子类：',issubclass(str,object))
print('hello是否为tuple类的实例：',isinstance(hello,tuple))
print("str是否为tuple的子类：",isinstance(str,tuple))
my_list=[2,4]
print('[2,4]是否是list的实例：',isinstance(my_list,list))
print('[2,4]是否是object类及其子类的实例',isinstance(my_list,object))
print('list是否是object类的子类：',issubclass(list,object))
print('[2,4]是否是tuple类的实例',isinstance(my_list,tuple))
print('list是否是tuple类的子类',issubclass(list,tuple))
'''
# 通过上面程序可以看出，issubclass()和isinstance()两个函数差不多，区别只是insubclass的第一个参数是类名
#而isinstance第一个参数是变量，这也与两个函数的意义对应，issubclass判断是否子类，而instance是否为该类或子类的实例
#另外这两个函数的第二个参数都可以使用元组
'''
#python为所有类提供了一个__bases__属性，用过该属性可以查看该类的所有“直接”父类
class A:
    pass
class B:
    pass
class C(A,B):
    pass
print("c的直接父亲",C.__bases__)
#python为所有类提供了一个__subclasses__()属性，用过该属性可以查看该类的所有“直接”子类
print("A的直接子类",A.__subclasses__())
"""
6.8  枚举类
在某些情况下，一个类的对象是有限且固定的，比如季节类，只有春夏秋冬，这种实例有限且固定的类交枚举类
程序有两种方式定义枚举类
1.直接使用Enum列出多个枚举值来创建枚举类
2.通过继承Enum基类来派生枚举类
"""
#1.直接法
import enum

Season=enum.Enum('Season',('spring','summer','fall','winter'))
#第一个参数为类名,第二个参数为枚举值列表
#每个枚举成员有name,value两个属性，name为变量名，value为序号
print(Season.spring.name)
print(Season.summer.value)
print(Season(3))
#枚举类__members__属性，该属性返回一个字典dict，包含所有枚举实例   如：：
for name,member in Season.__members__.items():
    print(name,'->',member,member.value)
#2. 间接法（适用于复杂的枚举）
import enum
class Orientation(enum.Enum):
    EAST='东'
    SOUNTH='南'
    WEST='西'
    NORTH='北'
    def info(self):
        print("这是一个代表方向【%s】的枚举"%self.value)
print(Orientation.SOUNTH)
print(Orientation.SOUNTH.value)
print(Orientation['WEST'])
print(Orientation('南'))#虽然枚举的value是str类型，但是也可以通过这个value来访问
Orientation.EAST.info()
for name,member in Orientation.__members__.items():
    print(name,'->',member,member.value)
#6.8.2枚举的构造器
class Gender(enum.Enum):
    MALE='男','陈锐爱'
    FEMALE='女','陈瑞也爱'
    def __init__(self,cn_name,desc):
        self._cn_name=cn_name
        self._desc=desc
    @property
    def desc(self):
        return self._desc
    @property
    def cn_name(self):
        return self._cn_name
print('FEMALE的name',Gender.FEMALE.name)
print('FEMALE的vale',Gender.FEMALE.value)
print('FEMALE的字定义cn_name属性',Gender.FEMALE.cn_name)
'''
Gender类定义了一个构造器，调用该构造器需要传入cn_name,和desc两个参数
因此程序使用代码定义Gender的枚举值
MALE='男'，'陈锐爱'
上面代码为MALE枚举指定的value是男和阳刚之力这两个字符串，其实它们会被自动封装成元组后传给MALE的value属性;
而且此处传入的男和阳刚之力这两个参数值正好分别传给 cn_ _name 和desc两个参数。简单来说，枚举的构造器需要几个参数，
此处就必须指定几个值。
'''