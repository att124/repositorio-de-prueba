from Automovil import Automovil



class AutomovilVolador(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad,ruedas):   
        super().__init__(color, marca, aceleracion, velocidad,ruedas)
        self.esta_volando = True
        self.ruedas = 6

    def volar(self):
        if self.esta_volando == True:
        
            print(f"El automovil ya se encuentra volando")
    
        else:
            self.esta_volando = False

            print(f"El automovil comienza a volvar")

    def aterrizar(self):
        if self.esta_volando == False:

            print(f"El automovil ya se encuentra en el suelo")
        
        else:
            print(f"El automovil comienza a aterrizar")

            self.esta_volando = False
        

automovil_volador = AutomovilVolador("Rojo","toyota",12,100,6)

automovil_volador.aterrizar()

automovil_volador.frenar()