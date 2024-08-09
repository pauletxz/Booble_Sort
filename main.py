import bubbleSort as bs
import geradorListaTelefonica as gl

def main():
    gl.gerarTelefone()
    gl.gerarContantos()
    lista = gl.gerarArquivo()
    bs.bubbleSort(lista)
    nome_arquivo = "contatos.txt"
    linhas = bs.lerArquivo(nome_arquivo)
    linhas_ordenadas = bs.bubbleSort(linhas)
    bs.escreverArquivo(nome_arquivo, linhas_ordenadas)

if __name__ == "__main__":
    main()