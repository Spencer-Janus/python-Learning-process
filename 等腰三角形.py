n=10
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'*(2*i-1),end='')
    print('')


for i in range(1,n+1):
    print(' '*(n-i),end='')
    for i in range(0,2*i-1):
        print('*',end='')
    print('')

