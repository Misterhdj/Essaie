
def check_real_word(nom):
    def modifier_caracteres(s):
        # Remplacer é,è,ê par e
        s = s.replace('é', 'e').replace('è', 'e').replace('ê', 'e')

        # Remplacer à,ä,â par a
        s = s.replace('à', 'a').replace('ä', 'a').replace('â', 'a')

        return s

    with open("t.txt", 'r') as fichier:
            # Lire chaque ligne du fichier
        lignes = fichier.readlines()

            # Créer une liste pour stocker les éléments de chaque ligne
        liste_elements = []

            # Parcourir chaque ligne et ajouter les éléments à la liste
        for ligne in lignes:
                # Supprimer les caractères de saut de ligne (\n)
        
            ligne = ligne.strip()
            
                # Séparer les éléments en utilisant un séparateur, par exemple une virgule (`,`)
            elements = modifier_caracteres(ligne.split(',')[0])
                # Ajouter la liste d'éléments à la liste principale
        
            # Afficher la liste résultante
        #print("Liste des éléments de chaque ligne :", liste_elements
            
            liste_elements.append(elements)

    for word in liste_elements:
        if nom == word:
            print("yes")
        else:   
            continue 
