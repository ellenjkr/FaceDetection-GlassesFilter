import tkinter as tk
from tkinter import ttk
from pygameTeste import main

def armazenaValores(nome, var):
	arquivoEntrada = open('registro.txt', 'r')
	linhas = arquivoEntrada.readlines()
	arquivoEntrada.close()

	usuarios = []
	oculos = []

	for linha in linhas:
		try:
			dados = linha.split(',')
			usuarios.append(dados[0])
			oculos.append(dados[1])
		except:
			pass

	existe = False
	for pos, individuo in enumerate(usuarios):
		if nome == individuo:
			oculos[pos] = var
			existe = True

	arquivoSaida = open('registro.txt', 'w')
	
	for i in range(0, len(usuarios)):
		arquivoSaida.write(f'{usuarios[i]},{oculos[i]},\n')

	if nome != '' and nome != ' ' and var != 0 and existe == False:
		arquivoSaida.write(f'{nome},{var},\n')


def executaPrograma(user):
	arquivoEntrada = open('registro.txt', 'r')
	linhas = arquivoEntrada.readlines()
	arquivoEntrada.close()

	usuarios = []
	oculos = []

	for linha in linhas:
		try:
			dados = linha.split(',')
			usuarios.append(dados[0])
			oculos.append(dados[1])
		except:
			pass

	for pos, individuo in enumerate(usuarios):
		if user == individuo:
			oculosPrincipal = oculos[pos]
			main(oculosPrincipal)




window = tk.Tk()

frame = tk.Frame(window, bd=3, bg='white')
frame.pack(fill='both', expand=True)

oculos = tk.PhotoImage(file='images/opcoesOculos.png')
labelOculos = tk.Label(frame, image=oculos)
labelOculos.pack(side='top')

frameOpcoesOculos = tk.Label(frame, bg='white')
frameOpcoesOculos.pack(side='top')
var = tk.IntVar()
R1 = ttk.Radiobutton(frameOpcoesOculos, text="Óculos 1", variable=var, value=1)
R1.pack(side='left', anchor='n')
R2 = ttk.Radiobutton(frameOpcoesOculos, text="Óculos 2", variable=var, value=2)
R2.pack(side='left', anchor='n')
R3 = ttk.Radiobutton(frameOpcoesOculos, text="Óculos 3", variable=var, value=3)
R3.pack(side='left', anchor='n')

frameRegister = tk.Frame(frame, bg='white')
frameRegister.pack(side='top')
labelNome = tk.Label(frameRegister, text='Nome: ', bg='white')
labelNome.pack(side='left')
name = ttk.Entry(frameRegister)
name.pack(side='left')
nameButton = ttk.Button(frameRegister, text='Registrar', command=lambda: armazenaValores(name.get(), var.get()))
nameButton.pack(side='left')

frameUsername = tk.Frame(frame, bg='white')
frameUsername.pack(side='top')
labelNome = tk.Label(frameUsername, text='Nome: ', bg='white')
labelNome.pack(side='left')
user = ttk.Entry(frameUsername)
user.pack(side='left')
userButton = ttk.Button(frameUsername, text='Aplicar', command=lambda: executaPrograma(user.get()))
userButton.pack(side='left')

window.mainloop()
