import random
#list_0 = {"coucou","salut"}

dico1 = {}

list_1 = {"chat","soleil","maison","plage","pomme","arbre","ciel","école","livre","fleur","eau","montagne","robe","bateau","piano","oiseau","chien","route","nuage","cheval","coeur","jardin","avion","orange","étoile","fenêtre","ballon","poisson","lapin","cadeau","chemin","nuage","souris","porte","fenêtre","chapeau","manger","étoile","voiture","camion","train","lune","téléphone","ordinateur","table","chaise","pain","église","montre","carte","chaussure","vêtement","écrire","danse","musique","fruit","légume","photo","vacances","plante", "lettre","question","réponse","peinture","vacances","sport","paysage","merci","écrire","lire","dessiner", "écouter","regarder","jouer","courir","manger","dormir","chanter","rire","pleurer", "penser","aimer","parler","sauter","travailler","voyager","sourire","explorer","découvrir","grandir","apprendre","santé","bonheur","sagesse","amitié","espoir","paix","amour"}
 #list_2 = ["coucou"]
 #list_3 = ["coucou"]
 #list_4 = ["coucou"]

dico1["1"] = list_1



ennemy = int(input("Contre qui voulez vous jouer ?                                          Contre l'ordinnateur:1                                                                  Contre un deuxième joueur:2   "))
while not 1 <= ennemy <= 2:
    print("Il faut choisir entre 1 et 2!")
    ennemy = int(input("Contre qui voulez vous jouer ?                                          Contre l'ordinnateur:1                                                                  Contre un deuxième joueur:2   "))
print(ennemy)

if ennemy == 1:
    difficulty = int(input("Choississez la difficulté, Facile:1 Medium:2 Hard:3 Chauchemar:4  "))
    while not 1 <= difficulty <= 4:
        print("La difficulté doit être de 1,2,3 ou 4")
        difficulty = int(input("Choississez la difficulté, Facile:1 Medium:2 Hard:3 Chauchemar:4:  "))
        
    mot = random.choice(dico(difficulty))


else:
    mot = str(input("Joueur 2, Quelle est le mot à faire deviner ?"))
print(mot)
           
      
       