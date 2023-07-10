import math
#Se crea una clase Trig, que almacena el valor de pi, y almacena el seno, coseno y tangente de pi.
class Trig:
    
    def __init__(self):
        self.pi = math.pi

    def sin_pi(self):
        return math.sin(self.pi)
    
    def cos_pi(self):
        return math.cos(self.pi)
    
    def tan_pi(self):
        return math.tan(self.pi)
#
# Crear una instancia de la clase Trig
#trig_instance = Trig()

# Asegurar que el codigo funcione
#print("seno de pi:", trig_instance.sin_pi())
#print(" coseno de pi:", trig_instance.cos_pi())