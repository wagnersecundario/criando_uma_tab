import tkinter as tk

janela = tk.Tk()
janela.title('Minha primeira janela')

label = tk.Label(janela, text='Nome', font=('', 10))
label.grid(row=0, column=0, sticky ='nsew', padx=10, pady=10)

entrada1 = tk.Entry(janela, font=('', 10))
entrada1.grid(row=0, column=1, sticky='w', padx=10, pady=10)

botao = tk.Button(janela, text='Salvar', font=('', 10), borderwidth=4)
botao.grid(row=1, column=1, sticky='w', padx=25)

janela.mainloop()