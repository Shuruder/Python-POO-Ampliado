#   Interface define o que uma classe deve fazer/implementar e não como
#   Porém no python não temos uma palavra para Interface, porém podemos abstrair o conceito pelas classes abstratas

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod     #   Essa invocação define o metodo como abstrato
    def desligar(self): #   Obrigando todos os herdeiros da classe a implementar e seguir o padrão dando maior segurança a implementação do código
        pass

    @property
    @abstractproperty
    def marca(self):    #   Também é possivel forçar propriedades abstratas
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)