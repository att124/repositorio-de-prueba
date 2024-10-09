from Automovil import Automovil



class AutomovilVolador(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad,ruedas,modelo , año):   
        super().__init__(color, marca, aceleracion, velocidad,ruedas,modelo , año)
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

    def datos(self):
        
        ruedas = self.ruedas

        return (f"El automovil es volador y sus ruedas: {ruedas}")
    

    
        

automovil_volador = AutomovilVolador("Rojo","toyota",12,100,6,"asd",123)

automovil_volador.aterrizar()

automovil_volador.frenar()