
#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 1.0
# 02/05/2024
# Ficha: 2877795
#Funcionalidad: Calcular el area y perimetro del Circulo, Triangulo y Rectangulo

#*************





#Importamos las libreria os(para acceder a los archivos del sistema)
import os
from colorama import Fore, Style,Back

#Importamos nuestras funciones que estan en la carpeta modulos
import modules.classes as classes 
import modules.funtions as functions


#Ceramos una funcion para que el usuario solo pueda digitar numeros decimales
def ISN(prompt):
    while True:
        entrada=input(prompt)
        try:
            num = float(entrada)
            return num
        except ValueError:
            print ("Solo se pueden digitar numeros")



#Creamos una funcion principal
def main():
    
    #Importamos las clases que vayamos a usar,en este caso (Rectangulo,Circulo y Triangulo)
    rect1 = classes.Rectangulo()
    circ1 = classes.Circulo()
    tria1 = classes.Triangulo()
    
    
    #Creamos un bucle while para que el usuario mas adelante pueda digitar si quiere volver a iniciar o salir del programa
    while True:
        #Usamos esta funcion para limpiar la pantalla
        os.system('cls')
        
        #Le decimos al usuario que va a empezar con el rectangulo
        print('\n' f"{Fore.LIGHTRED_EX} ***************** RECTANGULO ***************** {Style.RESET_ALL}"'\n')
        
        #Estas son las indicaciones que va a digitar el usuario
        rect1.set_ancho
        
        #Por ejemplo en este input le pedimos al usuario que digite el ancho de su rectangulo y lo guarde en el rect2 del rectangulo
        rect2 = ISN('Digite el ancho del rectangulo: ' )
        rect1.set_ancho(rect2)
        #Este print lo podemos usar para dejar un espacio entre linea
        print(" ")
        
        
        rect1.set_largo
        
        #Aca le pedimos que digite el largo del rectangulo y lo guarde en rect3
        rect3 = ISN('Digite el largo del rectangulo: ')
        rect1.set_largo(rect3)
        #Este print lo podemos usar para dejar un espacio entre linea
        print(" ")
        
        #Le mostramos al usuario que va a seguir con el circulo
        print('\n' f"{Fore.LIGHTRED_EX} ***************** CIRCULO *****************{Style.RESET_ALL} "'\n')
        
        circ1.set_radio
        
        #Le pedimos al usuario que digite el radio de su circulo
        circ = ISN('Digite el radio  del circulo: ')
        circ1.set_radio(circ)
        #Este print lo podemos usar para dejar un espacio entre linea
        print(" ")
        
        #Le mostramos al usuario que va a seguir con el triangulo
        print('\n'f"{Fore.LIGHTRED_EX} ***************** TRIANGULO *****************{Style.RESET_ALL} "'\n')
        
        tria1.set_cateto_a
        
        #Le pedimos al usuario que digite el primer cateto del triangulo
        tria =ISN('Digite el primer cateto del triangulo: ')
        tria1.set_cateto_a(tria)
        #Este print lo podemos usar para dejar un espacio entre linea
        print(" ")
        
        tria1.set_cateto_b
        
        #Le pedimos al usuario que digite el segundo cateto del triangulo
        tria2 = ISN('Digite el segundo cateto del triangulo: ')
        tria1.set_cateto_b(tria2)
        #Este print lo podemos usar para dejar un espacio entre linea
        print(" ")
        
        tria1.set_cateto_c
        
        #Le pedimos al usuario que digite el tercer cateto del triangulo
        tria3 = ISN('Digite el tercer cateto del triangulo: ')
        tria1.set_cateto_c(tria3)
        #Este print lo podemos usar para dejar un espacio entre linea
        print(" ")
        
        functions.imprimir(rect1,circ1,tria1)
        
    #Le preguntamos al usuario si desea ejecutar otra vez este programa o desea salirse
        entrada = input(f"{Fore.LIGHTGREEN_EX}Desea ejecutar nuevamente el programa? Digite S/N: {Style.RESET_ALL}").upper()
        #Este while es por si el usuario digita una tecla que no sea S o N
        while entrada not in['S','N']:
            print('\n'"Solamente puede digitar S/N en mayusculas. ")
            entrada = input('\n'"Elija de nuevo: ").upper()

        #Este if es cuando el usuario digite N le salga un mensaje que diga vuelva pronto y se salga del programa
        if entrada =='N':
            os.system('cls')
            break

#Esta funcion es bastante importante en cualquier programa ya que verfifica que la funcion es la principal para ejecutarla, si no pues no la ejecuta
if __name__ =='__main__':
    main()
