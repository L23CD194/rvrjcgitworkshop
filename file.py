def fact(n):
    if n==0 or n==1:
        return 1
    else:
            return n*fact(n-1)
n=fact(4)
print(n)