## Lista Telefonica Organizada Utilizando BubbleSort

## Descrição

## Passos do Projeto

1. Gerar uma lista telefonica randomicamente.
2. Armazena a lista gerada em arquivo .txt.
3. Ordenar a lista em ordem alfabética usando Bubble Sort.
4. Reeorganiza o arquivo .txt

## Como utilizar 
1. Clone este repositório:
    ```sh
    git clone https://github.com/pauletxz/Booble_Sort
    ```
2. Execute o seguinte comando:
    ```sh
    python main.py
    ```

## Função Bubble Sort
     def bubbleSort(arr): 
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j].lower() > arr[j+1].lower():
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

## Calculo de complexidade 
    
     def bubbleSort(arr): #1 
        n = len(arr) #1 
        for i in range(n): #n+1
            for j in range(0, n-i-1): #(n+1) * (n/2)
                if arr[j].lower() > arr[j+1].lower(): #(n+1) * (n/2) * 1
                    arr[j], arr[j+1] = arr[j+1], arr[j] #(n+1) * (n/2) * 1
        return arr #1
      
 T(n) = 1 + 1+ (n+1) + (n+1)  * (n/2) + (n+1) * (n/2) +  (n+1) * (n/2) * 1
 T(n) = 3n^2/2 + 5n/2 + 3 
 O(n^2)  #Complexidade Quadrática
## Exemplificando o funcionamento do Bubble Sort 

<p align="center">
 <img src="./anexos/BubbleSort_Exemplo.gif"/>
</p>

## Desenvolvedores: 

[Igor Cavalcante Rocha](https://github.com/Igor-C-Rocha)

[Paulo Henrique Souza Lima](https://github.com/pauletxz)