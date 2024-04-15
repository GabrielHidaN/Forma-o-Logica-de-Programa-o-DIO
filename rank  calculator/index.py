def calculador_de_Rank(numWin , numDefeat):
  resultadoRank = numWin - numDefeat
  return resultadoRank

numWin = int(input('Digite o número de Vitórias: '))
numDefeat = int(input('Digite o número de derrotas: '))


def main ():
  classification = calculador_de_Rank(numWin= numWin , numDefeat=numDefeat)
  if classification <= 10:
    rank = 'Ferro'
    print(f'O Herói tem de saldo  {classification} vitórias e está no nível de {rank}.' )
  elif classification <= 20:
    rank = 'Bronze'
    print(f'O Herói tem de saldo  {classification} vitórias e está no nível de {rank}.' )
  elif classification <= 50:
    rank = 'Prata'
    print(f'O Herói tem de saldo  {classification} vitórias e está no nível de {rank}.' )
  elif classification <= 80:
    rank = 'Ouro'
    print(f'O Herói tem de saldo  {classification} vitórias e está no nível de {rank}.' )
  elif classification <= 90:
    rank = 'Diamante'
    print(f'O Herói tem de saldo  {classification} vitórias e está no nível de {rank}.' )
  elif classification <= 100:
    rank = 'Lendário'
    print(f'O Herói tem de saldo  {classification} vitórias e está no nível de {rank}.')
  else:
    rank = 'imortal'
    print(f'O Herói tem de saldo  {classification} vitórias e está no nível de {rank}.' )
main()
