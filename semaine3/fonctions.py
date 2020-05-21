
####################
# import of another function file outside of this directory
####################
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../')

from squallFunction import *
####################


def exo1():
    L=[]
    n=saisieInt("nombre d'éléments de la liste: ")
    for i in range(n):
        a=-1
        while(a<0 or a>9):
            a=saisieInt("Saisissez l'élément {} : ".format(i+1))
        L.append((a))
    x=saisieInt("Valeur de n: ")
    for b in range(x):
        affichageListe(L)

def exo2_1():
    memeParite=False
    a=saisieInt("valeur de l'entier a : ")
    b=saisieInt("valeur de l'entier b : ")
    if(a%2==b%2):
        memeParite=True
    print("memeParite = ", memeParite)

def exo2_2():
    a=0
    b=2
    while(a<=0):
        a=saisieInt("longueur du côté : ")
    for i in range(a):
        for j in range(a):
            c=4 if(b%2==0) else 2
            print(c, " ",end="")
            b+=1
        print(end="\n")

def exo3_1
           