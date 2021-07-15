def fact(n):
    if n>1:
        return n*fact(n-1)
    elif n==1:
        return 1

print("Hesaplanmasini istediginiz tamsayiyi giriniz..\n")
a=int(input())
print(fact(a))