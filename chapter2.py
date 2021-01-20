'''
注释
'''
#注释 转义字符
s='hello\nworld\n'
print(s)
#格式化字符串
user='Yu Zhihang'
age=20
print('%s is a %s years old boy'%(user,age))
age=18
print('His age is %6d'%(age))#6是宽度
print('Her age is %06d'%(age))#0表示补0
x=-3.1415926
print('x的值为%8.3f'%(x))           #宽度为8，保留三位
print('x的值为%+08.3f'%(x))          #宽度为8，保留三位，左边补0，始终带符号
#索引
s_1='You are very handsome'
print(s_1[1:2])#第二个索引不被输出.缺少则表示开始或者是末尾
print(s_1[1:10])
print(s_1[:-1])
print(s_1[:])
print('very'in s_1)  #判断s是否包含字符串    bool
print(len(s_1))#获取字符串长度
print(max(s_1),min(s_1))  #输出最大最小字符（空格）
#在str类中常用的函数
#title()每个单词首字母大写
#lower()每个单词改为小写
#upper()每个单词改为大写
#strip()删除字符串前后的空白
#lstrip()删除前面的空白
#rstrip()删除后面的空白
#startwith()是否以指定字符串开头    bool
#endwith
#find()查找指定子串的位置，找不到则返回-1  find('  '.9)表示从9开始查找
#index同上
#replace()用指定子串替换目标子串
#split()按指定分割成短语   括号里是什么就按什么分割 split(None，2)2表示只分割前两个单词
#join()将短语连接成字符串

#!!!!!1以上函数在本质上并没有改变字符串，字符串不能被改变
s_2='           You are very handsome'
print(s_1.title())
print(s_2.strip())
print(s_1.find('handsome'))
print(s_1.find('handsome',4))
print(s_1.startswith('you'))
print(s_1.replace('You','We',1)) #1表示个数
print(s_1.split())  #返回的是列表
s_3=s_1.split()
print(','.join(s_3)) #以逗号为分隔符，将s3连接  返回的是字符串
print(type((','.join(s_3))))
a=b=x=d=0 #连续赋值

#算数运算符*可以作为字符串的连接运算符
#/除法 //整除，小数部分舍弃
# %为求余运算符
# 乘方运算 5**2 5的二次方
#位运算符  &：按位与  |：按位或  ^:异或  ~：取反 <<：左位移     >>：右位移
#扩展赋值运算符 += -= *= 。。。。。。
print(s_1*2)
print('5%-2.9的结果是',5%-2.9)
#索引运算符
print(s_1[::2]) #最后一位数字为步长
#比较运算符 >,<,==,      is:判断两个变量所引用的对象是否相同(地址相同则相同)，相同返回ture  is not相反
#python的两个bool值可以当作0，1使用，可以参加算术运算
print(1+True)
#逻辑运算符，逻辑运算返回的也是bool值，  and、 or、  not
#三目运算符 if
a=5
b=3
st='a大于b'if a>b else 'a不大于b'
print(st)
#三目运算符嵌套
c=5
d=5
print('c>d')if c>d else(print('c<d') if c<d else print('c=d'))
print('it'in s_1)
s_4='fkjava.org'
s_5=s_4.replace('.','-',1)
print(s_5)
print(s_1.split())








S_9='chen rui is a god of man'
print('I want say is %s'%S_9)
print(S_9.split(' '))
print(S_9.startswith('?'))
print(S_9.upper())
print(S_9[::2])
s=-3.1415926666664498465198465151687464
print("圆周率Π的值为：",s)
print("圆周率Π的值为：%.4f"%(s))
print(S_9.replace('chen rui','zhuangzhuang'))
print(S_9.find('x'))

















