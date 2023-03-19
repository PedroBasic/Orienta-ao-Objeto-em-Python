"""

Progarmação orientada a Objeto e Python

Classe, objetos. atribustos, metodos

"""
#Utilizamos a palavra reservada class

# Em Python geralmente utilizamos a sintaxe  PascalCase para definir os nomes
# das nossas classes

class Pokemon:
    
    # O método __init__ e o método iniciador da classe (alguns aceitam o método construtor).
    # O método __init__ e chamdo semre que instanciamos uma class
    # Os método funcionam como funções comns em Python, a diferença é que sendo um método de instâncoa da class 
    # les SEMPRE recebem como primeiro argumento o self
    def __init__(self, name, type, health):
        
        self._name = name
        self._type = type
        self._health = health

    def attack(self):
        print(f"{self._name} Atacaou !!")

    def dodge(self):
        print(f"{self._name} Deviou !! ")

    def evolve(self):
        print(f"{self._name} evoluiu !! ")

if __name__ == "__main__":
    
    # A linha abaixo instancia 
    pikachu = Pokemon(name="Pikachu", type="Eletrico", health=70)
    print(pikachu)

    # Dessa maneira chamamos os metodos

    pikachu.attack()
    pikachu.evolve()