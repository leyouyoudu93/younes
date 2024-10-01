
def rep(c, n):
    if n>0:
       return c*n
   
print(rep('c',2))

"""def rep(c, d, n, m):
    if n>0 and m>0:
        return c*n + d*m
print(rep('c','m', 8,9))"""




my_str = "younes"
reversed_str = "".join(reversed(my_str))
print(reversed_str)



def afficher_numerote(ch,n):
    if n>0:
        for i in range(1,n+1):
            print(f"{i}. {ch}")
afficher_numerote("ch", 5)



def afficher_caractere_repetes(c,n):
    if n>0:
        for i in range(1, n+1):
            print(c*1)

afficher_caractere_repetes("*",5)
