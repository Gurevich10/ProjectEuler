def factores_primos(n):
    lista=[]
    while n!=1:
        j=2
        while n%j!=0: j=j+1
        n=n/j
        lista.append(j)
    return lista

primos=factores_primos(600851475143)
print(primos[len(primos)-1])