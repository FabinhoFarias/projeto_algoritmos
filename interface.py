import tkinter as tk

class InterfaceGrafo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cheirinho de viagem :)")

        # Variáveis de controle para os campos de entrada
        self.var_cidade_origem = tk.StringVar()
        self.var_cidade_destino = tk.StringVar()

        # Rótulo e campo de entrada para a cidade de origem
        self.rotulo_origem = tk.Label(janela, text="Cidade de Origem:")
        self.rotulo_origem.grid(row=0, column=0, padx=10, pady=5)
        self.entrada_origem = tk.Entry(janela, textvariable=self.var_cidade_origem)
        self.entrada_origem.grid(row=0, column=1, padx=10, pady=5)

        # Rótulo e campo de entrada para a cidade de destino
        self.rotulo_destino = tk.Label(janela, text="Cidade de Destino:")
        self.rotulo_destino.grid(row=1, column=0, padx=10, pady=5)
        self.entrada_destino = tk.Entry(janela, textvariable=self.var_cidade_destino)
        self.entrada_destino.grid(row=1, column=1, padx=10, pady=5)

        # botão 
        self.botao_obter_cidades = tk.Button(janela, text="RODAR", command=self.obter_cidades and janela.quit)
        self.botao_obter_cidades.grid(row=2, columnspan=2, padx=10, pady=5)

    def obter_cidades(self):
        cidade_origem = self.var_cidade_origem.get()
        cidade_destino = self.var_cidade_destino.get()
        
        lista_cidades = [cidade_origem.upper(), cidade_destino.upper()] #Coloquei o upper para evitar erros
        return lista_cidades

# criar a interface e obter as cidades
def rodar_interface():
    janela_principal = tk.Tk()
    app = InterfaceGrafo(janela_principal)
    janela_principal.mainloop()

    cidades_selecionadas = app.obter_cidades()
    return cidades_selecionadas

def mostrar_lista(cidades):
    root = tk.Tk()
    root.title("Lista de Cidades")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    label = tk.Label(frame, text="Lista de Cidades", font=("Helvetica", 16))
    label.pack(pady=10)

    for cidade in cidades:
        if cidade == cidades[-1]:
            cidade_label = tk.Label(frame, text=f'{cidade}')
        else:
            cidade_label = tk.Label(frame, text=f'{cidade} --> ')
        cidade_label.pack()

    root.mainloop()
