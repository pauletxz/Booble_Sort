def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            return [linha.strip() for linha in linhas]
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return []

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def escrever_arquivo(nome_arquivo, arr):
    with open(nome_arquivo, 'w') as arquivo:
        for linha in arr:
            arquivo.write(linha + "\n")

nome_arquivo = "contatos.txt"
linhas = ler_arquivo(nome_arquivo)
linhas_ordenadas = bubbleSort(linhas)
escrever_arquivo(nome_arquivo, linhas_ordenadas)