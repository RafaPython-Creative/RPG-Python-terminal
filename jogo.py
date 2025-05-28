import random
#Personagem: classe mãe
#heroi: controlado pelo usuario
#inimigo: adversário do usuario

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}, Vida: {self.get_vida()}, Nível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() *2, self.get_nivel() *4)  # Dano aleatório baseado no nível
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} ataca {alvo.get_nome()} causando {dano} de dano!")

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()},\nHabilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 10)  # Dano especial aleatório
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usa {self.get_habilidade()} em {alvo.get_nome()} causando {dano} de dano!")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()},\nTipo: {self.get_tipo()}"

class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Ragnar", vida=100, nivel=40, habilidade="Espada Flamejante")
        self.inimigo = Inimigo(nome="Orc", vida=80, nivel=1, tipo="Guerreiro")

    def iniciar_batalha(self):
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1 - ataque normal, 2 - ataque especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
               self.heroi.ataque_especial(self.inimigo)
            
            else:
                print("Escolha inválida!")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print(f"{self.heroi.get_nome()} venceu a batalha!")
        else:
            print(f"{self.inimigo.get_nome()} venceu a batalha!")

jogo = Jogo()
jogo.iniciar_batalha()
