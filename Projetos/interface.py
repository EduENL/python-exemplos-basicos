import tkinter as tk

def mostrar_mensagem():
    texto = caixa_texto.get()
    label_resultado.config(text=texto)

janela = tk.Tk()
janela.title("Exemplo de interface")
janela.geometry("400x150")

caixa_texto = tk.Entry(janela, width=60)
caixa_texto.pack(pady=10)

botao = tk.Button(janela, text="Mostrar Texto", command=mostrar_mensagem)
botao.pack(pady=5)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=5)

janela.mainloop()
