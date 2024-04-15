const calculador_de_rank = (numWin , numDefeat)=>{
  resultadoRank = numWin - numDefeat
  return resultadoRank
}

let numWin = 30
let numDefeat = 5

const main = ()=>{
  let classification = calculador_de_rank(numWin , numDefeat)

  if (classification <= 10){
    let rank = 'ferro'
    console.log(`O Herói tem de saldo  ${classification} vitórias e está no nível de ${rank}.`)
  }

  else if (classification <= 20){
    let rank = 'Bronze'
    console.log(`O Herói tem de saldo  ${classification} vitórias e está no nível de ${rank}.`)
  }

  else if (classification <= 50){
    let rank = 'Prata'
    console.log(`O Herói tem de saldo  ${classification} vitórias e está no nível de ${rank}.`)
  }

  else if (classification <= 80){
    let rank = 'Ouro'
    console.log(`O Herói tem de saldo  ${classification} vitórias e está no nível de ${rank}.`)
  }

  else if (classification <= 90){
    let rank = 'Diamante'
    console.log(`O Herói tem de saldo  ${classification} vitórias e está no nível de ${rank}.`)
  }

  else if (classification <= 100){
    let rank = 'Lendário'
    console.log(`O Herói tem de saldo  ${classification} vitórias e está no nível de ${rank}.`)
  }

  else {
    let rank = 'Imortal'
    console.log(`O Herói tem de saldo  ${classification} vitórias e está no nível de ${rank}.`)
  }
}

main()
