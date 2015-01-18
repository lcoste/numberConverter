def afficher(x):                 #Permet d'afficher les listes (ex: hexa,romain)
    for i in range (len(x)):
        print (x[i],end="")
    print ("")


def menu():        #Ne sert qu'a afficher les choix de type d'entrée disponibles
    fini = True
    while fini:
        print ("Ce programme permet de convertir un nombre entier positif")
        print (fini)
        print ("en un autre type de nombre de votre choix")
        print ()                                   #Ne sert qu'a la presantation
        print ("1- Nombre Décimal")
        print ("2- Nombre Binaire")
        print ("3- Nombre Héxadécimal")
        print ("4- Nombre Romain")
        print ("")
        choix = int(input("Entré le chiffre correspondant au type que vous voulez entrer:"))
        if choix >= 1 and choix <= 4:  #Si l'utilsateur a choisi une des options
            fini = False
        else:
            print()
            print()
            print("!!!!!!!!Vous devez choisir parmi ce qui vous est proposer!!!!!!!!!")
            print()
            print()
    print()
    print()
    return choix                           #On renvoie le choix de l'utilisateur

def sortie():                  #Meme utilité que précedement mais pour la sortie
    fini = True
    while fini:
        print ()
        print ()
        print ()
        print ()
        print ()
        print ("1- Nombre Décimal")
        print ("2- Nombre Binaire")
        print ("3- Nombre Héxadécimal")
        print ("4- Nombre Romain")
        print ("")
        choix = int(input("Entré le chiffre correspondant au type que vous voulez en sortie:"))
        if choix >= 1 and choix <= 4:
            fini = False
        else:
            print()
            print()
            print()
            print()
            print("!!!!!!!!Vous devez choisir parmi ce qui vous est proposer!!!!!!!!!")
    print()
    print()
    print()
    return choix



def out_romain(temp):                     #Permet de convertir en chiffre romain
    X=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    LETTRE=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    resultat = []   
    i=0
    while temp != 0: #Les tableaus se font derouler du plus grand au plus petits
        if temp - X[i] >= 0:     #Si on peut soustraire une certaine valeur sans 
            resultat.append(LETTRE[i])                           ##passer sous 0
            temp = temp-X[i]
            i=0                           #Permet de repartir d debut du tableau
        else:
            i=i+1
    return resultat

def in_romain(temp):                        #Permet de lire les chiffres romains
    X=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    LETTRE=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    resultat = 0
    a= len(temp)
    i=0
    prec=1001
    z=0
    while i < a:
        try:    
            x= LETTRE.index(temp[i])
        except ValueError:
            return None     #Si l'utilisateur ne rentre pas un valeur acceptable
        if X[x]>prec:                                       ##On renvoie du vide
            return None
        if a-1!=i:                                    
            try:    
                y= LETTRE.index(temp[i+1])
            except ValueError:
                return None
            try:
                z=X.index(X[y]-X[x])
            except ValueError:
                resultat = resultat + X[x]
                prec= X[x]
            else:
                if z%2==1:
                    if X[z]>=prec:
                        return None
                    resultat = resultat + X[z]
                    prec=X[z]
                    i=i+1
                else:
                    return None
        else:
            resultat = resultat + X[x]
        i=i+1
    return resultat
        

def out_binaire(temp):                             #De meme mais pour le binaire
    i = 1
    resultat = 0
    while temp > 0:
        resultat = (temp%2*i)+resultat                         #Sans commentaire
        temp = temp//2
        i=i*10
    return resultat

def in_binaire(temp):
    a= len(temp)
    add=1
    resultat=0
    for i in range (a):
        x = temp[a-i-1]
        if x=='1':
            resultat=resultat+add
        elif x=='0':
            None                                               #Rien ne se passe
        else:
            return None
        add=add*2
    return resultat

def out_hexa(temp):                                  #De meme mais pour les hexa
    LETTRE=["a","b","c","d","e","f"]
    X=[10,11,12,13,14,15]
    resultat = []
    while temp > 0:
        x=temp%16
        if x>9:
            i=0
            while i<6:
                if x==X[i]:
                    resultat.append(LETTRE[i])
                    break
                else:
                    i=i+1
        else:
            resultat.append(x)
        temp = temp//16
    resultat.reverse()                         #Sinon le resultat est a l'envers
    return resultat

def in_hexa(temp):
    LETTRE=['0','1','2','3','4','5','6','7','8','9',"a","b","c","d","e","f"]
    X=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    a= len(temp)
    add=1
    resultat=0
    for i in range (a):                                        #Sans commentaire
        x = temp[a-i-1]
        if LETTRE.count(x)!=0:
            n=0
            while n<16:
                if x==LETTRE[n]:
                    resultat=resultat+(X[n]*add)
                    break
                else:
                    n=n+1
        else:
            return None
        add=add*16
    return resultat
        
    
#Deroulement du programme
fini = True
while fini:			
    select=menu()
    if select == 1:
        try:
            entree = int(input("Entrer:"))
            nombre= entree
        except ValueError:
            nombre=None
                    
    if select == 2:
        entree = input("Entrer:")
        nombre = in_binaire(entree)
        
    
    if select == 3:
        entree = input("Entrer:")
        nombre = in_hexa(entree)
    
    if select == 4:
        entree = input("Entrer:")
        nombre = in_romain(entree)

    if nombre != None:     #L'utilisateur a-t-il rentrer un variable acceptable?
        select = sortie()
        
        if select == 1:
            convertie = nombre
            print (entree,"en décimal: ",convertie)
                        
        if select == 2:
            convertie = out_binaire(nombre)
            print (entree,"en binaire: ",convertie)
        
        if select == 3:
            convertie = out_hexa(nombre)
            print (entree, "en héxadécimal: ",end="")
            afficher (convertie)
        
        if select == 4:
            convertie = out_romain(nombre)
            print (entree,"en chiffre romain: ",end="")
            afficher (convertie)
    
    else:                       #L'utilisateur n'a pas rentre un valeur correcte
        print()
        print()
        print("**********ECHEC**********")
        print()
        print()
        print("Vous n'avez pas entré une variable correcte")


        
    print()
    print()
    print()
    print()
    print("Voulez Recommencer:    1-Oui    2-Non    ",end='')
    fin = int(input())
    if fin!=1:
        break
    else:
        for i in range(55):
            print()

    
