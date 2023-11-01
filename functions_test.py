def somme(T):
    S = 0
    for i in range(10):
        S += T[i]
    return S

def produit(T):
    p = 1
    for i in range(10):
        p *= T[i]
    return p

def moyenne(T):
    m = somme(T) / 10
    return m

def sign(T):
    P = []
    N = []

    print("Les éléments positifs sont :")
    for i in range(10):
        if T[i] > 0:
            P.append(T[i])
    v=" "
    for i in range(len(P)):
     v+=str(P[i])
    
    print(v)
    
    
   

    print("Les éléments négatifs sont :")
    for i in range(10):
        if T[i] < 0:
            N.append(T[i])
    s=" "
    for i in range(len(P)):
     s+=str(N[i])
    
    print(s)

T = []
for i in range(10):
    value = float(input("Entrer un réel : "))
    T.append(value)

print("La somme est", somme(T))
print("Le produit est", produit(T))
print("La moyenne est", moyenne(T))
print("Le signe est")
sign(T)
