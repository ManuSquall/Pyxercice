from squallFunction import *

def exo1():
    for i in range(10):
        print((i+1),' - ',2020)

def exo2():
    for i in range(2021, 2038,1):
        print(i)

def exo3():
    for i in range(42,62):
        print(i," ", end="")
        if(i==61):
            print(end="\n")
    for i in range(65,85):
        print(i," ", end="")
        if(i==84):
            print(end="\n")

def exo4():
    x=int(input("Donner une valeur pour x : "))
    for i in range(x, x+21,10):
        if(i==x+20):
            print(i,end="\n")
        else:
            print(i,", ", end="")


def exo5():
    # L = [31, 12, 81, 9, 65]
    L = [42]
    print(L[0]," ", L[(len(L)-1)])

def exo6():
    A=saisieListe()
    print("La liste saisie est: ")
    affichageListe(A)
    n=saisieInt("\n\nQuel élément de la liste voulez vous afficher")
    if(n in range(1,(len(A)+1))):
        # print("Present")
        print("l'élément ",n," de la liste est : ", A[(n-1)])
    else:
        print("rang invalide")

def exo7():
    n=0
    while(n<3):
        n=saisieInt("nombre d'éléments de la liste (n>=3) : ")
    L=saisieNListe(n)
    A=L
    A[0]*=10
    A[1]*=10
    A[(len(A)-1)]*=10

    print("Après modification : ")
    affichageListe(A)
    
def exo8():
    A=saisieListe()
    x=saisieInt("Saisissez la valeur de x : ")

    if((x in A) or ((x+1) in A) or ((x-1) in A)):
        ok = True
    else:
        ok = False

    affichageListe(A)
    print("ok = ", ok)

def exo9():
    a=saisieInt("Valeur pour a : ")
    b=saisieInt("Valeur pour b : ")
    c=saisieInt("Valeur pour c : ")

    L=[]

    d= (b**2) - (4*a*c)

    if(d>0):
        print("L’équation admet deux solutions réelles")
        x= (-b-(d**0.5))/(2*a)
        y= (-b+(d**0.5))/(2*a)
        L.append(x)
        L.append(y)
        print( x , " et ", y)
    elif(d==0):
        print("L’équation admet une seule solution réelle")
        x = (-b/(2*a))
        print(x)
    else:
        print("L’équation n’admet aucune solution")
        print("Aucune")

    print("Si a = ",a,", b = ",b," et c = ",c," alors S ",end="")
    if(len(L)==0):
        print("est la liste vide")
    else:
        affichageListe(L)

def exo10():
    L=list(range(1,13))
    m=13
    while (m>12 or m<1):
        m=saisieInt("\nvaleur de m : ")
    if(((L.index(m)-1)%2)==1):
        est_mois_31 = True
    else:
        est_mois_31 = False
    print(est_mois_31)

def exo11():
    L=saisieListe()
    a=L[0]
    L[0] = L[(len(L)-1)]
    L[(len(L)-1)] = a

    affichageListe(L)

def exo12():
    L=saisieListe()
    for i in range(0, len(L)-1,2):
        a = L[i]
        L[i]=L[i+1]
        L[i+1] = a
    affichageListe(L)

def exo13():
    L=saisieListe()
    for i in range(0, (len(L)-1)//2,1):
        a= L[i]
        L[i]= L[(len(L)-i-1)]
        L[(len(L)-i-1)] = a
    affichageListe(L)

def exo14():
    ok = False

    x=saisieInt("Donnez une valeur entière pour x :")
    y=saisieInt("Donnez une valeur entière pour y :")

    if(x>0 and x<5 and y>0 and y<5):
        if ((x-y==-3) or (x-y==3)):
            ok = True
        elif((x-y==-1) or (x-y==1)):
            ok = True

    print(ok)

def exo15():
    L=saisieListe()
    affichageListe(L)
    for i in range(len(L)):
        print(i, " -> ", L[i])

def exo16():
    while(True):
        a= saisieInt("Saisir a (a>=b) :")
        b= saisieInt("Saisir b (a>=b) :")
        if(a>=b):
            break
    for i in range(a, b-1, -1):
        print(i)

def exo17():
    L=saisieListe()
    for i in range(len(L)):
        L[i] *= 10
    affichageListe(L)

def exo18():
    a=0
    while(True):
        n= saisieInt("Saisir n (n>=0) :")
        if(n>=0):
            break
    for i in range(n+1):
        a+=i
    print(a)
    # print((n*(n+1))/2)

def exo20():
    while(True):
        a= saisieInt("Saisir a (a<=b) :")
        b= saisieInt("Saisir b (a<=b) :")
        if(a<=b):
            break
    for i in range(a,b,1):
        print(i," ",i+0.5," ", end="")
    print(b)

def exo50():
    b=""
    a=input("Donnez la chaine initiale :\n")
    for i in range(len(a)):
        b+=a[i]+a[i]
    print(b)

def exo53():
    a=""
    p = ["je", "tu", "il/elle", "nous", "vous", "ils/elles"]
    t = ["e", "es", "e", "ons", "ez", "ent"]
    v=input("Donnez le verbe du premier groupe à conjuguer : \n")
    for i in range((len(v)-2)):
        a+=v[i]
    # print(a)
    for i in range(6):
        print(p[i]," ",a+t[i])

