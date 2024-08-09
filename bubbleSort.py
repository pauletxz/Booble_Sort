# Função lerArquivo: Lê e verifica o arquivo está vazio ou nao 
def lerArquivo(contatos):
    try:
        with open(contatos, 'r') as arquivo:
            linhas = arquivo.readlines()
            return [linha.strip() for linha in linhas]
    except FileNotFoundError:
        print(f"Arquivo {contatos} não encontrado.")
        return []
    
# Funcao bubbleSort: Ordena os nomes da função gerarContatos em ordem alfabetica utilizando o metodo bubble sort 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#  Função escreverArquivo : Reescreve o arquivo contatos.txt, aplicando a função bubbleSort
def escreverArquivo(nome_arquivo, arr):
    with open(nome_arquivo, 'w') as arquivo:
        for linha in arr:
            arquivo.write(linha + "\n")

nome_arquivo = "contatos.txt"
linhas = lerArquivo(nome_arquivo)
linhas_ordenadas = bubbleSort(linhas)
escreverArquivo(nome_arquivo, linhas_ordenadas)