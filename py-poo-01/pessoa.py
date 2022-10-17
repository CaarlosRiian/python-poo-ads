class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self):
        self.idade += 1 
        
    def engordar(self, peso):
        self.peso += peso
        
    def emagrecer(self, peso):
        self.peso -= peso
        
    def crescer(self, altura):
        if self.idade <= 21:
            self.altura += 0.5
        
    def mostrarpessoa(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}kg, Altura: {self.altura}cm.')
        
rian = pessoa('Rian', 19, 85, 168)
rian.mostrarpessoa()
rian.envelhecer()
rian.emagrecer(2)
rian.mostrarpessoa()
    