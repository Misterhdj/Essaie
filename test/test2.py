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
window = tk.Tk()
#window.config(bg='magenta')
window.attributes('-fullscreen', True)
window.resizable(0,1)
window.title('survive or get hanged')

bienvenue = tk.Label(window, text="bienvenue dans survive or get hanged")
bienvenue.pack()

button = tk.Button(window, text="quitter le jeu", command=quitter, fg='red', bg='red')
button.place(x=1000,y=1000)
button.pack


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