def nat(n):
    if n==1:
        return 1
    return n + nat(n-1)


print(nat(5))