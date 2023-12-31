import random

nomes = ['Ana', 'Joao', 'Maria', 'Pedro', 'Julia', 'Lucas', 'Beatriz', 'Guilherme', 'Isabela', 'Matheus',
         'Sophia', 'Rafael', 'Laura', 'Gabriel', 'Manuela', 'Leonardo', 'Valentina', 'Felipe', 'Luiza', 'Enzo']

sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Almeida", "Pereira", "Gomes", "Costa",
              "Carvalho", "Martins", "Ribeiro", "Lima", "Araujo", "Cruz", "Mendes", "Nascimento", "Fernandes", "Cardoso"]

# Gerar uma idade aleatória entre 16 e 69 anos
def gerar_idade():
    return random.randint(16, 69)
#Gerar uma altura aleatória entre 1,50 e 2,00m
def gerar_altura():
    return random.uniform(1.50, 2.00)
# Função principal para criar o arquivo com N nomes completos e idades aleatórias
def criar_arquivo_com_dados_aleatorios(N, nome_do_arquivo="nome_completo_idade_altura.txt"):
    with open(nome_do_arquivo, 'w') as arquivo:
        for _ in range(N):
            nome = random.choice(nomes)
            sobrenome = random.choice(sobrenomes)
            idade = gerar_idade()
            altura = round(gerar_altura(), 2)
            nome_completo = f"{nome} {sobrenome}"
            linha = f"{nome_completo},{idade},{altura}m\n"
            arquivo.write(linha)

if __name__ == "__main__":
    try:
        N = int(input("Digite o número de nomes a serem gerados: "))
        criar_arquivo_com_dados_aleatorios(N)
        print(f"{N} nomes completos e idades aleatórias foram gerados e escritos em 'nome_completo_idade.txt'.")
    except ValueError:
        print("Por favor, insira um número válido para N.")
