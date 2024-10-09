class Automovil: 

    
    def __init__(self, color, marca, aceleracion, velocidad, ruedas, modelo , año):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad
        self.ruedas = 4
        self.__modelo = modelo
        self._año = año

    def get_color(self):
        return self.color

    def get_marca(self):
        return self.marca

    def get_aceleracion(self):
        return self.aceleracion
    
    def get_velocidad(self):
        return self.velocidad
    
    def get_ruedas(self):
        return self.ruedas

    def set_color(self, color):
        self.color = color
    
    def set_marca(self, marca):
        self.marca = marca
    
    def set_aceleracion(self, aceleracion):
        self.aceleracion = aceleracion
    
    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
    
    def set_modelo(self, marca):
        self.__modelo = marca

    def get_modelo(self):
        return self.__modelo
    
    def set_año(self,año):
        self._año = año
    
    def get_año(self):
        return self._año

    def datos(self):

        cantidad_ruedas = self.ruedas

        print ("la cantidad de ruedas es de: "+ str(cantidad_ruedas))

        return "el automovil tiene esta cantidad de ruedas: "+ str(self.ruedas)
        


    def __str__(self):
        return f"El automovil es de color: {self.color} y la marca es {self.marca}"

    def mostrar_ruedas_aceleracion(self):
        print(f"La cantidad de ruedas es de: {self.ruedas} y la aceleracion es {self.aceleracion}")
    
    def acelera(self):
        print(f"La velocidad antes de acelerar: {self.velocidad}")
        velocidad = self.velocidad + self.aceleracion
        self.velocidad = velocidad
        print(f"La velocidad actual es {self.velocidad}")
        
    def frenar(self):
        
        print(f"La velocidad antes de frenar: {self.velocidad}")
        frenado = self.velocidad - self.aceleracion
        self.velocidad = frenado
        print(f"La velocidad actual: {self.velocidad}")

        

automovil_nuevo = Automovil("rojo", "toyota", 12, 120,4,"asd",1980)
automovil_dos = Automovil("Verde","toyota",13,140,4,"asd",2000)

print(automovil_nuevo) 
automovil_nuevo.mostrar_ruedas_aceleracion()


automovil_dos.acelera()

automovil_dos.frenar()
automovil_dos.frenar()
automovil_dos.frenar()
automovil_dos.frenar()

print(automovil_dos.ruedas) # Se accede ya que no es privado

print("El modelo es: "+automovil_dos.get_modelo())

automovil_dos.set_modelo("Nueva_marca")

print("El nuevo modelo es: "+automovil_dos.get_modelo())


automovil_dos.datos()
