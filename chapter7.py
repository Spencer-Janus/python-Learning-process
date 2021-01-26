#chapter7

'''
Python的异常机制主要依赖try,except，else，finally，raise五个关键字
try块里放置可能引发异常的代码，在except后对应的是异常类型和一个代码块，用于表明该except块处理这种类型的代码块
在多个except后可以放一个else块，表明程序不出现异常时还要执行else块，最后还可以跟一个finally块，finally块用于回收
在try里打开的物理资源，异常处理机制保证finally块总被执行，而raise用于引发一个实际的异常，raise可以单独作为语句使用，
引发一个具体的异常对象
'''
#7.1异常概述 异常处理机制使得程序有更好的容错性，更加健壮
#7.2异常处理机制： 程序运行意外时，系统会自动生成一个Error对象来通知程序
'''
异常处理机制语法结构
try:
    实现代码
except (Error1,Error2,....)as e:
    处理
当python收到异常对象时，会寻找能处理该异常对象的except块，如果找到合适得except块，则把该异常对象交给except块
处理，这个过程被称为捕获异常，如果python解释器找不到捕获异常的eexcept，则运行时坏境终止，python解释器退出
'''
def div(a,b):
    return a/b
try:
    x=div(5,2)
except Exception as  e:
    print("程序出错了！！！！！")
else:
    print("结果是：",x)
try:
    file=open('ddd.txt')
    print(file.read())
    file.close()
except Exception as e:  #给异常起了一个变量名e
    print(e)
'''
Exception  是所有错误类型的父类
如KeyError FileNotFoundError
Exception 这个位置 写错误类型，可以是一个也可以是多个
'''
'''
age=input("请输入你的年龄")
if age.isdigit():#Python isdigit() 方法检测字符串是否只由数字组成。返回bool  具有局限性
    age=int(age)
    if age>18:
        print("欢迎来到我的网站")
    else:
        print("年龄不足，请离开")
else:
    print("输入的不是数字")
具有很大的局限性
'''
age=input('输入年龄')
try:
    age=float(age)
except ValueError as e:
    print('输入的不是数字')
else:
    if age>18:
        print("欢迎来到我的网站")
    else:
        print("年龄不足，自行离开")
#7.2.2 异常类的继承体系 python所有的异常类的基类是BaseException，单用户要实现字定义异常则应该继承 Exception类
#BaseException的主要子类就是Exception
import sys
try:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=a/b
    print('输入的两个数相除的结果')
except IndexError:
    print("索引错误")
except ValueError:
    print('数值错误')
except ArithmeticError:
    print("算术错误")
except Exception:   #原则：先处理小异常，再处理大异常
    print("未知异常")
#7.2.3  多异常捕捉
import sys
try:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=a/b
    print('输入的两个数相除的结果')
except (IndexError,ValueError,ArithmeticError):
    print("程序发生了数组越界，数字格式，算数异常之一")
except Exception:#可以省略Exception不指定要捕获的异常类型，这种语句也合法，它表示可捕获所有类型的异常，一般为最后一个except块
    print("另外未知异常")
#多异常捕捉使用元组，在元组里写多个异常名即可

#访问异常信息
'''
所有的异常都包含以下几个属性和方法
args: 异常的错误编号和描述字符串
errno： 错误编号
strerror： 异常的描述字符串
with_traceback() 通过该方法可处理异常的传播轨迹信息
'''
def foo():
    try:
        file=open("a.txt")
    except Exception as e:
        print(e.args)
        print(e.errno)
        print(e.strerror)
foo()

#7.2.5 else 块
s=input("请输入除数")
try:
    result=20/int(s)
    print('20除以%s的结果是：'%(s),result)
except ValueError:
    print("值错误必须输入数值")
except ArithmeticError:
    print("算术错误，您不能输入0")
else:
    print("没有异常")
'''
只有当try没有异常才会执行else，那么直接把else放在try块的代码之后不就行了？
实际上大部分语言的异常处理没有try块，直接放在try块之后即可
但Python的else块并不是多余语法，当try没有异常，而else有异常的时候，就能体现出else的作用了
'''
def else_test():
    s=input('请输入除数')
    result=20/int(s)
    print('20除以%s的结果是：' % (s), result)
def right_main():
    try:
        print("try块的代码，没有异常")
    except:
        print('出现异常')
    else:
        else_test()
def wrong_main():
    try:
        print('try块的代码，没有异常')
        else_test()
    except:
        print('程序出现异常')
wrong_main()
right_main()
# 分别输入 0 ringht main报错
#else块的代码所引发的异常不会被except块捕获，所以，如果希望某段代码的异常能被捕捉则放在try块后，如果希望异常向外传播，则放在else块
#
#7.2.6使用gunally回收资源
'''
# 在try里打开了一些物理资源（数据库连接，网络连接，磁盘文件）这些物理资源必须显式回收
#python的垃圾回收机制不会回收任何物理资源，只能回收堆内存中对象所占用的内存
为了保证一定能回收在try块中打开的物理资源，异常处理机制提供了finally块，不管try块中的代码是否出现异常，
也不管哪一个except块被执行，甚至在try和except块里出现了return finally总会被执行，python完整的异常处理结构如下:
try:    
    *********
except Exception:

except Exception:
 
else:
    
finally:
    资源回收
'''
import os
def treat():
    fis=None
    try:
        fis=open("asd.txt")
    except OSError as e:
        print(e.strerror)
        return   #虽然有return  但是finally仍然执行
        os._exit(1)   #如果return被注释掉使用此条语句来退出python解释器，finally将失去执行的机会
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("资源回收")
treat()
'''
除非在try、except中调用了退出python解释器的方法（os._exit()），否则不管在try块，except块中执行怎样的代码，
出现怎样的情况finally总会被执行，调用sys.exit()不能阻止finally的执行，这个方法本身就是通过引发
SystemExit异常来退出程序的
在通常情况下，不要在finally块中，使用如return 或raise等导致方法终止的语句，一旦在finally中使用，
将会导致try，except块中的 return raise语句失效
'''
def test():
    try:
        return True
    finally:
        return False#将会导致 上面的return True失去作用
a=test()
print(a)
'''
如果 Python程序在执行try块、except块时遇到了return或raise语句，这两条语句都会导致该方法立即结束，那么系统执行
这两条语句并不会结束该方法，而是去寻找该异常处理流程中的finally块，如果没有找到 finally块，
程序立即执行return或raise语句,方法中止:如果找到finally块,系统立即开始执行finally块——只有当finally块执行完成后,
系统才会再次跳回来执行try块、except块里的return或raise语句;如果在 finally块里也使用了return或raise等导致方法中止的语句，
finally块已经中止了方法，系统将不会跳回去执行try块、except块里的任何代码。
'''
#7.2.7 异常处理的嵌套
#完整的异常处理流程既可以放在try块里，except块里，finally块里，通常没有必要使用超过两层的嵌套的异常处理，
#使用深层次的嵌套反而没有太大的必要，而且容易导致程序的可读性降低

#7.3使用 raise 引发异常 当程序出现错误时，系统会自动引发异常，除此之外，python也允许程序自行引发异常，自行引发异常使用raise完成

#执行与既定的业务需求不符，这就是一种异常，由于与业务需求不符而产生的异常，必须由程序员来决定引发
'''
raise 语句有如下三种常用的用法
raise: 单独一个raise，该语句引发当前上下文中捕获的异常（比如在except块中），或默认引发RuntimeError异常
raise 异常类：raise后带一个异常类，该语句引发指定异常类的默认实例
raise 异常对象：引发指定的异常对象
raise 【     exceptionName [(reason)]             】
reason为描述信息
其中，用 [] 括起来的为可选参数，其作用是指定抛出的异常名称，以及异常信息的相关描述。如果可选参数全部省略，则 raise 会把当前错误原样抛出；如果仅省略 (reason)，则在抛出异常时，将不附带任何的异常描述信息。
'''

#事实上，raise 语句引发的异常通常用 try except（else finally）异常处理结构来捕获并进行处理。例如：
try:
	a = input("输入一个数：")
	#判断用户输入的是否为数字
	if(not a.isdigit()):
	    raise ValueError("a 必须是数字")  #抛出异常 try得到
except ValueError as e:
	print("引发异常：",repr(e))   #repr() 函数将对象转化为供解释器读取的形式。


#raise 不需要参数
try:
	a = input("输入一个数：")
	if(not a.isdigit()):
		raise             #当在没有引发过异常的程序使用无参的 raise 语句时，它默认引发的是 RuntimeError 异常。
except RuntimeError as e:
	print("引发异常：",repr(e))

#自定义异常类(异常的类名通常包含了该异常的有用信息)
#用户字定义异常都应该继承Exception基类或Exception的子类，在自定义异常类时基本不需要书写更多的代码，只需要指出父类即可
class AuctionException(Exception):
    pass

#7.3.3except和raise同时使用 （一个异常出现，单个方法无法完全处理，为了实现通过多个方法协作处理同一个异常的情形）
class AuctionText:
    def __init__(self,init_price):
        self.init_price=init_price
    def bid(self,bid_price):
        d=0.0
        try:
            d=float(bid_price)
        except Exception as e:
            print('出现异常')
            raise AuctionException("竞拍价必须只含有数字")   #若raise不带参数，默认引发RuntimeError异常
        if self.init_price>d:
            raise  AuctionException("竞拍价比起拍价低，不允许竞拍")
        initPrice=d
def main():
    at=AuctionText(20.4)
    try:
        at.bid("df")
    except AuctionException as e:
        print("异常是：",e)
main()
#7.4 python的异常传播轨迹（了解即可。未写笔记）

#7.5 异常处理规则
'''
1.不要过度使用异常，错误处理代码有时候比异常处理机制更有效
2.不要使用过于庞大的try块，正确的做法，把大块的try块分割成多个可能出现异常的程序段落，并把它们放在单独的try块
3.不要忽略捕获到的异常
'''
