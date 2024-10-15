'''plus petit que exercice 7
def lpp(a,b):
    if a<b:
        return(a)
    else: 
        return(b)
print(lpp(1,2))'''




''' exercice 9 savoir si oui ou non il est entier
def  est_entier (x):
    if x==(int):
        return True
    else:
        return False
print (est_entier(2.5))'''



def est_pair(n):
    if n%2==0:
        return True
    else:
        return False
print(est_pair(2))




def carre(n):
    carre = []
    for k in range(1  ,n+1):
        carre.append(k**2)
    return carre
print(carre(5))



def carre_compr(n):
    l = [k*2 for k in range(1,n+1)]
    return l 
print(carre_compr(100))



liste_1=[x for x in range (1,20,2)]
print(liste_1) 
liste_2=[x**2 for x in range(11)]
print(liste_2)
liste_3=[2**x for x in range(11)]
print(liste_3)    
liste_4=[x for x in range(3,52) if x%3==0] 
print(liste_4)
