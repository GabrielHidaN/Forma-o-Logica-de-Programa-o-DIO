class classDeUmJogo{

  constructor(nome , idade , tipo){
    this.nome = nome;
    this.idade = idade;
    this.tipo = tipo;
  }

  atacar(){
    if (this.tipo == 'mago'){
      var tipoDeAtaque = "Magia"
      var atacando = `O ${this.tipo} atacou usando ${tipoDeAtaque}`
    }
    else if (this.tipo == 'monge'){
      var tipoDeAtaque = "Artes marciais"
      var atacando = `O ${this.tipo} atacou usando ${tipoDeAtaque}`
    }
    else if (this.tipo == 'guerreiro'){
      var tipoDeAtaque = "Espada"
      var atacando = `O ${this.tipo} atacou usando ${tipoDeAtaque}`
    }
    else if (this.tipo == 'ninja'){
      var tipoDeAtaque = "Shuriken"
      var atacando = `O ${this.tipo} atacou usando ${tipoDeAtaque}`
    }
    return atacando
  }


}
let personagem = new classDeUmJogo('Riuk', 20 , 'mago')

let ataque = personagem.atacar()
console.log(ataque)
