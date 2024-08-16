import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Interface Avançada")
janela.geometry("400x500")

label_nome = tk.Label(janela, text="Digite seu nome: ")
label_nome.pack(pady=5)
caixa_texto = tk.Entry(janela, width=40)
caixa_texto.pack(pady=5)

label_preferencia = tk.Label(janela, text="Digite sua preferência: ")
label_preferencia.pack(pady=5)
var_radio = tk.StringVar(value="Café")
radio_cafe = tk.Radiobutton(janela, text="Café", variable=var_radio,
                            value="Café")
radio_cha = tk.Radiobutton(janela, text="Café", variable=var_radio,
                            value="Chá")
radio_suco = tk.Radiobutton(janela, text="Café", variable=var_radio,
                            value="Suco")
radio_agua = tk.Radiobutton(janela, text="Café", variable=var_radio,
                            value="Agua")
radio_cafe.pack()
radio_agua.pack()
radio_cha.pack()
radio_suco.pack()

var_check_saudacao = tk.BooleanVar()
check_saudacao = tk.Checkbutton(janela, text= "Usar saudação informal",
                                variable= var_check_saudacao)
check_saudacao.pack(pady=5)

var_check_personalizada = tk.BooleanVar()
check_personalizada = tk.Checkbutton(janela, text= "Usar saudação personalizada",
                                     variable= var_check_personalizada)
check_personalizada.pack(pady=5)

label_cor = tk.Label(janela, text="Digite sua cor favorita: ")
label_cor.pack(pady=5)
combo_cor = ttk.Combobox(janela, values=["Vermelho", "Azul", "Verde", "Preto"])
combo_cor.pack(pady=5)

botao_atualizar = tk.Button(janela, text="Atualizar")
botao_atualizar.pack(pady=10)
botao_limpar = tk.Button(janela, text="Limpar")
botao_limpar.pack(pady=10)


janela.mainloop()