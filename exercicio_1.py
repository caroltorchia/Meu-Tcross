# 1 Crie uma classe que modele o objeto "carro". ok 

class Meu_Tcross: 
    def __init__(self):
        self.ligada = False # 2 Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade. ok 
        self.cor = 'black'
        self.modelo = 'suv'
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 200
     

    def ligar(self):
        self.ligada = True # 3 Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.ok 

    
    def desligar(self):
        self.ligada = False
    
    def mudar_velocidade_para_cima(self):
        if not self.ligada:
            return

        if self.velocidade < self.velocidade_max:
            self.velocidade += 1

    def mudar_velocidade_para_baixo(self):
        if not self.ligada:
            return

        if self.velocidade > self.velocidade_min:
            self.velocidade -= 1
    

    def __str__(self) -> str:
        return f'Meu_Tcross - ligada {self.ligada} - velocidade {self.velocidade}'


carro_garagem = Meu_Tcross() # 4 Crie uma instância da classe carro.
carro_rua = Meu_Tcross()

print(carro_garagem)

carro_garagem.ligar()
print('carro foi ligado!', carro_garagem.ligada)

#5 Faça o carro "andar" utilizando os métodos da sua classe.
for _ in range(5):
    carro_garagem.mudar_velocidade_para_cima()
    print(carro_garagem)


#6 Faça o carro "parar" utilizando os métodos da sua classe.

for _ in range(carro_garagem.velocidade):
    carro_garagem.mudar_velocidade_para_baixo()
    print(carro_garagem)
