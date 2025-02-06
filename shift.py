l=[1,2,3,4,5]
def shift(l,n):
    if not l:
        return l
    n=n%len(l)
    return l[n:] + l[:n]


print(shift(l,1))