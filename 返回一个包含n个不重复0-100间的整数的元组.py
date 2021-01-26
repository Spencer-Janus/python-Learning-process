import random
list2=[]
def fn(n):
    for i in range(0,n):
        x=random.randint(1,101)
        while x in list2:
            x=random.randint(1,101)
        list2.append(x)
    a=tuple(list2)
    return  a
print(fn(10))


