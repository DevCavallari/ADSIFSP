import tkinter as tk

def mostrar_local(opcao):
    locais = {
        1: "Loja de Informática: 1º andar, à esquerda do elevador.",
        2: "Lan House: à esquerda da Fenix.",
        3: "Escritório: 2º andar."
    }
    resposta.config(text=locais.get(opcao, "Opção inválida."))

janela = tk.Tk()
janela.title("Locais")
janela.geometry("300x200")

tk.Label(janela, text="Escolha um local:").pack()

tk.Button(janela, text="Informática", command=lambda: mostrar_local(1)).pack()
tk.Button(janela, text="Lan House", command=lambda: mostrar_local(2)).pack()
tk.Button(janela, text="Advocacia", command=lambda: mostrar_local(3)).pack()

resposta = tk.Label(janela, text="", fg="green")
resposta.pack(pady=10)

janela.mainloop()
