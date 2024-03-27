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




if __name__ == "__main__":
    servico_aluguel = ServicoAluguel()
    carro1 = Carro("Renault", "KWID", 2023)
    carro2 = Carro("BYD", "Dolphin mini", 2024)
    carro3 = Carro("Toyota", "Yaris", 2024)
    servico_aluguel.adicionar_carro(carro1)
    servico_aluguel.adicionar_carro(carro2)
    servico_aluguel.adicionar_carro(carro3)

    carros_disponiveis = servico_aluguel.encontrar_carros_disponiveis()
    print("Carros disponíveis para aluguel:")
    for carro in carros_disponiveis:
        print(f"{carro.marca} {carro.modelo}")

    cliente = Cliente("Gabi", "Gabi_gamer12anos@gmail.com")
    carro_alugado = carros_disponiveis[0]
    print(servico_aluguel.alugar_carro(cliente.nome, carro_alugado))

    pagamento = Pagamento()
    print(pagamento.processar_pagamento(100))

    print(servico_aluguel.devolver_carro(carro_alugado))


