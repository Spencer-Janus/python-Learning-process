SIZE=7
array=[[0]*SIZE]
print(array)
#创建长度为size*size的二维列表
for i in range(SIZE-1):
    array+=[[0]*SIZE]
print(array)
orient=0
#orient代表绕圈的方向 0向下 1向右 2向左 3向上
j=0#行索引
k=0#列索引
for i in range(1,SIZE*SIZE+1):
    array[j][k]=i
    if j+k==SIZE-1:           #位于一号转弯线
        if j>k:         #左下角
            orient=1
        else:          #右上角
            orient=2
    elif(k==j)and(k>=SIZE/2):#二号转弯线，行列索引相等
        orient=3
    elif(j==k-1)and(k<=SIZE/2):#三号转弯线，行索引等于列索引-1
        orient=0
    if orient==0:
        j+=1
    elif orient==1:
        k+=1
    elif orient==2:
        k-=1
    elif orient==3:
        j-=1
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d '%array[i][j],end='')
    print(end='\n')