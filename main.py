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
