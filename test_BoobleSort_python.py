from tkinter import *
# eu to so testando essa biblioteca que me indicaram,
# para deixar deixar a apresentacao mais "vistosa",
# e eu tenho fe que ela nao vai perguntar como usa essa bibleoteca que eu nao faca a minima ideia 
class Application:
    def __init__(self, master=None):
        
        # Aluno: Janela para melhorar a demonstracao das implementacoes 
        self.widget1 =Frame(master)
        self.widget1.pack()
        self.aluno = Label(self.widget1, text="Cadastros Alunos")
        self.aluno["font"]= "Arial"
        self.aluno.pack ()
        
        # Saida: Botao para encerrar o programa
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack ()

        pass
root = Tk()
Application(root)
root.mainloop()

# bubbleSort: Funcao de ordernacao
# Ordena os nomes digitados pelo usuario em ordem alfabetica
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
# main: Por enquanto ela existe, mas por enquanto 
def main():
    nomes = []
    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para terminar): ")
        if nome.lower() == 'fim':
            break
        nomes.append(nome)
    
    bubble_sort(nomes)
    
    print("\nNomes dos alunos em ordem alfabética:")
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}- {nome}")

if __name__ == "__main__":
    main()

# TODO ei igor esse foi o melhor exemplo que eu pude pensar,
#  é basicamente é um lista q voce vai digitar nomes aleatorios e so sera finalizada qunado a pessoa digitar "fim"
#  e depois ele vai ordenar a lista em ordem alfabetica e vai exibir na tela

#  se voce quiser mudar qualquer coisa pode mudar, so que deixa os comentarios que eu olho e tento entender oq foi feito, 
# se quiser usar outra linguagem pode usar, so usei python pq é mais de boa para digitar.
#  qualquer coisa coloca o codigo em algum conversor de linguagem ai pode trocar se tu achaar melhor

# TODO lá no readme eu vou deixar uma breve explicacao para caso a nossa apresentancao continue assim.