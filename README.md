# Estruturas de Dados 1 

## Função Bubble Sort :
Está função junto com a biblioteca Tkinter(Utilzida para criar a interface grafica), cria um campo para o usuario cadastrar um aluno, e utilizado o método Bubble Sort, organiza os alunos cadastrados em ordem alfabetica:

     def bubbleSort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.arr[j].lower() > self.arr[j+1].lower():
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

## Participantes: 

1. Igor Cavalcante Rocha
2. Paulo Henrique Souza Lima

# Passos do Projeto

1. Coletar os nomes digitados pelo usuarios.
2. Armazenar esses nomes em uma lista.
3. Ordenar a lista em ordem alfabética usando Bubble Sort.
4. Exibir a lista ordenada.

## Exemplificando o funcionamento do Bubble Sort 
<p align="center">
 <img src="./imagens/BubbleSort_Exemplo.gif"/>
</p>