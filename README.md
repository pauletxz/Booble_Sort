# Estrutura de Ordenação Bubble Sort

## Desenvolvedores: 

[Igor Cavalcante Rocha](https://github.com/Igor-C-Rocha)
[Paulo Henrique Souza Lima](https://github.com/pauletxz)

## Explicação

## Calculo de complexidade 

# Passos do Projeto

[1. Gerar uma lista telefonica randomicamente.]()
[2. Armazena a lista gerada em arquivo .txt.]()
[3. Ordenar a lista em ordem alfabética usando Bubble Sort.]()
[4. Reeorganiza o arquivo .txt]()

## Função Bubble Sort :

     def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j].lower() > arr[j+1].lower():
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
## Função gerarListaContatos



        def gerarTelefone():
            return f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        


        def gerarContantos():
            contatos = []
                for _ in range(10000):
                     nome = f"{random.choice(primeiros_nomes)} {random.choice(sobrenomes)} {random.choice(segundoSobrenome)}"
            telefone = gerarTelefone()
            contatos.append({'nome': nome, 'telefone': telefone})
        return contatos

        


## Exemplificando o funcionamento do Bubble Sort 

<p align="center">
 <img src="./anexos/BubbleSort_Exemplo.gif"/>
</p>
