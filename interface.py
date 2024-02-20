
# olá :)

# criação da interface, depois vou organizar de forma separada 
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
        self.botao_obter_cidades = tk.Button(janela, text="Obter Cidades", command=self.obter_cidades)
        self.botao_obter_cidades.grid(row=2, columnspan=2, padx=10, pady=5)

    def obter_cidades(self):
        cidade_origem = self.var_cidade_origem.get()
        cidade_destino = self.var_cidade_destino.get()
        
        lista_cidades = [cidade_origem, cidade_destino]
        return lista_cidades

# criar a interface e obter as cidades
def obter_cidades_interface():
    janela_principal = tk.Tk()
    app = InterfaceGrafo(janela_principal)
    janela_principal.mainloop()

    cidades_selecionadas = app.obter_cidades()
    return cidades_selecionadas

cidades_selecionadas = obter_cidades_interface()
#print("Cidades selecionadas:", cidades_selecionadas)
