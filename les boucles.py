
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




def sous_chaine(ch1, ch2):
    if  ch1 in ch2 or ch2 in ch1:
        return True
    else:
        return False

print(sous_chaine("you","younes"))



def triple_six(ch):
    return"666" in ch
print(triple_six("ruivh666inàv$çu"))




def triple_six_exact(ch):
    n=len(ch)
    if ch[0:3]=="666" and (n<=3 or ch[3]!="6"):
        return True 
    if ch[n-3:n]=="666" and ch[n-3] !='6':
        return True
    for k in range(1, n-3):
     if ch[k:k+3]=="666" and ch[k-1] !=6 and ch[k+3] !=6:
        return True 
    return False
print(triple_six_exact('66666'))




def sansespace(ch):
    mot=""
    for i in range(len(ch)):
        if ch[i] !=" ":
            mot=mot+ch[i]
    return mot 
print(sansespace(" mac v "))
