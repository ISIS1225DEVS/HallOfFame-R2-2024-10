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
    return controller.new_controller()
   


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


def load_data(control, mem =False):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    return controller.load_data(control, memflag = mem)


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(total_offers, offers_country, offers_experience):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print("Ofertas por país: " + str(offers_country))
    print("Ofertas por experiencia: " + str(offers_experience))
    print()
    columns = ['published_at', 'title', 'company_name', 'experience_level', 'country_code', 'city', 'company_size', 'workplace_type', 'open_to_hire_ukrainians']
    view = view_data(total_offers, columns)
    if view[1]:
        print('\nPrimeros 5 Datos\n')
        print(tabulate(view[0][0],headers='keys'))
        print('\nÚltimos 5 Datos\n')
        print(tabulate(view[0][1],headers='keys'))
    else:
        print(tabulate(view[0],headers='keys'))


def print_req_2(jobs_found,n_sublist, company, city):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    columns = ['published_at','country_code','city','company_name','title','experience_level','remote_interview','workplace_type']
    view = view_data(n_sublist, columns)
    if view[1]:
        print('\nPrimeros 5 Datos\n')
        print(tabulate(view[0][0],headers='keys'))
        print('\nÚltimos 5 Datos\n')
        print(tabulate(view[0][1],headers='keys'))
    else:
        print(tabulate(view[0],headers='keys'))
    
    print ('\nTotal de ofertas encontradas de ' + company + ' en ' + city + ': ' + str(jobs_found) + '\n')

def print_req_3(total_ofertas,junior,mid,senior,jobs_in_dates):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    msg = 'Se obtuvo la siguiente información: \n'
    msg += '\nEl total de ofertas de la empresa en el periodo de consulta: '+ str(total_ofertas)
    msg += '\nEl total de ofertas publicadas con experiencia JUNIOR es: '+ str(junior)
    msg += '\nEl total de ofertas publicadas con experiencia MID es: '+ str(mid)
    msg += '\nEl total de ofertas publicadas con experiencia SENIOR es: '+ str(senior)

    columns = ['published_at','title','experience_level','company_name','city','workplace_type','remote_interview','open_to_hire_ukrainians']
    view = view_data(jobs_in_dates, columns)
    if view[1]:
        print('\nPrimeros 5 Datos\n')
        print(tabulate(view[0][0],headers='keys'))
        print('\nÚltimos 5 Datos\n')
        print(tabulate(view[0][1],headers='keys'))
    else:
        print(tabulate(view[0],headers='keys'))
    
    print(msg)


def print_req_4(n_offers, n_companies , n_cities , city_max , n_city_max , city_min , n_city_min ,jobs_in_dates):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    msg = 'Se obtuvo la siguiente información: \n'
    msg += '\nEl total de ofertas en el país en el periodo de consulta: '+ str(n_offers)
    msg += '\nEl total de empresas que publicaron al menos una oferta en el país de consulta: '+ str(n_companies)
    msg += '\nNúmero total de ciudades del país de consulta en las que se publicaron ofertas: '+ str(n_cities)
    msg += '\nLa ciudad con mayor numero de ofertas fue '+ city_max + ' con ' + str(n_city_max) + ' ofertas.' 
    msg += '\nLa ciudad con menor numero de ofertas fue '+ city_min + ' con ' + str(n_city_min) + ' ofertas.'

    columns = ['published_at','title','experience_level','company_name','city','workplace_type','remote_interview','open_to_hire_ukrainians']
    view = view_data(jobs_in_dates, columns)
    if view[1]:
        print('\nPrimeros 5 Datos\n')
        print(tabulate(view[0][0],headers='keys'))
        print('\nÚltimos 5 Datos\n')
        print(tabulate(view[0][1],headers='keys'))
    else:
        print(tabulate(view[0],headers='keys'))
    
    print(msg)


def print_req_5(n_companies, n_offers, company_max, company_n_max, company_min, company_n_min, offers_in_dates):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    msg = ""
    msg = 'Se obtuvo la siguiente información: \n'
    msg += '\nEl total de ofertas en la ciudad en el periodo de consulta: '+ str(n_offers)
    msg += '\nEl total de empresas que publicaron al menos una oferta en la ciudad de consulta: '+ str(n_companies)
    msg += '\nLa empresa con mayor numero de ofertas fue '+ company_max + ' con ' + str(company_n_max) + ' ofertas.' 
    msg += '\nLa empresa con menor numero de ofertas fue '+ company_min + ' con ' + str(company_n_min) + ' ofertas.'

    columns = ['published_at','title','company_name','workplace_type','company_size']
    view = view_data(offers_in_dates, columns)
    if view[1]:
        print('\nPrimeros 5 Datos\n')
        print(tabulate(view[0][0],headers='keys'))
        print('\nÚltimos 5 Datos\n')
        print(tabulate(view[0][1],headers='keys'))
    else:
        print(tabulate(view[0],headers='keys'))
    
    print(msg)


def print_req_6(control, amount_cities, level_expertise, year):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    info, deltatime = controller.req_6(control, amount_cities, level_expertise, year)
    tabular, n_cities, n_companies, best_city, worst_city, amountoffers = info
    print("Requerimiento 6 --- Respuesta\n")
    print(f"El tiempo utilizado fue de {deltatime} milisegundos\n")
    print(f"Se obtuvieron {n_cities} ciudades que cumplen con los criterios de busqueda\n")
    print(f"Se obtuvieron {n_companies} empresas que cumplen con los criterios de busqueda\n")
    print(f"Se obtuvieron {amountoffers} ofertas que cumplen los criterios de busqueda")
    
    print("La ciudad con mayor cantidad de ofertas fue: \n")
    tabular_best_city = [mp.get(best_city, 'city')['value'], lt.size(mp.get(best_city, 'offers')['value']), lt.size(mp.get(best_city, 'list_companies')['value'])]
    print(tabulate([tabular_best_city], headers=['Ciudad', 'Cantidad de ofertas', 'Cantidad de empresas'], tablefmt='grid'))
    
    print("\nLa ciudad con menor cantidad de ofertas fue: \n")
    tabular_worst_city = [mp.get(worst_city, 'city')['value'], lt.size(mp.get(worst_city, 'offers')['value']), lt.size(mp.get(worst_city, 'list_companies')['value'])]
    print(tabulate([tabular_worst_city], headers=['Ciudad', 'Cantidad de ofertas', 'Cantidad de empresas'], tablefmt='grid'))
    
    print(f"El top {amount_cities} de ciudades con mayor cantidad de ofertas de trabajo en el año {year} por nivel de experticia {level_expertise} fue: \n")
    
    headers = ["Nombre", "Pais", "# Ofertas", "Salario Promedio", "# Companies", "Mejor Empresa", "Mejor Oferta", "Peor Oferta"]
    
    print(tabulate(tabular, headers=headers, tablefmt='grid' ,maxcolwidths=[None, None, None, 15, None, 20, 30, 30]))
    
    
def print_req_7(total_offers,  total_cities , highest_country , highest_n_country, city_max , city_n_max , junior_ans , mid_ans , senior_ans):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    primera_parte = [{'Total de ofertas':total_offers,
                     'Número de ciudades \ndonde se ofertó':total_cities,
                     'Nombre del país con \nmayor cantidad de ofertas y su conteo': (highest_country,highest_n_country),
                     'Nombre de la ciudad con \nmayor cantidad de ofertas y su conteo': (city_max,city_n_max),
                     }]
    print(tabulate(primera_parte,headers='keys'))
    print('\nA continuación se encuentra la información en conjunto de los países dividida por cada nivel de experticia\n')
    
    data_name = '\nCálculos para junior\n','\nCálculos para mid\n','\nCálculos para senior\n'
    data = junior_ans , mid_ans , senior_ans
    i = 0
    while i<3:
        print(data_name[i])
        experience = data[i]
        segunda_parte = [{'Conteo de habilidades \ndiferentes':experience[0],
                         'Habilidad más\n solicitada,conteo': (experience[1],experience[2]),
                         'Habilidad menos\n solicitada, conteo':(experience[3],experience[4]),
                         'Nivel mínimo promedio \nde las habilidades':experience[5],
                         'Empresas que \npublicaron una oferta \ncon este nivel':experience[6],
                         'Empresa con \nmayor número de\n ofertas, conteo': (experience[7],experience[8]),
                         'Empresa con \nmenor número de\n ofertas, conteo': (experience[9],experience[10]),
                         'Empresas del nivel que \ntienen una o más sedes': experience[11]
                         }]
        print(tabulate(segunda_parte,headers='keys', colalign=("left", "left"),tablefmt="pretty", numalign="center", stralign='center'))
        i +=1


def print_req_8(part_1, part_2):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    
    total_companies, total_offers,total_countries, total_cities, range_salary, fixed_salary, no_salary, countries_ans = part_1
    most_salary, least_salary = part_2
    columns = ['País','Promedio de oferta salarial','Número de empresas que publicaron','Numero de ofertas publicadas','Número de ofertas con salario', 'Número promedio de habilidades por oferta']
    view = view_data(countries_ans, columns)
    if view[1]:
        print('\nPrimeros 5 Datos\n')
        print(tabulate(view[0][0],headers='keys',tablefmt="pretty"))
        print('\nÚltimos 5 Datos\n')
        print(tabulate(view[0][1],headers='keys',tablefmt="pretty"))
    else:
        print(tabulate(view[0],headers='keys',tablefmt="pretty"))
    
    print ('\nTotal de empresas que publicaron ofertas: ' + str(total_companies))
    print ('\nNúmero total de ofertas de empleo que cumplen la consulta: ' + str(total_offers))
    print ('\nNúmero de países que cumplan la consulta: ' + str(total_countries))
    print('\nNúmero de ciudades que cumplan la consulta: '+ str(total_cities))
    print('\nNúmero de ofertas publicadas con rango salarial: '+ str(range_salary))
    print('\nNúmero de ofertas publicadas con valor fijo de salario: '+ str(fixed_salary))
    print('\nNúmero de ofertas publicadas sin salario: '+ str(no_salary))
    
    print('\nPais con el mayor promedio de salario: ' )
    for key, value in most_salary.items():
        print(f"{key}: {value}")
    
    print('\nPais con el menor promedio de salario: ' )
    for key, value in least_salary.items():
        print(f"{key}: {value}")
    
          
def print_load_data_answer(answer,control):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if len(answer)>2:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[1]:.3f}", "||",
              "Cantidad de ofertas de trabajo cargadas: "+ str(answer[2]))

    else:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}","||",
              "Cantidad de ofertas de trabajo cargadas: "+ str(answer[1]))
    
    primeros_tres(control['model']['jobs'])
    ultimos_tres(control['model']['jobs'])

def cast_boolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False

def view_data(control, keys):
    return controller.view_data(control,keys)

def ultimos_tres(lst):
    #Retorna una tupla con los últimos tres elementos de la lista
    columns = ['title','city','country_code','company_name','experience_level','published_at']
    size = lt.size(lst)
    last_3 = lt.subList(lst,size-3,3)
    table = view_data(last_3,columns)
    print('\nLos últimos tres elementos de la lista son: \n')
    print(tabulate(table[0],headers='keys'))

def primeros_tres(lst):
    #Retorna una tupla con los primeros tres elementos de la lista}
    columns = ['title','city','country_code','company_name','experience_level','published_at']
    first_3 = lt.subList(lst,1,3)
    table = view_data(first_3,columns)
    print('\nLos primeros tres elementos de la lista son: \n')
    print(tabulate(table[0],headers='keys'))

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
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = cast_boolean(mem)
            print("Cargando información de los archivos ....\n")
            data = load_data(control,mem=mem)
            print_load_data_answer(data,control)
            
        elif int(inputs) == 2:
            n_offers = int(input("Ingrese el número de ofertas a consultar: "))
            country_code = input("Ingrese el código del país: ")
            experience_level = input("Ingrese el nivel de experiencia: ")
            print()
            
            info, delta_time = controller.req_1(control, n_offers, country_code, experience_level)
            DeltaTime = f"{delta_time:.3f}"
            if info is not None:
                total_offers, offers_country, offers_experience = info
                print_req_1(total_offers, offers_country, offers_experience)
                print('\nTiempo medido:'+ str(DeltaTime)+'[ms]')
            else:
                print("No se encontraron ofertas con los parámetros ingresados ")
                print()

        elif int(inputs) == 3:
            n = int(input('Ingrese el número de ofertas de trabajo que desea consultar: '))
            company = input('Ingrese el nombre de la empresa: ')
            city = input('Ingrese el nombre de la ciudad: ')
            
            info, delta_time = controller.req_2(control, n, company, city)
            DeltaTime = f"{delta_time:.3f}"
            
            if info is not None:
                jobs_found,n_sublist = info
                print_req_2(jobs_found,n_sublist, company, city)
                print('\nTiempo medido:'+ str(DeltaTime)+'[ms]')

        elif int(inputs) == 4:
            empresa = input('\nIngrese el nombre de la empresa que desea consultar: ')
            fecha1 = input('\nFecha inicial en formato %Y-%m-%d: ')
            fecha2 = input('\nFecha final en formato %Y-%m-%d: ')
            print('\nA continuación se mostrará el listado de ofertas ordenado cronológicamente. En caso de tener la misma fecha se ordena según el código de país.\n')
            print('\nCargando información...\n')
            info, delta_time = controller.req_3(control,empresa,fecha1,fecha2)
            DeltaTime = f"{delta_time:.3f}"
            
            if info is not None:
                total_ofertas,junior,mid,senior,jobs_in_dates = info
                print_req_3(total_ofertas,junior,mid,senior,jobs_in_dates)
                print('\nTiempo medido:'+ str(DeltaTime)+'[ms]')
            else: 
                print('No se halló una oferta')

        elif int(inputs) == 5:
            country = input('\nIngrese el código del país de consulta: ')
            start = input('\nFecha inicial en formato %Y-%m-%d: ')
            end = input('\nFecha final en formato %Y-%m-%d: ')
            print('\nA continuación se mostrará el listado de ofertas ordenado cronológicamente. En caso de tener la misma fecha se ordena según el nombre de la compañía.\n')
            print('\nCargando información...\n')
            info, delta_time = controller.req_4(control,country,start,end)
            DeltaTime = f"{delta_time:.3f}"
            
            if info is not None:
                n_offers, n_companies , n_cities , city_max , n_city_max , city_min , n_city_min ,jobs_in_dates = info
                print_req_4(n_offers, n_companies , n_cities , city_max , n_city_max , city_min , n_city_min ,jobs_in_dates)
                print('\nTiempo medido:'+ str(DeltaTime)+'[ms]\n')
            else: 
                print('No se halló una oferta en el periodo especificado para el país '+ country)
  

        elif int(inputs) == 6:
            city = input('\nIngrese el nombre de la ciudad de consulta: ')
            starting_date = input('\nFecha inicial en formato %Y-%m-%d: ')
            ending_date = input('\nFecha final en formato %Y-%m-%d: ')
            print('\nCargando información...\n')
            print()
            info, delta_time = controller.req_5(control,city,starting_date,ending_date)
            DeltaTime = f"{delta_time:.3f}"
            
            if info is not None:
                n_companies, n_offers, company_max, company_n_max, company_min, company_n_min, offers_in_dates = info
                print_req_5(n_companies, n_offers, company_max, company_n_max, company_min, company_n_min, offers_in_dates)
                print('\nTiempo medido:'+ str(DeltaTime)+'[ms]')
            else:
                print('No se halló una oferta en el periodo especificado para la ciudad '+ city)

        elif int(inputs) == 7:
            print("Requerimiento 6 - Clasificar las N ciudades con mayor número de ofertas de trabajo de un año por experticia\n")
            amount_cities = input("Ingrese el número de ciudades a consultar: ")
            level_expertise = input("Ingrese el nivel de experiencia (junior, mid, senior, IND): ")
            if level_expertise not in ['junior', 'mid', 'senior']:
                level_expertise = None
            year = input("Ingrese el año a consultar: ")
            
            print_req_6(control, amount_cities, level_expertise, year)

        elif int(inputs) == 8:
            best_n_countries = input('\nIngrese el número de paises para la consulta: ')
            year = input('\nAño (yyyy): ')
            month = input('\nMes (MM): ')
            print('\nCargando información...\n')
            info,delta_time = controller.req_7(control,best_n_countries,year,month)
            DeltaTime = f"{delta_time:.3f}"
            if info is not None:
                total_offers,  total_cities , highest_country , highest_n_country, city_max , city_n_max , junior_ans , mid_ans , senior_ans = info
                print_req_7(total_offers,  total_cities , highest_country , highest_n_country, city_max , city_n_max , junior_ans , mid_ans , senior_ans)
                print('\nTiempo medido:'+ str(DeltaTime)+'[ms]')
            else: 
                print('No se hallaron ofertas para estas fechas')
           

        elif int(inputs) == 9:
            experience = input('\nIngrese el nivel de experiencia ("IND" para indiferente): ')
            currency = input('\nIngrese la divisa: ')
            start = input('\nFecha inicial en formato %Y-%m-%d: ')
            end = input('\nFecha final en formato %Y-%m-%d: ')
            info,delta_time = controller.req_8(control,experience,currency,start,end)
            DeltaTime = f"{delta_time:.3f}"
            if info is not None:
                part_1, part_2 = info
                print_req_8(part_1, part_2)
                print('\nTiempo medido:'+ str(DeltaTime)+'[ms]')
            else:
                print('No se halló información para la consulta')
            

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)