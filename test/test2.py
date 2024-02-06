import tkinter as tk
def option1_function():
    print("tu as choisi le mode difficle")
def option2_function():
    print('tu as choisi le mode facile')
def quitter():
    tk.Menu,quit()
def dimensionner():
    width= window.winfo_screenwidth()                
    height= window.winfo_screenheight()              
    window.geometry("%dx%d" % (width, height))

#PhotoImage()


window = tk.Tk()
#window.config(bg='magenta')
window.attributes('-fullscreen', True)
window.resizable(0,1)
window.title('survive or get hanged')
bienvenue = tk.Label(window, text="bienvenue dans survive or get hanged")

button_q = tk.Button(window, text="quitter le jeu", command=quitter, bg='yellow')
button_q.place(x=0,y=0,width=100, height=50)
#button_q.pack(side='left')
#button_s = tk.Button(window,text='start',bg='blue')

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