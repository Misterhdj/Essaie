import random
import points
from Excel_module import *
from test2 import *


window.mainloop
dico1 = {}
score = 0 
i = 0
scores = []

list_1 = ["chat","soleil","maison","plage","pomme","arbre","ciel","école","livre","fleur","eau","montagne","robe","bateau","piano","oiseau","chien","route","nuage","cheval","coeur","jardin","avion","orange","étoile","fenêtre","ballon","poisson","lapin","cadeau","chemin","nuage","souris","porte","fenêtre","chapeau","manger","étoile","voiture","camion","train","lune","téléphone","ordinateur","table","chaise","pain","église","montre","carte","chaussure","vêtement","écrire","danse","musique","fruit","légume","photo","vacances","plante", "lettre","question","réponse","peinture","vacances","sport","paysage","merci","écrire","lire","dessiner", "écouter","regarder","jouer","courir","manger","dormir","chanter","rire","pleurer", "penser","aimer","parler","sauter","travailler","voyager","sourire","explorer","découvrir","grandir","apprendre","santé","bonheur","sagesse","amitié","espoir","paix","amour"]
list_2 = ["coucou","anticonstitutionnellement", "hippopotomonstrosesquippedaliophobie", "supercalifragilisticexpialidocious", "pneumonoultramicroscopicsilicovolcanoconiosis", "électroencéphalographie", "parallaxe", "équinoxe", "soliloque", "quintessence", "équivoque", "péremptoire", "simultanéité", "épigone", "synecdoque", "génuflexion", "procrastination", "exacerbation", "idiosyncrasie", "ineffable", "trichotillomanie", "syllogisme", "altruisme", "nihilisme", "métacognition", "circumlocution", "anachronisme", "hypothalamus", "mégalomanie", "égocentrique", "sycophante", "palimpseste", "osmose", "aporie", "ésotérique", "électrolyse", "acquiescence", "ébullition", "inefficacité", "rétrospective", "véracité", "palpitation", "prophylaxie", "obsolescence", "perspicacité", "ébullition", "prémonition", "incandescence", "monotonie", "épiphanie", "fluctuation", "ambivalence", "euphémisme", "polyvalent",
           "ambidextre", "antagonisme", "équidistant", "décadence", "juxtaposition", "proéminence", "monomanie", "irrévérence", "omnipotence", "persévérance", "rétrospection", "inhibition", "pléthore", "inefficience", "plénitude", "concomitant", "concaténation", "infatigable", "pérennité", "intransigeant", "infinitésimal", "supposition", "dialectique", "oxygénation", "désoxydation", "aberration", "prémisse", "sérendipité", "hétérogénéité", "paradoxe", "diaphanéité", "réminiscence", "transcendance", "concaténation", "alchimie", "idiosyncrasie", "antithèse", "omniprésence", "infrastructures", "mégalithique", "amalgamation", "hétéroclite", "excentricité", "réfraction", "multifacette", "corollaire", "étiolement", "diffraction", "bicaméral", "infrastructures", "hypothétique", "égocentrisme", "éclectique", "sophisme", "évanescence", "cryptographie", "nécromancie", "diachronique", "protagoniste",
             "présage", "prédilection", "rémission", "obfuscation", "sérendipité", "épithète", "symbiotique", "divergence", "nostalgie", "prodigieux", "prémices", "éphémère", "entropie", "crépusculaire", "pléonasme", "omniscient", "sérendipité", "dissonance", "redondance", "incantation", "prolifération", "frugalité", "placidité", "éloquence", "authentique", "exacerbation", "insouciance", "incongru", "impudence", "inexorable", "élixir", "incantation", "cacophonie", "opulence", "pluralité", "nébuleux", "parité", "cryptique", "quadrature", "quintessence", "incorrigible", "querelle", "propension", "polymorphe", "polymathique", "paroxysme", "absolution", "conjecture", "effervescence", "euphorie", "catharsis", "dystopie", "astucieux", "clémence", "prophylactique", "altérité", "impénétrable", "magnanime", "discordance", "clarté", "catégorique", "catatonique", "converger", "digresser", "équivoque",
               "élucider", "dialectique", "épiphanie", "érudition", "excentrique", "exhorter", "époustouflant", "extravagant", "fébrile", "flegmatique", "fulgurant", "générique", "hiérarchie", "hétérodoxe", "immuable", "imparable", "imperméable", "inaltérable", "ineffable", "infamie", "inlassable", "intransigeant", "invétéré", "irréfragable", "irrévocable", "limpide", "magnanime", "magnificence", "majestueux", "mélancolique", "méticuleux", "multiforme", "mythique", "nébuleux", "néophyte", "nostalgie", "nouveau", "ondoyant", "onirique", "paradoxal", "pathétique", "pécuniaire", "péremptoire", "périlleux", "pétrifié", "philanthropie", "platonique", "polémique", "polyglotte"]

dico1[1] = list_1
listf=["1","2"]
listd=["1","2","3","4"]

a = input("Contre qui voulez vous jouer ?                                          Contre l'ordinnateur:1                                                                  Contre un deuxième joueur:2   ")

while a not in listf :
    print("Il faut choisir entre 1 et 2!")
    a = input("Contre qui voulez vous jouer ?                                          Contre l'ordinnateur:1                                                                  Contre un deuxième joueur:2   ")
ennemy = int(a)
if ennemy == 1 :
      Pseudo1=input("Quel est votre pseudo ? ")
if ennemy == 2 : 
     Pseudo1=input("Quel est le pseudo du joeueur 1 ? ")
     Pseudo2=input("Quel est le pseudo du joeur 2 ? ")     
for i in range(6) :
    i = i + 1
    if ennemy == 1:
        b = input("Choississez la difficulté, Facile:1 Medium:2 Hard:3 Chauchemar:4  ")
        while b not in listd:
            print("La difficulté doit être de 1,2,3 ou 4")
            b = input("Choississez la difficulté, Facile:1 Medium:2 Hard:3 Chauchemar:4:  ")
        difficulty=int(b)
        if difficulty == 1 :
            mot =list_1[int(random.randint(0,len(list_1)-1))]
            print(mot)
            y = 10
        if difficulty == 2 :
            mot =list_1[int(random.randint(0,len(list_1)-1))]
            print(mot)
            y = 6
        if difficulty == 3 :
            mot =list_1[int(random.randint(0,len(list_1)-1))]
            print(mot)
            y = 8
        else:
            mot =list_1[int(random.randint(0,len(list_1)-1))]
            print(mot)
            y = 6

    else:
        if i%2!=0 :
             u = 2
        if i%2==0 : 
             u = 1 
        mot = str(input("Joueur {0}, Quelle est le mot à faire deviner ?".format(u)))
        print(mot)
        y=8
    mot=mot.lower()
    mot = list(mot)
    e=["é","è","ê"]
    for i in range(len(mot)) : 
            if mot[i] in e :
                mot[i]="e"
    a2=["à","ä","â"]
    for i in range(len(mot)) : 
            if mot[i] in a2 :
                mot[i]="a"
    for i in range(len(mot)):
        if mot[i]=="ü":
            mot[i]="u"
    for i in range(len(mot)):
        if mot[i]=="ö":
            mot[i]="o"
    for i in range(len(mot)):
        if mot[i]=="î":
            mot[i]="i"
    for i in range(len(mot)):
        if mot[i]=="ç":
            mot[i]="c"
    
    check_real_word(mot)




    z2=mot
    z3=z2.copy()
    pave= list("_"*len(z2))
    lettres = []
    alphabet=list("qwertzuiopasdfghjklyxcvbnm-")
    

    print(pave)
    while len(z2)!=0:
        print("Il reste {0} lettres à deviner".format(len(z2)))
        
        x = input("Donnez une lettre, vous avez déjà essayer {0}".format(lettres))
        while len(x)>1 or len(x)==0 or x in lettres or x not in alphabet:
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
            lettres.append(x)
            print(pave)
            print("La lettre {0} est contenue dans le mot".format(x))
            if len(z2)== 0 and y!=0 :
                print("Tu as gagné")
                if difficulty == 1 :
                    score= 50 + y*5
                if difficulty == 2 :
                        score= 100 + y*5
                if difficulty == 3 :
                        score =  150 + y*5
                if difficulty == 4 :
                        score =  200 + y*5
                scores.append(score)
                
         
        else :
            print(pave)
            print("La lettre {0} n'est pas contenue dans le mot".format(x))
            y = y-1
            print("Il vous reste {0} essaie(s)".format(y))
            lettres.append(x)
            if y ==0 :
                print("Tu as perdu") 
                print("Le mot était {0}".format(z3))
            
              
if ennemy == 1 : 
     somme = 0 
     for i in scores : 
          somme += i 
if ennemy == 2 :
     point1=0
     point2=0
     for i in scores : 
          if i%2==0 :
               point1 += i 
          if i%2!=0 :  
               point2 += i 
          
f = open("leaderboard.txt","a")
if ennemy == 1 :
    f.writelines(str("{0}".format(somme))+",{0}".format(Pseudo1)+"\n")
if ennemy == 2 :
     f.writelines(str("{0}".format(point1))+",{0}".format(Pseudo1))
     f.writelines(str("{0}".format(point2))+",{0}".format(Pseudo2))

f.close()

f = open("leaderboard.txt","r")
lines =f.readlines()
lead = {}
i = 0
for line in lines :
     line = line.strip("\n")
     player = line.split(",")
     i = i + 1 
     lead[i]=player
     
f.close()
import z 
z.classe()  
     
     



