a=input('请输入一串字符串（空格为间隔）：')
list_0=a.split()
list_1=[]
for i in range(0,len(list_0)):
    b=list_0[i]
    if b not in list_1:
        list_1.append(b)
print(list_1)



## cnds
'''
#codeing: utf-8
str1 = input("请输入多个字符串，并用空格隔开：")
lstr = str1.split(" ")
str_list = []
for l in lstr:
    if l not in str_list:
        str_list.append(l)
print(str_list)
'''
