"""
Encapsulamento

É o cenoseito onde "escondemos" informações interna do objeto, e definimos as "interfaces"
púlicas, onde o usuario terá acesso

"""

class ContaBancaria:

    def __init__(self, nome, saldo=0):
        
        #Criamos dois atribustos privados da classe

        self._nome = nome
        self._saldo = saldo


    def mostra_saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return valor

        print("Você não possui saldo disponivel ")


if __name__ == "__main__":
    
    conta_corrente_viacredi = ContaBancaria(nome="ViaCredii", saldo=1000)

    print(conta_corrente_viacredi.mostra_saldo())
    conta_corrente_viacredi.depositar(100)

    print(conta_corrente_viacredi.mostra_saldo())
    conta_corrente_viacredi.depositar(100)

    print(conta_corrente_viacredi.mostra_saldo())
    conta_corrente_viacredi.sacar(1200)
    ''
    print(conta_corrente_viacredi.mostra_saldo())

