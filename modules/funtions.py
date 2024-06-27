#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 2.0
# 02/05/2024
# Ficha: 2877795
#Funcionalidad: Calcular el area y perimetro del Circulo, Triangulo y Rectangulo

#*************


#Importamos las libreria os(para acceder a los archivos del sistema)
import os
from colorama import Fore, Style

#Creamos una funcion la cual vamos a guardar toda la informacion y mostrarla en pantalla 
def imprimir(obj1,obj2,obj3):
    #Esta variable es para saber donde va a iniciar nuestra tabla
    tabla =f"""
{Fore.BLUE}+---------------------------------------------------------------------------------------------------------------+{Style.RESET_ALL}
{Fore.BLUE}|{Fore.GREEN}                                           Figuras Geometricas                                                {Fore.BLUE} |{Style.RESET_ALL} 
{Fore.BLUE}|-------------------------------------------------------------------------------------------------------------- |{Style.RESET_ALL}
{Fore.BLUE}|{Fore.LIGHTYELLOW_EX}   Figura     Parametros                                                          Area       Perimetro        {Fore.BLUE} |{Style.RESET_ALL}
{Fore.BLUE}|---------------------------------------------------------------------------------------------------------------|{Style.RESET_ALL}
"""

    #Definimos los parametros del largo y ancho de la tabla
    param_rect = 'Ancho: {0} Largo: {1}'.format(format(obj1.get_ancho(), '.2f'), format(obj1.get_largo(), '.2f'))
    
    #Definimos los parametros del radio en la tabla
    param_circ = 'Radio:{0}'.format(format(obj2.get_radio(), '.2f'))
    
    #Definimos los parametros de los catetos en la tabla
    param_tria = 'Cateto A: {0} Cateto B: {1} Cateto C:{2}'.format(format(obj3.get_cateto_a(), '.2f'), format(obj3.get_cateto_b(), '.2f'),format(obj3.get_cateto_c(), '.2f'))
    
    #Editamos los parametros para que queden ajustados a nuestra tabla
    tabla = tabla + '{4}{0:<15s} {1:<65s} {2:<10.2f} {3:<5.2f} {4:>13s}\n'.format(
        'Rectangulo', param_rect, obj1.area_rectangulo(), obj1.perimetro_rectangulo(),  '| ' )
    tabla = tabla +  '{4}{0:<15s} {1:<65s} {2:<10.2f} {3:<5.2f} {4:>13s}\n'.format(
        'Circulo', param_circ, obj2.area_circulo(), obj2.perimetro_circulo(),   '| ' ) 
    tabla = tabla +  '{4}{0:<15s} {1:<65s} {2:<10.2f} {3:<5.2f} {4:>13s}\n'.format(
        'Triangulo', param_tria, obj3.area_triangulo(), obj3.perimetro_triangulo(),   '| ') 
    tabla = tabla + f" {Fore.BLUE}+---------------------------------------------------------------------------------------------------------------+ \n {Style.RESET_ALL}" 
    
    #Esta funcion es para limpiar la pantalla 
    os.system('cls')
    
    #Imprimimos toda la tabla
    print(tabla)