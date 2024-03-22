from PIL import ImageTk, Image
import tkinter as tk
from pathlib import Path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
#définition des chemins des images utilisées
path = str(script_dir)+ "/accueil.jpg"
path_2 = str(script_dir)+ "/fond.jpg" 

w_fin = tk.Tk() #création de la fenêtre
w_fin.attributes('-fullscreen', True) #ouverture en fullscreen
w_fin.resizable(0,1)
w_fin.title('survive or get hanged') #nom de la fenêtre
img_2 = ImageTk.PhotoImage(Image.open(path_2)) #dans l'ordre, définition de ce qu'est l'image et d'où elle se trouve et placement de l'image
image_fin = tk.Label(w_fin,image=img_2 )
image_fin.place(relx=0,relwidth=1,relheight=1) 
fin =tk.Label(w_fin,text='le jeu est fini voilà le classement',) #text affiché à la fin, + son placement
fin.place(anchor='center',relx=0.5,rely=0.25)
#création du leaderboard
#leaderboard_1 = tk.Label(w_fin,text=)
#leaderboard_2 = tk.Label(w_fin,text=)
#leaderboard_3 = tk.Label(w_fin,text=)
#leaderboard_4 = tk.Label(w_fin,text=)
#leaderboard_5 = tk.Label(w_fin,text=)