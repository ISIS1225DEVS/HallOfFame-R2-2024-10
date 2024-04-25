"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import threading
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

default_limit=1000
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, ):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    jobs, multilocations, employments, skills, respuesta = controller.load_data(control, memflag=True)
    return jobs, multilocations, employments, skills, respuesta


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(req1, elapsed_time):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    if len(req1) > 1:
        print(f'Total de ofertas de trabajo en el país: {req1[2]}' )
        print(f'Total de ofertas de trabajo en el país con el nivel de experiencia especificado: {req1[0]}' )
        print('Si la lista supera los 10 elementos, se mostrarán las 5 primeras y 5 últimas ofertas.')
        print(tabulate(req1[1]))
        delta_time_str = f"{elapsed_time:.3f}"
        print("tiempo:", delta_time_str, "[ms]")
    else:
        print('No se encontraron ofertas de trabajo con las especificaciones dadas.')


def print_req_2(req2, elapsed_time):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    if len(req2) > 1:
        print(f'El total de ofertas ofrecida por la empresa y ciudad es {req2[0]}.' )
        print('Si la lista supera los 10 elementos, se mostrarán las 5 primeras y 5 últimas ofertas.')
        print(tabulate(req2[1]))
        delta_time_str = f"{elapsed_time:.3f}"
        print("tiempo:", delta_time_str, "[ms]")
    else:
        print('No se encontraron ofertas de trabajo con las especificaciones dadas.')
    pass


def print_req_3(req3, elapsed_time):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    if len(req3) > 1:
        print(f'Total de ofertas de la empresa en el periodo de consulta: {req3[0]}')
        print(f'Total de ofertas de la empresa en el periodo de consulta con experticia junior: {req3[1]}')
        print(f'Total de ofertas de la empresa en el periodo de consulta con experticia mid: {req3[2]}')
        print(f'Total de ofertas de la empresa en el periodo de consulta con experticia senior: {req3[3]}')
        print('Si la lista supera los 10 elementos, se mostrarán las 5 primeras y 5 últimas ofertas.')
        print(tabulate(req3[4]))
        delta_time_str = f"{elapsed_time:.3f}"
        print("tiempo:", delta_time_str, "[ms]")
    else:
        print('No se encontraron ofertas de trabajo con las especificaciones dadas.')
    pass


def print_req_4(req4, elapsed_time):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    if len(req4) > 1:
        print(f'Total de ofertas en el país en el periodo de consulta: {req4[0]}')
        print(f'Total de empresas que publicarion en el país: {req4[1]}')
        print(f'Total de ciudades en el país de consulta con ofertas: {req4[2]}')
        print(f'La ciudad con mayor cantidad de ofertas es {req4[3][0]} con {req4[3][1]}.')
        print(f'La ciudad con menor cantidad de ofertas es {req4[4][0]} con {req4[4][1]}.')
        print('Si la lista supera los 10 elementos, se mostrarán las 5 primeras y 5 últimas ofertas.')
        print(tabulate(req4[5]))
        delta_time_str = f"{elapsed_time:.3f}"
        print("tiempo:", delta_time_str, "[ms]")
    else:
        print('No se encontraron ofertas de trabajo con las especificaciones dadas.')
    pass


def print_req_5(req5, elapsed_time):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    if len(req5) > 1:
        print(f'Total de ofertas en el país en el periodo de consulta: {req5[0]}')
        print(f'Total de empresas que publicarion en el país: {req5[1]}')
        print(f'La empresa con mayor cantidad de ofertas es {req5[2][0]} con {req5[2][1]}.')
        print(f'La empresa con menor cantidad de ofertas es {req5[3][0]} con {req5[3][1]}.')
        print(tabulate(req5[4]))
        delta_time_str = f"{elapsed_time:.3f}"
        print("tiempo:", delta_time_str, "[ms]")
    else:
        print('No se encontraron ofertas de trabajo con las especificaciones dadas.')
    pass


def print_req_6(req6, elapsed_time):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    if len(req6) > 1:
        print(f'Total de ciudades que cumplen con las condiciones: {req6[0]}')
        print(f'Total de empresas que cumplen con las condiciones: {req6[1]}')
        print(f'Total de ofertas publicadas que cumplen con las condiciones: {req6[2]}')
        print(f'La ciudad con mayor cantidad de ofertas es {req6[3][0]} con {req6[3][2]}.')
        print(f'La ciudad con menor cantidad de ofertas es {req6[4][0]} con {req6[4][2]}.')
        print('Si la lista supera los 10 elementos, se mostrarán las 5 primeras y 5 últimas ciudades.')
        print(tabulate(req6[5]))
        delta_time_str = f"{elapsed_time:.3f}"
        print("tiempo:", delta_time_str, "[ms]")
    else:
        print('No se logro clasificar las ciudades con las especificaciones dadas.')
    pass


def print_req_7(req7, elapsed_time):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    if len(req7) >= 1:
        print(f'Total de ofertas de empleo: {req7[0]}')
        print(f'Número de ciudades donde se ofertó en los países resultantes de la consulta: {req7[1]}')
        print(f'Nombre del país con mayor cantidad de ofertas es {req7[2][0]} con {req7[2][1]}')
        print(f'Nombre de la ciudad con mayor cantidad de ofertas es {req7[3][0]} con {req7[3][1]}')
        #junior
        print('Para el nivel de experticia junior se tienen los siguientes datos:')
        print(f'El conteo de habilidades diferentes solicitadas en ofertas de trabajo es {req7[4][0]}')
        print(f'El nombre de la habilidad mas solicitada es {req7[4][1][0]} con {req7[4][1][1]}.')
        print(f'El nombre de la habilidad menos solicitada es {req7[4][2][0]} con {req7[4][2][1]}.')
        print(f'El promedio del nivel minimo de habilidad es {req7[4][3]}.')
        print(f'El conteo de empresas que publicaron una oferta con este nivel es {req7[4][4]}')
        print(f'El nombre de la empresa con mayor número de ofertas es {req7[4][5][0]} con {req7[4][5][1]}.')
        print(f'El nombre de la empresa con menor número de ofertas es {req7[4][6][0]} con {req7[4][6][1]}.')
        #mid
        print('Para el nivel de experticia mid se tienen los siguientes datos:')
        print(f'El conteo de habilidades diferentes solicitadas en ofertas de trabajo es {req7[5][0]}')
        print(f'El nombre de la habilidad mas solicitada es {req7[5][1][0]} con {req7[5][1][1]}.')
        print(f'El nombre de la habilidad menos solicitada es {req7[5][2][0]} con {req7[5][2][1]}.')
        print(f'El promedio del nivel minimo de habilidad es {req7[5][3]}.')
        print(f'El conteo de empresas que publicaron una oferta con este nivel es {req7[5][4]}')
        print(f'El nombre de la empresa con mayor número de ofertas es {req7[5][5][0]} con {req7[5][5][1]}.')
        print(f'El nombre de la empresa con menor número de ofertas es {req7[5][6][0]} con {req7[5][6][1]}.')
        #senior
        print('Para el nivel de experticia senior se tienen los siguientes datos:')
        print(f'El conteo de habilidades diferentes solicitadas en ofertas de trabajo es {req7[6][0]}')
        print(f'El nombre de la habilidad mas solicitada es {req7[6][1][0]} con {req7[6][1][1]}.')
        print(f'El nombre de la habilidad menos solicitada es {req7[6][2][0]} con {req7[6][2][1]}.')
        print(f'El promedio del nivel minimo de habilidad es {req7[6][3]}.')
        print(f'El conteo de empresas que publicaron una oferta con este nivel es {req7[6][4]}')
        print(f'El nombre de la empresa con mayor número de ofertas es {req7[6][5][0]} con {req7[6][5][1]}.')
        print(f'El nombre de la empresa con menor número de ofertas es {req7[6][6][0]} con {req7[6][6][1]}.')
        delta_time_str = f"{elapsed_time:.3f}"
        print("tiempo:", delta_time_str, "[ms]")
    else:
        print('No se pudo clasificar los países  con las especificaciones dadas.')
    pass


def print_req_8(req8, elapsed_time):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    if len(req8) > 1:
        print(f'Total de empresas que publicarion ofertas: {req8[0]}')
        print(f'Total de ofertas de empleo: {req8[1]}')
        print(f'Total de países con ofertas: {req8[2]}')
        print(f'Total de países con ofertas: {req8[3]}')
        print(f'Número ofertas con rango salarial: {req8[4]}')
        print(f'Número ofertas con salario fijo: {req8[5]}')
        print(f'Número ofertas sin salario: {req8[6]}')
        print(tabulate(req8))
        delta_time_str = f"{elapsed_time:.3f}"
        print("tiempo:", delta_time_str, "[ms]")
    else:
        print('No se pudo identificar los países.')
    pass

def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer:.3f}")


def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False
    
# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            jobs, multilocations, employments, skills, respuesta = load_data(control)
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            print("Ofertas cargadas: " + str(jobs))
            print("Multilocations cargadas: " + str(multilocations))
            print("Empleos cargados: " + str(employments))
            print("Skills cargadas: " + str(skills))
            printLoadDataAnswer(respuesta)
            print_tres=controller.tres_info(control)
            print(tabulate(print_tres))
        elif int(inputs) == 2:
            print("Listar las últimas N ofertas de trabajo según su país y nivel de experticia.\n")
            num_ofertas=int(input("Ingrese el número de últimas ofertas a listar\n"))
            codigo_pais= input("Ingrese el código del país del cual quiera conocer las ofertas\n")
            nivel_experticia= input("Ingrese el nivel de experticia de las ofertas a consultar\n")
            start_time = controller.getTime()
            req1= controller.req_1(control,num_ofertas,codigo_pais,nivel_experticia)
            end_time = controller.getTime()
            elapsed_time = controller.deltaTime(end_time, start_time)
            print_req_1(req1, elapsed_time)

        elif int(inputs) == 3:
            print("Listar las últimas N ofertas de trabajo por empresa y ciudad.\n")
            num_ofertas=int(input("Ingrese el número de últimas ofertas a listar\n"))
            nom_empresa= input("Ingrese el nombre de la empresa de la cual quiera conocer sus ofertas\n")
            ciudad_oferta= input("Ingrese la ciudad de las ofertas a consultar\n")
            start_time = controller.getTime()
            req2= controller.req_2(control,num_ofertas,nom_empresa,ciudad_oferta)
            end_time = controller.getTime()
            elapsed_time = controller.deltaTime(end_time, start_time)
            print_req_2(req2,elapsed_time)

        elif int(inputs) == 4:
            print("Consultar las ofertas que publicó una empresa durante un periodo especifico de tiempo.\n")
            nom_empresa=input("Ingrese el nombre de la empresa de la cual quiera conocer sus ofertas\n")
            fecha_inicial= input("Ingrese la fecha inicial del periodo del cual quiera conocer sus ofertas\n")
            fecha_final= input("Ingrese la fecha final del periodo del cual quiera conocer sus ofertas\n")
            start_time = controller.getTime()
            req3= controller.req_3(control,nom_empresa,fecha_inicial,fecha_final)
            end_time = controller.getTime()
            elapsed_time = controller.deltaTime(end_time, start_time)
            print_req_3(req3,elapsed_time)

        elif int(inputs) == 5:
            print(": Consultar las ofertas que se publicaron en un país durante un periodo de tiempo.\n")
            codigo_pais= input("Ingrese el código del país del cual quiera conocer las ofertas\n")
            fecha_inicial= input("Ingrese la fecha inicial del periodo del cual quiera conocer sus ofertas\n")
            fecha_final= input("Ingrese la fecha final del periodo del cual quiera conocer sus ofertas\n")
            start_time = controller.getTime()
            req4= controller.req_4(control,codigo_pais,fecha_inicial,fecha_final)
            end_time = controller.getTime()
            elapsed_time = controller.deltaTime(end_time, start_time)
            print_req_4(req4,elapsed_time)

        elif int(inputs) == 6:
            print("Consultar las ofertas que se publicaron en una ciudad durante un periodo de tiempo.\n")
            ciudad_oferta= input("Ingrese la ciudad de las ofertas a consultar\n")
            fecha_inicial= input("Ingrese la fecha inicial del periodo del cual quiera conocer sus ofertas\n")
            fecha_final= input("Ingrese la fecha final del periodo del cual quiera conocer sus ofertas\n")
            start_time = controller.getTime()
            req5= controller.req_5(control,ciudad_oferta,fecha_inicial,fecha_final)
            end_time = controller.getTime()
            elapsed_time = controller.deltaTime(end_time, start_time)
            print_req_5(req5,elapsed_time)

        elif int(inputs) == 7:
            print("Clasificar las N ciudades con mayor número de ofertas de trabajo de un año por experticia.\n")
            num_ciudades=int(input("Ingrese el número de ciudades para consultar\n"))
            nivel_experticia= input("Ingrese el nivel de experticia de las ofertas a consultar\n")
            ano_consulta= int(input("Ingrese el año de las ofertas a consultar\n"))
            start_time = controller.getTime()
            req6= controller.req_6(control,num_ciudades,nivel_experticia,ano_consulta)
            end_time = controller.getTime()
            elapsed_time = controller.deltaTime(end_time, start_time)
            print_req_6(req6,elapsed_time)

        elif int(inputs) == 8:
            print("Clasificar los N países con mayor número de ofertas de trabajo.\n")
            num_paises=int(input("Ingrese el número de países para consultar\n"))
            ano_consulta= int(input("Ingrese el año de las ofertas a consultar\n"))
            mes_consulta= int(input("Ingrese el mes de las ofertas a consultar\n"))
            start_time = controller.getTime()
            req7= controller.req_7(control,num_paises,ano_consulta,mes_consulta)
            end_time = controller.getTime()
            elapsed_time = controller.deltaTime(end_time, start_time)
            print_req_7(req7,elapsed_time)

        elif int(inputs) == 9:
            print(": Identificación de los países con mayor y menor ofertas de trabajo en un rango de fechas.\n")
            nivel_experticia= input("Ingrese el nivel de experticia de las ofertas a consultar\n")
            divisa= input("Ingrese la divisa de las ofertas a consultar\n")
            fecha_inicial= input("Ingrese la fecha inicial del periodo del cual quiera conocer sus ofertas\n")
            fecha_final= input("Ingrese la fecha final del periodo del cual quiera conocer sus ofertas\n")
            start_time = controller.getTime()
            req8= controller.req_8(control,nivel_experticia,divisa,fecha_inicial,fecha_final)
            end_time = controller.getTime()
            elapsed_time = controller.deltaTime(end_time, start_time)
            print_req_8(req8,elapsed_time)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
