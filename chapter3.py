#列表，元组，字典                         列表与元组的区别：元组不支持对元素的修改
my_list=['crazy',20,'cool']#列表
print(my_list)
your_list=('color',15,'red')#元组
print(your_list)
#列表和元组元素同字符串一样，也可通过序列访问，例：
print(my_list[0])
#切片：访问[start:end:step]   step为步长
print(my_list[::2])
#加法：两个元素的总和，列表只能同列表相加
we=my_list + my_list
print(we)
print(my_list+['gaiwa'])#还可用加法增添元素
#乘法加法结合
order_endings=('st','nd','rd')\
    +('th',)*17+('st','nd','rd')\
    +('th',)*7+('st',)
print(order_endings)
'''day=input('输入日期1-13：')
day_int=int(day)
print(day+order_endings[day_int-1])'''
#in 运算符同样适用于此,返回bool值
print('20'in my_list)
#python内置的len（）、max（）、min（）函数来获取元组或者列表的长度，比较大小时，字符串依次比较每个字母的ASCII码，且python支持将多个值赋值给多个变量
x,y,z=1,2,3
a,b,*rest=range(1,10)     #列表保存剩余的
print(rest)
*rest2,last=range(1,10)   #列表保存前边剩余的元素
print(rest2)
#list()函数可以将元组、区间（range）等对象转换为列表,字符串也可以，会被拆分成单个字母
tuple_=('xin','six',6)
b_tuple=list(tuple_)
print(b_tuple)
a_range=range(1,10)
list_range=list(a_range)
print(list_range)
#tuple()函数可以将列表、区间、等转化为元组
c_tuple=tuple(range(1,50,6))
print(c_tuple)
print(1)
#为列表增加元素  append()改变原列表！！！  括号里可以是单个值，也可以是元组、列表，不能是区间！！！但元组和列表只是作为单个元素加入,字符串作为整体
our_list=['crazy',20,'cool']
my_list.append('50')
#my_list2=my_list.append(my_list1),括号内当作单个元素的加入     #这种方法不可取
print(my_list)
my_list.append(our_list)
print(my_list)
my_list.append(tuple_)
print(my_list)
#若不希望被作为单个元素加入   使用extend()函数  区间/列表/元组         改变原列表！！！,若是字符串，则会被单个拆分
our_list=['crazy',20,'cool']
our_list.extend([1,2,3])
our_list.extend(('ok','ko'))
our_list.extend(range(1,100,10))
print(our_list)
#将元素插入到具体位置   insert(位置，)  若是字符串，则不会被单个拆分，元组列表均不拆分                           改变原列表！！！
c_list=list(range(1,6))
print(c_list)
c_list.insert(3,100)
c_list.insert(4,our_list)
c_list.insert(1,(10086,10000))                      #将列表元组插入的时候均作为单个元素
print(c_list)
#删除列表元素  del语句,不仅可以删除列表元素，也可删除变量，删除后后来者居上
d_list=list(range(1,6))
del(d_list[2])
print(d_list)
del(d_list[0:2])    #可使用索引
print(d_list)
'''name=1
del name
print(name)'''   #删除变量
#删除元素     remove(**)只删除第一次找到的**删除后后来者居上
e_list=list(range(1,6))
e_list.append(1)
e_list.remove(1)
print(e_list)
#删除元素          clear()清空列表所有元素
#修改元素         对列表元素直接赋值便可修改
f_list=[1,2,3,4,5,6]
f_list[1]=0
print(f_list)
f_list[1]=[0,1,2]
print(f_list)
f_list[:3]=[0]       #不要求修改元素个数与被修改的相同value删除后0-2位置上只有一个0
print(f_list)
#修改元素  切片法
g_list=[2,2,2,2,2,2]
g_list[1:1]=[0,0,0,0,0]           #同样对插入的元素个数不作限制，插入索引1，元素逐个插入，并非作为一个整体,元组列表区间均可插入！！！
print(g_list)
#修改元素    可通过修改实现删除
g_list=[2,2,2,2,2,2]
g_list[0:4]=[]
print(g_list)
#修改元素   使用切片修改时，使用字符串赋值会被拆分,若不想拆分转换成列表(因为切片法会拆元素)
h_list=[2,2,2,2,2,2]
h_list[1:1]='Gabby'
print(h_list)
h_list=[2,2,2,2,2,2]
h_list[1:1]=['Gabby',]
print(h_list)
#修改元素  使用切片若指定了步长，则修改与被修改个数应该相同!!!!
i_list=[1,2,3,4,5,6]
i_list[0:4:2]=[9,9]
print(i_list)
#列表的其它常用用法
#count()统计某一元素出现的个数
#index()判断某个元素出现的位置  index(x,2)从2开始寻找x  index(x,2，4)从2到4(不包括)寻找x
#pop()实现元素出栈（最后一个元素 ）
#reverse()列表元素的逆置
#sort()排序
#从根本上改变列表
j_list=[0,1,2,3,5]
print(j_list.index(2,2,4))
print(j_list.index(2,2))
stack=[0,1,2,3]
stack.pop()
print(stack)
#需要特别说明的是 sort()可带两个参数sort(key=,reverse=True)  key为每个元素比较大小的依据，len则为每个元素的长度，reverse 为Ture则从大到小排列，默认从小到大
#字典 本质：key-value键对，key必须为不可变类型，故列表不能成为key
scores={'语文':100,'数学':99,'英语':98}
print(scores)
#元组也可以成为key,数字也可以成为key，合法
dic2={(20,30):'good',30:'bad'}
print(dic2)
#使用dict函数来创建字典，可以传入多个列表或元组参数作为键值对，每个列表或元组将被当成一个键值对，因此列表元组都必须只有2个元素！！！！  dcit传入空参数则建立一个空字典
vegetables=[('carrot',1.33),('lettuce',2.00)]
dict_1=dict(vegetables)
print(dict_1)
#使用关键字参数来建立字典
dict_2=dict(fx='acc',gyf='acct')
print(dict_2)
#字典的基本用法  通过key访问value，key访问key-value对，key删除key-value对，修改value对，判断value对是否存在
#通过key访问value
print(scores['语文'])
#若要添加value对，直接添加
scores['phsics']=90
print(scores)
#删除键值对，使用del语句
del scores['语文']
print(scores)
#修改键值对，直接对key进行新的赋值，则可完成修改
#判断字典是否包含指定的key，in或者not in都是基于key来判断的
#dict的一些函数
#clear()清空所有的键值对
scores.clear()
print(scores)
#get（）函数：根据key获取value,若key不存在，返回None
cars={'BMW':10,'AUDI':20}
print(cars.get('AUDI'))
#update(),括用一个字典包含的键值对来更新已经有的字典。若被更新的已包含对应的键值对，原有键值对会被更新
cars_1={'benci':30}
cars.update(cars_1)
print(cars)
#items((返回长度为2的元组))、keys（）、values（）用于获取所有的键值对，键、值，返回值均为列表
print(list(cars.items()))
print(cars.items())
print(cars.keys())
#pop()用于获取指定key所对的value,并且删除这个键值对
cars={'BMW':10,'AUDI':20,'gaiwa':1000}
print(cars.pop('BMW'))
print(cars)
#popitem随即弹出字典中的一个键值对（假随机，字典没有顺序），返回的是一个元组
print(cars.popitem())
cars={'BMW':10,'AUDI':20,'gaiwa':1000}
x,y=cars.popitem()
print('x=%s,y=%s'%(x,y))
#setdefault用法：根据key来获取对应的value，当key不存在时，设置一个默认值,并且将这个键值对添加进这个字典
Cars={'BMW':100,'benci':100,'audi':200}
print(Cars.setdefault('cc','fx'))
print(Cars)
#fromkeys():用给定的多个key创建字典，value的默认值均是None，也可以额外传入一个参数作为默认值 key：可为元组或者列表
a_dict=dict.fromkeys((1,2,2,23,4,5,),'gabby')
print(a_dict)
#通过字典格式化字符串：
temp='书名：%(name)s,价格是：%(price)4.2f,出版社：%(publish)s'
book={'name':'fxacc','price':200,'publish':'cc'}
print(temp % book)





"""
列表总结：
列表和元组的区别：元组不可修改
list函数可以将元组/range（）/字符串等列表化，其中字符串元素被拆分
max，min，len函数列表也可以使用
列表只能同列表相加
列表元素的添加：
append（）将列表元祖字符串等格式整体插入列表作为单个元素
extend()将列表元组字符串等格式拆分为单个加入
insert(x，)把元素按固定位置插入，插入时作为整体插入
列表元素的删除：
clear()函数清空列表元素
del（list[:]） 按索引切除   （也可以用del来删除变量）
列表元素的修改：
1.直接赋值修改：
例：
listc[0]=1  listc[0]=[1,2,3](作为整体)
2.利用切片修改：   需要注意的是使用切片修改时拆分后加入（字符串也一样，若不想被拆分把字符串改为列表）
listc[0:4]=[]
listc[0:2]=[1,2,3,4]
i_list[0:4:2]=[9,9]     注意：设定步长以后，左右元素个数必须相同
3.pop（）函数
弹出列表的最后一个元素



字典总结:
本质：键值对  key要求不可变，可以是元组。字符串
字典的创建：
1.使用dict函数例如：    a可以是列表也可以是元组，但里边的每一项都必须有两个元素
a=(['a',10],('b',20))
b=dict(a)
print(b)
2.直接创建
socres={（20,30）：10，‘a’=10}
基本用法：通过key访问value，key访问key-value对，key删除key-value对，修改value对，判断value对是否存在
字典用法：
1.直接添加  scores['a']=30
2.删除键值对 del scores['a']  clear()函数清空字典
3.根据key访问value
print(cars.get('AUDI'))
4.update()函数用来更新键值对
cars_1={'benci':30}
cars.update(cars_1)
！！！如果没有这个键值对，那么久自动添加
5.#items((返回长度为2的元组))、keys（）、values（）用于获取所有的键值对，键、值，返回值均为列表
print(list(cars.items()))
print(cars.items())
print(cars.keys())
6.pop（）用于获取指定的键值对应的value，并删除这个键值对
print(cars.pop('BMW'))
7.popitem随即弹出字典中的一个键值对（假随机，字典没有顺序），返回的是一个元组
x,y=cars.popitem()
8.fromkeys():用给定的多个key创建字典，value的默认值均是None，也可以额外传入一个参数作为默认值 key：可为元组或者列表
a_dict=dict.fromkeys((1,2,2,23,4,5,),'gabby')
9.通过字典格式化字符串
"""
























