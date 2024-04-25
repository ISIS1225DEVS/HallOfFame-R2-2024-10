"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
1* This program is free software: you can redistribute it and/or modify
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
import threading

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit = 1000

def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control=controller.new_controller()
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

def tamanio_archivo():
    """
    Función que le pide al usuario que seleccione el tamaño del archivo que desea cargar

    Returns:
    retorno: string con el tamaño del archivo que se va a cargar
    """
    #Se le muestra al usuario las opciones de tamaño de archivo que puede cargar
    print("Seleccione el tamaño del archivo a cargar")
    opciones={"1": "10",
              "2": "20",
              "3": "30",
              "4": "40",
              "5": "50",
              "6": "60",
              "7": "70",
              "8": "80",
              "9": "90",
              "10": "small",
              "11": "medium",
              "12": "large"}
    #Se iteran las opciones y se imprimen
    for opcion in opciones:
        print(opcion + "- " + opciones[opcion])
    #Se le pide al usuario que seleccione una opción
    inputs = input('Seleccione una opción para continuar\n')
    #Se valida que la opción seleccionada sea válida y exista en el diccionario de opciones
    if inputs in opciones:
        retorno= opciones[inputs]
    else:
        print("Opción errónea, vuelva a elegir.\n")
        retorno= tamanio_archivo()
    return retorno
def load_data(control,memoria):
    """
    Carga los datos
    Args:
    control: instancia del controlador con el modelo cargado en memoria
    Returns:
    datos: diccionario con la información de los archivos cargados
    """
    #Se inicia una variable donde la elección del tamaño del archivo es False
    eleccion=False
    tamanio=None
    #Se itera hasta que el usuario seleccione un tamaño de archivo
    while eleccion==False:
        tamanio=tamanio_archivo()
        if tamanio_archivo!=None:
            eleccion=True
    #Se le muestra al usuario el tamaño de archivo que seleccionó
    print("-"*20)
    print("El tamaño elegido es "+ tamanio)
    print("-"*20)
    print("Cargando información de los archivos ....\n")
    #Se llama la función load_data del controlador
    datos=controller.load_data(control, tamanio, memoria)
    return datos


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    cantidad=int(input("Ingrese cantidad: "))
    cod_pais=input("Ingrese código de país: ")
    experticia=input("Ingrese nivel de experticia: ")
    memoria=memoria_pregunta()
    retorno=controller.req_1(control, cantidad, cod_pais, experticia, memoria)
    datos=retorno[0]
    #Se crea una tabla con los datos que se van a imprimir
    header=["#","Fecha publicación", "Titulo oferta", "Nombre empresa", "Nivel experticia", "Pais oferta", "Ciudad oferta","Tamaño empresa","Tipo ubicación","Contrata ucranianos"]
    tabla=[]
    tamanio_pais=datos[1]
    tamanio_experiencia=datos[2]
    #Se imprime el numero de ofertas que se encontraron
    print("Se encontraron "+str(tamanio_pais)+" ofertas en "+ cod_pais)
    print("Se encontraron "+str(tamanio_experiencia)+" ofertas de experiencia " + experticia)
    if memoria==True:
        print("La memoria usada ha sido:",retorno[2],"KB")
    #Se itera sobre el numero de ofertas que se quieren imprimir y se agregan a la tabla
    if lt.size(datos[0])<=10:
        for i in range(1,cantidad+1):
            tabla.append([i, lt.getElement(datos[0],i)["published_at"],
                                lt.getElement(datos[0],i)["title"],
                                lt.getElement(datos[0],i)["company_name"],
                                lt.getElement(datos[0],i)["experience_level"],
                                lt.getElement(datos[0],i)["country_code"], 
                                lt.getElement(datos[0],i)["city"],
                                lt.getElement(datos[0],i)["company_size"],
                                lt.getElement(datos[0],i)["workplace_type"],
                                lt.getElement(datos[0],i)["open_to_hire_ukrainians"]])
    else:
        for i in range(1,6):
            tabla.append([i, lt.getElement(datos[0],i)["published_at"],
                                lt.getElement(datos[0],i)["title"],
                                lt.getElement(datos[0],i)["company_name"],
                                lt.getElement(datos[0],i)["experience_level"],
                                lt.getElement(datos[0],i)["country_code"], 
                                lt.getElement(datos[0],i)["city"],
                                lt.getElement(datos[0],i)["company_size"],
                                lt.getElement(datos[0],i)["workplace_type"],
                                lt.getElement(datos[0],i)["open_to_hire_ukrainians"]])
            for i in range(lt.size(datos[0])-4, lt.size(datos[0])+1):
                tabla.append([i, lt.getElement(datos[0],i)["published_at"],
                                lt.getElement(datos[0],i)["title"],
                                lt.getElement(datos[0],i)["company_name"],
                                lt.getElement(datos[0],i)["experience_level"],
                                lt.getElement(datos[0],i)["country_code"], 
                                lt.getElement(datos[0],i)["city"],
                                lt.getElement(datos[0],i)["company_size"],
                                lt.getElement(datos[0],i)["workplace_type"],
                                lt.getElement(datos[0],i)["open_to_hire_ukrainians"]])
    #Se imprime la tabla
    print(tabulate(tabla, headers=header, tablefmt="grid"))
    print("El tiempo total es de "+ str(round(retorno[1],2))+" ms")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    num_ofertas=int(input("Ingrese el número de ofertas: "))
    empresa=input("Ingrese el nombre de la empresa: ")
    ciudad=input("Ingrese la ciudad: ")
    memoria=memoria_pregunta()
    retorno=controller.req_2(control, num_ofertas, empresa, ciudad, memoria)
    datos=retorno[0]
    if datos!=None:
        print("Se encontraron "+str(datos[1])+" ofertas en "+ciudad+" de la empresa "+empresa)
        if memoria==True:
            print("La memoria usada ha sido:",retorno[2],"KB")
        header=["#","Fecha publicación", "Pais oferta", "Ciudad oferta", "Nombre empresa", "Titulo oferta", "Nivel Experticia", "Formato aplicacion", "Tipo trabajo"]
        tabla=[]
        if lt.size(datos[0])<=10:
            for i in range(1,lt.size(datos[0])+1):
                tabla.append([i,lt.getElement(datos[0],i)["published_at"],
                lt.getElement(datos[0],i)["country_code"],
                lt.getElement(datos[0],i)["city"],
                lt.getElement(datos[0],i)["company_name"],
                lt.getElement(datos[0],i)["title"],
                lt.getElement(datos[0],i)["experience_level"],
                lt.getElement(datos[0],i)["remote_interview"],
                lt.getElement(datos[0],i)["workplace_type"]])
        else:
            for i in range(1,6):
                tabla.append([i,lt.getElement(datos[0],i)["published_at"],
                lt.getElement(datos[0],i)["country_code"],
                lt.getElement(datos[0],i)["city"],
                lt.getElement(datos[0],i)["company_name"],
                lt.getElement(datos[0],i)["title"],
                lt.getElement(datos[0],i)["experience_level"],
                lt.getElement(datos[0],i)["remote_interview"],
                lt.getElement(datos[0],i)["workplace_type"]])
            for i in range(lt.size(datos[0])-4, lt.size(datos[0])+1):
                tabla.append([i,lt.getElement(datos[0],i)["published_at"],
                lt.getElement(datos[0],i)["country_code"],
                lt.getElement(datos[0],i)["city"],
                lt.getElement(datos[0],i)["company_name"],
                lt.getElement(datos[0],i)["title"],
                lt.getElement(datos[0],i)["experience_level"],
                lt.getElement(datos[0],i)["remote_interview"],
                lt.getElement(datos[0],i)["workplace_type"]])
        print(tabulate(tabla, headers=header, tablefmt="grid"))
        print("El tiempo total es de "+ str(round(retorno[1],2))+" ms")
    else:
        print("No se encontraron ofertas")


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """

    nombre_empresa=input("Ingrese el nombre de la empresa: ")
    fecha_ini=input("Ingrese la fecha de inicio: ")
    fecha_fin=input("Ingrese la fecha de fin: ")
    memoria=memoria_pregunta()
    retorno=controller.req_3(control, nombre_empresa, fecha_ini, fecha_fin, memoria)
    datos=retorno[0]
    tiempo=retorno[1]
    print("El numero de ofertas de la empresa "+nombre_empresa+" entre las fechas "+fecha_ini+" y "+fecha_fin+" es de "+str(datos[0]))
    print("El numero de ofertas de experiencia junior de la empresa "+nombre_empresa+" entre las fechas "+fecha_ini+" y "+fecha_fin+" es de "+str(datos[1]))
    print("El numero de ofertas de experiencia mid de la empresa "+nombre_empresa+" entre las fechas "+fecha_ini+" y "+fecha_fin+" es de "+str(datos[2]))
    print("El numero de ofertas de experiencia senior de la empresa "+nombre_empresa+" entre las fechas "+fecha_ini+" y "+fecha_fin+" es de "+str(datos[3]))
    print("El tiempo total es de "+ str(round(tiempo,2))+" ms")
    if memoria==True:
        print("La memoria usada ha sido:",retorno[2],"KB")
    if datos!=None:
        header=("#","Fecha publicacion", "Titulo oferta", "Nivel experticia", "Ciudad", "Pais", "Tamaño empresa", "Tipo lugar", "Contrata Ucranianos")
        if datos[0]>10:
            tabla=[]
            for i in range(1,6):
                tabla.append([i,lt.getElement(datos[4],i)["published_at"],
                              lt.getElement(datos[4],i)["title"],
                                lt.getElement(datos[4],i)["experience_level"],
                                lt.getElement(datos[4],i)["city"],
                                lt.getElement(datos[4],i)["country_code"],
                                lt.getElement(datos[4],i)["company_size"],
                                lt.getElement(datos[4],i)["workplace_type"],
                                lt.getElement(datos[4],i)["open_to_hire_ukrainians"]])
            print(tabulate(tabla, headers=header, tablefmt="grid"))
            tabla=[]
            for i in range(lt.size(datos[4])-4, lt.size(datos[4])+1):
                tabla.append([i,lt.getElement(datos[4],i)["published_at"],
                              lt.getElement(datos[4],i)["title"],
                                lt.getElement(datos[4],i)["experience_level"],
                                lt.getElement(datos[4],i)["city"],
                                lt.getElement(datos[4],i)["country_code"],
                                lt.getElement(datos[4],i)["company_size"],
                                lt.getElement(datos[4],i)["workplace_type"],
                                lt.getElement(datos[4],i)["open_to_hire_ukrainians"]])
            print(tabulate(tabla, headers=header, tablefmt="grid"))
        else:
            tabla=[]
            contador=1
            for i in lt.iterator(datos[4]):
                tabla.append(contador, i["published_at"], i["title"], i["experience_level"], i["city"], i["country_code"], i["company_size"], i["workplace_type"], i["open_to_hire_ukrainians"])
                contador+=1
            print(tabla)



def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pais=input("Ingrese el país que desea consultar: ")
    fecha_1=input("Ingrese la fecha de inicio en formato YYYY-MM-DD: ")
    fecha_2=input("Ingrese la fecha de fin en formato YYYY-MM-DD: ")
    print("-"*20+"Cargando..."+"-"*20)
    memoria=memoria_pregunta()
    datos=controller.req_4(control, pais, fecha_1, fecha_2)
    retorno=datos[0]
    
    print("El total de ofertas publicadas en "+str(pais)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" es de "+str(lt.size(retorno[0]))+" ofertas")
    print("El total de empresas que publicaron ofertas en el país "+str(pais)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" son: "+str(retorno[1])+" empresas")
    print("El total de ciudades que publicaron ofertas en el país "+str(pais)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" es de: "+str(retorno[2])+ " ciudades")
    print("La ciudad con más ofertas publicadas en "+str(pais)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" es: "+str(retorno[3][0])+ " con "+str(retorno[3][1])+" ofertas")
    print("La ciudad con menos ofertas publicadas en "+str(pais)+" entre las fechas "+str(fecha_1)+" y "+str(fecha_2)+" es: "+str(retorno[4][0])+ " con "+str(retorno[4][1])+" ofertas")
    print("Los datos ordenados son:")
    if memoria==True:
            print("La memoria usada ha sido:",retorno[2],"KB")
    header=["#","Fecha de publicacion","Titulo oferta","Nivel experticia", "Nombre empresa","Ciudad de la empresa", "Tipo lugar", "Tipo trabajo", "Contrata Ucranianos"]
    tabla=[]
    if (lt.size(retorno[0])+1)>10:
      for i in range(1,6):
        tabla.append([i,lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["title"],lt.getElement(retorno[0],i)["experience_level"],lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["city"],lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["remote_interview"],lt.getElement(retorno[0],i)["open_to_hire_ukrainians"]])
      print(tabulate(tabla, headers=header, tablefmt="grid"))
      tabla=[]
      for i in range(lt.size(retorno[0])-4, lt.size(retorno[0])+1):
        print(".")
        tabla.append([i,lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["title"],lt.getElement(retorno[0],i)["experience_level"],lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["city"],lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["remote_interview"],lt.getElement(retorno[0],i)["open_to_hire_ukrainians"]])
      print(tabulate(tabla, headers=header, tablefmt="grid"))
    else:
        for i in (lt.size(retorno[0])+1):
          print(".")
          tabla.append([i,lt.getElement(retorno[0],i)["published_at"], lt.getElement(retorno[0],i)["title"],lt.getElement(retorno[0],i)["experience_level"],lt.getElement(retorno[0],i)["company_name"], lt.getElement(retorno[0],i)["city"],lt.getElement(retorno[0],i)["workplace_type"], lt.getElement(retorno[0],i)["remote_interview"],lt.getElement(retorno[0],i)["open_to_hire_ukrainians"]])
        print(tabulate(tabla, headers=header, tablefmt="grid"))
    
    print("El tiempo total es de "+ str(round(datos[1],2))+" ms")

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    ciudad=input("Ingrese la ciudad: ")
    fecha_ini=input("Ingrese la fecha de inicio: ")
    fecha_fin=input("Ingrese la fecha de fin: ")
    memoria=memoria_pregunta()
    retorno=controller.req_5(control, ciudad, fecha_ini, fecha_fin, memoria)
    if retorno[0]==None:
        print("No se han encontrado ofertas")
    else:
        print("La cantidad de ofertas en"+ciudad+" entre "+fecha_ini+" y "+fecha_fin+" es de "+str(retorno[0][1]))
        print("El total de empresas con al menos una oferta es de: "+str(retorno[0][2]))
        print("La empresa con mayor ofertas es: "+str(retorno[0][3][0])+" con "+str(retorno[0][3][1])+" ofertas")
        print("La empresa con menor ofertas es: "+str(retorno[0][4][0])+" con "+str(retorno[0][4][1])+" ofertas")
        print("El tiempo total es de "+ str(round(retorno[1],2))+" ms")
        if memoria==True:
            print("La memoria usada ha sido:",retorno[2],"KB")
        header=["#","Fecha publicación", "Titulo Oferta", "Nombre empresa", "Tipo trabajo", "Tamaño Empresa"]
        tabla=[]
        if lt.size(retorno[0][0])<=10:
            for i in range(1,lt.size(retorno[0][0])+1):
                tabla.append([i,lt.getElement(retorno[0][0],i)["published_at"],
                lt.getElement(retorno[0][0],i)["title"],
                lt.getElement(retorno[0][0],i)["company_name"],
                lt.getElement(retorno[0][0],i)["workplace_type"],
                lt.getElement(retorno[0][0],i)["company_size"]])
        else:
            for i in range(1,6):
                tabla.append([i,lt.getElement(retorno[0][0],i)["published_at"],
                lt.getElement(retorno[0][0],i)["title"],
                lt.getElement(retorno[0][0],i)["company_name"],
                lt.getElement(retorno[0][0],i)["workplace_type"],
                lt.getElement(retorno[0][0],i)["company_size"]])
            for i in range(lt.size(retorno[0][0])-4, lt.size(retorno[0][0])+1):
                tabla.append([i,lt.getElement(retorno[0][0],i)["published_at"],
                lt.getElement(retorno[0][0],i)["title"],
                lt.getElement(retorno[0][0],i)["company_name"],
                lt.getElement(retorno[0][0],i)["workplace_type"],
                lt.getElement(retorno[0][0],i)["company_size"]])
        print(tabulate(tabla, headers=header, tablefmt="grid"))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    num_ciudades=int(input("Ingrese el número de ciudades: "))
    experticia=input("Ingrese el nivel de experticia (junior, mid, senior, indiferente): ")
    anio=input("Ingrese el año: ")
    memoria=memoria_pregunta()
    retorno=controller.req_6(control, num_ciudades, experticia, anio, memoria)
    datos=retorno[0]
    tiempo=retorno[1]
    if datos!=None:
        print("El total de ciudades con ofertas de "+experticia+" en "+anio+" es de "+str(datos[0]))
        print("El total de empresas con ofertas de "+experticia+" en "+anio+" es de "+str(datos[1]))
        print("El total de ofertas de "+experticia+" en "+anio+" es de "+str(datos[2]))
        print("La ciudad con mayor ofertas de "+experticia+" en "+anio+" es "+datos[3][0]+" con "+str(datos[3][1])+" ofertas")
        print("La ciudad con menor ofertas de "+experticia+" en "+anio+" es "+datos[4][0]+" con "+str(datos[4][1])+" ofertas")
        print("El tiempo total es de "+ str(round(tiempo,2))+" ms")
        if memoria==True:
            print("La memoria usada ha sido:",retorno[2],"KB")
        for i in lt.iterator(datos[5]):
            tabla=[]
            headers=["Ciudad","Pais","Cantidad ofertas", "Salario promedio", "Cantidad empresas", "Empresa mas ofertas", "Mejor oferta", "Peor oferta"]
            for j in range(1,7):
                tabla.append([headers[j-1],lt.getElement(i,j)])
            for j in range(7,9):
                tabla.append([headers[j-1],(lt.getElement(i,j)["title"],lt.getElement(i,j)["salario"])])
            print(tabulate(tabla, tablefmt="grid"))
            print("="*30)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    num_paises=int(input("Ingrese el número de paises: "))
    anio_consulta=input("Ingrese el año de consulta: ")
    mes_consulta=input("Ingrese el mes de consulta: ")
    memoria=memoria_pregunta()
    retorno=controller.req_7(control, num_paises, anio_consulta, mes_consulta, memoria)
    datos=retorno[0]
    tiempo=retorno[1]
    print("El numero total de ofertas en "+mes_consulta+" de "+anio_consulta+" es de "+str(datos[0]))
    print("El numero total de ciudades con ofertas en "+mes_consulta+" de "+anio_consulta+" es de "+str(datos[1]))
    print("El pais con mayor ofertas en "+mes_consulta+" de "+anio_consulta+" es "+datos[2][0]+" con "+str(datos[2][1])+" ofertas")
    print("La ciudad con mayor ofertas en "+mes_consulta+" de "+anio_consulta+" es "+datos[3][0]+" con "+str(datos[3][1])+" ofertas")
    print("El tiempo total es de "+ str(round(tiempo,2))+" ms")
    if memoria==True:
        print("La memoria usada ha sido:",retorno[2],"KB")
    for i in lt.iterator(datos[4]):
        headers=["Pais","Nivel experticia","Cantidad habilidades","Habilidad mas solicitada","Habilidad menos solicitada","Promedio Habilidades","Cantidad empresas","Empresa mas ofertas","Empresa menos ofertas","Empresas una o mas sedes"]
        limite=lt.size(i)
        k=0
        while k<limite:
            tabla=[]
            for j in range(1+k,11+k):
                tabla.append([headers[j-1-k],lt.getElement(i,j)])
            print(tabulate(tabla, tablefmt="grid"))
            print("="*30)
            k+=10
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    nivel_experticia=input("Ingrese el nivel de experticia: ")
    divisa=input("Ingrese la divisa: ")
    fecha_ini=input("Ingrese la fecha de inicio: ")
    fecha_fin=input("Ingrese la fecha de fin: ")
    memoria=memoria_pregunta()
    retorno=controller.req_8(control, nivel_experticia, divisa, fecha_ini, fecha_fin, memoria)
    datos=retorno[0]
    tiempo=retorno[1]
    print("El tiempo total es de "+ str(round(tiempo,2))+" ms")
    if memoria==True:
        print("La memoria usada ha sido:",retorno[2],"KB")
    parte_1=datos[0]
    parte_2=datos[1]
    print("========PARTE 1========")
    print("El total de empresas con ofertas de "+nivel_experticia+" en "+divisa+" entre "+fecha_ini+" y "+fecha_fin+" es de "+str(parte_1[0]))
    print("El total de ofertas de "+nivel_experticia+" en "+divisa+" entre "+fecha_ini+" y "+fecha_fin+" es de "+str(parte_1[1]))
    print("El numero de países con ofertas de "+nivel_experticia+" en "+divisa+" entre "+fecha_ini+" y "+fecha_fin+" es de "+str(parte_1[2]))
    print("El numero de ciudades con ofertas de "+nivel_experticia+" en "+divisa+" entre "+fecha_ini+" y "+fecha_fin+" es de "+str(parte_1[3]))
    print("El numero de ofertas con rango salarial en "+nivel_experticia+" en "+divisa+" entre "+fecha_ini+" y "+fecha_fin+" es de "+str(parte_1[4]))
    print("El numero de ofertas con salario fijo en "+nivel_experticia+" en "+divisa+" entre "+fecha_ini+" y "+fecha_fin+" es de "+str(parte_1[5]))
    print("El numero de ofertas sin salario en "+nivel_experticia+" en "+divisa+" entre "+fecha_ini+" y "+fecha_fin+" es de "+str(parte_1[6]))
    tabla=[]
    headers=("#","Nombre pais", "Promedio salario", "Numero empresas", "Numero ofertas", "Numero ofertas salario", "Numero habilidades")
    if lt.size(parte_1[7])<=10:
        for i in range(1,lt.size(parte_1[7])+1):
            tabla.append([i,lt.getElement(parte_1[7],i)[0],
            lt.getElement(parte_1[7],i)[1],
            lt.getElement(parte_1[7],i)[2],
            lt.getElement(parte_1[7],i)[3],
            lt.getElement(parte_1[7],i)[4],
            lt.getElement(parte_1[7],i)[5]])
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        for i in range(1,6):
            tabla.append([i,lt.getElement(parte_1[7],i)[0],
            lt.getElement(parte_1[7],i)[1],
            lt.getElement(parte_1[7],i)[2],
            lt.getElement(parte_1[7],i)[3],
            lt.getElement(parte_1[7],i)[4],
            lt.getElement(parte_1[7],i)[5]])
        for i in range(lt.size(parte_1[7])-4, lt.size(parte_1[7])+1):
            tabla.append([i,lt.getElement(parte_1[7],i)[0],
            lt.getElement(parte_1[7],i)[1],
            lt.getElement(parte_1[7],i)[2],
            lt.getElement(parte_1[7],i)[3],
            lt.getElement(parte_1[7],i)[4],
            lt.getElement(parte_1[7],i)[5]])
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    print("========PARTE 2========")
    mayor=parte_2[0]
    menor=parte_2[1]
    headers=("Codigo pais","Total ofertas", "Promedio salario", "Numero ciudades", "Numero empresas", "Salario mayor", "Salario menor", "Habilidades")
    print("============MAYOR============")
    tabla=[]
    for i in range(1,9):
        tabla.append([headers[i-1], lt.getElement(mayor, i)])
    print(tabulate(tabla, tablefmt="grid"))
    print("============MENOR============")
    tabla=[]
    for i in range(1,9):
        print(lt.getElement(menor, i))
        tabla.append([headers[i-1], lt.getElement(menor, i)])
    print(tabulate(tabla, tablefmt="grid"))

sys.setrecursionlimit(100000000)

def memoria_pregunta():
    pregunta=input("¿Desea ver la memoria usada? (s/n): ")
    if pregunta.lower()=="s":
        return True
    else:
        return False


# Se crea el controlador asociado a la vista

if __name__ == "__main__":
    """
    Menu principal
    """
    #ciclo del menu
    def menu_principal():
        datos_cargados = False
        working = True
        algoritmo_orden_seleccionado = False
        while working:
            print_menu()
            inputs = input('Seleccione una opción para continuar\n')
            if int(inputs) == 1:
                if datos_cargados==False:
                    control = new_controller()
                    memoria=memoria_pregunta()
                    data = load_data(control,memoria)
                    print("-"*10+"Carga de datos exitosa"+"-"*10)
                    size=lt.size(data[0]["jobs"])
                    print("Se han cargado "+str(size)+" trabajos")
                    header=["#","Fecha publicacion","Titulo oferta", "Nombre empresa", "Nivel experticia", "Pais de oferta", "Ciudad de oferta"]
                    tabla=[]
                    for i in range(1,4):
                        tabla.append([i,lt.getElement(data[0]["jobs"],i)["published_at"], lt.getElement(data[0]["jobs"],i)["title"], lt.getElement(data[0]["jobs"],i)["company_name"], lt.getElement(data[0]["jobs"],i)["experience_level"], lt.getElement(data[0]["jobs"],i)["country_code"], lt.getElement(data[0]["jobs"],i)["city"]])
                    print(tabulate(tabla, headers=header, tablefmt="grid"))
                    tabla=[]
                    for i in range(size-2, size+1):
                        print(".")
                        tabla.append([i,lt.getElement(data[0]["jobs"],i)["published_at"], lt.getElement(data[0]["jobs"],i)["title"], lt.getElement(data[0]["jobs"],i)["company_name"], lt.getElement(data[0]["jobs"],i)["experience_level"], lt.getElement(data[0]["jobs"],i)["country_code"], lt.getElement(data[0]["jobs"],i)["city"]])
                    print(tabulate(tabla, headers=header, tablefmt="grid"))
                    datos_cargados=True
                    print("="*40)
                    print("El tiempo que ha tomado en la ejecución es:",data[1],"ms")
                    if memoria==True:
                        print("La memoria usada ha sido:",data[2],"KB")
                    print("="*40)
                else:
                    print("Los datos ya han sido cargados")
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
            elif int(inputs)==0:
                working=False
                print("\nGracias por utilizar el programa") 
            else:
                print("Opción errónea, vuelva a elegir.\n")
        sys.exit(0)
    threading.stack_size(67108864*2)
    sys.setrecursionlimit(default_limit*10)
    thread=threading.Thread(target=menu_principal)
    menu_principal()