import random

# Listas de nomes comuns
primeiros_nomes = ['Antonio','Marco','Batista','Gabriel','Nestor','Carlos', 'Ana', 'Bruno', 'Fernanda', 'Gustavo', 'Juliana', 'Ricardo', 'Mariana', 'Tiago', 'Beatriz', 'Joana', 'Paulo', 'Romario','Fernando', 'Peter', 'Jordana', 'Kayc', 'Neto','Kayo','Sofia', 'Isabela', 'Lara', 'Miguel', 'Arthur', 'Helena', 'Alice', 'Laura', 'Valentina', 'Enzo', 'Henrique', 'Eduardo', 'Camila', 'Leticia', 'Samuel', 'Daniel', 'Leonardo','Vitor', 'Marcos', 'Renata', 'Patricia', 'Thiago', 'Aline', 'Roberto', 'Vanessa', 'Claudia', 'Felipe', 'André', 'Carla', 'Rodrigo', 'Marta', 'João', 'Elisa', 'Bruna', 'Diego', 'Mariana', 'Fábio']
sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Almeida', 'Costa', 'Gomes', 'Martins', 'Maia', 'Solimões', 'Vasconcelos', 'Machado', 'Rocha', 'Pedra', 'Barbosa','Piton', 'Praxedes', 'Figueiredo', 'Freitas', 'Guimarães', 'Vieira', 'Monteiro', 'Barros', 'Cardoso', 'Farias', 'Melo', 'Pinto', 'Ramos', 'Sousa', 'Pereira', 'Nunes', 'Mendes', 'Teixeira', 'Carvalho', 'Azevedo', 'Moura', 'Vieira']
segundoSobrenome = ['Olievira', 'Paiva', 'Lima', 'Ribeiro', 'Rêgo', 'Tavares', 'Bessa', 'Santana', 'Castro', 'Agostini', 'Antonelli', 'Diniz', 'Medina', 'Alonso', 'Miller', 'Taylor', 'Fagundes','Diogenes','Leite', 'Morais', 'Moura']

# Função para gerar um número de telefone aleatório
def gerarTelefone():
    return f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

# Gerar 2000 contatos aleatórios
contatos = []
for _ in range(10000):
    nome = f"{random.choice(primeiros_nomes)} {random.choice(sobrenomes)} {random.choice(segundoSobrenome)}"
    telefone = gerarTelefone()
    contatos.append({'nome': nome, 'telefone': telefone})

# Salvar os contatos em um arquivo .txt
with open('contatos.txt', 'w') as arquivo:
    for contato in contatos:
        arquivo.write(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}\n")

print("Contatos salvos em 'contatos.txt'")
