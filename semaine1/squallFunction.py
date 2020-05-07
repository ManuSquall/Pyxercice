def palindrome(chaine):
    return chaine == chaine[::-1]

def saisieInt(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Valeur invalide.")
       continue
    else:
       return userInput 
       break 

def saisieFloat(message):
  while True:
    try:
       userInput = float(input(message))       
    except ValueError:
       print("Valeur invalide.")
       continue
    else:
       return userInput 
       break 

def factoriel(n):
    resultat=1
    for i in range(1,n+1):
        #resultat=resultat*i
        resultat*=i
    return (resultat,n)


def saisieMatrice(n,m):
    A=[]
    for i in range(n):
        L=list()
        for j in range(m):
            # a=int(input("Donner la valeur a{}{}\n".format(i+1,j+1)))
            a=saisieInt("Donner une valeur entière a{}{}\n".format(i+1,j+1))
            L.append(a)
        A.append(L)
    return A
    
def saisieListe():
    L=[]
    n=saisieInt("nombre d'éléments de la liste: ")
    for i in range(n):
        L.append((saisieInt("Saisissez l'élément {} : ".format(i+1))))
    return L

def saisieNListe(n):
    L=[]
    for i in range(n):
        L.append((saisieInt("Saisissez l'élément {} : ".format(i+1))))
    return L

def affichageListe(L):
    print("[ ", end="")
    for i in range(len(L)):
        print(L[i], end="")
        if(i!=(len(L)-1)):
            print(" - ", end="")

    print("] ", end="\n")
    

def formattageMatrice(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end="\t")
        print()


def factorielRecursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorielRecursive(n-1)