def judgesum():
    str1=input('请输入一串字符串:')
    list_1=list(str1)
    print(list_1)
    numstr='0123456789'
    sum1={'number':0,'Englishchar':0,'space':0,'else':0}
    for i in list_1 :
        if i in numstr:
            sum1['number']+=1
        elif ('a'<=i<='z')or('A'<=i<='Z'):
            print(i)
            sum1['Englishchar']+=1
        elif i==' ':
            sum1['space']+=1
        else:
            sum1['else']+=1
    print(sum1)
judgesum()





