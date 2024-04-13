
while True :
  nomeHeroi = input('Digite o Nome do Seu Herói : \n')
  expHeroi = input('Digite o XP do Seu Herói: \n')
  nivelHeroi = ''
  try:
    expHeroi = int(expHeroi)
    validador = expHeroi.is_integer()
  except:
    validador = False

  if validador is True:

    if expHeroi < 1000:
      nivelHeroi = 'Ferro'
      print(f'O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}')
      break

    elif expHeroi <= 2000:
      nivelHeroi = 'Bronze'
      print(f'O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}')
      break

    elif expHeroi <= 5000:
      nivelHeroi = 'Prata'
      print(f'O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}')
      break
    elif expHeroi <= 7000:
      nivelHeroi = 'Ouro'
      print(f'O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}')
      break
    elif expHeroi <= 8000:
      nivelHeroi = 'Platina'
      print(f'O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}')
      break
    elif expHeroi <= 9000:
      nivelHeroi = 'Ascendente'
      print(f'O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}')
      break
    elif expHeroi <= 10000:
      nivelHeroi = 'Imortal'
      print(f'O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}')
      break
    else:
      nivelHeroi = 'Radiante'
      print(f'O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}')
      break
  else:
    print('O XP do seu Herói Deve ser um valor Inteiro!')
