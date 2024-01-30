import tkinter as tk

def clic():
    print("Le bouton a été cliqué !")

test = tk.Tk()
button = tk.Button(root, text="Cliquez ici", command=clic)
button.pack()

test.mainloop()