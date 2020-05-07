from squallFunction import *

def exo1():
    x = 81
    y = 31
    print(x,y)
    x,y = y,x
    print(x,y)

def exo2():
    x = 10**6
    print("a = ",x)

    z = 666/(74*9)
    print("b = ",z)

    y = (2*3.14159) + 2.71828 + (1.4142*5)
    print("c = ", y)

def exo3():
    x = -1 * 1**2
    print(x)

def exo4():
    milliard =1000000000
    million = 1000000

    rs = (200 * milliard * million) + (2020 * million) - (925*milliard)
    print(rs)

def exo5():
    une_heure = 3600
    j = 24 * une_heure
    an = (365 * j) + (j/4)
    siecle = an*100
    print("dans un siècle il y a ", siecle, " seconde")

def exo6():
    if(2020/101 == 0):
        print("101 est un diviseur de 2020")
    else:
        print("101 n'est pas un diviseur de 2020")

    print()
    print()
    print()
    print("Le reste de la division de 192642212037519289 /2020 = ", 192642212037519289%2020)
    print("Le reste de la division de 138633362400520449 /2020 = ", 192642212037519289%2020)


def exo7():
    n = 0
    i = 1
    while n<5:
        if(i%421 == 0):
            n += 1
            # print(i)
            print(i, end=", ")
        i += 1

def exo8():

    # 1 tour -> 7 minutes
    # x tours -> 240
    print("En 240 minutes il effectuera {} tours".format(240/7))
    

def exo9():
    x = int(input("veuillez saisir x svp"))
    print("x = ",x," => 10 * x + 1 = ",(10*x)+1)

def exo10():
    cond = False
    x = int(input("Donnez la valeur de x : "))
    if(x%10==0):
        cond = True
        print("x est un multiple de 10")
        print(x," passe le test")
    elif((x%2!=0) and (x%3!=0) and x>=42 and x<=421):
        cond=True
        print(x," passe le test")
    else:
        print(x," ne passe pas le test")

def exo11():
    j = 0
    m= 0
    while (j<1 or j>31):
        print("Donnez la valeur pour j :")
        j=int(input())
    while (m<1 or m>12):
        print("Donnez la valeur pour m :")
        m=int(input())

    enVacances = False

    if (m>7 and m<9):
        enVacances =True
    elif (m==7):
        if(j>=8):
            enVacances =True
    elif (m==9):
        if(j<=3):
            enVacances =True

    # juillet 7
    # sept 9

    print(enVacances)


def exo12():
    a = saisieInt("Saisir la valeur de a :\n")
    b = saisieInt("Saisir la valeur de b :\n")
    c = saisieInt("Saisir la valeur de c :\n")
    d = saisieInt("Saisir la valeur de d :\n")
    e = saisieInt("Saisir la valeur de e :\n")

    if(a==5 and b==5 and c==5 and d==4 and e==4):
        var_bool=True
    elif(a==5 and b==5 and c==5 and d==5 and e==5):
        var_bool=False  
    print(var_bool)

def exo13():

    a= 0
    b= 0
    c= 0
    ok = False

    while (a<1):
        print("Donnez une valeur entière positive pour a :")
        a=int(input())
    while (b<1):
        print("Donnez une valeur entière positive pour b :")
        b=int(input())
    while (c<1):
        print("Donnez une valeur entière positive pour c :")
        c=int(input())

    if(((a%2==0) or (b%2==0) or (c%2==0)) and (a>=100 or b>=100 or c>=100)):
        ok= True

    print(ok)

def exo14():

    ok = False

    print("Donnez une valeur entière pour x :")
    x=int(input())
    print("Donnez une valeur entière pour y :")
    y=int(input())

    if(x>0 and x<5 and y>0 and y<5):
        if ((x-y==-3) or (x-y==3)):
            ok = True
        elif((x-y==-1) or (x-y==1)):
            ok = True

    print(ok)

def exo15():

    print("Donnez une valeur entière pour x :")
    x=int(input())

    g = 1 + x + (x**2) + (x**3)
    d = ((x**4)-1) // (x-1)  

    print("l'expression donne : ", g, " = ", d)
    if(g==d):
        print("equal")
    else:
        print("not equal")

def exo16():

    avoir_n_chiffres = False
    x, n, a, b = 0, 0, 1, 0

    print("Donnez une valeur entière pour x :")
    x=int(input())
    print()
    print("Donnez une valeur entière pour n :")
    n=int(input())
    b=x
    while (b//10!=0):
        if ((b%10!=1) or (b%10!=0)):
            b= b/10
            a+=1

    if(n==a):
        avoir_n_chiffres = True
    else:
        avoir_n_chiffres = False


    print(" avoir_n_chiffres = ", avoir_n_chiffres)
    print(x, " a ", a, " chiffres")

def exo17():

    print("Donnez une valeur entière pour a :")
    a=int(input())
    print("Donnez une valeur entière pour b :")
    b=int(input())
    print("Donnez une valeur entière pour c :")
    c=int(input())

    if((a>=b and a<=c) or (a<=b and a>=c)):
        print("a = ",a)
    elif((c>=b and c<=a) or (c<=b and c>=a)):
        print("c = ",c)
    elif((b>=a and b<=c) or (b<=a and b>=c)):
        print("b = ",b)

def exo18():

    print("Combien de passager p peut contenir un bus??")
    p = int(input("Donnez la valeur de p : "))
    print()
    print()
    print("Combien de passager n doivent être transportés?")
    n = int(input("Donnez la valeur de n : "))

    a = n//p

    print("Pour transporter ",n," passagers il faut ", a," bus" )

def exo19():

    print("Quel est le montant m d'euro à payer?")
    m = int(input("Donnez la valeur de m : "))
    a=m%20
    print("L'excedent est de : ",a) 

def exo20():

    a = int(input("Saisissez l'entier de la combinaison a : "))
    print()
    print()
    b = int(input("Saisissez l'entier de la combinaison b : "))
    points = 0

    if(a==b):
        points += 10
    if((a-b==-1) or (a-b==1)):
        points += 3

    print()
    print()
    print("Cette combinaison rapporte ",points," points")

def exo21():

    def f(j, h):
        ouvert = False
        if(j>0 and j<6):
            if(h>=8 and h<=18):
                ouvert = True
        if(j==6 and (h>=9 and h<=12)):
            ouvert = True
        return ouvert


    j, h = 0, -1
    while(j<1 or j>7):
        j = int(input("Donnez la valeur du jour j entre 1 et 7: "))
    print()
    while(h<0 or h>23):
        h = int(input("Donnez la valeur de l'heure h entre 0 et 23h: "))
    print()
    print(f(j,h))

def exo22():

    n = -1
    he = -1
    mi = -1
    # while (n<0):
    #     n = int(input("Saisissez un entier n positif ou nul : "))
    m = round(n/5)*5
    # print("m = ",m)

    while (0 > he or he > 23):
        he = int(input("Donnez une valeur pour l'heure : "))
    while (0 > mi or mi > 59):
        mi = int(input("Donnez une valeur pour les minutes : "))
    H= he
    M = round(mi/5)*5

    if(M==60):
        M=0
        if(H==23):
            H=0
        else:
            H+= 1

    print(he,"h ", mi,"m -> [",H,", ",M,"]")

def exo23():

    print("Pour la résolution d'une équation du second degré:")
    a = int(input("Saisissez la valeur a : "))
    print()
    b = int(input("Saisissez la valeur b : "))
    print()
    c = int(input("Saisissez la valeur c : "))


    d= (b**2) - (4*a*c)

    if(d>0):
        print("L’équation admet deux solutions réelles")
        print( (-b-(d**0.5))/(2*a) , " et ", (-b+(d**0.5))/(2*a))
    elif(d==0):
        print("L’équation admet une seule solution réelle")
        print((-b/(2*a)))
    else:
        print("L’équation n’admet aucune solution")
        print("Aucune")

