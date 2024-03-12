import tkinter as tk
Pseudo=""
def dimensionner():
    width= window.winfo_screenwidth()                
    height= window.winfo_screenheight()        
    window.geometry("%dx%d" % (width, height))
def ordinateur():
    button_ordinateur.destroy()
    button_joueur.destroy()
    button_pseudo.place(x=900,y=400,width=50,height=50)
    pseudo.place(x=675,y=400,width=250,height=50)
    pseudo_affichage.place(x=750,y=300)
 
def joueur():
    button_ordinateur.destroy()
    button_joueur.destroy()
    print('vous avez choisi le mode joueur')
def start():
    button_s.destroy()
    button_joueur.place(x=750,y=500,width=100,height=50)
    button_ordinateur.place(x=750,y=100,width=100,height=50)
def facile():
    button_f.destroy()
    button_m.destroy()
    button_h.destroy()
    button_c.destroy()
    x=1
def medium():
    button_f.destroy()
    button_m.destroy()
    button_h.destroy()
    button_c.destroy()
    x=2
def hard():
    button_f.destroy()
    button_m.destroy()
    button_h.destroy()
    button_c.destroy()
    x=3
def cauchemar():
    button_f.destroy()
    button_m.destroy()
    button_h.destroy()
    button_c.destroy()
    x=4
def var_pseudo():
    global Pseudo
    Pseudo=pseudo.get()
    print(pseudo)
    erreur=tk.Label(window, text='choisi un pseudo!!!!!!')
    if Pseudo == '':
        erreur.place(x=750,y=300)
        pseudo_affichage.destroy()
    else:
        pseudo_affichage.destroy()
        pseudo.destroy()
        erreur.destroy()
        button_pseudo.destroy()
        button_f.place(x=750,y=100,width=100, height=50)
        button_m.place(x=750,y=300,width=100, height=50)
        button_h.place(x=750,y=500,width=100, height=50)
        button_c.place(x=750,y=700,width=100, height=50)
x=0
window = tk.Tk()
#window.config(bg='magenta')
window.attributes('-fullscreen', True)
window.resizable(0,1)
window.title('survive or get hanged')
bienvenue = tk.Label(window, text="bienvenue dans survive or get hanged")
 
button_q = tk.Button(window, text="quitter le jeu"
                     , command=window.destroy
                     , fg='red')
button_q.place(x=1500,y=0,width=100, height=50)
#button_q.pack(side='left')
button_s = tk.Button(window
                     ,text='start'
                     ,command=start
                      ,bg='blue',)
button_s.place(x=700,y=500,width=200, height=50)
 
button_f = tk.Button(window,
                      text='facile',command=facile)
button_m = tk.Button(window,
                    text='medium',
                     command=medium)
button_h = tk.Button(window,
                    text='hard',
                     command=hard)
button_c = tk.Button(window,
                     text='cauchemar',
                     command=cauchemar)
 
button_ordinateur=tk.Button(window,
                            text='ordinateur',command=ordinateur)
button_joueur=tk.Button(window,
                        text='joueur',command=joueur)
 
 
nom=tk.StringVar()
pseudo_affichage=tk.Label(window,text='choisi ton pseudo')
pseudo=tk.Entry(window,text= 'choisi ton pseudo',textvariable = nom,)
button_pseudo=tk.Button(window,text='enter',command=var_pseudo)
 
 
 
menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(
    label='Exit',
    command=window.destroy
)
menu.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
window.mainloop()
window
