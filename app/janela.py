from tkinter import *

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="Minha janela exibida")
texto.pack()

pic = PhotoImage(file="./app/python.png")
logo = Label(master=janelaPrincipal, image=pic)
logo.pack()

# Mantenha uma referência ao objeto PhotoImage para evitar que seja coletado pelo coletor de lixo Python
logo.image = pic  

botao = Button(master=janelaPrincipal, text='Clique', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()