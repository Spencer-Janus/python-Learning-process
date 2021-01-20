def f(n):
    sum_=0
    for i in range(1,n+1):
        n=i**3
        sum_+=n
    print(sum_)
f(3)