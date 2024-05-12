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
from datetime import datetime
import traceback

default_limit = 1000 
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def new_controller(data_size, data_structure, load_factor):
    """
    Se crea una instancia del controlador
    """
    control = controller.new_controller(data_size, data_structure, load_factor)
    return control

def print_menu():
    print("\nBIENVENIDO")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Configuración")
    print("0- Salir\n")


# Funciones para la carga de datos

def choose_data_structure():
    """
    Función que permite elegir la estructura de datos
    """
    print("""\nPor favor elija la estructura de datos que prefiera:
    1. Linear PROBING
    2. Separate CHAINING\n""")

    user_input = int(input("Seleccione una opción: "))

    if user_input == 1:
        data_structure = 'PROBING'
    else:
        data_structure = 'CHAINING'
    
    load_factor = float(input(f'Ingrese el factor de carga para la estructura de datos {data_structure}: '))
    
    return data_structure, load_factor 

def choose_data_size():
    """
    Función que permite cambiar el tamaño de los datos
    """
    print("""\nPor favor elija el tamaño de archivo a cargar:
    1. Small
    2. Medium
    3. Large
    4. Elegir porcentaje\n""")

    choice = int(input('Seleccione una opción: '))

    if choice == 1:
        return 'small', 120000
    elif choice == 2:
        return 'medium', 200000
    elif choice == 3:
        return 'large', 204000
    else:
        pct_input = int(input('Ingrese el porcentaje que desea ver: '))
        pct = (pct_input // 10) * 10

        if pct > 50:
            return str(pct) + '-por', 140000
        else:
            return str(pct) + '-por', 210000
        
def choose_sort_algorithm():
    """
    Función que permite elegir el algoritmo de ordenamiento
    """
    print("""\nSeleccione el algoritmo de ordenamiento:
    1. Selection Sort
    2. Insertion Sort
    3. Shell Sort
    4. Merge Sort
    5. Quick Sort\n""")
    
    choice = int(input('Seleccione una opción: '))

    return choice

def choose_memory_measurement():
    """
    Función que permite elegir si se desea medir la memoria
    """
    print("\nDesea observar el uso de memoria? (y/n)")
    
    memflag = input('Respuesta: ')
    memflag = castBoolean(memflag.lower())

    return memflag

def load_data(control, datasize, memflag):
    """
    Carga los datos
    """
    jobs, time, memory = controller.load_data(control, datasize, memflag)
    print("Datos cargados correctamente...")

    print_jobs(jobs, 3, 'load_data')

    return lt.size(jobs), time, memory


# Funciones para imprimir datos

def print_data(control, id, type):
    """
    Función que imprime datos dado su ID
    """
    if type == 'load_data':
        job = lt.getElement(control, id)
        job_date = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

        data = tabulate([
            ('Fecha de publicación: ', job_date),
            ('Titulo de la oferta: ', job['title']),
            ('Nombre de la empresa: ', job['company_name']),
            ('Nivel de experiencia: ', job['experience_level']),
            ('País: ', job['country_code']),
            ('Ciudad: ', job['city'])
        ])

    elif type == 'req-1':
        job = lt.getElement(control, id)
        job_date = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

        ucr = 'No'
        if job['open_to_hire_ukrainians'] == 'True':
            ucr = 'Si'

        data = tabulate([
        ('Fecha de publicación: ', job_date),
        ('Titulo de la oferta: ', job['title']),
        ('Nombre de la empresa: ', job['company_name']),
        ('Nivel de experiencia: ', job['experience_level']),
        ('País: ', job['country_code']),
        ('Ciudad: ', job['city']),
        ('Tamaño de la empresa: ', job['company_size']),
        ('Tipo de ubicación: ', job['workplace_type']),
        ('Disponible a contratar ucranianos: ', ucr)
        ])
    
    elif type == 'req-2':
        job = lt.getElement(control, id)
        job_date = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

        aplication = 'Entrevista presencial'
        if job['remote_interview'] == 'True':
            aplication = 'Entrevista remota'

        data = tabulate([
            ('Fecha de publicación: ', job_date),
            ('País: ', job['country_code']),
            ('Ciudad: ', job['city']),
            ('Nombre de la empresa: ', job['company_name']),
            ('Titulo de la oferta: ', job['title']),
            ('Nivel de experiencia: ', job['experience_level']),
            ('Formato de aplicación: ', aplication),
            ('Tipo de trabajo: ', job['workplace_type'])
        ])

    elif type == 'req-4':
        job = lt.getElement(control, id)
        job_date = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

        ucr = 'No'
        if job['open_to_hire_ukrainians'] == 'True':
            ucr = 'Si'

        data = tabulate([
            ('Fecha de publicación: ', job_date),
            ('Titulo de la oferta: ', job['title']),
            ('Nivel de experiencia: ', job['experience_level']),
            ('Nombre de la empresa: ', job['company_name']),
            ('Ciudad: ', job['city']),
            ('Tipo de trabajo: ', job['workplace_type']),
            ('Disponible a contratar ucranianos: ', ucr)
        ])

    elif type == 'req-6':
        city = lt.getElement(control, id)
        best_company, value = me.getKey(city['best_company']), me.getValue(city['best_company'])
        data = tabulate([
            ('Ciudad: ', city['name']),
            ('País: ', city['country']),
            ('Número total de ofertas: ', city['offers']),
            ('Salario promedio: ', f"{city['average_salary']:.0f}"),
            ('Empresas con ofertas: ', city['companies']),
            ('Empresa con mayor número de ofertas: ', best_company + ' - ' + str(value))
        ])
        print(data)
        
        print('La mejor oferta por salario de ' + city['name'] + ' es:')
        job = city['highest_salary']
        job_date = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        data = tabulate([
            ('Fecha de publicación: ', job_date),
            ('Titulo de la oferta: ', job['title']),
            ('Nombre de la empresa: ', job['company_name']),
            ('Nivel de experiencia: ', job['experience_level']),
            ('Salario: ', job['salary'])
        ])
        print(data)

        print('La peor oferta por salario de ' + city['name'] + ' es:')
        job = city['lowest_salary']
        job_date = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        data = tabulate([
            ('Fecha de publicación: ', job_date),
            ('Titulo de la oferta: ', job['title']),
            ('Nombre de la empresa: ', job['company_name']),
            ('Nivel de experiencia: ', job['experience_level']),
            ('Salario: ', job['salary'])
        ])
        print(data)
        data = '\n'

    elif type == 'req-8-part1':
        country = lt.getElement(control, id)

        if country['average_salary'] == 0:
            avg_salary = 'No aplica'
        else:
            avg_salary = f"{country['average_salary']:.0f}"

        data = tabulate([
            ('Código del país: ', country['code']),
            ('Salario promedio: ', avg_salary),
            ('Empresas con ofertas: ', country['companies']),
            ('Número total de ofertas: ', country['offers']),
            ('Ofertas con rango salarial: ', country['offers_with_salary']),
            ('Promedio de habilidades requeridas: ', int(country['average_skills']))
        ])

    elif type == 'req-8-part2':
        country = lt.getElement(control, id)

        avg_salary = 'No aplica'
        if country['average_salary'] != 0:
            avg_salary = f"{country['average_salary']:.0f}"

        if country['highest_salary'] == 0:
            country['highest_salary'] = 'No aplica'
        if country['lowest_salary'] == 1000000:
            country['lowest_salary'] = 'No aplica'
        
        data = tabulate([
            ('Código del país: ', country['code']),
            ('Número total de ofertas: ', country['offers']),
            ('Salario promedio: ', avg_salary),
            ('Ciudades con ofertas: ', country['cities']),
            ('Empresas con ofertas: ', country['companies']),
            ('Valor del mayor salario ofertado: ', country['highest_salary']),
            ('Valor del menor salario ofertado: ', country['lowest_salary']),
            ('Promedio de habilidades requeridas: ', int(country['average_skills']))
        ])

    print(data)

def print_jobs(control, sample, type):
    """
    Función que imprime las n ofertas de la lista
    """
    size = lt.size(control)
    
    if size == 1:
        print('\nLa única oferta encontrada es: ')
        print_data(control, 1, type)

    elif size <= sample*2:
        print("\nLas", size, "ofertas son:")
        i = 1
        while i <= size:
            print_data(control, i, type)
            i += 1

    else:
        print("\nLas", sample, "primeras ofertas son:")
        i = 1
        while i <= sample:
            print_data(control, i, type)
            i += 1

        print("\nLas", sample, "últimas ofertas son:")
        i = size - sample + 1
        while i <= size:
            print_data(control, i, type)
            i += 1

def print_cities(control, sample, type):
    """
    Funcion que imprime las n ciudades de la lista
    """
    size = lt.size(control)

    if size == 1:
        print('\nLa única ciudad encontrada es: ')
        print_data(control, i, type)
    
    elif size < sample*2:
        print("\nLas", size, "ciudades son:")
        i = 1
        while i <= size:
            print_data(control, i, type)
            i += 1

    else:
        print("\nLas", sample, "primeras ciudades son:")
        i = 1
        while i <= sample:
            print_data(control, i, type)
            i += 1

        print("\nLas", sample, "últimas ciudades son:")
        i = size - sample + 1
        while i <= size:
            print_data(control, i, type)
            i += 1

def print_countries(control, sample, type):
    """
    Funcion que imprime las n ciudades de la lista
    """
    size = lt.size(control)

    if size == 1:
        print('\nEl único país encontrado es: ')
        print_data(control, i, type)
    
    elif size < sample*2:
        print("\nLos", size, "paises son:")
        i = 1
        while i <= size:
            print_data(control, i, type)
            i += 1

    else:
        print("\nLos", sample, "primeros paises son:")
        i = 1
        while i <= sample:
            print_data(control, i, type)
            i += 1

        print("\nLos", sample, "últimos paises son:")
        i = size - sample + 1
        while i <= size:
            print_data(control, i, type)
            i += 1


def print_req_1(control, num, country, exp, memflag):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    filtered_jobs, country_offers, time, memory = controller.req_1(control, num, country, exp, memflag)

    if lt.size(filtered_jobs) == 0:
        return None, 0, 0
    
    print_jobs(filtered_jobs, 5, 'req-1')
    
    return lt.size(filtered_jobs), country_offers, time, memory

def print_req_2(control, num, company_name, city, memflag):
    """
    Función que imprime la solución del Requerimiento 2 en consola
    """
    filtered_jobs, time, memory = controller.req_2(control, num, company_name, city, memflag)

    if lt.size(filtered_jobs) == 0:
        return None, 0, 0
    
    print_jobs(filtered_jobs, 5, 'req-2')

    return lt.size(filtered_jobs), time, memory

def print_req_3(control, nombre_empresa, fecha_inicial, fecha_final):
    """
    Función que imprime la solución del Requerimiento 3 en consola
    """
    num_offers, num_junior, num_mid, num_senior, res, deltatime = controller.req_3(control, nombre_empresa, fecha_inicial, fecha_final)
    print(f"{deltatime:.3f}")
    print("numero total de ofertas: ", num_offers)
    print("numero total ofertas junior: ", num_junior)
    print("numero total ofertas mid: ", num_mid)
    print("numero total ofertas senior: ", num_senior)
    print(tabulate(lt.iterator(res), headers="keys", tablefmt="grid"))

def print_req_4(control, country, min_date, max_date, memflag):
    """
    Función que imprime la solución del Requerimiento 4 en consola
    """
    filtered_jobs, cities, companies, time, memory = controller.req_4(control, country, min_date, max_date, memflag)

    if filtered_jobs == None:
        return None, None, 0, 0, 0

    print_jobs(filtered_jobs, 5, 'req-4')

    return lt.size(filtered_jobs), cities, companies, time, memory

def print_req_5(control, ciudad, fecha_inicio, fecha_fin, memflag):
    """
    Función que imprime la solución del Requerimiento 5 en consola
    """
    offer_ciudad, empresas, maximo, minimo, res, time, memory = controller.req_5(control, ciudad, fecha_inicio, fecha_fin, memflag)
    print(tabulate(lt.iterator(res), headers = "keys", tablefmt = "grid"))

    print("El numero total de ofertas es: ", offer_ciudad)
    print("Total empresas: ", empresas)
    print("La empresa con mayor numero de ofertas es ", maximo["name"], "con un total de " , maximo["total"])
    print("La empresa con menor numero de ofertas es ", minimo["name"], "con un total de ", minimo["total"])

    delta_time = f"{time:.3f}"
    delta_memory = f"{memory:.3f}"

    print("\nTiempo de ejecución:", str(delta_time), "[ms]")
    print("Memoria utilizada:", str(delta_memory), "[kb]")

def print_req_6(control, num_cities, exp, year, memflag):
    """
    Función que imprime la solución del Requerimiento 6 en consola
    """
    filtered_cities, stadistics, time, memory = controller.req_6(control, num_cities, exp, year, memflag)

    if lt.size(filtered_cities) == 0:
        return None, 0, 0, 0
    
    print_cities(filtered_cities, 5, 'req-6')

    return filtered_cities, stadistics, time, memory

def print_req_7(control,num_countries, year, month):
    """
    Función que imprime la solución del Requerimiento 7 en consola
    """
    filtered_jobs, time, memory = controller.req_7(control, num_countries, year, month)

    return lt.size(filtered_jobs),time,memory

def print_req_8(control, exp, min_date, max_date, memflag):
    """
    Función que imprime la solución del Requerimiento 8 en consola
    """
    filtered_countries, stadistics, time, memory = controller.req_8(control, exp, min_date, max_date, memflag)

    if lt.size(filtered_countries) == 0:
        return None, 0, 0, 0
    
    print_countries(filtered_countries, 5, 'req-8-part1')

    return lt.size(filtered_countries), stadistics, time, memory


# Funciones adicionales

def settings(choice):
    """
    Configura las condiciones de la aplicación
    """
    if choice == 1: # Cambiar tamaño de los datos
        filename, data_size = choose_data_size()
        print('Has escogido el tamaño de archivo: ' + filename)
        print('\nSeleccione la opción 1 para volver a cargar los datos...')

        return filename, data_size

    elif choice == 2: # Cambiar la estructura de datos
        data_structure, load_factor = choose_data_structure()
        print('Ha escogido un factor de carga de: ' + str(load_factor))     
        print('\nSeleccione la opción 1 para volver a cargar los datos...')

        return data_structure, load_factor

    elif choice == 3: # Cambiar algoritmo de ordenamiento
        algorithm = choose_sort_algorithm()
        selected_algo = controller.set_sort_algorithm(algorithm)
        print("Eligió la configuración - " + selected_algo)

    elif choice == 4: # Cambiar medicion de memoria
        memflag = choose_memory_measurement()

        return memflag

    else:
        print('Regresando al menú principal...')

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('si', 's', 'yes', 'y', '1'):
        return True
    else:
        return False


# Se crea el controlador asociado a la vista
control = None
filename = None
data_structure = None
algorithm = None
memflag = None

def menu_cycle(control, filename, data_structure, algorithm, memflag):
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')

        if int(inputs) == 1: # Carga de datos
            if data_structure == None:
                data_structure, load_factor = choose_data_structure()
                print('Ha escogido un factor de carga de: ' + str(load_factor))      
        
            if filename == None:
                filename, data_size = choose_data_size()
                print('Ha escogido el tamaño de archivo: ' + filename)

            if algorithm == None:
                algorithm = choose_sort_algorithm()
                selected_algo = controller.set_sort_algorithm(algorithm)
                print("Eligió la configuración - " + str(selected_algo))

            if memflag == None:
                memflag = choose_memory_measurement()

            print("\nCargando información de los archivos ....\n")
            control = new_controller(data_size, data_structure, load_factor)

            jb, time, memory = load_data(control, filename, memflag)
            delta_time = f"{time:.3f}"
            delta_memory = f"{memory:.3f}"

            print("Total de ofertas de trabajo cargadas: " + str(jb))

            print("\nTiempo de ejecución:", str(delta_time), "[ms]")
            print("Memoria utilizada:", str(delta_memory), "[kb]")

        elif int(inputs) == 2: # Requerimiento 1
            country = input('\nIngrese el país a buscar: ')
            exp = input('Ingrese el nivel de experiencia: ')
            num = int(input('Ingrese la cantidad de ofertas que desea listar: '))

            req_1, country_offers, time, memory = print_req_1(control, num, country, exp, memflag)

            if req_1 != None:
                delta_time = f"{time:.3f}"
                delta_memory = f"{memory:.3f}"
                print(f"En {country.upper()} existen un total de {str(country_offers)} ofertas publicadas.")
                print(f"Para el nivel de experiencia seleccionado se obtuvieron {str(req_1)} ofertas.")
                print(f"\nTiempo de ejecución : {str(delta_time)} [ms]")
                print(f"Memoria utilizada: {str(delta_memory)} [kb]")
            else:
                print('No hay niguna oferta que cumpla con los criterios de busqueda.')

        elif int(inputs) == 3: # Requerimiento 2
            company_name = input('\nIngrese el nombre de la empresa a buscar: ')
            city = input('Ingrese la ciudad a buscar: ')
            num = int(input('Ingrese la cantidad de ofertas que desea listar: '))

            print('\nBuscando ofertas...')
            req_2, time, memory = print_req_2(control, num, company_name, city, memflag)

            if req_2 != None:
                delta_time = f"{time:.3f}"
                delta_memory = f"{memory:.3f}"
                print(f"Se obtuvieron un total de {str(req_2)} ofertas filtradas por el nombre de la empresa y ciudad.")
                print(f"\nTiempo de ejecución : {str(delta_time)} [ms]")
                print(f"Memoria utilizada: {str(delta_memory)} [kb]")
            else:
                print('\nNo hay niguna oferta que cumpla con los criterios de busqueda.')

        elif int(inputs) == 4: # Requerimiento 3
            nombre_empresa = input("Ingrese el nombre de la empresa:")
            fecha_inicial = input("Ingrese la fecha minima que desea analizar en formato yy-mm-dd (ej: 2023-02-13):")
            fecha_final = input("Ingrese la fecha maxima que desea analizar en formato yy-mm-dd (ej: 2023-02-13):")

            fecha_inicial = fecha_inicial + "T00:00:00.000Z"
            fecha_final = fecha_final + "T00:00:00.000Z"

            print_req_3(control, nombre_empresa, fecha_inicial, fecha_final)

        elif int(inputs) == 5: # Requerimiento 4
            country = input('\nIngrese el país a buscar: ')
            print("A continuación debe ingresar las fechas limites para la busqueda (ej. 2024-04-21)...")
            min_date = input('Ingrese el limite inferior de busqueda: ')
            max_date = input('Ingrese el limite superior de busqueda: ')

            min_date = f"{min_date}T00:00:00.000Z"
            max_date = f"{max_date}T00:00:00.000Z"

            print('\nBuscando ofertas...')
            req_4, cities, companies, time, memory = print_req_4(control, country, min_date, max_date, memflag)

            cities_size = lt.size(cities)
            highest = lt.firstElement(cities)
            lowest = lt.lastElement(cities)

            if req_4 != None:
                delta_time = f"{time:.3f}"
                delta_memory = f"{memory:.3f}"

                print("Se obtuvieron " + str(req_4) + " ofertas filtradas por país y un rango de fechas.")
                print('En total ' + str(companies) + ' empresas publicaron al menos una oferta.')
                print('Se registraron un total de ' + str(cities_size) + ' ciudades en las que se publicaron ofertas.')
                print('La ciudad con mayor número de ofertas es ' + highest['name'] + ' con un total de ' + str(highest['offers']))
                print('Las ciudades con menor número de ofertas (' + str(lowest['offers']) + ') son: ')

                for city in lt.iterator(cities):
                    if city['offers'] == lowest['offers']:
                        print('    · ' + city['name'])

                print(f"\nTiempo de ejecución : {str(delta_time)} [ms]")
                print(f"Memoria utilizada: {str(delta_memory)} [kb]")

            else:
                print('No hay niguna oferta que cumpla con los criterios de busqueda.')

        elif int(inputs) == 6: # Requerimiento 5
            ciudad = input("Ingrese el nombre de la ciudad a consultar: ")
            print("A continuación debe ingresar las fechas limites para la busqueda (ej. 2024-04-21)...")
            fecha_inicio = input("Ingrese la fecha inicial que desea analizar: ")
            fecha_fin = input("Ingrese la fecha final que desea analizar: ")
            
            fecha_inicio = fecha_inicio + "T00:00:00.000Z"
            fecha_fin = fecha_fin +  "T00:00:00.000Z"   
            print_req_5(control, ciudad, fecha_inicio, fecha_fin, memflag)        

        elif int(inputs) == 7: # Requerimiento 6
            num_cities = int(input('\nIngrese la cantidad de ciudades que desea listar: '))
            exp = input('Ingrese el nivel de experiencia a buscar: ')
            year = input('Ingrese el año de busqueda (ej. 2024): ')

            print('\nBuscando ciudades...')
            req_6, stadistics, time, memory = print_req_6(control, num_cities, exp, year, memflag)

            if req_6 != None:
                total_cities = lt.size(req_6)
                total_offers = stadistics[0]
                total_companies = stadistics[1]
                best_city = lt.firstElement(req_6)
                worst_city = lt.lastElement(req_6)

                delta_time = f"{time:.3f}"
                delta_memory = f"{memory:.3f}"

                print(f"Ciudades encontradas: {str(total_cities)}")
                print(f"Número de ofertas publicadas: {str(total_offers)}")
                print(f"Empresas con ofertas publicadas: {str(total_companies)}\n")

                print(f"La ciudad con mayor número de ofertas es {best_city['name']} con un total de {str(best_city['offers'])} ofertas.")
                print(f"La ciudad con menor número de ofertas es {worst_city['name']} con un total de {str(worst_city['offers'])} ofertas.")

                print(f"\nTiempo de ejecución : {str(delta_time)} [ms]")
                print(f"Memoria utilizada: {str(delta_memory)} [kb]")
                
            else:
                print('\nNo hay niguna oferta que cumpla con los criterios de busqueda.')

        elif int(inputs) == 8: # Requerimiento 7
            num_countries = int(input("Ingrese la cantidad de ciudades que desea listar: "))
            year = int(input("Ingrese el año de busqueda (ej. 2024): "))
            month = int(input("Ingrese el numero del mes de busqueda (ej. 07): "))

            req_7,time,memory = print_req_7(control, num_countries, year, month)

            print (req_7)

            
            """if req_7 != None:
                delta_time = f"{time:.3f}"
                delta_memory = f"{memory:.3f}"
                print(f"Se obtuvieron un total de ",req_7, " ciudades que cumplen con los parámetros de búsqueda.")
                
                print(f"\nTiempo de ejecución : {str(delta_time)} [ms]")
                print(f"Memoria utilizada: {str(delta_memory)} [kb]")
            else:
                print('\nNo hay niguna oferta que cumpla con los criterios de busqueda.')"""

        elif int(inputs) == 9: # Requerimiento 8
            exp = input('\nIngrese el nivel de experiencia a buscar: ')
            print("A continuación debe ingresar las fechas limites para la busqueda (ej. 2024-04-21)...")
            min_date = input('Ingrese el limite inferior de busqueda: ')
            max_date = input('Ingrese el limite superior de busqueda: ')

            min_date = f"{min_date}T00:00:00.000Z"
            max_date = f"{max_date}T00:00:00.000Z"
           
            req_8, stadistics, time, memory = print_req_8(control, exp, min_date, max_date, memflag)

            total_offers = stadistics[0]
            total_companies = stadistics[1]
            total_cities = stadistics[2]
            offers_with_offers = stadistics[3]
            offers_without_offers = stadistics[4]
            highest_country = stadistics[5]
            lowest_country = stadistics[6]

            if req_8 != None:
                print(f"Número de ofertas publicadas: {str(total_offers)}")
                print(f"Empresas con ofertas publicadas: {str(total_companies)}")
                print(f"Paises que cumplen las condiciones: {str(req_8)}")
                print(f"Ciudades que cumplen las condiciones: {str(total_cities)}")

                print(f'\nOfertas publicadas con salario: {str(offers_with_offers)}')
                print(f'Ofertas publicadas sin salario: {str(offers_without_offers)}')

                print('\nEl país con mayor oferta salarial es: ')
                print_data(highest_country, 1, 'req-8-part2')
                print('\nEl país con menor oferta salarial es: ')
                print_data(lowest_country, 1, 'req-8-part2')

                delta_time = f"{time:.3f}"
                delta_memory = f"{memory:.3f}"

                print(f"\nTiempo de ejecución : {str(delta_time)} [ms]")
                print(f"Memoria utilizada: {str(delta_memory)} [kb]")

            else:
                print('\nNo hay niguna oferta que cumpla con los criterios de busqueda.')

        elif int(inputs) == 10: # Configuraciones
            print("\nPor favor elije que deseas modificar: ")
            print('1. Tamaño de los datos')
            print('2. Estructura de datos')
            print('3. Algoritmo de ordenamiento')
            print('4. Medición de memoria')
            print('0. Cancelar\n')
            user_input = int(input("Selecciona una opción: "))

            change = settings(user_input)

            if user_input == 1:
                filename, data_size = change
            elif user_input == 2:
                data_structure, load_factor = change
            elif user_input == 4:
                memflag = change

        elif int(inputs) == 0: # Salir
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

# main del reto
if __name__ == "__main__":
    menu_cycle(control, filename, data_structure, algorithm, memflag)