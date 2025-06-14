import tkinter as tk

def escolher_local(opcao):
    if opcao == 1:
        mensagem = "A Loja de Informática fica no 1º andar, à esquerda do elevador."
    elif opcao == 2:
        mensagem = "A Lan House fica à esquerda da Fenix."
    elif opcao == 3:
        mensagem = "O Escritório de Advocacia está no 2º andar."
    
    resposta_label.config(text=mensagem)

janela = tk.Tk()
janela.title("Destinos Possíveis")
janela.geometry

label = tk.Label(janela, text="Bem-vindo!\nEscolha um local para visitar:")
label.pack(pady=10)


btn1 = tk.Button(janela, text="Fenix Informática", command=lambda: escolher_local(1))
btn1.pack(pady=5)

btn2 = tk.Button(janela, text="Lan House", command=lambda: escolher_local(2))
btn2.pack(pady=5)

btn3 = tk.Button(janela, text="Escritório de Advocacia", command=lambda: escolher_local(3))
btn3.pack(pady=5)

resposta_label = tk.Label(janela, text="", fg="green", )
resposta_label.pack(pady=15)

janela.mainloop()

