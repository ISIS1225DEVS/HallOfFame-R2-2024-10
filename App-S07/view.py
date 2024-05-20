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
import threading

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from additional import consoleMethods as coco

assert cf
from tabulate import tabulate
import traceback


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
    global control
    control= controller.new_controller()
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


def load_data(control):
    controller.load_data(control)
    #TODO: Realizar la carga de datos
    pass


def print_daa(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, country, exp, N):
    ##! [TESTING]
    catalog = control['model']
    ans = controller.req_1(catalog, country, exp, N)
    # mostRecent, NoJobsPerCountry, NoJobsPerExperienc
    print("El total de ofertas de trabajo ofrecidas según el país es: " + str(ans[1]) + "\n")
    print("El total de ofertas de trabajo ofre2cidas según la condición son : " + str(ans[2]) + "\n")
    mostRecent = ans[0]['elements']
    print("Las " + str(N) + " publicaciones más recientes dadas los criterios son: \n")
    print(tabulate(mostRecent, headers = "keys"))
    print("Se encontraron un total de: " +str(ans[3])+ " coincidentes con ciudad Y nivel de experiencia")
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """

    nombre_compañia= input("Ingrese el nombre de la compañia a conocer: ")
    ciudad= input("Ingrese la ciudad a conocer: ")
    print("Desea saber un numero especifico de ofertas? ")
    flag= input("Ingrese si o no: ")

    if flag== "si":
        n= input("Cual es la cantidad deseada: ")
    else:
        n=None

    total_ciudades, total_empresas, ofertas_info= controller.req_2(control, n, nombre_compañia, ciudad)

    print("El total de empresas es: ", total_empresas)
    print("El total de de ofertas: ", total_ciudades)

    headers = ["Fecha", "Pais", "Ciudad", "Titulo oferta", "Nivel experiencia", "Formato aplicación", "Tipo trabajo"]

    if n != None:
        print(ofertas_info)
        n= int(n)
        top_n_ofertas = []
        for oferta in ofertas_info[:n]:
            top_n_ofertas.append(list(oferta.values()))

        print(tabulate(top_n_ofertas, headers=headers, tablefmt="grid"))

    else:
        print("Las primeras 5: ")
        top5 = []
        for oferta in ofertas_info[:5]:
            top5.append(list(oferta.values()))

        print(tabulate(top5, headers=headers, tablefmt="grid"))    

        print("Las ultimas 5: ")
        last5 = []
        for oferta in ofertas_info[-5:]:
           last5.append(list(oferta.values()))

        print(tabulate(last5, headers=headers, tablefmt="grid"))
    

def print_req_3(control, company, startDate, endDate, N):
    catalog= control['model']
    ans = controller.req_3(catalog, company, startDate, endDate, N)
    # totaldeOffer, noByJunior, noByMid, noBySenior, table
    print("Número total de ofertas: " + str(ans[0]))
    print("Número total de ofertas con experticia junior: "+ str(ans[1]))
    print("Número total de ofertas con experticia mid: " + str(ans[2]))
    print("Número total de ofertas con experticia senior: " + str(ans[3]))
    table = ans[4]
    print(tabulate(table, headers = "keys"))


def print_req_4(control, CODpais, Ffirst, Flast):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    res = controller.req_4(control, CODpais, Ffirst, Flast)
    print(res[0])
    print("La cantidad de ofertas en el país en el periodo de consulta es "+str(res[0]))
    print("La cantidad de empresas que publicaron al menos una oferta es "+str(res[1]))
    print("La cantidad de ciudades en el país de consulta que publicaron ofertas es "+str(res[2]))
    print("La ciudad del país con mayor número de ofertas es "+str(res[3]["key"])+" con "+str(res[3]["value"])+" ofertas")
    print("La ciudad del país con menor número de ofertas es "+str(res[4]["key"])+" con "+str(res[4]["value"])+" ofertas")
    
    keep =["published_at","title", "company_name", "experience_level", "city", "workplace_type", "workplace_type", "open_to_hire_ukrainians"]
    table = coco.DicKeepOnly(keep, res[5], lt.size(res[5]))
    print(tabulate(table['elements'], headers = "keys"))
        
    

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    ciudad= input("Ingrese la ciudad deseada: ")
    print("Ingrese las fechas en formato YYYY-MM-DD")
    fecha_inicial= input("Ingrese la fecha incial: ")
    fecha_final= input("Ingrese la fecha final: ")
    total_ciudad, total_empresas, tupla_max, tupla_min, ofertas_sorted =controller.req_5(control, ciudad, fecha_inicial, fecha_final)
    empresa_max, conteo_empresa_max= tupla_max
    empresa_min, conteo_empresa_min= tupla_min
    
    print("Total de ofertas:", total_ciudad)
    print("Total de empresas:", total_empresas)
    print("Empresa con mayor cantidad de ofertas:", empresa_max, "con", conteo_empresa_max, "ofertas.")
    print("Empresa con menor cantidad de ofertas:", empresa_min, "con", conteo_empresa_min, "ofertas.")

    print("Las primeras 5 son: ")
    for oferta in ofertas_sorted[0:5]:
        oferta_data = [
            oferta["Fecha"],
            oferta["Titulo"],
            oferta["Nombre_empresa_oferta"],
            oferta["Tipo_lugar"],
            oferta["Tamaño_empresa"]
        ]
        print(tabulate([oferta_data], headers=["Fecha de Publicación", "Título de la Oferta", "Nombre de la Empresa", "Tipo de Lugar", "Tamaño de la Empresa"]))

    print("Las ultimas 5 son: ")
    for oferta in ofertas_sorted[-5:]:
        oferta_data = [
           oferta["Fecha"],
            oferta["Titulo"],
            oferta["Nombre_empresa_oferta"],
            oferta["Tipo_lugar"],
            oferta["Tamaño_empresa"]
        ]
        print(tabulate([oferta_data], headers=["Fecha de Publicación", "Título de la Oferta", "Nombre de la Empresa", "Tipo de Lugar", "Tamaño de la Empresa"]))
    
def print_req_6(control, exp, year, N):
    catalog = control['model']
    ans = controller.req_6(catalog, exp, year, N)
    # cityTotal, compTotal, totalOffers, maxCityName, maxCityCount, minCityName, minCityCount, GreatreturnList
    print("Total de ciudades que cumplen con las condiciones de la consulta " + str(ans[0]))
    print("El total de empresas que cumplen con las condiciones de la consulta " + str(ans[1]))
    print("El total de ofertas publicadas que cumplen con las condiciones de la consulta " + str(ans[2]))
    print('Nombre de la ciudad con mayor cantidad de ofertas de empleos y su conteo ' + str(ans[3]) + " conteo " + str(ans[4]))
    print('Nombre de la ciudad con menor cantidad de ofertas de empleos y su conteo ' + str(ans[5])+ " conteo " + str(ans[6]))
    print("----- No Values-----")
    pass


def print_req_7(control, numeroPaises, año, mes):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    res = controller.req_7(control, numeroPaises, año, mes)
    print(res[8])
    keep =['title',
            'street',
            'city',
            'country_code',
            'address_text',
            'marker_icon',
            'workplace_type',
            'company_name',
            'company_url',
            'company_size',
            'experience_level',
            'published_at',
            'remote_interview',
            'open_to_hire_ukrainians',
            'id',
            'display_offer',
            'contract_type',
            'currency_salary',
            'salary_from',
            'salary_to',
            'skill',
            'short_name']
    table = coco.DicKeepOnly(keep, res[7], lt.size(res[7]))
    print(tabulate(table['elements'], headers = "keys"))
    print("Número ofertas de empleo:",res[0])
    print("Número de ciudades:",res[3])
    print("País con mayor cantidad:",res[1])
    print("Ciudad con mayor cantidad:",res[2])
    print("\nPara Junior :")
    for dato in res[4]:
        print(dato)
    print("\nPara Mid :")
    for dato in res[5]:
        print(dato)
    print("\nPara Senior :")
    for dato in res[6]:
        print(dato)
    


def print_req_8(control,Nivel_experticia,Divisa,Ffirst,Flast):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    res=controller.req_8(control,Nivel_experticia,Divisa,Ffirst,Flast)
    print("Número empresas: ",res[0])
    print("Número ofertas: ",res[1])
    print("Número paises: ",res[2])
    print("Número ciudades: ",res[3])
    
    #print("Número ofertas con rango salarial: ",res[4])




# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    controller.load_data(control) #! [QUITAR/DEBUG/REMOVER]
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
            data = load_data(control)
            
        elif int(inputs) == 2:
            country = input("Digite el código de pais a consultar: ").upper()
            exp = input("Digite el nivel de experiencia a consultar: ")
            N = int(input("Digite el número de ofertas más recientes a listar: "))
            print_req_1(control, country, exp, N)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            company = input("Digite Nombre de la compañía a consultar: ")
            startDate = input("Digite fecha de inicio rango YYYY-MM-DD: ")
            endDate = input("Digite fecha de fin rango YYYY-MM-DD: ")
            N = int(input("Digite el número de ofertas más recientes a listar: "))
            print_req_3(control, company, startDate, endDate, N)

        elif int(inputs) == 5:
            CODpais=input("Ingrese el código del país para consulta: ")
            Ffirst=input("Ingrese la fecha inicial del periodo a consultar con formato (Año-Mes-Día): ")
            Flast=input("Ingrese la fecha final del periodo a consultar con formato (Año-Mes-Día): ")
            print_req_4(control, CODpais, Ffirst, Flast)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            country = input("Digite el código de pais a consultar: ").upper()
            exp = input("Digite el nivel de experiencia a consultar: ")
            year = input("Digite un año a consultar: ")
            N = int(input("Digite el número de ofertas más recientes a listar: "))
            print_req_6(control, exp, year, N)

        elif int(inputs) == 8:
            numeroPaises=int(input("Ingrese el número de paises a consultar: "))
            año=input("Ingrese el año de la consulta (con formato “%Y”): ")
            mes=input("Ingrese el mes de la consulta (con formato “%m”): ")
            print_req_7(control, numeroPaises, año, mes)

        elif int(inputs) == 9:
            Nivel_experticia = input("Ingrese el nivel de experticia a consultar: ")
            Divisa = input("Ingrese la divisa a consultar: ")
            Ffirst=input("Ingrese la fecha inicial del periodo a consultar con formato (Año-Mes-Día): ")
            Flast=input("Ingrese la fecha final del periodo a consultar con formato (Año-Mes-Día): ")
            print_req_8(control,Nivel_experticia,Divisa,Ffirst,Flast)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)