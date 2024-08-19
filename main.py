import listaTelefonica as lt
import bubbleSort as bs
import time

def main():
    # Gerar a lista de contatos e salvar no arquivo 'contatos.txt'
    contatos = lt.gerarContatos()
    lt.gerarArquivo(contatos)
    
    # Ler o arquivo, ordenar os contatos e salvar a lista ordenada no mesmo arquivo
    arquivo = "contatos.txt"
    linhas = bs.lerArquivo(arquivo)
    if linhas:
        # Medir o tempo de execução da função bubbleSort
        tempoInicial = time.time()
        linhasOrdenadas = bs.bubbleSort(linhas)
        tempoFinal = time.time()
        
        # Calcula o tempo total de execução
        tempoTotal = tempoFinal - tempoInicial
        print(f"Tempo de execução do bubbleSort: {tempoTotal} segundos")
        
        bs.escreverArquivo(arquivo, linhasOrdenadas)
        print("Contatos ordenados e salvos em 'contatos.txt'")
    else:
        print("Nenhuma linha foi lida do arquivo.")

if __name__ == "__main__":
    main()
