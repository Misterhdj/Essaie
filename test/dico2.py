z=input("Donner le mot à deviner")
z2=list(z)
z3=list(z2)
y = int(input("Nombre de try"))
pave= list("_"*len(z2))
print(pave)
while len(z2)!=0:
    print("Il reste {0} lettres à deviner".format(len(z2)))
    
    x = input("Donnez une lettre")
    while len(x)>1 or len(x)==0:
        x=input("Donnez une lettre")
    if x in z2 :
       index = []
       for i in range(len(z3)) :
           if z3[i] == x :
               index.append(i)
       print(index)
       for i in index :
            pave[i]=x
            for i in z2 : 
               if i == x :
                z2.remove(x)
       print(pave)
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