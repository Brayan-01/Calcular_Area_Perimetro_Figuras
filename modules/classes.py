
#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 2.0
# 02/05/2024
# Ficha: 2877795
#Funcionalidad: Calcular el area y perimetro del Circulo, Triangulo y Rectangulo

#*************



#Importamos las librerias que necesitemos,en este caso (libreria para hacer operaciones matematicas mas facilmente) 
import math

#Creamos el primer objeto, en este caso la del rectangulo
class Rectangulo:
    
    #Creamos una funcion inicial para definir el ancho y largo del rectangulo (El self lo usamos en todo momento para referirse al objeto en si)
    def __init__(self,ancho=0, largo=0):
        self.__ancho = ancho
        self.__largo = largo
    
    
    #Esta funcion es para guardar el valor que el usuario vaya a digitar
    def set_ancho(self,value):
        self.__ancho = value 
    
    #Esta funcion es para mostrar el valor que el usuario vaya a digitar
    def get_ancho(self):
        return int(self.__ancho)
    
    #Esta funcion es para guardar el valor que el usuario vaya a digitar
    def set_largo(self,value):
        self.__largo = value 
    
    
    #Esta funcion es para mostrar el valor que el usuario vaya a digitar
    def get_largo(self):
        return int(self.__largo)
    
    
    #Esta funcion es para hacer la operacion matematica de el area del rectangulo
    def area_rectangulo(self):
        return self.get_ancho()*self.get_largo()
    
    
    #Esta funcion es para hacer la operacion matematica del perimetro del rectangulo
    def perimetro_rectangulo(self):
        return self.get_ancho()*2 + self.get_largo()*2
    
    

#Creamos el objeto "Circulo" 
class Circulo():
    
    #Este valor es para el numero pi, y lo hacemos con 6 digitos despues del punto para que sea mas exacto, ademas le agregamos "__" antes del PI para encapsularlo
    __PI = 3.141595
    
    
    #Creamos una funcion inicial para definir el radio del circulo (El self lo usamos en todo momento para referirse al objeto en si)
    def __init__(self,radio=0):
        self.__radio = radio    
    
    #Esta funcion es para guardar el valor que el usuario vaya a digitar
    def set_radio(self,value):
        self.__radio = value
    
    
    #Esta funcion es para mostrar el valor que el usuario vaya a digitar
    def get_radio(self):
        return int(self.__radio)
    
    
    #Creamos esta funcion para calcular el area del circulo
    def area_circulo(self):
        return math.pi*pow(self.get_radio(), 2)
    
    
    #Creamos esta otra funcion para calcular el perimetro de nuestro circulo
    def perimetro_circulo(self):
        return 2*math.pi*self.get_radio()

#Creamos  nuestro objeto, en este caso el Triangulo
class Triangulo:
    
    #Creamos una funcion inicial para definirlso catetos del triangulo (El self lo usamos en todo momento para referirse al objeto en si)
    def __init__(self,cateto_a=0, cateto_b=0, cateto_c=0):
        self.__cateto_a = cateto_a
        self.__cateto_b = cateto_b
        self.__cateto_c = cateto_c
    
    #Esta funcion es para guardar el valor que el usuario vaya a digitar
    def set_cateto_a(self,value):
        self.__cateto_a = value
    
    
    #Esta funcion es para mostrar el valor que el usuario vaya a digitar
    def get_cateto_a(self):
        return self.__cateto_a
    
    
    #Esta funcion es para guardar el valor que el usuario vaya a digitar
    def set_cateto_b(self,value):
        self.__cateto_b = value
    
    
    #Esta funcion es para mostrar el valor que el usuario vaya a digitar
    def get_cateto_b(self):
        return self.__cateto_b
    
    
    #Esta funcion es para guardar el valor que el usuario vaya a digitar
    def set_cateto_c(self,value):
        self.__cateto_c = value
    
    
    #Esta funcion es para mostrar el valor que el usuario vaya a digitar
    def get_cateto_c(self):
        return self.__cateto_c
    
    
    #Creamos esta funcion para calcular el area del triangulo
    def area_triangulo(self):
        s = self.perimetro_triangulo()
        #Retornamos la operacion del area con los catetos
        return math.sqrt(s*(s-self.get_cateto_a())* (s-self.get_cateto_b()) * (s-self.get_cateto_c()))
    
    #Creamos esta funcion para calcular el perimetro del triangulo
    def perimetro_triangulo(self):
        #Retornamos la operacion del perimetros
        return self.get_cateto_a()+self.get_cateto_b()+self.get_cateto_c()