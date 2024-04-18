#jogo Pedra, papel e tesoura


import random

def jogo():
  opcoes = ['pedra', 'papel', 'tesoura'] 

  escolha_do_usuario = input('Escolha uma opçao: pedra, papel ou tesoura?')
  escolha_computador = random.choice(opcoes) #opção aleatória do computador 

  print("\n você escolheu:" + escolha_do_usuario)
  print("\n o computador escolheu: " + escolha_computador)

  if escolha_do_usuario == escolha_computador:
        print("Empate!")
  elif (escolha_do_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_do_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_do_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("\n Você ganhou!")
  else:
         print("\n Você perdeu!")

jogo() # Aqui está sendo chamada função do jogo
