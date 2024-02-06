import tkinter as tk
def option1_function():
    print("tu as choisi le mode difficle")
def clic():
    print("Le bouton a été cliqué !")
def option2_function():
    print('tu as choisi le mode facile')

test = tk.Tk()
test.title('le meilleur hangman de tous les temps')
greeting = tk.Label(test, text="Hello, Tkinter")
greeting.pack()
button = tk.Button(test, text="Cliquez ici", command=clic)
button.pack()

import tkinter as tk
from tkinter import Menu

# create a menubar
menu = Menu(test)
test.config(menu=menu)
file_menu = Menu(menu, tearoff=False)
# add a menu item to the menu
file_menu.add_command(
    label='Exit',
    command=test.destroy
)
        

# add the File menu to the menubar
menu.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
#menu=tk.Menu(menu, tearoff=False)
#tk.Menu.add_command(label='difficle', command=option1_function) 
#tk.Menu.add_command(label='facile', command=option2_function)
test.mainloop()