from modelo import Modelo_historia
import pygame
import time

# Inicializar o Pygame
pygame.init()

# Definições do personagem
personagem = {
    "nome": "Alex",
    "cargo": "Estagiário",
    "nivel": 1,
    "xp": 0,
    "carisma": 2,
    "inteligencia": 2,
    "resistencia_estresse": 2,
    "saude_mental": 2,
    "estresse": 0
}
with open('./prompt_historia.txt', 'r', encoding='utf-8') as arquivo:
    prompt = arquivo.read()

        
mestre = Modelo_historia("SUA-CHAVE-API")
historia = mestre.comecar_historia(prompt)
print(historia)

with open('./prompt_jogo.txt', 'r', encoding='utf-8') as arquivo:
    prompt = arquivo.read()
    
mestre_auxiliar = Modelo_historia("SUA-CHAVE-API")
informacoes = mestre_auxiliar.comecar_historia(prompt + historia)
print(informacoes)

# Loop principal do jogo
rodando = True
while rodando:
    historia = mestre.set_mensagem(input("Digite sua escolha: "))
    #time.sleep(20)
    informacoes = mestre_auxiliar.set_mensagem(historia)
    print(historia)
    print(informacoes)

pygame.quit()
