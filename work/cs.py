def cs(l:list):
    c=0
    while True:
        l.sort(reverse=True)
        print(l)
        if l.count(l[0])==len(l):
            break
        l=list(map(lambda x:x+1,l))
        l[0]=l[0]-1
        c=c+1
    return c

# g=cs([1,2,3,5])
# print(g)

# a=((1,2),6)
# b=(5,6)
# a[0]=a[0]+b