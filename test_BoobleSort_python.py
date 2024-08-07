from tkinter import *
import os

class Application:

    def __init__(self, master=None):
        self.arr = []

        self.widget1 = Frame(master)
        
        # Aluno: Janela para melhorar a demonstracao das implementacoes 
        self.widget1 =Frame(master)
        self.widget1.pack()

        self.fontePadrao = ("Arial", 10)

        self.entrada1 = Frame(master)
        self.entrada1.pack(pady=10)

        self.nomeLabel = Label(self.entrada1, text="Nome:", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nomeEntry = Entry(self.entrada1, font=self.fontePadrao)
        self.nomeEntry.pack(side=LEFT, padx=10)

        self.cadastrar = Button(self.entrada1)
        self.cadastrar["text"] = "Cadastrar"
        self.cadastrar["width"] = 10
        self.cadastrar["font"] = self.fontePadrao
        self.cadastrar["command"] = self.cadastrarNome
        self.cadastrar.pack(side=LEFT, padx=10)

        self.sair = Button(master)
        self.aluno = Label(self.widget1, text="Cadastros Alunos")
        self.aluno["font"]= "Arial"
        self.aluno.pack ()
        
        # Saida: Botao para encerrar o programa
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", 10)
        self.sair["width"] = 10
        self.sair["command"] = master.destroy
        self.sair.pack(pady=20)

    def cadastrarNome(self):
        nome = self.nomeEntry.get()
        if nome:  # Verifica se o campo não está vazio
            self.adicionarNome(nome)
            self.bubbleSort()
            print("Nomes ordenados:", self.arr)
            self.nomeEntry.delete(0, END)  # Limpa o campo de entrada após adicionar o nome
            self.salvarNomes()  # Salva os nomes no arquivo de texto

    def adicionarNome(self, nome):
        self.arr.append(nome)

    def bubbleSort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.arr[j].lower() > self.arr[j+1].lower():
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def salvarNomes(self):
        with open("nomes_cadastrados.txt", "w") as file:
            for index, nome in enumerate(self.arr, start=1):
                file.write(nome + "\n")

root = Tk()
root.geometry("800x600")
app = Application(root)
root.mainloop()
