import random 
import bancoNomes  # Importa o módulo com as listas de nomes e sobrenomes

# Função para gerar um número de telefone aleatório
def gerarTelefone():
    numeros = f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    return numeros

# Função para gerar contatos aleatórios com base no banco de nomes
def gerarContatos():
    contatos = []
    for _ in range(1000):
        nome = f"{random.choice(bancoNomes.primeiroNome)} {random.choice(bancoNomes.sobrenome)} {random.choice(bancoNomes.segundoSobrenome)}"
        telefone = gerarTelefone()
        contatos.append({'nome': nome, 'telefone': telefone})
    return contatos

# Função gerarArquivo: gera o arquivo "contatos.txt" com nomes e números telefônicos aleatórios
def gerarArquivo(contatos):
    with open('contatos.txt', 'w') as arquivo:
        for contato in contatos:
            arquivo.write(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}\n")

# Gerar contatos e salvar em arquivo
contatos = gerarContatos()  # Gera contatos com base nas listas do módulo bancoNomes
gerarArquivo(contatos)  # Salva os contatos em um arquivo

print("Contatos salvos em 'contatos.txt'")