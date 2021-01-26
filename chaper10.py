import  re
#10.6 正则表达式
'''
正则表达式(Regular Expression）用于描述一种字符串匹配的模式（Pattern)，它可用于检查一个字符串是否含有某个子串，也可用于从字符串中提取匹配的子串，或者对字符串中匹配的子串执行替换操作。
另外：python的re模块是匹配字符串的模块，很多功能依据正则表达式实现
'''
print(re.__all__)#查看re模块的全部属性和函数
'''
re.compile(pattern,falgs=0):该函数用于将正则表达式字符串编译成_sre.Sre_Pattern对象，该对象代表了正则表达式编译之后
在内存中的对象，它可以缓存并复用正则表达式字符串。如果程序需要多次使用同一个正则表达式字符串，则可以考虑先编译它

pattern参数为它所编译的正则表达式字符串，flags代表了正则表达式的匹配旗标
编译得到的_sre.SRE_Pattern对象包含了re模块中绝大部分函数对应的方法
'''
p=re.compile('abc') #编译_sre.Sre_Pattern对象，p对象程序可复用
p.search("www.abc.com")
#直接用正则表达式匹配目标字符串（同上两行代码效果基本相同）
re.search('abc','www.abc.com')
'''
re.match(pattern,string,flags=0):尝试从字符串开始的位置来匹配正则表达式，如果从开始的位置匹配不成功，match()返回none。

pattern参数代表正则表达式；sting代表被匹配的字符串；flags则代表正则表达式的匹配旗标
该函数返回_sre.SRE_Match对象！！！，该对象包含的span(n)方法用于获取第n+1个组的匹配位置，group(n)方法用于获取第n+1个组所匹配的子串

re.search(pattern,string,flags=0):扫描整个字符串，并返回字符串中第一处匹配pattern的匹配对象。

pattern参数代表正则表达式，string代表被匹配的字符串；flags代表正则表达式的匹配旗标。
该函数也返回_sre.SRE_Match对象！！！

match()和search()的区别在于：match()必须从字符串开始处就匹配，但search()可以搜索整个字符串
'''
import re
ml=re.search('abc','www.abc.com')
print(ml.span())  #span返回匹配的位置
print(ml.group()) #group返回匹配的组
print(re.match('fkit','www.fkit.com'))  #从开始的位置匹配不到
print(re.match('www','www.fkit.com'))
m2=re.search('www','www.fkit.org')
print(m2.span())
print(m2.group())
m3=re.search('fkit','www.fkit.com')
print(m3.span())
print(m3.group())
'''
re.findall(pattern,string,flags=0):扫描整个字符串，并返回字符串中所有匹配patterm的子串组成的列表。

其中 pattern参数代表正则表达式;string 代表被匹配的字符串;flags则代表正则表达式的匹配旗标。

re.finditer(pattern, string,flags=0):扫描整个字符串，并返回字符串中所有匹配pattern的子串组成的迭代器,
迭代器的元素是_sre.SRE_Match对象!!!!。
其中 pattern参数代表正则表达式;string 代表被匹配的字符串;flags则代表正则表达式的匹配旗标。

从上面介绍不难看出，findall()与finditer()函数的功能基本相似,区别在于它们的返回值不同，findall()函数返回所有匹配 patten的子串组成的列表;而finditer()函数则返回所有匹配 pattern 的子串组成的迭代器。

如果对比 findall()、finditer()和 search()函数，它们的区别也很明显，search()只返回字符串中第一处匹配pattern 的子串;而findall()和 finditer()则返回字符串中所有匹配patten的子串。

'''
print(re.findall('fkit','FkIt is very good,fkit.org is my favorite',re.I))#返回子串组成的列表，忽略大小写
it=re.finditer('fkit','fkit is very goof,Fkit .org is my favorite',re.I)#返回子串组成的迭代器
for e in it:
    print(str(e.span())+"-->"+e.group())
'''
re.fullmatch(pattern, string，flags=0):该函数要求整个字符串能匹配pattern，如果匹配则返回包含匹配信息的_sre.SRE_Match对象！！！;否则返回None。

re.sub(pattern, repl, string, count=0, flags=0):该函数用于将string字符串中所有匹配pattern的内容替换成repl;
repl 既可是被替换的字符串，也可是一个函数。count参数控制最多替换多少次，如果指定count为0，则表示全部替换。
'''
my_date='2008-08-18'
print(re.sub(r'-','/',my_date))
print(re.sub(r'-','/',my_date,1)) #只替换一次
#上面程序所使用的r-是原始字符串，其中r代表原始字符串，通过使用原始字符串，可以避免对字符串中的特殊字符进行转义。

def fun(matched):  #matched为匹配到的对象，函数的功能是在匹配到的对象前后加文字
    value="《carzy"+(matched.group('lang'))+"讲义》"
    return value
s='Python很好，java也很好'
#对s里面的英文单词（用re.A旗标控制）进行替换
#使用fun函数指定替换的内容
print(re.sub(r'(?P<lang>\w+)',fun,s,flags=re.A))

'''
r(?P<lang>\w+)"正则表达式用圆括号表达式创建了一个组，并使用“?P”选项为该组起名为lang———所起的组名要放在尖括号内。剩下的“\w+”才是正则表达式的内容，其中“\w”代表任意字符;“+”用于限定前面的“\w”可出现一次到多次，
因此“\w+”代表一个或多个任意字符。又由于程序执行sub()函数时指定了re.A选项，这样“\w”就只能代表ASCII字符，不能代表汉字。


当使用sub()函数执行替换时，正则表达式“Iw+”所匹配的内容可以通过组名“lang”来获取，
这样fun()函数就调用了matched.group('lang')来获取“\w+”所匹配的内容。

re.split(pattern, string，maxsplit=0,flags=O):使用pattern对string进行分割，该函数返回分割得到的多个子串组成的列表。其中 maxsplit参数控制最多分割几次。
'''
print(re.split(',','fkjava,fkit,crazyit'))
print(re.split(',','fkit,fkitjava,crazy'))#只分割一次
print(re.split('a','fkit,fkjava,crazyit'))#使用a分割
print(re.split('x','fkit,fkjava,crazyit'))#使用x进行分割，没有匹配内容不执行分割
'''
re.purge(:清除正则表达式缓存。
re.escape(pattern):对模式中除ASCII字符、数值、下画线(_)之外的其他字符进行转义。如下程序示范了escape(函数的用法。
'''