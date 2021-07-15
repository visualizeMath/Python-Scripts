
def tamBolenleriBul(n):
    bolenler=[]
    for i in range(2,n):
        if n%i==0:
            bolenler.append(i)
    return bolenler



def asalBolenleriBul(x):
    
    tamBolenler=tamBolenleriBul(x)
    j=0

    for i in range(0,len(tamBolenler)):
        while j<len(tamBolenler): 
            j=j+1
            if j<len(tamBolenler):    
                a=int(tamBolenler[j])
                b=int(tamBolenler[i])

                if a%b==0:
                    tamBolenler.remove(a)
                    j=0
                
    return tamBolenler

print("Asal bölenleri hesaplanacak sayiyi giriniz..\n")
x=int(input())
print("\n\t")
print(asalBolenleriBul(x))