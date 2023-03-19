"""
Herança 

Henrança acontece quando uma classe herda atributo e caracteristicas de uma classe mãe 
ou superclasse

"""
from excecoes import SaldoInsufucienteError

class ContaFinanceira:

    def __init__(self, nome, saldo=0):
        self._nome = nome
        self._saldo = saldo

    def mostra_saldo(self):
        print(f"O saldo atual da conta '{self._nome}' e de {self._saldo:.2f} ")

    def sacar(self):
        raise NotImplementedError

    def depositar(self):
        raise NotImplementedError
    
    def transferir(self):
        raise NotImplementedError

# Quando queremos indicar a classe a qual sera herda, idicamos o seu nome entre
# parentesis
# No caso abaixo, ndiamos que a classe ContaCorrente herda da ContaFinanceira

class ContaCorrente(ContaFinanceira):
        
        def sacar(self, valor):

            if valor <= self._saldo:
                self._saldo -= valor
                return valor

            else:
                raise SaldoInsufucienteError

        def depositar(self, valor):
            self._saldo += valor

class ContaInvestimento(ContaFinanceira):

    def __init__(self, nome, saldo=0, taxa= 0.01):
        self._taxa = taxa
        super().__init__(nome=nome, saldo=saldo)

    def render(self):
        self._saldo = self._saldo + self._saldo * self._taxa

        

if __name__ == "__main__":

    conta = ContaCorrente(nome="Santander", saldo=5000)
    conta.sacar(3000)
    conta.mostra_saldo()

    conta_poupanca = ContaInvestimento('Poupança Caixa', saldo=1000)
    conta_poupanca.mostra_saldo()
    conta_poupanca.render()
    conta_poupanca.mostra_saldo()
