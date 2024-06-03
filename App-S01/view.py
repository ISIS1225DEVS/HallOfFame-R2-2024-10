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


def new_controller(tipo, alfa, archivo):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(tipo, alfa, archivo)
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    return control


def print_menu():
    print("\nBienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print('10- Obtener un dato dado su id')
    print("0- Salir")

def load_data(control, filename, memory):
    """
    Carga los datos
    """
    data= controller.load_data(control, filename,memory)
    #TODO: Realizar la carga de datos
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    print('================================')
    data = controller.get_data(control, id)
    if data == None:
        print('No hay una oferta de trabajo asociada a ese ID.')
    else:
        print('Estos son los datos que corresponen al ID ingresado: ')
        print('Oferta de trabajo: ')
        print(data[0])
        print('\nHabilidades requeridas: ')
        print(tabulate(lt.iterator(data[1]),headers="keys", tablefmt = "grid", showindex=False))
        print('\nTipo de empleo: ')
        print(data[2])
        print('\nDiferentes puntos de trabajo: ')
        print(tabulate(lt.iterator(data[3]),headers="keys", tablefmt = "grid", showindex=False))

def nombre_archivo():
    print('================================')
    print('Porcentajes de datos en archivos')
    print('1. 10%')
    print('2. 20%')
    print('3. 30%')
    print('4. 40%')
    print('5. 50%')
    print('6. 60%')
    print('7. 70%')
    print('8. 80%')
    print('9. 90%')
    print('10. small')
    print('11. medium')
    print('12. large')
    archivo=int(input('Seleccionar el porcentaje de datos a cargar: '))
    default='small-'
    if archivo==1:
        default='10-por-'
    elif archivo==2:
        default='20-por-'
    elif archivo==3:
        default='30-por-'
    elif archivo==4:
        default='40-por-'
    elif archivo==5:
        default='50-por-'
    elif archivo==6:
        default='60-por-'
    elif archivo==7:
        default='70-por-'
    elif archivo==8:
        default='80-por-'
    elif archivo==9:
        default='90-por-'
    elif archivo==10:
        default='small-'
    elif archivo==11:
        default='medium-'
    elif archivo==12:
        default='large-'
    else:
        print('Nombre de archivo inválido. Se cargarán los archivos con prefijo ',default,'.')
    return default
    
def tipo_y_factor():
    print('================================')
    print('Tipos de mapa')
    print('1. CHAINING')
    print('2. PROBING')
    tipo=int(input('Seleccionar el tipo de mapa para cargar los datos: '))
    default='CHAINING'
    if tipo==1:
        default='CHAINING'
    elif tipo==2:
        default='PROBING'
    else:
        print('Inválido. Se usará ', default, ' por defecto.')
    alpha=float(input('Ingresar el factor de carga: '))
    return default, alpha

def print_tabulate(list, sample=5):
    size = lt.size(list)
    if size < sample:
        print("Hay menos de ", sample ," registros: ")
        print(tabulate(lt.iterator(list),headers="keys", tablefmt = "grid", showindex=False))
    else:
        primeros = lt.subList(list,1,sample)
        ultimos = lt.subList(list,size-sample,sample)
        print(tabulate(lt.iterator(primeros),headers="keys", tablefmt = "grid", showindex=False))
        print('.......')
        print(tabulate(lt.iterator(ultimos),headers="keys", tablefmt = "grid", showindex=False))

def carga_de_datos_vista(data, memoria):
    print('\n================================')
    print('Número de trabajos: ', lt.size(data[0]))
    print('Número de habilidades: ', lt.size(data[1]))
    print('Número de tipos de empleo: ', lt.size(data[2]))
    print('Número de multilocacione1s: ', lt.size(data[3]))
    print('================================')
    print('A continuación se presentan los tres primeros y tres últimos registros del archivo jobs ordenados por fecha: ')
    print('=============== Trabajos =============== ')
    size = lt.size(data[0])
    primeros = lt.subList(data[0],1,3)
    ultimos = lt.subList(data[0],size-2,3)
    for dato in lt.iterator(ultimos):
        lt.addLast(primeros, dato)
    print(tabulate(lt.iterator(primeros),headers="keys", tablefmt = "grid", showindex=False))
    print('====== Tiempo de carga [ms] ======')
    print(round(data[4],2))
    if memoria==True:
        print('====== Memoria utilizada [KiB] ======')
        print(round(data[5],2))


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    n=int(input('Ingresar el número de ofertas a listar: '))
    pais=input('Ingresar el código del país a consultar: ')
    exp=input('Ingresar el nivel de experiticia de las ofertas a consultar (junior, mid, senior): ')
    data=controller.req_1(control, n, pais, exp)
    print('============================== ')
    print('Total de ofertas de trabajo para', pais, ':', data[1][1] )
    print('Total de ofertas de trabajo para', exp, ':', data[1][2])
    if data[1][0] == None:
        print('No hay ofertas que cumplan esos parámetros.')
    elif lt.size(data[1][0]) < n:
        print('Hay menos de ', n, ' datos. Se presentan a continuación: ')
        print(tabulate(lt.iterator(data[1][0]),headers="keys", tablefmt = "grid", showindex=False))
    elif lt.size(data[1][0]) > 10:
        print('Hay más de 10 registros. Se presentan los 5 primeros y 5 últimos: ')
        print_tabulate(data[1][0], 5)
    else:
        print(tabulate(lt.iterator(data[1][0]),headers="keys", tablefmt = "grid", showindex=False))
        
    print('====== Tiempo de ejecución [ms] ======')
    print(round(data[0],2))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    empresa=input('Ingrese el nombre de la compañia a buscar: ')
    ciudad=input('Ingrese la ciudad a buscar: ')
    n=int(input('Ingrese el numero de ofertas a buscar: '))
    rta=controller.req_2(control,empresa,ciudad,n)
    print('============================== ')
    print('El total de ofertas de trabajo para ',empresa,' en ',ciudad,' son: ',rta[1][0])
    if rta[1][0] == None:
        print('No hay ofertas que cumplan esos parámetros.')
    elif (rta[1][0]) < n:
        print('Hay menos de ', n, ' datos. Se presentan a continuación: ')
        print(tabulate(lt.iterator(rta[1][1]),headers="keys", tablefmt = "grid", showindex=False))
    elif (rta[1][0]) > 10:
        print('Hay más de 10 registros. Se presentan los 5 primeros y 5 últimos: ')
        print_tabulate(rta[1][1], 5)
    else:
        print(tabulate(lt.iterator(rta[1][1]),headers="keys", tablefmt = "grid", showindex=False))
    
    print('====== Tiempo de ejecución [ms] ======')
    print(round(rta[0],2))
    
    
    


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    nombre = input("Ingrese el nombre de la empresa: ")
    inicio = input("Ingrese la fecha inicial: ")
    final = input("Ingrese la fecha final: ")
    ofertas=controller.req_3(control, nombre, inicio, final)
    
    print('\n=================================')
    print("El número total de ofertas es: ", str(ofertas[1][0]))
    print("Ofertas con experiencia junior es: ", str(ofertas[1][1]))
    print("Ofertas con experiencias mid es: ", str(ofertas[1][2]))
    print("Ofertas con experiencia senior es: ", str(ofertas[1][3]))
    print("El listado de las ofertas son: ")
    
    if str(ofertas[1][0]) == "0":
        print('No hay ofertas que cumplan esos parámetros.')
    elif (ofertas[1][0]) > 10:
        print('Hay más de 10 registros. Se presentan los 5 primeros y 5 últimos: ')
        print_tabulate(ofertas[1][4], 5)
    else:
        print(tabulate(lt.iterator(ofertas[1][4]),headers="keys", tablefmt = "grid", showindex=False))
    
    print('====== Tiempo de ejecución [ms] ======')
    print(round(ofertas[0],2))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    pais=input("Ingrese el código del país a consultar: ")
    fecha_inicio=input("Ingrese la fecha inicial del periodo a consultar (formato \'%Y-%m-%d\'): ")
    fecha_fin=input("Ingrese la fecha final del periodo a consultar (formato \'%Y-%m-%d\'): ")
    ans=controller.req_4(control,pais,fecha_inicio,fecha_fin)
    time=ans[0]
    ofertas=ans[1]
    print('============================== ')
    if ofertas==None:
        print ('No hay ofertas para el país y las fechas seleccionadas.')
    else:
        print('Hay',ofertas[0], 'ofertas en',pais,'entre', fecha_inicio,'y',fecha_fin,'.' )
        print('Hay',ofertas[1], 'empresas que publicaron al menos una oferta en',pais,'.' )
        print('En total,',ofertas[2], 'ciudades publicaron ofertas, entre las cuales:')
        print('\t',ofertas[3][0], 'fue la ciudad con mayor número de ofertas. Hay',ofertas[3][1],'ofertas.')
        print('\t',ofertas[4][0], 'fue la ciudad con menor número de ofertas. Hay',ofertas[4][1],'ofertas.')
        if lt.size(ofertas[5])>10:
            print('\nHay más de 10 registros. Se presentan los 5 primeros y 5 últimos: ')
            print_tabulate(ofertas[5], 5)
        else:
            print('\nEl listado de ofertas es el siguiente:' )
            print(tabulate(lt.iterator(ofertas[5]),headers="keys", tablefmt = "grid", showindex=False))
        
    print('====== Tiempo de ejecución [ms] ======')
    print(round(time,2))

def print_req_5(control):
    ciudad=input('Ingrese la ciudad a consultar: ')
    fecha_inicio=input('Ingrese la fecha inicial del periodo a consultar en el  formato (\'%Y-%m-%d\'): ')
    fecha_fin=input('Ingrese la fecha final del periodo a consultar en el  formato (\'%Y-%m-%d\'): ')
    rta=controller.req_5(control,ciudad,fecha_inicio,fecha_fin)
    time=rta[0]
    ofertas=rta[1]
    if ofertas==None:
        print ('No hay ofertas para el país y las fechas seleccionadas.')
    else:
        print('Hay',ofertas[0], 'ofertas en',ciudad,'entre', fecha_inicio,'y',fecha_fin,'.' )
        print('Hay',ofertas[1], 'empresas que publicaron al menos una oferta en',ciudad,'.' )
        print('\t',ofertas[2][0], 'fue la empresa con mayor número de ofertas. Hay',ofertas[2][1],'ofertas.')
        print('\t',ofertas[3][0], 'fue la empresa con menor número de ofertas. Hay',ofertas[3][1],'ofertas.')
        if lt.size(ofertas[4])>10:
            print('\nHay más de 10 registros. Se presentan los 5 primeros y 5 últimos: ')
            print_tabulate(ofertas[4], 5)
        else:
            print('\nEl listado de ofertas es el siguiente:' )
            print(tabulate(lt.iterator(ofertas[4]),headers="keys", tablefmt = "fancy_grid", showindex=False))
        
    print('====== Tiempo de ejecución [ms] ======')
    print(round(time,2))
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    n= int(input("Ingrese el número de ciudades a consultar: "))
    exp = input("Ingrese el nivel de experticia a consultar (junior, mid, senior o indiferente): ")
    anio=input('Ingrese el año (formato \'%Y\'): ')
    ans=controller.req_6(control,n, exp, anio)
    respuesta=ans[1]
    time=ans[0]
    print('=============================================')
    if respuesta==None:
        print('No hay información para esos datos.')
    else:
        print('Hay',respuesta[0],'ciudades dentro del rango del número de ciudades ingresado.' )
        print('Hay',respuesta[1], 'empresas que cumplen con las condiciones de consulta.' )
        print('Hay',respuesta[2],'ofertas publicadas que cumplen con las condiciones de consulta.')
        print('La ciudad con mayor cantidad de ofertas es',respuesta[3][0], 'con',respuesta[3][1],'ofertas.')
        print('La ciudad con menor cantidad de ofertas es',respuesta[4][0], 'con',respuesta[4][1],'ofertas.')
        print('A continuación, se presenta el listado de las',respuesta[0],'ciudades ordenadas:')
        print(tabulate(lt.iterator(respuesta[5]),headers=['Nombre', 'País','Total ofertas','Salario promedio','Empresas','Mayor empresa y conteo','Mejor oferta','Peor oferta'], tablefmt = "fancy_grid", showindex=False))
    print('====== Tiempo de ejecución [ms] ======')
    print(round(time,2))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    n_pais=int(input('Ingrese el número de países a consultar: '))
    anio_mes=input("Ingrese el año y el mes a consultar (formato \'%Y-%m\'): ")
    respuesta=controller.req_7(control, n_pais, anio_mes)
    ofertas=respuesta[1]
    time=respuesta[0]
    if ofertas==None:
        print ('No hay ofertas para el país y las fechas seleccionadas.')
    else:
        print('Hay',ofertas[0], 'ofertas en',n_pais,' paises en ', anio_mes,' .' )
        print('Hay',ofertas[1], 'ciudades que publicaron al menos una oferta en los ',n_pais,' paises.' )
        print('\t',ofertas[2][0], 'fue el pais con mayor número de ofertas. Hay',ofertas[2][1],'ofertas.')
        print('\t',ofertas[3][0], 'fue la ciudad con mayor número de ofertas. Hay',ofertas[3][1],'ofertas.')
        print('\nPara el nivel de experticia junior : ')
        print('\nHay',ofertas[4][0], 'habilidades diferentes solicitadas, la mayor fue: ',ofertas[4][1][0],' con ',ofertas[4][1][1],'ofertas.\n la menor fue: ',ofertas[4][2][0],'con ',ofertas[4][2][1],' ofertas.')
        print('\nTienen un promedio de nivel de: ',ofertas[4][3])
        print('\nLas empresas que publicaron al menos una oferta con este nivel son: ',ofertas[4][4],' la mayor fue :',ofertas[4][5][0],' con: ',ofertas[4][5][1],'ofertas.\n la menor fue ',ofertas[4][6][0],'con ',ofertas[4][6][1],' ofertas.')
        print('\nLas empresas que tienen una sede o mas son: ',ofertas[4][7])
        print('\nPara el nivel de experticia mid : ')
        print('\nHay',ofertas[5][0], 'habilidades diferentes solicitadas, la mayor fue: ',ofertas[5][1][0],' con ',ofertas[5][1][1],'ofertas.\n la menor fue: ',ofertas[5][2][0],'con ',ofertas[5][2][1],' ofertas.')
        print('\nTienen un promedio de nivel de: ',ofertas[5][3])
        print('\nLas empresas que publicaron al menos una oferta con este nivel son: ',ofertas[5][4],' la mayor fue :',ofertas[5][5][0],' con: ',ofertas[5][5][1],'ofertas.\n la menor fue ',ofertas[5][6][0],'con ',ofertas[5][6][1],' ofertas.')
        print('\nLas empresas que tienen una sede o mas son: ',ofertas[5][7])
        print('\nPara el nivel de experticia senior : ')
        print('\nHay',ofertas[6][0], 'habilidades diferentes solicitadas, la mayor fue: ',ofertas[6][1][0],' con ',ofertas[6][1][1],'ofertas.\n la menor fue: ',ofertas[6][2][0],'con ',ofertas[6][2][1],' ofertas.')
        print('\nTienen un promedio de nivel de: ',ofertas[6][3])
        print('\nLas empresas que publicaron al menos una oferta con este nivel son: ',ofertas[6][4],' la mayor fue :',ofertas[6][5][0],' con: ',ofertas[6][5][1],'ofertas.\n la menor fue ',ofertas[6][6][0],'con ',ofertas[6][6][1],' ofertas.')
        print('\nLas empresas que tienen una sede o mas son: ',ofertas[6][7])
        
    print('====== Tiempo de ejecución [ms] ======')
    print(round(time,2))
    

    
    
    


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
#control = new_controller('PROBING', 0.5)

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
            archivo=nombre_archivo()
            tipo, alfa = tipo_y_factor()
            control=new_controller(tipo, alfa, archivo)
            print('================================') 
            print('¿Desea ver la memoria utilizada?')
            print('1. Sí')
            print('2. No')
            memoria=int(input())
            if memoria==1:
                print("Cargando información de los archivos ....")
                data=load_data(control, archivo, True) 
                rta=True
            else:
                rta=False
                print('No se medirá la memoria.')
                print("Cargando información de los archivos ....")
                data=load_data(control, archivo, False)
                
            carga_de_datos_vista(data, rta)
                
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
            
        elif int(inputs) == 10:
            id=input('Ingresar el ID a buscar: ')
            print_data(control, id)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
