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
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

default_limit = 1000
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
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
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


def load_data(control,memflag):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    return controller.load_data(control,memflag)


def print_carga_datos(control,data):
    jobs = control["model"]["jobs"]
    encabezados = ["Fecha","Nombre","Compañía","Nivel","País","Ciudad"]
    
    lista = controller.prim_ult_tres(jobs)
    
    n = lt.size(jobs)
    
    print(f"Se cargaron {n} ofertas de trabajo.")
    print(tabulate(lt.iterator(lista),headers=encabezados ,tablefmt="grid",showindex=False))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    num_ofertas = int(input("Cuántas ofertas quiere ver: "))
    pais = input("Escriba el código del país: ")
    nivel = input("Escriba el nivel de experticia: ")
    mem = input("Consumo memoria: ")
    mem = castBoolean(mem)
    print("Cargando información....")
    if mem == True:
        data, tiempo, total_trabajos,total_ofertas_pais,memoria = controller.req_1(control,pais,nivel,num_ofertas,memflag=mem)
    else:
        data, tiempo, total_trabajos,total_ofertas_pais = controller.req_1(control,pais,nivel,num_ofertas,memflag=mem)
    
    encabezados = ["Fecha", "Título", "Compañía", "Nivel", "País", "Ciudad", "Tamaño","Tipo","Ucranianos S/N"]
        
    print(tabulate(lt.iterator(data), headers=encabezados ,tablefmt="grid",showindex=False))
    print(f"{pais} Tiene un total de {total_ofertas_pais} ofertas.")
    print(f"Se cargaron {total_trabajos} trabajos con nivel de experiencia {nivel}.")
    
    if mem == True:
        tiempo = (tiempo,memoria)
        printLoadDataAnswer(tiempo)
    else:
        printLoadDataAnswer(tiempo)
        
    
def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    num_ofertas = int(input("Cuántas ofertas quiere ver: "))
    empresa = input("Escriba el nombre de la empresa: ")
    ciudad = input("Escriba la ciudad de la empresa: ")
    mem = input("Consumo memoria: ")
    mem = castBoolean(mem)
    
    
    print("Cargando información....")
    
    if mem == True:
        data,total_ofertas,tiempo,memoria = controller.req_2(control,empresa.lower(),ciudad,num_ofertas,memflag=mem)
    else:
        data,total_ofertas,tiempo = controller.req_2(control,empresa.lower(),ciudad,num_ofertas,memflag=mem)

    encabezados = ["Fecha", "País", "Ciudad", "Compañía", "Nombre", "Nivel", 
              "Entrevista remota","Lugar"]
    print(tabulate(lt.iterator(data), headers=encabezados ,tablefmt="grid",showindex=False))
    print(f"Se cargaron {total_ofertas} trabajos.")
    
    if mem == True:
        tiempo = (tiempo,memoria)
        printLoadDataAnswer(tiempo)
    else:
        printLoadDataAnswer(tiempo)
    
def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    empresa = input("Escriba la empresa: ")
    fecha_inicial = input("Escriba la fecha inicial (YY-MM-DD): ")
    fecha_final = input("Escriba la fecha final (YY-MM-DD): ")
    mem = input("Consumo memoria: ")
    mem = castBoolean(mem)
    
    encabezados = ["Fecha", "Nombre","Nivel","Ciudad","País", "Tamaño","Tipo","Contrata ucranianos"]
    print("Cargando información....")
    
    if mem == True:
        data, junior, mid, senior,total, tiempo, memoria = controller.req_3(control, empresa.lower(), fecha_inicial, fecha_final,mem)
    else:
        data, junior, mid, senior,total, tiempo = controller.req_3(control, empresa.lower(), fecha_inicial, fecha_final,mem)
        
    print(tabulate(lt.iterator(data), headers=encabezados ,tablefmt="grid",showindex=False))
    print(f"Se cargaron {total} ofertas de la empresa {empresa} entre {fecha_inicial} y {fecha_final}.")
    print(f"Total de ofertas junior: {junior}")
    print(f"Total de ofertas mid: {mid}")
    print(f"Total de ofertas senior: {senior}")
    
    if mem == True:
        tiempo = (tiempo,memoria)
        printLoadDataAnswer(tiempo)
    else:
        print(tiempo)
        
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    codigo = input("Escriba el codigo del pais: ")
    fechaInicio = input("Escriba la fecha inicial (YY-MM-DD): ")
    fechaFin = input("Escriba la fecha final (YY-MM-DD): ")
    encabezados = ["Fecha", "Título", "Nivel", "Compañía", "Ciudad", "Lugar", "Remoto", "Contrata ucranianos"] 
    
    print("Cargando información....")
    
    data, total_ofertas_final,total_empresas,total_ciudades,ciudad_mayor_ofertas,ciudad_menor_ofertas, deltaTime = controller.req_4(control, codigo.upper(), fechaInicio, fechaFin)
    print(tabulate(lt.iterator(data), headers=encabezados ,tablefmt="grid",showindex=False))
    print(f"Se cargaron {total_ofertas_final} ofertas del país {codigo} entre {fechaInicio} y {fechaFin} en {deltaTime} ms.")
    print(f"Se cargaron {total_empresas} empresas que publicaron por lo menos una oferta en el pais {codigo}.")
    print(f"Se cargaron {total_ciudades} ciudades que publicaron por lo menos una oferta en el pais {codigo}.")
    print(f"La ciudad {ciudad_mayor_ofertas[0]} es la que tiene mayor número de ofertas con {ciudad_mayor_ofertas[1]} ofertas.")
    print(f"La ciudad {ciudad_menor_ofertas[0]} es la que tiene mmenor número de ofertas con {ciudad_menor_ofertas[1]} ofertas.")

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    ciudad = input("Escriba el nombre de la ciudad: ")
    fecha_inicial = input("Escriba la fecha inicial (YY-MM-DD): ")
    fecha_final = input("Escriba la fecha final (YY-MM-DD): ")
    encabezados = ["Fecha", "Titulo", "Empresa", "Tamaño", "Tipo"]
    
    print("Cargando información....")
    
    try: 
        data, n_empresas, empresa_mayor, mayor, empresa_menor, menor,n, deltaTime = controller.req_5(control, ciudad.lower(), fecha_inicial, fecha_final)
        print(tabulate(lt.iterator(data), headers=encabezados ,tablefmt="grid",showindex=False))
        print(f"Se cargaron {n} ofertas de la ciudad {ciudad} entre {fecha_inicial} y {fecha_final} en {deltaTime} ms.")
        print(f"Se cargaron {n_empresas} empresas que publicaron por lo menos una oferta en la ciudad.")
        print(f"La empresa {empresa_mayor} es la que tiene mayor número de ofertas con {mayor} ofertas")
        print(f"La empresa {empresa_menor} es la que tiene menor número de ofertas con {menor} ofertas")
        
    except:
        print("\nDigita bien los datos!!\n")

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    nivel = input("Ingrese el nivel de experticia: ")
    anio = input("Ingrese el año: ")
    num_ciudades = int(input("Cuántas ciudades quiere consultar: "))
    mem = input("Consumo memoria: ")
    mem = castBoolean(mem)
    try:
        data,total_ciudades_que_cumplen, total_empresas_que_cumplen, total_ofertas_que_cumplen, ciudad_mayor, ciudad_menor,tiempo,memoria = controller.req_6(control,nivel,anio,num_ciudades,mem)
        tabla = print_tabulate(data, ['ciudad', "total_ofertas","promedio_total","total_empresas","mayor_empresa","mejor_oferta","peor_oferta"])
        print(tabla)
        print(f"Total de ciudades que cumplen con las condiciones de la consulta: {total_ciudades_que_cumplen}")
        print(f"Total de empresas que cumplen con las condiciones de la consulta: {total_empresas_que_cumplen}")
        print(f"Total de ofertas publicadas que cumplen con las condiciones de la consulta: {total_ofertas_que_cumplen} ")
        print (f"La ciudad con mayor cantidad de ofertas es {ciudad_mayor['ciudad']} con {ciudad_mayor['ofertas']}.")
        print(f"La ciudad con menor cantidad de ofertas es {ciudad_menor['ciudad']} con {ciudad_menor['ofertas']}.")
        if mem != 0:
            tiempo = (tiempo,memoria)
            printLoadDataAnswer(tiempo)
        else:
            print(f"Se cargaron tus datos en {tiempo} ms.")
    except:
        data,total_ciudades_que_cumplen, total_empresas_que_cumplen, total_ofertas_que_cumplen,tiempo,memoria = controller.req_6(control,nivel,anio,num_ciudades,mem)

        tabla = print_tabulate(data, ['ciudad', "total_ofertas","promedio_total","total_empresas","mayor_empresa","mejor_oferta","peor_oferta"])
        print(tabla)
        print(f"Total de ciudades que cumplen con las condiciones de la consulta: {total_ciudades_que_cumplen}")
        print(f"Total de empresas que cumplen con las condiciones de la consulta: {total_empresas_que_cumplen}")
        print(f"Total de ofertas publicadas que cumplen con las condiciones de la consulta: {total_ofertas_que_cumplen} ")
        if mem != 0:
            tiempo = (tiempo,memoria)
            printLoadDataAnswer(tiempo)
        else:
            print(f"Se cargaron tus datos en {tiempo} ms.")

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    num_paises = int(input("Escriba el número de países a consultar: "))
    anio = input("Escriba el año (YYYY): ")
    mes = input("Escriba el mes (MM): ")
    mem = input("Consumo memoria: ")
    mem = castBoolean(mem)
    
    if mem == True:
        data,total_ofertas,mayor_pais, junior, mid, senior, tiempo, memoria= controller.req_7(control,anio,mes,num_paises,mem)
    else:
        data,total_ofertas,mayor_pais, junior, mid, senior, tiempo = controller.req_7(control,anio,mes,num_paises,mem)

    print(f"El total de ofertas fue de: {total_ofertas}")
    print(f"El país con más ofertas fue {mayor_pais['pais']} con {mayor_pais['conteo']} ofertas.")
    print(tabulate(lt.iterator(data),headers="keys",tablefmt="grid",showindex=False))
    print("")
    print("Información de las ofertas junior:")
    print(tabulate([junior],headers="keys",tablefmt="grid",showindex=False))
    print("")
    print("Información de las ofertas mid:")
    print(tabulate([mid],headers="keys",tablefmt="grid",showindex=False))
    print("")
    print("Información de las ofertas senior:")
    print(tabulate([senior],headers="keys",tablefmt="grid",showindex=False))
    
    print(f"Se cargaron tus datos en {tiempo} ms.")
    if mem == True:
        tiempo = tiempo,memoria
        printLoadDataAnswer(tiempo)
    
def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{answer[0]}", "||",
              "Memoria [kB]: ", f"{answer[1]}")
    else:
        print("Tiempo [ms]: ", f"{answer}")

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False

def print_tabulate(data_struct, columns):
    data = data_struct

    if lt.isEmpty(data):
        return 'No hay datos'

    if lt.size(data_struct) > 6:
        data = controller.get_first_last_five(data_struct)

    #Lista vacía para crear la tabla
    reduced = []

    #Iterar cada línea de la lista
    for result in lt.iterator(data):
        line = []
        #Iterar las columnas para solo imprimir las deseadas
        for column in columns:
            line.append(result[column])
        reduced.append(line)
    table = tabulate(reduced, headers=columns, tablefmt="grid", maxcolwidths=30)
    return table 

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
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            data = load_data(control, memflag=mem)
            print_carga_datos(control,data)
            printLoadDataAnswer(data)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
