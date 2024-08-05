def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]

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