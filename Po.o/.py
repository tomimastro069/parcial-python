class personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):

        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.aguante = fuerza*vida

    def atributos(self):

        print(self.nombre, ":", sep="")

        print("-Fuerza: ", self.fuerza)

        print("-inteligencia: ", self.inteligencia)

        print("-defensa: ", self.defensa)

        print("-vida: ", self.vida)

        print("-aguante: ", self.aguante)

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa += defensa
        self.aguante = self.fuerza * self.vida
    def esta_vivo(self):
        return self.vida > 0
    def morir(self):
        self.vida = 0
        print("--------------------")
        print(self.nombre, "ha muerto")
        print("--------------------")
    def revivir(self):
        self.vida = 100
        print(self.nombre, "ha revivido")
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre,  "ha realizado ", daño, " puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida actual de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class guerrero(personaje):
        def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada= 5 ):
            super().__init__( nombre, fuerza, inteligencia, defensa, vida)
            self.espada = espada
        def cambiar_arma(self):
            opcion = int(input("Elige un arma:  \n | 1 acero valyrio, daño 8 \n | 2 maza , daño 10 \n"))
            if opcion == 1:
                self.espada = 8
            elif opcion == 2:
                self.espada = 10
            else:
                print("Numero incorrecto")
        def atributos(self):
            super().atributos()
            print("-Espada", self.espada)
        def daño(self, enemigo):
            return self.fuerza*self.espada - enemigo.defensa



def main():
    
    guts = guerrero("guts", 10, 10,10,1000)
    mi_personaje = personaje("tomas", 10,2,8,100)
    mi_enemigo = personaje("enemigo",4,2,10,100)


    mi_personaje.atributos()
    print("--------------------")
    mi_personaje.subir_nivel(1,2,4)
    mi_personaje.atributos()
    print("--------------------")
    mi_personaje.morir()
    mi_personaje.revivir()
    print("--------------------")
    mi_personaje.atributos()
    print("--------------------")
    mi_personaje.atacar(mi_enemigo)
    mi_enemigo.atributos()
    guts.atributos()
    guts.cambiar_arma()
    guts.atributos()
    guts.atacar(mi_enemigo)
    mi_enemigo.atributos()
if __name__ == "__main__":
    main()

 