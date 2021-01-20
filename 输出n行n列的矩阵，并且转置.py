SIZE=7
array=[[0]*SIZE]
#创建长度为size*size的二维列表
for i in range(SIZE-1):
    array+=[[0]*SIZE]
print(array)
def fn(n):
    sum1=1
    SIZE=n
    array=[[0]*SIZE]
    for i in range(SIZE-1):
        array+=[[0]*SIZE]
    array2=[[0]*SIZE]
    for i in range(SIZE-1):
        array2+=[[0]*SIZE]
    for i in range(SIZE):
        for j in range(SIZE):
            array[i][j]=sum1
            sum1+=1
    for i in range(SIZE):
        for j in range(SIZE):
            array2[i][j]=array[j][i]
    for i in range(SIZE):
        print(array[i])
    for i in range(SIZE):
        print(array2[i])
    for i in range(SIZE):
        for j in range(SIZE):
            print('%2d ' % array[i][j], end='')
        print(end='\n')
    for i in range(SIZE):
        for j in range(SIZE):
            print('%2d ' % array2[i][j], end='')
        print(end='\n')


fn(3)
