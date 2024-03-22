import random                        # importation des modules pour 1: pouvoir choisir un element aleatoire dans une liste
import points
from Excel_module import *           # 2: verifier si le mot a faire deviner est un vrai mot
from test2 import *                   # 3: interface de tkinter
from test3 import *                 # interface tkinter
import z 


dico1 = {}
score = 0                             # creation de nombreuse variable pour pouvoir les utiliser plus tard  
i = 0
o = 0
scores = []
u = 1 

list_1 = ["chat","soleil","maison","plage","pomme","arbre","ciel","école","livre","fleur","eau","montagne","robe","bateau","piano","oiseau","chien","route","nuage","cheval","coeur","jardin","avion","orange","étoile","fenêtre","ballon","poisson","lapin","cadeau","chemin","nuage","souris","porte","fenêtre","chapeau","manger","étoile","voiture","camion","train","lune","téléphone","ordinateur","table","chaise","pain","église","montre","carte","chaussure","vêtement","écrire","danse","musique","fruit","légume","photo","vacances","plante", "lettre","question","réponse","peinture","vacances","sport","paysage","merci","écrire","lire","dessiner", "écouter","regarder","jouer","courir","manger","dormir","chanter","rire","pleurer", "penser","aimer","parler","sauter","travailler","voyager","sourire","explorer","découvrir","grandir","apprendre","santé","bonheur","sagesse","amitié","espoir","paix","amour"]
list_2 = ["coucou", "supercalifragilisticexpialidocious", "pneumonoultramicroscopicsilicovolcanoconiosis", "électroencéphalographie", "parallaxe", "équinoxe", "soliloque", "quintessence", "équivoque", "péremptoire", "simultanéité", "épigone", "synecdoque", "génuflexion", "procrastination", "exacerbation", "idiosyncrasie", "ineffable", "trichotillomanie", "syllogisme", "altruisme", "nihilisme", "métacognition", "circumlocution", "anachronisme", "hypothalamus", "mégalomanie", "égocentrique", "sycophante", "palimpseste", "osmose", "aporie", "ésotérique", "électrolyse", "acquiescence", "ébullition", "inefficacité", "rétrospective", "véracité", "palpitation", "prophylaxie", "obsolescence", "perspicacité", "ébullition", "prémonition", "incandescence", "monotonie", "épiphanie", "fluctuation", "ambivalence", "euphémisme", "polyvalent",
           "ambidextre", "antagonisme", "équidistant", "décadence", "juxtaposition", "proéminence", "monomanie", "irrévérence", "omnipotence", "persévérance", "rétrospection", "inhibition", "pléthore", "inefficience", "plénitude", "concomitant", "concaténation", "infatigable", "pérennité", "intransigeant", "infinitésimal", "supposition", "dialectique", "oxygénation", "désoxydation", "aberration", "prémisse", "sérendipité", "hétérogénéité", "paradoxe", "diaphanéité", "réminiscence", "transcendance", "concaténation", "alchimie", "idiosyncrasie", "antithèse", "omniprésence", "infrastructures", "mégalithique", "amalgamation", "hétéroclite", "excentricité", "réfraction", "multifacette", "corollaire", "étiolement", "diffraction", "bicaméral", "infrastructures", "hypothétique", "égocentrisme", "éclectique", "sophisme", "évanescence", "cryptographie", "nécromancie", "diachronique", "protagoniste",
             "présage", "prédilection", "rémission", "obfuscation", "sérendipité", "épithète", "symbiotique", "divergence", "nostalgie", "prodigieux", "prémices", "éphémère", "entropie", "crépusculaire", "pléonasme", "omniscient", "sérendipité", "dissonance", "redondance", "incantation", "prolifération", "frugalité", "placidité", "éloquence", "authentique", "exacerbation", "insouciance", "incongru", "impudence", "inexorable", "élixir", "incantation", "cacophonie", "opulence", "pluralité", "nébuleux", "parité", "cryptique", "quadrature", "quintessence", "incorrigible", "querelle", "propension", "polymorphe", "polymathique", "paroxysme", "absolution", "conjecture", "effervescence", "euphorie", "catharsis", "dystopie", "astucieux", "clémence", "prophylactique", "altérité", "impénétrable", "magnanime", "discordance", "clarté", "catégorique", "catatonique", "converger", "digresser", "équivoque",
               "élucider", "dialectique", "épiphanie", "érudition", "excentrique", "exhorter", "époustouflant", "extravagant", "fébrile", "flegmatique", "fulgurant", "générique", "hiérarchie", "hétérodoxe", "immuable", "imparable", "imperméable", "inaltérable", "ineffable", "infamie", "inlassable", "intransigeant", "invétéré", "irréfragable", "irrévocable", "limpide", "magnanime", "magnificence", "majestueux", "mélancolique", "méticuleux", "multiforme", "mythique", "nébuleux", "néophyte", "nostalgie", "nouveau", "ondoyant", "onirique", "paradoxal", "pathétique", "pécuniaire", "péremptoire", "périlleux", "pétrifié", "philanthropie", "platonique", "polémique", "polyglotte"]
                                                          # creation des listes pour les differnetes difficulté
dico1[1] = list_1
listf=["1","2"]
listd=["1","2","3","4"]
a = input("Contre qui voulez vous jouer ?                                          Contre l'ordinnateur:1                                                                  Contre un deuxième joueur:2   ")
                                                          # demande le mode de jeu 
while a not in listf :
    print("Il faut choisir entre 1 et 2!")                # force le joueur a choisir l'un des deux modes de jeu
    a = input("Contre qui voulez vous jouer ?                                          Contre l'ordinnateur:1                                                                  Contre un deuxième joueur:2   ")
ennemy = int(a)
if ennemy == 1 :
      Pseudo1=input("Quel est votre pseudo ? ") 
if ennemy == 2 :                                          # demande le pseudo du/des joueur/s en fonction du mode de jeu  
     Pseudo1=input("Quel est le pseudo du joueur 1 ? ")
     Pseudo2=input("Quel est le pseudo du joueur 2 ? ")     
while u == 1 :                                            # boucle pour pouvoir rejouer a la fin d'une partie
    for i in range(6) :                                   # nombre de mot à deviner par partie
        i = i + 1
        if ennemy == 1:                                   # choix de la difficulté si mode de jeu contre l'ordinnateur
            difficulty = input("Choississez la difficulté, Facile:1 Medium:2 Hard:3 Chauchemar:4  ")
            while difficulty not in listd:
                print("La difficulté doit être de 1,2,3 ou 4")
                difficulty = input("Choississez la difficulté, Facile:1 Medium:2 Hard:3 Chauchemar:4:  ")
            if difficulty == 1 :
                mot =list_1[int(random.randint(0,len(list_1)-1))]       # la difficulté correspond au nombre d'essaie pour deviner le mot aléatoire et de la complexité du mot aléatoire,
                                                                        # la list_1 contient des mots plutot simples et pas trop long et la list_2 contient des mots très compliqué et long
                print(mot)
                y = 10                    # on definit le nb d'essaie permit: ( le nombre de fausse lettres qu'on a le droit d'écrire avant de perdre)
            if difficulty == 2 :
                mot =list_1[int(random.randint(0,len(list_1)-1))]       
                print(mot)
                y = 6
            if difficulty == 3 :
                mot =list_2[int(random.randint(0,len(list_2)-1))]
                print(mot)
                y = 8
            else:
                mot =list_2[int(random.randint(0,len(list_2)-1))]
                print(mot)
                y = 6

        else:                                                                            # pour le mode de jeu a plusieurs, on regarde au combient-ieme mot à deviner nous en sommes, 
            if i%2!=0 :
                u = 2
            if i%2==0 :                                                                  # si c'est pair c'est au premier joueur de faire deviner et si c'est impair c'est au deuxieme.
                u = 1 
            y = 8                                                                        # on definit le nb d'essaie 
            mot = str(input("Joueur {0}, Quelle est le mot à faire deviner ?".format(u)))
            modifier_caracteres(mot)                                                     # on simplifie le mot donné en enlevant tout accents/cédille..... 
            check_real_word(mot)                                                         # grace a cette fonction, on verrifie dans un fichier contenant environ 140'000 mot francais également simplifié sans accents/cédille si
                                                                                         # le mot proposé pour etre deviné est un vrai mot (francais), si oui on accepte le mot le jeu va commencer, sinon on redemande un nouveau mot au joueur.
            while j != 1:
                print("Ce mot n'est pas français, choisissez un vrai mot à faire deviner !")
                mot = str(input("Joueur {0}, Quelle est le mot à faire deviner ?".format(u)))
                modifier_caracteres(mot)
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
                x=input("Donnez une lettre, vous avez déjà essayer celle-la")
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
                    if len(z3)>8 :
                        o = (len(z3)-8)*1.5
                        
                    if difficulty == 1 :                    # calcul du score de chaque mot deviné en fonction de la difficlté choisi,
                        score= 5 + y*5 + o                  # du nombre d'essaie qu'il vous reste apres avoir gagné et en fonction de la longueur du mot deviné
                    if difficulty == 2 :
                            score= 10 + y*5 + o
                    if difficulty == 3 :
                            score =  15 + y*5 + o 
                    if difficulty == 4 :
                            score =  20 + y*5 + o 
                    scores.append(score)                   # chaque score des mots deviné est rajouté à une liste de score 
                                                           # (exemple: [3/6/7]   => pour mot_1, score = 3 point/ pour mot_2, score = 6 points et pour mot_3, score = 7 points)
            
            else :
                print(pave)
                print("La lettre {0} n'est pas contenue dans le mot".format(x))
                y = y-1
                print("Il vous reste {0} essaie(s)".format(y))
                lettres.append(x)
                if y ==0 :
                    print("Tu as perdu") 
                    print("Le mot était {0}".format(z3))
    u = int(input("Voulez-vous recommencer si oui, taper 1 sinon, taper 2"))               
            
              
if ennemy == 1 :                                          # si mode de jeu contre l'ordinateur, alors le score total du joueur dans cette partie égal a la somme des score de chaque mot deviné
     somme = 0                                           
     for i in scores :                                   
          somme += i 
if ennemy == 2 :                                          # si mode de jeu à plusieurs, alors le score total du joueur 1 est la somme des scores de chaque mot pair et pareil pour joueur 2 avec 
     point1=0                                             # les scores de mots impair. ( score tot joueur1 = score mot 2 + 4 + 6 et score tot joueur 2 = score mot 1 + 3 + 5)
     point2=0
     for i in scores : 
          if i%2==0 :
               point1 += i 
          if i%2!=0 :  
               point2 += i 
          
f = open("leaderboard.txt","a")                                                                                 # ouverture d'un fichier pour le scoreboard
if ennemy == 1 :
    f.writelines(str("{0}".format(somme))+":{0}".format(Pseudo1)+"\n")                                          # si mode de jeu contre ordinateur, alors enrengistre le score et le nom du joueur
if ennemy == 2 :                                                                                                # sinon pour mode de jeu a plusieur, imprime le gagnant et enrengistre le double du score et le nom de joueur gagnant.
     if point1>point2 :                                                                                         # car contre l'ordinateur le joueur devine 6 mots alors qu'a plusieurs chacun devine 3 mots donc le score
          print("{0} à gagner, avec un score de {1}, {2} a quant à lui fait un score de {3}".format(Pseudo1,point1,Pseudo2,point2))   # du mode de jeu a plusieurs doit etre 2 fois plus grand pour etre comparé avec le mode contre l'ordinateur
          f.writelines(str("{0}".format(point1*2))+":{0}".format(Pseudo1)+"\n")                                                        
     if point1<point2 :
           print("{0} à gagner, avec un score de {1}, {2} a quant à lui fait un score de {3}".format(Pseudo2,point2,Pseudo1,point1))
           f.writelines(str("{0}".format(point2*2))+":{0}".format(Pseudo2)+"\n")
     if point1 == point2: 
         print("Vous avez fait une égalité avec tout deux {0} points, bien joué !".format(point1*2))
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
z.classe()