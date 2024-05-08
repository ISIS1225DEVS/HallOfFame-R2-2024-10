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
#from tabulate import tabulate
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


def load_data(control, size_str):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    size = controller.load_data(control, size_str)
    return size


def print_data(data, data_structs):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    size_jobs = data[0]
    size_paises = data[1]
    size_ciudades = data[2]
    size_empresas = data[3]
    size_years = data[4]
    size_skills = data[5]
    size_employment_types = data[6]
    size_multilocations = data[7]
    print ("-------------------------------------------")
    print ("Total de ofertas de trabajo cargadas: ", size_jobs)
    print ("-------------------------------------------")
    print ("Total de paises cargados: ", size_paises)
    print ("-------------------------------------------") 
    print ("Total de ciudades cargadas: ", size_ciudades)
    print ("-------------------------------------------")
    print ("Total de empresas cargadas: ", size_empresas)
    print ("-------------------------------------------")
    print ("Total de años cargados: ", size_years)
    print ("-------------------------------------------")
    print ("Total de skills cargadas: ", size_skills)
    print ("-------------------------------------------")
    print ("Total de tipos de empleo: ", size_employment_types)
    print ("-------------------------------------------")
    print ("Total de trabajos con multilocations: ", size_employment_types)
    print ("-------------------------------------------")
    print("\n")
    print ("-------------------------------------------")
    print("Tiempo [ms]: ", f"{data[8]:.3f}", "||",
        "Memoria [kB]: ", f"{data[9]:.3f}")
    print ("-------------------------------------------")     

def print_req_1(ofertas, ultimos):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    elem = ofertas["elements"]
    size = lt.size(ofertas)
    print ("-"*40)
    print ("Total de ofertas cargadas: ", size)
    print ("-"*40)
    if size < ultimos:
        for job in elem:
            print("|" + ' FECHA: ' + job['published_at'] + "|"  + 'TITULO: ' + job['title'] + "|" + ' COMPANY: ' +
                job['company_name'] + "|" + "EXPERIENCIA: " + job["experience_level"] + "|" +
                ' PAIS: ' + job['country_code'] + "|" + ' CITY: ' + job['city'] + "|" + 
                ' TAMAÑO: ' + job['company_size'] + "|" + ' TIPO DE UBICACION: ' + job['workplace_type'] + "|" + 
                ' DISPONIBLE A CONTRATAR UCRANIANOS: ' + job['open_to_hire_ukrainians'])
    else:
        for i in range(ultimos):
            job = elem[i]
            print("|" + ' FECHA: ' + job['published_at'] + "|"  + 'TITULO: ' + job['title'] + "|" + ' COMPANY: ' +
                job['company_name'] + "|" + "EXPERIENCIA: " + job["experience_level"] + "|" +
                ' PAIS: ' + job['country_code'] + "|" + ' CITY: ' + job['city'] + "|" + 
                ' TAMAÑO: ' + job['company_size'] + "|" + ' TIPO DE UBICACION: ' + job['workplace_type'] + "|" + 
                ' DISPONIBLE A CONTRATAR UCRANIANOS: ' + job['open_to_hire_ukrainians'])



def print_req_2(ofertas, ultimos):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    elem = ofertas["elements"]
    size = lt.size(ofertas)
    print ("-"*40)
    print ("Total de ofertas cargadas: ", size)
    print ("-"*40)
    if size < ultimos:
        for job in elem:
            print("|" + ' FECHA: ' + job['published_at'] + "|"  + 'TITULO: ' + job['title'] + "|" + ' COMPANY: ' +
                job['company_name'] + "|" + "EXPERIENCIA: " + job["experience_level"] + "|" +
                ' PAIS: ' + job['country_code'] + "|" + ' CITY: ' + job['city'] + "|" + 
                ' TAMAÑO: ' + job['company_size'] + "|" + ' TIPO DE UBICACION: ' + job['workplace_type'] + "|" + 
                ' DISPONIBLE A CONTRATAR UCRANIANOS: ' + job['open_to_hire_ukrainians'])
    else:
        for i in range(ultimos):
            job = elem[i]
            print("|" + ' FECHA: ' + job['published_at'] + "|"  + 'TITULO: ' + job['title'] + "|" + ' COMPANY: ' +
                job['company_name'] + "|" + "EXPERIENCIA: " + job["experience_level"] + "|" +
                ' PAIS: ' + job['country_code'] + "|" + ' CITY: ' + job['city'] + "|" + 
                ' TAMAÑO: ' + job['company_size'] + "|" + ' TIPO DE UBICACION: ' + job['workplace_type'] + "|" + 
                ' DISPONIBLE A CONTRATAR UCRANIANOS: ' + job['open_to_hire_ukrainians'])



def print_req_3(ofertas, empresa):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    lista_ofertas = ofertas[0]
    size = ofertas[1]
    print ("-"*40)
    print ("Total de ofertas cargadas: ", size)
    print ("-"*40)
    print("Total de ofertas con experticia JUNIOR: ", ofertas[2])
    print("Total de ofertas con experticia MID: ", ofertas[3])
    print("Total de ofertas con experticia SENIOR: ", ofertas[4])
    print ("-"*40)
        
    
    if size < 10:
        print ("-------------------------------------------")
        print("Las ofertas de ", empresa, " son las siguientes: ")
        print("\n")
        for element in lt.iterator(lista_ofertas):
            print("|" + "DATE: " + str(element["published_at"]) + "|" + "JOB: " + str(element["title"]) + "|" + "EXPERIENCE LEVEL: " + str(element["experience_level"]) + " CITY: " + str(element["city"]) + "|" + "COUNTRY: " + str(element["country_code"]) + "|" + "COMPANY SIZE: " + str(element["company_size"]) + "|" + "WORKPLACE TYPE: " + str(element["workplace_type"]) + "|" + "OPEN TU HIRE UKRAINIANS: " + str(element["open_to_hire_ukrainians"]) + "|" )
        print ("-------------------------------------------")
        print("\n")
    
    else:
        elements =lista_ofertas["elements"]
        print ("-------------------------------------------")
        print("Las primeras 5 ofertas de ", empresa, " son las siguientes: ")
        print("\n")
        for element in elements[:5]:
            print("|" + "DATE: " + str(element["published_at"]) + "|" + "JOB: " + str(element["title"]) + "|" + "EXPERIENCE LEVEL: " + str(element["experience_level"]) + " CITY: " + str(element["city"]) + "|" + "COUNTRY: " + str(element["country_code"]) + "|" + "COMPANY SIZE: " + str(element["company_size"]) + "|" + "WORKPLACE TYPE: " + str(element["workplace_type"]) + "|" + "OPEN TU HIRE UKRAINIANS: " + str(element["open_to_hire_ukrainians"]) + "|" )
        print("\n")
        print ("-------------------------------------------")
        print("Las últimas 5 ofertas de ", empresa, " son las siguientes: ")
        print("\n")
        for element in elements[- 5:]:
            print("|" + "DATE: " + str(element["published_at"]) + "|" + "JOB: " + str(element["title"]) + "|" + "EXPERIENCE LEVEL: " + str(element["experience_level"]) + " CITY: " + str(element["city"]) + "|" + "COUNTRY: " + str(element["country_code"]) + "|" + "COMPANY SIZE: " + str(element["company_size"]) + "|" + "WORKPLACE TYPE: " + str(element["workplace_type"]) + "|" + "OPEN TU HIRE UKRAINIANS: " + str(element["open_to_hire_ukrainians"]) + "|" )
        print("\n")
        print ("-------------------------------------------")
        print("\n")


def print_req_4(ofertas):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    size = lt.size(ofertas)
    print ("-"*40)
    print ("Total de ofertas cargadas: ", size)
    print ("-"*40)
    company = mp.newMap()
    city = mp.newMap()
    for job in lt.iterator(ofertas):
        if mp.contains(company, job["company_name"]) == False:
            mp.put(company, job["company_name"], 1)
        if mp.contains(city, job["city"]) == False:
            mp.put(city, job["city"], 1)
    print ("Total de empresas que publicaron al menos una oferta: ", mp.size(company))
    print ("-"*40)
    print ("Total de ciudades en las que se publicaron ofertas: ", mp.size(city))
    print ("-"*40)
    city_count = mp.newMap()
    for job in lt.iterator(ofertas):
        if mp.contains(city_count, job["city"]) == False:
            mp.put(city_count, job["city"], 1)
        else:
            city = mp.get(city_count, job["city"])
            value = me.getValue(city)
            mp.put(city_count, job["city"], value+1)
    key = mp.keySet(city_count)
    value = mp.valueSet(city_count)
    maximo = 0
    city_max = ""
    minimo = 0
    city_min = ""
    for k in lt.iterator(key):
        city_data = mp.get(city_count, k)
        num_ofertas = me.getValue(city_data)
        if minimo == 0:
            minimo = num_ofertas
        if int(num_ofertas) > maximo:
            maximo = num_ofertas
            city_max = str(k)
        if int(num_ofertas) < minimo:
            minimo  = num_ofertas
            city_min = str(k)
    print ("Ciudad del país con mayor número de ofertas y su conteo: " + str(city_max) + " -> " + str(maximo))
    print ("-"*40)
    print ("Ciudad del país con menor número de ofertas y su conteo: " + str(city_min) + " -> " + str(minimo))
    print ("-"*40)
    
    if size <= 10:
        for job in lt.iterator(ofertas):
            print("|" + 'FECHA: ' + job['published_at'] + " |"  + 'TITULO: ' + job['title'] + " |" + 
                "EXPERIENCIA: " + job["experience_level"] + " |" + 'COMPANY: ' + job['company_name'] + " |" +
                'CITY: ' + job['city'] + " |" + 'TIPO DE UBICACION: ' + job['workplace_type'] + " |" + 
                'DISPONIBLE A CONTRATAR UCRANIANOS: ' + job['open_to_hire_ukrainians'])
        print ("-------------------------------------------")
    else:
        elements = ofertas["elements"]
        print("Los primeros 5 elementos son los siguientes: ")
        print("\n")
        for job in elements[:5]:
            print("|" + 'FECHA: ' + job['published_at'] + " |"  + 'TITULO: ' + job['title'] + " |" + 
                "EXPERIENCIA: " + job["experience_level"] + " |" + 'COMPANY: ' + job['company_name'] + " |" +
                'CITY: ' + job['city'] + " |" + 'TIPO DE UBICACION: ' + job['workplace_type'] + " |" + 
                'DISPONIBLE A CONTRATAR UCRANIANOS: ' + job['open_to_hire_ukrainians'])
        print("\n")
        print ("-"*40)
        print("Los ultimos 5 elementos son los siguientes: ")
        print("\n")
        for job in elements[- 5:]:
            print("|" + 'FECHA: ' + job['published_at'] + " |"  + 'TITULO: ' + job['title'] + " |" + 
                "EXPERIENCIA: " + job["experience_level"] + " |" + 'COMPANY: ' + job['company_name'] + " |" +
                'CITY: ' + job['city'] + " |" + 'TIPO DE UBICACION: ' + job['workplace_type'] + " |" + 
                'DISPONIBLE A CONTRATAR UCRANIANOS: ' + job['open_to_hire_ukrainians'])
        print("\n")
        print ("-"*40)
        print("\n")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(ofertas):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    city_map, total_ciudades, total_empresas, total_ofertas, nombre_mayor_ciudad, conteo_mayor_ciudad, nombre_menor_ciudad, conteo_menor_ciudad, salarios, top_ranked_ciudades, data_structs = ofertas
    # TODO: Imprimir el resultado del requerimiento 6
    
    print ("-"*40)
    print("Total de ofertas cargadas: ", total_ofertas)
    print ("-"*40)
    print ("Total de empresas que cumplen con las condiciones de la consulta: ", total_empresas)
    print ("-"*40)
    print ("Total de ciudades que cumplen con las condiciones de la consulta: ", total_ciudades)
    print ("-"*40)
    print ("Ciudad con mayor número de ofertas y su conteo: " + str(nombre_mayor_ciudad) + " -> " + str(conteo_mayor_ciudad))
    print ("-"*40)
    print ("Ciudad con menor número de ofertas y su conteo: " + str(nombre_menor_ciudad) + " -> " + str(conteo_menor_ciudad))
    print ("-"*40)

    size = mp.size(city_map)
    
    if size <= 10:
        for city_element in lt.iterator(top_ranked_ciudades):
            city = city_element["ciudad"]
            entry = mp.get(city_map, city)
            city_value = me.getValue(entry)
            pais = city_value["elements"][0]["country_code"]
            size = lt.size(city_value) 
            
            company_list = lt.newList("ARRAY_LIST")
            for company in city_value["elements"]:
                if lt.isPresent(company_list, company["company_name"]) == 0:
                    lt.addLast(company_list, company["company_name"])    
            total_empresas = lt.size(company_list)
            
            empresa_mayor_oferta = controller.empresa_con_mas_ofertas(control, city_value)
            nombre_mayor_empresa, conteo_mayor_empresa = empresa_mayor_oferta
            
            total_salario_ciudad = 0
            mejor_salario = 0
            peor_salario = 0
            oferta_mejor_salario = ""
            oferta_peor_salario = ""
            for job in lt.iterator(city_value):
                salary = encontrar_salario(data_structs, job["id"], salarios)
                if salary == "":
                    continue
                else:
                    total_salario_ciudad += int(salary)
                    if peor_salario == 0:
                        peor_salario = int(salary)
                    if int(salary) > mejor_salario:
                        mejor_salario = int(salary)
                        oferta_mejor_salario = job
                    if int(salary) < peor_salario:
                        peor_salario = int(salary)
                        oferta_peor_salario = job
            promedio_salario_ciudad = round(total_salario_ciudad/lt.size(city_value), 2)
            
            print("|" + 'NOMBRE: ' + str(city) + "\n" + "|" + 'PAIS: ' + str(pais) + "\n" + "|" + 
                  'TOTAL DE OFERTAS: ' + str(size) + "\n" + "|" + 
                  'PROMEDIO DE SALARIO: ' + str(promedio_salario_ciudad) + "\n" + "|" + 
                  'EMPRESAS QUE PUBLICARON AL MENOS UNA OFERTA: ' + str(lt.size(company_list)) + "\n" + "|" + 
                  'EMPRESA CON MAYOR NUMERO DE OFERTAS: ' + str(nombre_mayor_empresa) + " -> " + str(conteo_mayor_empresa) + "\n" + "|" + 
                  'MEJOR OFERTA DE SALARIO: ' + str(mejor_salario) + " -> [" + str(oferta_mejor_salario) + "]" + "\n" + "|" + 
                  'PEOR OFERTA DE SALARIO: ' + str(peor_salario) + " -> [" + str(oferta_peor_salario) + "]")
            print ("-"*45)

    else:
        elements = top_ranked_ciudades["elements"]
        print("Los primeros 5 elementos son los siguientes: ")
        print("\n")
        for city_element in elements[:5]:
            city = city_element["ciudad"]
            entry = mp.get(city_map, city)
            city_value = me.getValue(entry)
            pais = city_value["elements"][0]["country_code"]
            size = lt.size(city_value) 
            
            company_list = lt.newList("ARRAY_LIST")
            for company in city_value["elements"]:
                if lt.isPresent(company_list, company["company_name"]) == 0:
                    lt.addLast(company_list, company["company_name"])    
            total_empresas = lt.size(company_list)
            
            empresa_mayor_oferta = controller.empresa_con_mas_ofertas(control, city_value)
            nombre_mayor_empresa, conteo_mayor_empresa = empresa_mayor_oferta
            
            total_salario_ciudad = 0
            mejor_salario = 0
            peor_salario = 0
            oferta_mejor_salario = ""
            oferta_peor_salario = ""
            for job in lt.iterator(city_value):
                salary = encontrar_salario(data_structs, job["id"], salarios)
                if salary == "":
                    continue
                else:
                    total_salario_ciudad += int(salary)
                    if peor_salario == 0:
                        peor_salario = int(salary)
                    if int(salary) > mejor_salario:
                        mejor_salario = int(salary)
                        oferta_mejor_salario = job
                    if int(salary) < peor_salario:
                        peor_salario = int(salary)
                        oferta_peor_salario = job
            promedio_salario_ciudad = round(total_salario_ciudad/lt.size(city_value), 2)
            
            print("|" + 'NOMBRE: ' + str(city) + "\n" + "|" + 'PAIS: ' + str(pais) + "\n" + "|" + 
                  'TOTAL DE OFERTAS: ' + str(size) + "\n" + "|" + 
                  'PROMEDIO DE SALARIO: ' + str(promedio_salario_ciudad) + "\n" + "|" + 
                  'EMPRESAS QUE PUBLICARON AL MENOS UNA OFERTA: ' + str(lt.size(company_list)) + "\n" + "|" + 
                  'EMPRESA CON MAYOR NUMERO DE OFERTAS: ' + str(nombre_mayor_empresa) + " -> " + str(conteo_mayor_empresa) + "\n" + "|" + 
                  'MEJOR OFERTA DE SALARIO: ' + str(mejor_salario) + " -> [" + str(oferta_mejor_salario) + "]" + "\n" + "|" + 
                  'PEOR OFERTA DE SALARIO: ' + str(peor_salario) + " -> [" + str(oferta_peor_salario) + "]")
            print ("-"*45)
        print("\n")
        print("Los ultimos 5 elementos son los siguientes: ")
        print("\n")
        for city_element in elements[- 5:]:
            city = city_element["ciudad"]
            entry = mp.get(city_map, city)
            city_value = me.getValue(entry)
            pais = city_value["elements"][0]["country_code"]
            size = lt.size(city_value) 
            
            company_list = lt.newList("ARRAY_LIST")
            for company in city_value["elements"]:
                if lt.isPresent(company_list, company["company_name"]) == 0:
                    lt.addLast(company_list, company["company_name"])    
            total_empresas = lt.size(company_list)
            
            empresa_mayor_oferta = controller.empresa_con_mas_ofertas(control, city_value)
            nombre_mayor_empresa, conteo_mayor_empresa = empresa_mayor_oferta
            
            total_salario_ciudad = 0
            mejor_salario = 0
            peor_salario = 0
            oferta_mejor_salario = ""
            oferta_peor_salario = ""
            for job in lt.iterator(city_value):
                salary = encontrar_salario(data_structs, job["id"], salarios)
                if salary == "":
                    continue
                else:
                    total_salario_ciudad += int(salary)
                    if peor_salario == 0:
                        peor_salario = int(salary)
                    if int(salary) > mejor_salario:
                        mejor_salario = int(salary)
                        oferta_mejor_salario = job
                    if int(salary) < peor_salario:
                        peor_salario = int(salary)
                        oferta_peor_salario = job
            promedio_salario_ciudad = round(total_salario_ciudad/lt.size(city_value), 2)
            
            print("|" + 'NOMBRE: ' + str(city) + "\n" + "|" + 'PAIS: ' + str(pais) + "\n" + "|" + 
                  'TOTAL DE OFERTAS: ' + str(size) + "\n" + "|" + 
                  'PROMEDIO DE SALARIO: ' + str(promedio_salario_ciudad) + "\n" + "|" + 
                  'EMPRESAS QUE PUBLICARON AL MENOS UNA OFERTA: ' + str(lt.size(company_list)) + "\n" + "|" + 
                  'EMPRESA CON MAYOR NUMERO DE OFERTAS: ' + str(nombre_mayor_empresa) + " -> " + str(conteo_mayor_empresa) + "\n" + "|" + 
                  'MEJOR OFERTA DE SALARIO: ' + str(mejor_salario) + " -> [" + str(oferta_mejor_salario) + "]" + "\n" + "|" + 
                  'PEOR OFERTA DE SALARIO: ' + str(peor_salario) + " -> [" + str(oferta_peor_salario) + "]")
            print ("-"*45)
        print("\n")
 
def encontrar_salario(data_structs, id, salarios):
    entry = mp.get(data_structs["employment_types"], id)
    elemento = me.getValue(entry)
    if elemento["currency_salary"] == "usd":
        salary_from = elemento["salary_from"]
        salary_to = elemento["salary_to"]
        salario_promedio = round((float(salary_from) +float(salary_to))/2, 2)
    elif elemento["currency_salary"] == "pln":
        salary_from = float(elemento["salary_from"]) * 0.25
        salary_to = float(elemento["salary_to"]) * 0.25
        salario_promedio = round((float(salary_from) +float(salary_to))/2, 2)
    elif elemento["currency_salary"] == "eur":
        salary_from = float(elemento["salary_from"]) * 1.09
        salary_to = float(elemento["salary_to"]) * 1.09
        salario_promedio = round((float(salary_from) +float(salary_to))/2, 2)
    elif elemento["currency_salary"] == "":
        salario_promedio = ""
    elif elemento["currency_salary"] == "gbp":
        salary_from = float(elemento["salary_from"]) * 1.27
        salary_to = float(elemento["salary_to"]) * 1.27
        salario_promedio = round((float(salary_from) +float(salary_to))/2, 2)
    elif elemento["currency_salary"] == "chf":
        salary_from = float(elemento["salary_from"]) * 1.13
        salary_to = float(elemento["salary_to"]) * 1.13
        salario_promedio = round((float(salary_from) +float(salary_to))/2, 2)
    return salario_promedio


def print_req_7(result):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    
    general_info = result[0]
    expertiece_level_info = result[1]
    
    junior_info = expertiece_level_info[0]
    mid_info = expertiece_level_info[1]
    senior_info = expertiece_level_info[2]
    
    print("\n")
    print ("-------------------------------------------")
    print("Total de ofertas de empleo: ", general_info[0])
    print ("-------------------------------------------") 
    print("Total de ciudades en donde se ofertó en los países resultantes: ", general_info[1])
    print ("-------------------------------------------")
    print("El país con mayor ofertas fue", general_info[2]["pais"], "con", general_info[2]["n_ofertas"],"ofertas")
    print ("-------------------------------------------")
    print("La ciudad con mayor ofertas fue", general_info[3]["ciudad"], "con", general_info[3]["n_ofertas"],"ofertas" )
    print ("-------------------------------------------")
    print("\n")
    print ("--------------OFERTAS JUNIOR---------------")
    print("Total de habilidades diferentes solicitadas: ", junior_info[0])    
    print("La habilidad más solicitada es", junior_info[1]["name"],"presente en", junior_info[1]["cantidad"], "ofertas")  
    print("La habilidad menos solicitada es", junior_info[2]["name"],"presente en", junior_info[2]["cantidad"], "ofertas") 
    print("El promedio de nivel minimo es ", junior_info[3])
    print ("-------------------------------------------")
    print("Numero empresas con ofertas junior: ", junior_info[4])
    print("La empresa con mayor ofertas junior es ",junior_info[5]["empresa"] ,"con", junior_info[5]["n_ofertas"], "ofertas")
    print("La empresa con menor ofertas junior es ",junior_info[6]["empresa"] ,"con", junior_info[6]["n_ofertas"], "ofertas")
    print("Numero de empresas con una o más sedes: ", junior_info[7])
    print ("-------------------------------------------")
    print("\n")
    print ("----------------OFERTAS MID----------------")
    print("Total de habilidades diferentes solicitadas: ", mid_info[0])    
    print("La habilidad más solicitada es", mid_info[1]["name"],"presente en", mid_info[1]["cantidad"], "ofertas")  
    print("La habilidad menos solicitada es", mid_info[2]["name"],"presente en", mid_info[2]["cantidad"], "ofertas") 
    print("El promedio de nivel minimo es ", mid_info[3])
    print ("-------------------------------------------")
    print("Numero empresas con ofertas mid: ", mid_info[4])
    print("La empresa con mayor ofertas mid es ",mid_info[5]["empresa"] ,"con", mid_info[5]["n_ofertas"], "ofertas")
    print("La empresa con menor ofertas mid es ",mid_info[6]["empresa"] ,"con", mid_info[6]["n_ofertas"], "ofertas")
    print("Numero de empresas con una o más sedes: ", mid_info[7])
    print ("-------------------------------------------")
    print("\n")
    print ("--------------OFERTAS SENIOR---------------")
    print("Total de habilidades diferentes solicitadas: ", senior_info[0])    
    print("La habilidad más solicitada es", senior_info[1]["name"],"presente en", senior_info[1]["cantidad"], "ofertas")  
    print("La habilidad menos solicitada es", senior_info[2]["name"],"presente en", senior_info[2]["cantidad"], "ofertas") 
    print("El promedio de nivel minimo es ", senior_info[3])
    print ("-------------------------------------------")
    print("Numero empresas con ofertas senior: ", senior_info[4])
    print("La empresa con mayor ofertas senior es ",senior_info[5]["empresa"] ,"con", senior_info[5]["n_ofertas"], "ofertas")
    print("La empresa con menor ofertas senior es ",senior_info[6]["empresa"] ,"con", senior_info[6]["n_ofertas"], "ofertas")
    print("Numero de empresas con una o más sedes: ", senior_info[7])
    print ("-------------------------------------------")



def print_req_8(control, result):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    
    ranked_paises, total_ofertas, lst_ciudades, lst_empresas, n_ofertas_rango_salarial, n_ofertas_salario_fijo, n_ofertas_sin_salario = result
    
    if lt.size(result[0]) > 0:
    
        if lt.size(result[0]) <= 10:

            print ("-------------------------------------------")
            print ("-------------- INFO GENERAL ---------------")
            print ("-------------------------------------------")
            print("\n")
            print ("-------------------------------------------")
            print("Numero de empresas que publicaron por lo menos una oferta: ", lt.size(lst_empresas) )
            print("Numero total de ofertas de empleo: ", total_ofertas)
            print("Numero de paises: ", lt.size(ranked_paises))
            print("Numero de ciudades: ", lt.size(lst_ciudades))
            print("Numero de ofertas publicadas con rango salarial: ", n_ofertas_rango_salarial)
            print("Numero de ofertas publicadas con valor fijo: ", n_ofertas_salario_fijo)
            print("Numero de ofertas sin salario: ", n_ofertas_sin_salario)
            print ("-------------------------------------------")
            print("\n")
            
            print ("-------------------------------------------")
            print ("--------------    PAISES    ---------------")
            print ("-------------------------------------------")
            
            for pais in lt.iterator(ranked_paises):
                print ("-------------------------------------------")
                print("|" + 'PAIS: ' + str(pais["pais"]) + "\n" + "|" + 
                    'PROMEDIO DE OFERTA SALARIAL: ' + str(round(pais["average_salary"],2)) + "\n" + "|" + 
                    'EMPRESAS QUE PUBLICARON ALGUNA OFERTA: ' + str(lt.size(pais["empresas"])) + "\n" + "|" + 
                    'TOTAL DE OFERTAS PUBLICADAS: ' + str(pais["ofertas"]) + "\n" + "|" + 
                    'OFERTAS CON RANGO SALARIAL: ' + str(pais["ofertas_rango_salarial"]) + "\n" + "|" + 
                    'HABILIDADES PROMEDIO POR OFERTA: ' + str(pais["average_skills"])
                    )
                print ("-------------------------------------------")
            
        else:
            
            print ("-------------------------------------------")
            print ("-------------- INFO GENERAL ---------------")
            print ("-------------------------------------------")
            print("\n")
            print ("-------------------------------------------")
            print("Numero de empresas que publicaron por lo menos una oferta: ", lt.size(lst_empresas) )
            print("Numero total de ofertas de empleo: ", total_ofertas)
            print("Numero de paises: ", lt.size(ranked_paises))
            print("Numero de ciudades: ", lt.size(lst_ciudades))
            print("Numero de ofertas publicadas con rango salarial: ", n_ofertas_rango_salarial)
            print("Numero de ofertas publicadas con valor fijo: ", n_ofertas_salario_fijo)
            print("Numero de ofertas sin salario: ", n_ofertas_sin_salario)
            print ("-------------------------------------------")
            print("\n")
        
            print ("-------------------------------------------")
            print ("--------------    PAISES    ---------------")
            print ("-------------------------------------------")
            print("\n")
            print ("-------------------------------------------")
            print("Los primeros 5 paises son: ")
            print ("-------------------------------------------")
            for pais in ranked_paises["elements"][:5]:
                
                print("|" + 'PAIS: ' + str(pais["pais"]) + "\n" + "|" + 
                    'PROMEDIO DE OFERTA SALARIAL: ' + str(round(pais["average_salary"],2)) + "\n" + "|" + 
                    'EMPRESAS QUE PUBLICARON ALGUNA OFERTA: ' + str(lt.size(pais["empresas"])) + "\n" + "|" + 
                    'TOTAL DE OFERTAS PUBLICADAS: ' + str(pais["ofertas"]) + "\n" + "|" + 
                    'OFERTAS CON RANGO SALARIAL: ' + str(pais["ofertas_rango_salarial"]) + "\n" + "|" + 
                    'HABILIDADES PROMEDIO POR OFERTA: ' + str(pais["average_skills"])
                    )
                print ("-------------------------------------------")
            
            print ("-------------------------------------------")
            print("Los últimos 5 paises son: ")
            print ("-------------------------------------------")
            for pais in ranked_paises["elements"][-5:]:
                
                print("|" + 'PAIS: ' + str(pais["pais"]) + "\n" + "|" + 
                    'PROMEDIO DE OFERTA SALARIAL: ' + str(round(pais["average_salary"],2)) + "\n" + "|" + 
                    'EMPRESAS QUE PUBLICARON ALGUNA OFERTA: ' + str(lt.size(pais["empresas"])) + "\n" + "|" + 
                    'TOTAL DE OFERTAS PUBLICADAS: ' + str(pais["ofertas"]) + "\n" + "|" + 
                    'OFERTAS CON RANGO SALARIAL: ' + str(pais["ofertas_rango_salarial"]) + "\n" + "|" + 
                    'HABILIDADES PROMEDIO POR OFERTA: ' + str(pais["average_skills"])
                    )
                print ("-------------------------------------------")
        
        #Segunda parte
        
        pais_mayor_salario = lt.firstElement(ranked_paises)
        pais_menor_salario = lt.lastElement(ranked_paises)
        print("\n")
        print ("-------------------------------------------")
        print("------ PAIS CON MAYOR OFERTA SALARIAL ------")
        print ("-------------------------------------------")
        print ("-------------------------------------------")
        print("|" + 'PAIS: ' + str(pais_mayor_salario["pais"]) + "\n" + "|" + 
                    'PROMEDIO DE OFERTA SALARIAL: ' + str(pais_mayor_salario["average_salary"]) + "\n" + "|" + 
                    'EMPRESAS QUE PUBLICARON ALGUNA OFERTA: ' + str(lt.size(pais_mayor_salario["empresas"])) + "\n" + "|" + 
                    'TOTAL DE OFERTAS PUBLICADAS: ' + str(pais_mayor_salario["ofertas"]) + "\n" + "|" + 
                    'NUMERO DE CIUDADES DONDE SE OFERTO: ' + str(lt.size(pais_mayor_salario["ciudades"])) + "\n" + "|" + 
                    'HABILIDADES PROMEDIO POR OFERTA: ' + str(pais_mayor_salario["average_skills"]) + "\n" + "|" +
                    'VALOR DEL MAYOR SALARIO OFERTADO: ' + str(pais_mayor_salario["salario_mayor"]) + "\n" + "|" +
                    'VALOR DEL MENOR SALARIO OFERTADO: ' + str(pais_mayor_salario["salario_menor"]) 
             )
        
        print("\n")
        
        print ("-------------------------------------------")
        print("------ PAIS CON MENOR OFERTA SALARIAL ------")
        print ("-------------------------------------------")
        print ("-------------------------------------------")
        print("|" + 'PAIS: ' + str(pais_menor_salario["pais"]) + "\n" + "|" + 
                    'PROMEDIO DE OFERTA SALARIAL: ' + str(pais_menor_salario["average_salary"]) + "\n" + "|" + 
                    'EMPRESAS QUE PUBLICARON ALGUNA OFERTA: ' + str(lt.size(pais_menor_salario["empresas"])) + "\n" + "|" + 
                    'TOTAL DE OFERTAS PUBLICADAS: ' + str(pais_menor_salario["ofertas"]) + "\n" + "|" + 
                    'NUMERO DE CIUDADES DONDE SE OFERTO: ' + str(lt.size(pais_menor_salario["ciudades"])) + "\n" + "|" + 
                    'HABILIDADES PROMEDIO POR OFERTA: ' + str(pais_menor_salario["average_skills"]) + "\n" + "|" +
                    'VALOR DEL MAYOR SALARIO OFERTADO: ' + str(pais_menor_salario["salario_mayor"]) + "\n" + "|" +
                    'VALOR DEL MENOR SALARIO OFERTADO: ' + str(pais_menor_salario["salario_menor"]) 
             )
        print ("-------------------------------------------")
        print("\n")
    
    else:
        print ("--------------------------------------------------------")
        print("No se encontraron paises con los criterios de la consulta")
        print ("--------------------------------------------------------")
    
    
    
    
    
    
    
    
    


archivo_str = """Seleccione el archivo a cargar:
                 10% ||  10
                 20% ||  20
                 30% ||  30
                 40% ||  40
                 50% ||  50
                 60% ||  60
                 70% ||  70
                 80% ||  80          
                 90% ||  90                                           
                 100% || large
                 Small || small
                 : """

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
            archivo_str = input(archivo_str)
            size_str = archivo_str
            print("Cargando información de los archivos ....\n")
            data = load_data(control,size_str)
            print_data(data, control["model"])          
            
        elif int(inputs) == 2:
            ultimos = int(input("Ingrese el número de ultimas ofertas a listar: "))
            codigo = input("Ingrese el codigo del pais a consultar: ")
            nivel = input("Ingrese el nivel de experticia: ")
            result = controller.req_1(control, codigo, nivel)
            ofertas = result[0]
            size = lt.size(ofertas)
            DeltaTime = f"{result[1]:.3f}"
            print("Para", size, "elementos, el tiempo es:",
                str(DeltaTime), "[ms]")
            print_req_1(ofertas, ultimos)

        elif int(inputs) == 3:
            ultimos = int(input("Ingrese el número de ultimas ofertas a listar: "))
            empresa = input("Ingrese el nombre de la empresa a consultar: ")
            ciudad = input("Ingrese la ciudad que desea buscar: ")
            result = controller.req_2(control, empresa, ciudad)
            ofertas = result[0]
            size = lt.size(ofertas)
            DeltaTime = f"{result[1]:.3f}"
            print("Para", size, "elementos, el tiempo es:",
                str(DeltaTime), "[ms]")
            print_req_2(ofertas, ultimos)

        elif int(inputs) == 4:
            empresa = input("Digite la empresa que desea consultar: ")
            fecha_inicial = input("Digite la fecha inicial del periodo a consultar [en formato: yyyy-mm-dd]: ")
            fecha_final = input("Digite la fecha final del periodo a consultar [en formato: yyyy-mm-dd]: ")
            result = controller.req_3(control, empresa, fecha_inicial,fecha_final)
            elementos = result[0]
            size = elementos[1]
            DeltaTime = f"{result[1]:.3f}"
            print("Para", size, "elementos, el tiempo es:",
                str(DeltaTime), "[ms]")
            print_req_3(elementos, empresa)

        elif int(inputs) == 5:
            codigo = input("Ingrese el codigo del pais a consultar: ")
            fecha_inicio = input("Digite la fecha inicial del periodo a consultar [en formato: yyyy-mm-dd]: ")
            fecha_fin = input("Digite la fecha final del periodo a consultar [en formato: yyyy-mm-dd]: ")
            data = controller.req_4(control, codigo, fecha_inicio, fecha_fin)
            ofertas = data[0]
            size = lt.size(ofertas)
            DeltaTime = f"{data[1]:.3f}"
            print("Para", size, "elementos, el tiempo es:",
                str(DeltaTime), "[ms]")
            print_req_4(ofertas)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            n_ciudades = input("Ingrese el numero de ciudades a consultar: ")
            año = input("Ingrese el año a consultar: ")
            experticia = input("Ingrese el nivel de experticia: ")
            data = controller.req_6(control, n_ciudades, año, experticia)
            ofertas = data[0]
            size = data[0][3]
            DeltaTime = f"{data[1]:.3f}"
            print("Para", size, "elementos, el tiempo es:",
                str(DeltaTime), "[ms]")
            print_req_6(ofertas)

        elif int(inputs) == 8:
            n_paises = int(input("Digite el numero de paises que desea consultar: "))
            year = input("Digite el año que desea consultar: ")
            month = input("Digite el mes que desea consultar: ")
            result, d_time = controller.req_7(control, n_paises, year, month)
            
            if result == "NONE_ELEMENTS":
                print ("-------------------------------------------")
                print("No se encontraron ofertas de trabajo en el", month, "de", year)
                print ("-------------------------------------------")
                
            elif result == "NONE_YEAR":
                print ("-------------------------------------------")
                print("El año digitado no se encuentra en la base de datos")
                print ("-------------------------------------------")
            
            else:
                size = result[0][0]
                DeltaTime = f"{d_time:.3f}"
                print("Para", size, "elementos, el tiempo es:",
                    str(DeltaTime), "[ms]")
                print_req_7 (result)

        elif int(inputs) == 9:
            experticia = input("Ingrese el nivel de experticia: ")
            divisa = input("Ingrese la divisa a consultar: ")
            fecha_inicial = input("Ingrese la fecha inicial del periodo a consultar [en formato: yyyy-mm-dd]: ")
            fecha_final = input("Ingrese la fecha final del periodo a consultar [en formato: yyyy-mm-dd]: ")
            
            result, delt_time = controller.req_8(control, experticia, divisa, fecha_inicial, fecha_final)
            size = result[1]
            DeltaTime = f"{delt_time:.3f}"
            print("Para", size, "elementos, el tiempo es:",
                str(DeltaTime), "[ms]")
            print_req_8(control, result)
                    
            
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
