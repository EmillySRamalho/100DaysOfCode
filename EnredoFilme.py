# GERADOR DE FILMES

import random

#Listas de filmes 

def gerar_genero():
  generos = [
      "Ação", "Comédia", "Drama", "Ficção científica", "Terror", "Romance", 
      "Animação", "Suspense", "Documentário", "Fantasia", "Aventura", 
      "Musical", "Crime", "Mistério", "Histórico", "Biografia", "Faroeste"
  ]
  return random.choice(generos)


def gerar_titulo(genero):
  adjetivos = ["A misteriosa", "O enigmático", "O inesperado", "O fascinante", "O incrível", "A implacável", "A inesquecível", "A intrigante", "A verdadeira", "A séria", "A bonita", "A alta", "A rica", "A maravilhosa", "A incrível", "Segredos", "Misterioso", "O poderoso", "A sombria", "A desafiadora", "A épica"]
  substantivos = ["da fantasia", "da aventura", "do mistério", "Perdido nas estrelas", "Perdidos no céu", "da vida", "da morte", "da esperança", "da felicidade", "do destino", "dos sonhos", "do perigo", "do desconhecido", "das sombras", "do amor", "da guerra", "da redenção", "da glória", "da destruição", "da eternidade"]
  return f"{random.choice(adjetivos)} {genero} {random.choice(substantivos)}"



def gerar_personagens():
  personagens = [
      "Nathan Smith", "Emma Johnson", "Liam Williams", "Olivia Brown", "Ethan Jones",
      "Sophia Davis", "Mason Taylor", "Ava Clark", "Logan Anderson", "Mia Martinez",
      "Lucas Garcia", "Isabel Miller", "Noah Wilson", "Emily Moore", "Aiden Taylor",
      "Madison Hall", "Michael Thompson", "Chloe Harris", "Daniel Rodriguez", "Ella Young"
  ]
  return random.choice(personagens)


def gerar_cenários ():
  cenarios = ["na praia", "no campo", "na floresta", "na cidade", "no deserto", "no mar", "na ilha", "na escola", "no cinema", "no hospital", "no parque", "na montanha", "no escritório", "na estação de metrô", "no restaurante", "na cafeteria", "no mercado", "na estação de trem", "no aeroporto", "na rua movimentada"]
  return random.choice(cenarios)  

def gerar_resumo(personagens, cenario, genero):
  acao = [
      f"No {cenario}, {personagens} embarca em uma jornada épica para encontrar um tesouro perdido.",
      f"Durante uma viagem à {cenario}, {personagens} descobre um segredo antigo que pode mudar o destino do mundo.",
      f"Enquanto explora {cenario}, {personagens} é surpreendido por uma tempestade que o deixa preso e lutando pela sobrevivência.",
      f"No coração da {cenario}, {personagens} se depara com uma criatura lendária que o desafia a uma batalha de proporções épicas.",
      f"Em meio à agitação da {cenario}, {personagens} se encontra no centro de uma conspiração perigosa que ameaça desestabilizar a ordem mundial.",
      f"Na pacata cidade de {cenario}, {personagens} descobre segredos sombrios que o levam a uma investigação cheia de reviravoltas.",
      f"Enquanto explora {cenario}, {personagens} encontra uma civilização perdida há muito tempo, onde segredos antigos são revelados.",
      f"No meio da {cenario}, {personagens} se vê envolvido em uma guerra entre facções rivais, lutando pela paz e pela justiça.",
      f"Em uma mansão assombrada na {cenario}, {personagens} enfrenta seus medos mais profundos enquanto luta para desvendar o mistério por trás das assombrações.",
      f"Em uma jornada pelo {cenario}, {personagens} descobre a verdade sobre seu passado e seu destino entrelaçado com o futuro da humanidade.",
      f"No {cenario}, {personagens} encontra um artefato antigo que concede poderes além da imaginação.",
      f"Durante uma visita à {cenario}, {personagens} se depara com um portal misterioso para outra dimensão.",
      f"Enquanto navega pelos perigos do {cenario}, {personagens} faz aliados improváveis para derrotar um inimigo comum.",
      f"No {cenario}, {personagens} descobre um diário antigo que revela segredos há muito esquecidos.",
      f"Em uma jornada pelo {cenario}, {personagens} enfrenta desafios inimagináveis para salvar seu mundo da destruição iminente.",
      f"No {cenario}, {personagens} se encontra no centro de uma guerra entre raças alienígenas em busca de um recurso valioso.",
      f"Em meio à paisagem desolada do {cenario}, {personagens} encontra uma comunidade oculta que desafia as leis da sociedade.",
      f"No {cenario}, {personagens} se torna o líder improvável de uma revolução contra um governo corrupto.",
      f"Durante uma expedição ao {cenario}, {personagens} descobre uma civilização subaquática perdida há séculos."
  ]
  return random.choice(acao)



genero = gerar_genero()
titulo = gerar_titulo(genero)
personagens = gerar_personagens()
cenario = gerar_cenários()
resumo = gerar_resumo(personagens, cenario, genero)

print("Gênero do filme:", genero)
print ("Título do filme:", titulo)
print("Personagens principais:", personagens)
print ("Cenário:", cenario)
print("Resumo:", resumo)