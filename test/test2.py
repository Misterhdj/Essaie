from PIL import ImageTk, Image
import tkinter as tk
Pseudo=""
def ordinateur(): #döfinition de l'action executée lorsqu'on appuie sur le bouton ordinateur
    global az 
    button_ordinateur.destroy() #détruit les deux derniers boutons
    button_joueur.destroy()
    az = 1
    #button_pseudo.place(relx=0.6,rely=0.5,width=50,height=50) #place la nouvelle fenêtre(le contenu)
    #pseudo.place(relx=0.4,rely=0.5,relwidth=0.2,height=50)
    #pseudo_affichage.place(relx=0.475,rely=0.4)

def joueur(): #définition du bouton joueur, qui permet de faire un 1vs1
    button_ordinateur.destroy() #détruit les deux boutons qui sont devenus inutiles
    button_joueur.destroy()
def start():#définition du bouton start, on le détruit et on place les deux prochains boutons
    button_s.destroy()
    button_joueur.place(relx=0.45,rely=0.33,relwidth=0.1,height=50)
    button_ordinateur.place(relx=0.45,rely=0.66,relwidth=0.1,height=50)
def facile(): #définition du bouton facile, détruit tous les derniers boutons et lance le jeu
    button_f.destroy()
    button_m.destroy()
    button_h.destroy()
    button_c.destroy()
    x=1
def medium():#définition du bouton medium, détruit tous les derniers boutons et lance le jeu
    button_f.destroy()
    button_m.destroy()
    button_h.destroy()
    button_c.destroy()
    x=2
def hard():#définition du bouton hard, détruit tous les derniers boutons et lance le jeu
    button_f.destroy()
    button_m.destroy()
    button_h.destroy()
    button_c.destroy()
    x=3
def cauchemar():#définition du bouton cauchemar, détruit tous les derniers boutons et lance le jeu
    button_f.destroy()
    button_m.destroy()
    button_h.destroy()
    button_c.destroy()
    x=4
def var_pseudo(): #définition de la "FENÊTRE" de pseudo
    global Pseudo
    Pseudo=pseudo.get()
    erreur=tk.Label(window, text='choisi un pseudo!!!!!!') #si l'utilisateur décide de mettre un truc vide
    #if Pseudo == '':                
    #
        #button_f.place(relx=0.45,rely=0.2,relwidth=0.1, height=50)
        #button_m.place(relx=0.45,rely=0.4,relwidth=0.1, height=50)
        #button_h.place(relx=0.45,rely=0.6,relwidth=0.1, height=50)
        #button_c.place(relx=0.45,rely=0.8,relwidth=0.1, height=50)
    erreur.destroy()
window_start = tk.Tk() #création de la fenêtre
#window.config(bg='magenta')
window_start.attributes('-fullscreen', False) #ouverture en fullscreen
window_start.resizable(0,1)
window_start.title('survive or get hanged')
bienvenue = tk.Label(window_start, text="bienvenue dans survive or get hanged")
button_q = tk.Button(window_start, text="quitter le jeu" #création du bouton quitter afin de quitter le jeu à tout moment
                     , command=window_start.destroy
                     , fg='red')
button_q.place(relx=0.9,rely=0,relwidth=0.1, height=50) #place du bouton quitter
#button_q.pack(side='left')
button_s = tk.Button(window_start #création du bouton start ainsi que son placement 
                     ,text='start'
 
                     ,command=start
                     ,bg='blue',)
button_s.place(relx=0.45,rely=0.5,relwidth=0.1, height=50)
#placements et créations des boutons pour les 4 difficultés
#button_f = tk.Button(window_start,
#                      text='facile',command=facile)
#button_m = tk.Button(window_start,
#                    text='medium',
 #                    command=medium)
#button_h = tk.Button(window_start,
 #                   text='hard',
  #                  command=hard)
#button_c = tk.Button(window,
            #         text='cauchemar',
             #        command=cauchemar)

button_ordinateur=tk.Button(window_start,#création du bouton ordinateur
                            text='ordinateur',command=ordinateur)
button_joueur=tk.Button(window_start,#création du bouton joueur 
                        text='joueur',command=joueur)


#nom=tk.StringVar()
#pseudo_affichage=tk.Label(window,text='choisi ton pseudo')
#pseudo=tk.Entry(window,text= 'choisi ton pseudo',textvariable = nom,)#entrée pour avoir le pseudo que le joueur veut
#button_pseudo=tk.Button(window,text='enter',command=var_pseudo)#bouton qu'on appuie pour avoir le pseudo

#lamda = 5
#underscore = tk.Label(window, text =lamda*'_')
#image1 = Image.open("<desktop/jeudupendufb.jpg>")

#sdfgsdfgsdfg




#création d'un menu pour pouvoir quitter nimporte quand
menu = tk.Menu(window_start)
window_start.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(
    label='Exit',
    command=window_start.destroy
)
menu.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
window_start.mainloop() 