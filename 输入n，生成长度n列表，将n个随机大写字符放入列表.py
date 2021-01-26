import random
str1 = input("请输入一个整数：")
n = int(str1)
ret_list = []
letter_list = [chr(i) for i in range(ord('A'),ord('Z')+1)]#chr(i) for i in range(ord('A'),ord('Z')+1)要用在列表中     ord() 函数是 chr() 函数（对于8位的ASCII字符串））的配对函数，
ret_list = random.sample(letter_list,n)#随机把前者的n个元素放入retlist
print(ret_list)
