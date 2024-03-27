# Princípio de Responsabilidade Única
class Carro:
    def __init__(self, marca, modelo, ano, disponivel=True):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.disponivel = disponivel

class ServicoAluguel:
    def __init__(self):
        self.carros = []

    # Princípio de Aberto/Fechado
    def adicionar_carro(self, carro):
        self.carros.append(carro)

    # Princípio de Substituição de Liskov
    def encontrar_carros_disponiveis(self):
        return [carro for carro in self.carros if carro.disponivel]

    # Princípio de Segregação de Interfaces
    def alugar_carro(self, cliente, carro):
        carro.disponivel = False
        return f"Carro {carro.marca} {carro.modelo} alugado para {cliente}"

    def devolver_carro(self, carro):
        carro.disponivel = True
        return f"Carro {carro.marca} {carro.modelo} devolvido"

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Pagamento:
    # Princípio de Inversão de Dependência e a priorização de composição sobre herança
    def processar_pagamento(self, valor):
        return f"Pagamento de R${valor} realizado com sucesso"




def main():
    servico_aluguel = ServicoAluguel()

    # Adicionando carros pré-definidos
    carro1 = Carro("Renault", "KWID", 2023)
    carro2 = Carro("BYD", "Dolphin mini", 2024)
    carro3 = Carro("Toyota", "Yaris", 2024)
    servico_aluguel.adicionar_carro(carro1)
    servico_aluguel.adicionar_carro(carro2)
    servico_aluguel.adicionar_carro(carro3)

    while True:
        print("\n===== Menu Principal =====")
        print("1. Adicionar novo registro de carro")
        print("2. Listar carros disponíveis para aluguel")
        print("3. Cadastrar novo cliente")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            ano = int(input("Digite o ano do carro: "))
            novo_carro = Carro(marca, modelo, ano)
            servico_aluguel.adicionar_carro(novo_carro)
            print("Registro de carro adicionado com sucesso!")

        elif opcao == "2":
            carros_disponiveis = servico_aluguel.encontrar_carros_disponiveis()
            print("\nCarros disponíveis para aluguel:")
            for idx, carro in enumerate(carros_disponiveis, start=1):
                print(f"{idx}. {carro.marca} {carro.modelo} ({carro.ano})")

        elif opcao == "3":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            novo_cliente = Cliente(nome, email)
            print(f"Cliente {novo_cliente.nome} cadastrado com sucesso!")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

