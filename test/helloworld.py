z=input("Donner le mot à deviner")
z2=list(z)
y = int(input("Nombre de try"))
pave=["_"*len(z2)]
while len(z2)!=0:
    print("Il reste {0} lettres à deviner".format(len(z2)))
    x = input("Donnez une lettre")
    while len(x)>1:
        x=input("Donnez une lettre")
    print(pave)
    if x in z2 :
       a = int(z2.index(x))
       pave[a]=x
       print(pave)
       z2.remove(x)
       print("Cette lettre est contenue dans le mot")
       if len(z2)== 0 and y!=0 :
           print("Tu as gagné")
           exit()
    else :
        print(pave)
        print("Cette lettre n'est pas contenue dans le mot")
        y = y-1
        if y ==0 :
            print("Tu as perdu") 
            exit()
        



    

      