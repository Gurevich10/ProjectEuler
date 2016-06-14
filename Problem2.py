def fibonacci(n): #Devuelve el término n-énesimo de la sucesión
    if n<1: return("Error: n<1")
    n,n1,n2=n-1,1,2
    for i in range(n):
        if i%2==0: n1=n1+n2
        else: n2=n1+n2
    if n%2==0: return n1
    else: return n2

sum,j=0,1
while fibonacci(j)<4000000:
    if fibonacci(j)%2==0: sum=sum+fibonacci(j)
    j=j+1
print (sum)




