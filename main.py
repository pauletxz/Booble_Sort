import geradorListaTelefonica
import bubbleSort

def main():
    # Passo 1: Gerar a lista de contatos e salvar no arquivo 'contatos.txt'
    contatos = geradorListaTelefonica.gerarContatos()
    geradorListaTelefonica.gerarArquivo(contatos)
    
    # Passo 2: Ler o arquivo, ordenar os contatos e salvar a lista ordenada no mesmo arquivo
    nome_arquivo = "contatos.txt"
    linhas = bubbleSort.lerArquivo(nome_arquivo)
    print(f"Linhas lidas: {len(linhas)}")  # Verifica a quantidade de linhas lidas do arquivo
    if linhas:
        linhas_ordenadas = bubbleSort.bubbleSort(linhas)
        bubbleSort.escreverArquivo(nome_arquivo, linhas_ordenadas)
        print("Contatos ordenados e salvos em 'contatos.txt'")
    else:
        print("Nenhuma linha foi lida do arquivo.")

if __name__ == "__main__":
    main()
