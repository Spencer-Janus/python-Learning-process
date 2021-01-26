letters=input('请输入若干大写字母')
list_1=list(letters)
dict_1=dict.fromkeys([chr(i) for i in range(ord('A'),ord('z')+1)],0)       #chr(i)括号里为ASCII码,返回对应字符，                ord（'i'）括号里为字符，反回相应的ASCII
for i in list_1:
    dict_1[i]+=1
print(dict_1)
