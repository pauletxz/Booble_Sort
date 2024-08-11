import listaTelefonica as lt
import bubbleSort as bs

def main():
    # Gerar a lista de contatos e salvar no arquivo 'contatos.txt'
    contatos = lt.gerarContatos()
    lt.gerarArquivo(contatos)
    
    # Ler o arquivo, ordenar os contatos e salvar a lista ordenada no mesmo arquivo
    arquivo = "contatos.txt"
    linhas = bs.lerArquivo(arquivo)
    if linhas:
        linhasOrdenadas = bs.bubbleSort(linhas)
        bs.escreverArquivo(arquivo, linhasOrdenadas)
        print("Contatos ordenados e salvos em 'contatos.txt'")
    else:
        print("Nenhuma linha foi lida do arquivo.")

if __name__ == "__main__":
    main()
