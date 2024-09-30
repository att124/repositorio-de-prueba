class Automovil: 

    ruedas = 4

    def __init__(self, color, marca, aceleracion, velocidad, ruedas):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad
        self.ruedas = ruedas

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
    

automovil_nuevo = Automovil("rojo", "toyota", 12, 120,4)
automovil_dos = Automovil("Verde","toyota",13,140,4)

print(automovil_nuevo) 
automovil_nuevo.mostrar_ruedas_aceleracion()

print()

automovil_dos.acelera()

automovil_dos.frenar()
automovil_dos.frenar()
automovil_dos.frenar()
automovil_dos.frenar()