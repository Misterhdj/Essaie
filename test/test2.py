import tkinter as tk
def option1_function():
    print("tu as choisi le mode difficle")
def option2_function():
    print('tu as choisi le mode facile')
def dimensionner():
    width= window.winfo_screenwidth()                
    height= window.winfo_screenheight()              
    window.geometry("%dx%d" % (width, height))
def start():
    button_s.destroy()
    button_f.place(x=750,y=100,width=100, height=50)
    button_m.place(x=750,y=300,width=100, height=50)
    button_h.place(x=750,y=500,width=100, height=50)
    button_c.place(x=750,y=700,width=100, height=50)
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
                      ,bg='blue')
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