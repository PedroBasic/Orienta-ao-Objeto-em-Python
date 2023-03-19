"""
Polimorfismo 

Polimorfismo significa "muitas formas", ou seja, uma função ou método que pode ser 
chamados de diferente maeniras ou possui diferentes coportamentos

"""
class Funcionario:
    
    def __init__(self, nome,):
        self._nome = nome

    def calcular_salario(self):
        # A linha abaixo força as classes filhas e implementam esse método
        raise NotImplementedError

class FuncionarioCLT:
    
    def __init__(self, nome, salario):
        self._salario = salario
        super().__init__(nome)

    def calcular_salario(self):
        return self._salario

class FuncionarioTerceirizado:
    
    def __init__(self, nome, valor_hora, qtd_horas):
        self._valor_hora = valor_hora
        self._qtd_horas = qtd_horas
        super().__init__(nome)

        def calcular_salario(self):
            return self._qtd_horas * valor_hora

class FuncionarioComissionario:
    

    def __init__(self, nome, valor_vendas, porcentagem_comissao):
        self._valor_vendas = valor_vendas
        self._porcentagem_comissao = porcentagem_comissao
        super().__init__(nome)

        def calcular_salario(self):
            return self._valor_vendas * (self._porcentagem_comissao / 100)

if __name__ == "__main__":
    pass
