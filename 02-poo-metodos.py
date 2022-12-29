#   Metodos de classe e estático
#   Diferenças:
#   Metodo de Classe recebe o primeiro parametro que aponta pra classe, o estático não
#   Estático não tem referencia para ser acessada ou alterada (Usado em metodos utilitários)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod        #   Desse modo temos uma referencia direta para a classe para não instanciar 2 pessoas
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 9, 7, "Gabriel")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

#   Outra forma de aplicação, funcional
#   print(p.e_maior_idade(p.idade))