from PIL import ImageTk, Image
import tkinter as tk
from pathlib import Path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
path = str(script_dir)+ "/accueil.jpg"
path_2 = str(script_dir)+ "/fond.jpg"
def rejouer():
    global u
    u = 1
    w_fin.destroy
def arreter():
    global U
    u=0
    w_fin.destroy()
w_fin = tk.Tk()
w_fin.attributes('-fullscreen', True) #ouverture en fullscreen
w_fin.resizable(0,1)
w_fin.title('survive or get hanged')
img_2 = ImageTk.PhotoImage(Image.open(path_2))
image_fin = tk.Label(w_fin,image=img_2 )
image_fin.place(relx=0,relwidth=1,relheight=1) 
fin =tk.Label(w_fin,text='le jeu est fini voilà le classement',)
fin.place(anchor='center',relx=0.5,rely=0.25)
#leaderboard_1 = tk.Label(w_fin,text=)
#leaderboard_2 = tk.Label(w_fin,text=)
#leaderboard_3 = tk.Label(w_fin,text=)
#leaderboard_4 = tk.Label(w_fin,text=)
#leaderboard_5 = tk.Label(w_fin,text=)
#bu_rej =tk.Button(w_fin,text='rejouer',command=rejouer)
#bu_rej.place(w_fin, anchor='center',relx=0.25,rely=0.75,)
#bu_arr = tk.Button(w_fin,text='arrêter',command=arreter)
#bu_arr.place(w_fin, anchor='center',relx=0.75,rely=0.75,)

w_fin.mainloop()
w_fin