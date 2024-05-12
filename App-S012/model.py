"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# algoritmos de ordenamiento, por defecto no se ha seleccionado ninguno
sort_algorithm = None

# Construccion de modelos

def new_data_structs(data_size, data_structure, load_factor):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog = { 
        'jobs': None,
        'skills': None,
        'employment_types': None,
        'multilocations': None
    }

    catalog['jobs'] = lt.newList('ARRAY_LIST')

    catalog['skills'] = mp.newMap(data_size,
                                  maptype=data_structure,
                                  loadfactor=load_factor)
    
    catalog['employment_types'] = mp.newMap(data_size,
                                            maptype=data_structure,
                                            loadfactor=load_factor)
    
    catalog['multilocations'] = mp.newMap(data_size,
                                            maptype=data_structure,
                                            loadfactor=load_factor)

    return catalog


# Funciones para agregar informacion al modelo

def add_lst(catalog, job):
    """
    Función para agregar nuevas elementos a la lista
    """
    lt.addLast(catalog, job)

def add_map(catalog, key, data):
    """
    Función para agregar nuevos elementos a la tabla de hash
    """
    mp.put(catalog, key, data)


# Funciones para creacion de datos

def new_job(catalog, job):
    """
    Crea una nueva estructura para modelar las ofertas
    """
    for key in job:
        if job[key] == 'Undefined':
            job[key] = 'Desconocido'

    add_lst(catalog['jobs'], job)
    add_map(catalog['skills'], job['id'], lt.newList())
    add_map(catalog['employment_types'], job['id'], lt.newList())
    add_map(catalog['multilocations'], job['id'], lt.newList())

def new_data(catalog, data):
    """
    Crea una nueva estructura para modelar los datos
    """
    lst = me.getValue(get_data(catalog, data['id']))
    add_lst(lst, data)

def new_employment_type(catalog, data):
    """
    Crea una nueva estructura para modelar los tipos de contratacion
    """
    for key in data:
        if data[key] == '':
            data[key] = '0'

    data = {
        'type': data['type'],
        'id': data['id'],
        'currency_salary': data['currency_salary'],
        'salary': (int(data['salary_from']) + int(data['salary_to'])) / 2
    }

    new_data(catalog, data)


# Funciones de consulta

def get_job_salary(salaries):
    """
    Retorna la suma de los salarios
    """
    job_salary = 0

    for salary in lt.iterator(salaries):
        job_salary += salary['salary']

    return job_salary / data_size(salaries, lt)

def get_data(catalog, key):
    """
    Retorna un dato a partir de su llave
    """
    return mp.get(catalog, key)

def get_sublist(catalog, pos, numelem):
    """
    Retorna una sublista de una lista dada.
    """
    return lt.subList(catalog, pos, numelem)

def data_size(catalog, data_structure):
    """
    Retorna el tamaño de la lista de datos
    """
    return data_structure.size(catalog)


# Funciones de requerimientos

def req_1(catalog, num, country, exp):
    """
    Función que soluciona el requerimiento 1
    """
    jobs = catalog['jobs']
    filtered_jobs = lt.newList()
    country_offers = 0

    for job in lt.iterator(jobs):

        if job['country_code'] == country.upper():
            country_offers += 1

            if job['experience_level'] == exp.lower():
                lt.addLast(filtered_jobs, job)
            if data_size(filtered_jobs, lt) == num:
                return filtered_jobs, country_offers
        
    return filtered_jobs, country_offers

def req_2(catalog, num, company_name, city):
    """
    Función que soluciona el requerimiento 2
    """
    jobs = catalog['jobs']
    filtered_jobs = lt.newList()

    for job in lt.iterator(jobs):
        if job['company_name'].lower() == company_name.lower() and job['city'].lower() == city.lower():
            lt.addLast(filtered_jobs, job)
        if lt.size(filtered_jobs) == num:
            return filtered_jobs
        
    return filtered_jobs

def req_3(catalog, nombre_empresa, fecha_inicial, fecha_final):
    offers = catalog["jobs"]
    res = lt.newList("ARRAY_LIST")  
    
    num_offers = 0
    num_senior = 0                                                      
    num_mid = 0
    num_junior = 0


    for job in lt.iterator(offers):
        if job["company_name"].lower() == nombre_empresa.lower() and fecha_inicial < job["published_at"] < fecha_final:
            num_offers += 1
            rta = job.copy()
            eliminar_datos(rta)
            lt.addLast(res, rta)

        
            if job["experience_level"] == "senior":
                num_senior += 1
            elif job["experience_level"] == "mid":
                 num_mid += 1
            
            elif job["experience_level"] == "junior":
                num_junior += 1

    sort(res,sort_req_3)        
    return num_offers, num_junior, num_mid, num_senior, res
  
def eliminar_datos(rta):
    del rta["street"]
    del rta["address_text"]
    del rta["marker_icon"]
    del rta["company_url"]
    del rta["remote_interview"]
    del rta["id"]
    del rta["display_offer"]



def req_4(catalog, country, min_date, max_date):
    """
    Función que soluciona el requerimiento 4
    """
    jobs = catalog['jobs']

    filtered_jobs = lt.newList()

    total_companies = mp.newMap(lt.size(jobs),
                                maptype='CHAINING',
                                loadfactor=4)

    counted_cities = mp.newMap(lt.size(jobs),
                                maptype='CHAINING',
                                loadfactor=4)
    
    min_date, max_date = datetime.strptime(min_date, '%Y-%m-%dT%H:%M:%S.%fZ'), datetime.strptime(max_date, '%Y-%m-%dT%H:%M:%S.%fZ')

    for job in lt.iterator(jobs):

        if job['country_code'] == country.upper():

            # Obtener la fecha de la oferta para la comparacion
            current_date = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

            if min_date < current_date < max_date:
                # Agregar la oferta a la lista
                lt.addLast(filtered_jobs, job)
                # Agregar la empresa a la tabla que contara el total de empresas con ofertas
                mp.put(total_companies, job['company_name'], None)

                # Manipular las ciudades y el numero de ofertas en cada ciudad
                if mp.contains(counted_cities, job['city']):
                    # Obtener el diccionario de la ciudad y agregar 1
                    city = me.getValue(get_data(counted_cities, job['city']))
                    city['offers'] += 1

                else:
                    # Crear estructura para modelar los datos
                    city = {'name': job['city'], 
                            'offers': 1}
                    # Añadir ciudad a la tabla de las ciudades
                    mp.put(counted_cities, job['city'], city)

    if lt.isEmpty(filtered_jobs):
        # Si no se encuentra ninguna oferta devolver None
        return None, None, None
    else:
        # Ordenar las ciudades de mayor a menor, por el numero de ofertas publicadas
        counted_cities = sort(mp.valueSet(counted_cities), sort_req_4)

        return filtered_jobs, counted_cities, mp.size(total_companies)


def req_5(catalog, ciudad, fecha_inicio, fecha_fin):
    """
    Función que soluciona el requerimiento 5
    """
    offers = catalog["jobs"]
    offer_ciudad = 0
    rta = lt.newList("ARRAY_LIST")
    ofertas = lt.newList("ARRAY_LIST")
    mayor = mp.newMap(100,
                                maptype='CHAINING',
                                loadfactor=4)
    
    for job in lt.iterator(offers):

        if job["city"].lower() == ciudad.lower() and fecha_inicio < job["published_at"] < fecha_fin:

            if mp.contains(mayor, job['company_name']):
                # Obtener el diccionario de la ciudad y agregar 1
                company = me.getValue(get_data(mayor, job['company_name']))
                company['total'] += 1
            else:
                # Crear estructura para modelar los datos
                company = {'name': job['company_name'], 
                            'total': 1}
                mp.put(mayor, job['company_name'], company)

            if not lt.isPresent(ofertas, job["company_name"]):
                lt.addLast(ofertas, job["company_name"])                
                
            offer_ciudad += 1
            res = {
                "fecha publicacion": job["published_at"],
                "titulo oferta" : job["title"],
                "Nombre empresa" : job["company_name"],
                "lugar de trabajo": job["workplace_type"],
                "tamaño empresa": job["company_size"]
            }

            lt.addLast(rta, res)

    counted_cities = sort(mp.valueSet(mayor), sort_req_5)
    maximo = lt.firstElement(counted_cities)
    minimo = lt.lastElement(counted_cities)
    empresas = lt.size(ofertas)
    sort(rta, sort_criteria_andres)

    return  offer_ciudad, empresas, maximo, minimo, rta


def req_6(catalog, num_cities, exp, year):
    """
    Función que soluciona el requerimiento 6
    """
    jobs = catalog['jobs']
    employment_types = catalog['employment_types']

    cities = mp.newMap(1000,
                        maptype='PROBING',
                        loadfactor=0.1)
    
    total_companies = mp.newMap(5000,
                                maptype='CHAINING',
                                loadfactor=10)

    total_offers = 0

    for job in lt.iterator(jobs):

        if year in job['published_at']:

            if exp.lower() == job['experience_level'] or exp.lower() == 'indiferente':
                
                # Obtener el salario promedio de la oferta
                salaries = me.getValue(get_data(employment_types, job['id']))
                job['salary'] = get_job_salary(salaries)
                # Obtener la pareja de la ciudad en la tabla de ciudades, si no existe devuelve None
                city = get_data(cities, job['city'])

                if city:
                    # Obtener el diccionario de la ciudad
                    city = me.getValue(city)

                    # Agregar 1 a la cantidad de ofertas
                    city['offers'] += 1

                    # Sumar el salario de la oferta a el salario promedio de la ciudad
                    city['average_salary'] += job['salary']

                    # Obtener la oferta con mejor y peor salario
                    if 0 < job['salary'] > city['highest_salary']['salary']:
                        city['highest_salary'] = job
                    if 0 < job['salary'] < city['lowest_salary']['salary']:
                        city['lowest_salary'] = job

                    # Manipular el contador de empresas que tienen ofertas en la ciudad
                    num = 0
                    company = get_data(city['companies'], job['company_name'])
                    if company:
                    # Si la empresa ya fue agregada, entonces obtener el numero de ofertas de esa empresa.
                        num = me.getValue(company)

                    # Agregar 1 a las ofertas totales de esa empresa
                    mp.put(city['companies'], job['company_name'], num+1)

                    # Obtener la mejor compañia de la ciudad y comparar el numero de ofertas
                    if me.getValue(get_data(city['companies'], city['best_company'])) < num+1:
                        # Si es mayor, entonces actualizar 'best_company'
                        city['best_company'] = job['company_name']

                else:
                    # Crear tabla de hash para almacenar las empresas que tienen ofertas en la ciudad
                    companies = mp.newMap(100,
                                          maptype='CHAINING',
                                          loadfactor=10)
                    mp.put(companies, job['company_name'], 1)

                    # Crear diccionario para modelar los datos
                    city = {
                        'name': job['city'],
                        'country': job['country_code'],
                        'offers': 1,
                        'average_salary': job['salary'],
                        'highest_salary': job,
                        'lowest_salary': job,
                        'companies': companies,
                        'best_company': job['company_name']
                    }

                    # Agregar la ciudad a la tabla de hash de las ciudades
                    mp.put(cities, city['name'], city)

                # Agregar la empresa de esa oferta a la tabla que contara el total de empresas
                mp.put(total_companies, job['company_name'], None)

    # Ordenar las ciudades de mayor a menor, por el numero de ofertas publicadas 
    cities = sort(mp.valueSet(cities), sort_req_6)

    # Obtener solo las n primeras ciudades en caso de que hayan mas de la cantidad ingresada por el usuario
    if data_size(cities, lt) > num_cities:
        cities = get_sublist(cities, 1, num_cities)

    for city in lt.iterator(cities):
        # Sumar el numero total de ofertas publicadas
        total_offers += city['offers']

        # Obtener el salario promedio de la ciudad
        city['average_salary'] /= city['offers']

        # Obtener la mejor compañia con el conteo de ofertas
        city['best_company'] = get_data(city['companies'], city['best_company'])
        # Obtener cuantas empresas publicaron al menos una oferta
        city['companies'] = data_size(city['companies'], mp)

    return cities, (total_offers, data_size(total_companies, mp))


def req_7(catalog, num_countries, year, month):
    """
    Función que soluciona el requerimiento 7
    """
    #nombramiento de variables

    skills = catalog["skills"]
    jobs = catalog["jobs"]
    jobs2 = lt.newList()
    jobs3 = lt.newList()
    #--------------------------
    # Filtro 1
    countries_map = mp.newMap(1000,
                        maptype='PROBING',
                        loadfactor=0.1)
    countries_dic = {}

    #1.0
    total_offers = 0
    2.0
    cities_map = mp.newMap(1000,
                        maptype='PROBING',
                        loadfactor=0.1)
    cities_dic = {}

    5.0
    skills_senior_map = mp.newMap
    senior_list = lt.newList()
    skill_senior_dic = {}
    #---------------------------
    list_1 = lt.newList()
    list_2 = lt.newList()

    #recorrido en jobs
    for job in lt.iterator(jobs):
        
        if (str(year) in job["published_at"]) and (str(month) in job["published_at"]) :
                
            #avanze en dic para saber el numero de ofertas de cada pais. FILTRO3

            if mp.contains(countries_map, job["country_code"]):
                sor = me.getValue(mp.get(countries_map,job["country_code"]))
                countries_dic["offers"] = int(sor["offers"]) + 1 
                countries_dic["name"] = job["country_code"]
                mp.put(countries_map,job["country_code"],countries_dic)
            else:
                countries_dic["name"] = job["country_code"]
                countries_dic["offers"] = 1 
                mp.put(countries_map,job["country_code"],countries_dic)
                
            #5.0 recorrido en mapa de skills
            sk = me.getValue(mp.get(skills,job["id"]))

            for i in (sk):
                if str(i) == "name":
                    job["skill"] = sk[i]
                if str(i) == "level":
                    job["skill_level"] = sk[i]

    
            #Sorteo de paises de mayor a menor en numero de ofertas
            countries_sorted = sort(mp.valueSet(countries_map),sort_req_7)
            #creo sublista con los primeros n paises ingresados por usuario.
            if lt.size(countries_sorted) > num_countries:
                countries_sorted = get_sublist(countries_sorted, 1, num_countries)

            lt.addLast(jobs2,job)

    for i in lt.iterator(jobs2):
        if i["country_code"] in countries_sorted:
            total_offers +=1
            lt.addLast(jobs3)

    for j in lt.iterator(jobs3):

        if mp.contains(cities_map, j["city"]):
                cities_dic["offers"] += 1 
                mp.put(cities_map,j["city"],cities_dic)
        else:
            cities_dic["name"] = j["city"]
            cities_dic["offers"] = 1 
            mp.put(cities_map,job["city"],cities_dic)
        
        if str(j["experience_level"]) == "senior":

            if mp.contains(skills_senior_map, j["skill"]):
                skill_senior_dic["offers"] += 1 
                mp.put(skills_senior_map,j["skill"],skill_senior_dic)
            else:
                countries_dic["name"] = j["skill"]
                countries_dic["offers"] = 1 
                mp.put(countries_map,job["skill"],skill_senior_dic)

    #agregar a listas

    #lista1
    #1.0
    lt.addLast(list_1,total_offers)
    #2.0
    lt.addLast(list_1,mp.size(cities_map))
    #3.0
    tres_punto_cero = lt.getElement(countries_sorted,1)
    lt.addLast(list_1,tres_punto_cero)
    #4.0
    cities_sorted = sort(mp.valueSet(cities_map),sort_req_7)
    cuatro_punto_cero = lt.getElement(cities_sorted,1)
    lt.addLast(list_1,cuatro_punto_cero)
    
    #lista2

    #senior_list
    #5.1
    cinco_punto_uno = mp.size(skills_senior_map)
    lt.addLast(senior_list,cinco_punto_uno)

    #5.2
    skills_senior_sorted = sort(mp.valueSet(skills_senior_map),sort_req_7)
    skill_senior_mas = lt.getElement(skills_senior_sorted,1)
    lt.addLast(senior_list,skill_senior_mas)

    #5.3
    skill_senior_menos = lt.getElement(skills_senior_sorted,(lt.size(skills_senior_sorted))-1)
    lt.addLast(senior_list,skill_senior_menos)

    lt.addLast(senior_list,list_2)

    return list_1,list_2


def req_8(catalog, exp, min_date, max_date):
    """
    Función que soluciona el requerimiento 8
    """
    jobs = catalog['jobs']
    employment_types = catalog['employment_types']
    skills = catalog['skills']

    total_companies = mp.newMap(100,
                                maptype='CHAINING',
                                loadfactor=10)
    total_cities = mp.newMap(100,
                                maptype='CHAINING',
                                loadfactor=10)
    countries = mp.newMap(100,
                          maptype='PROBING',
                          loadfactor=0.5)
    
    highest_country = lt.newList()
    lowest_country = lt.newList()

    offers_with_salary = 0
    offers_without_salary = 0
    total_offers = 0

    min_date, max_date = datetime.strptime(min_date, '%Y-%m-%dT%H:%M:%S.%fZ'), datetime.strptime(max_date, '%Y-%m-%dT%H:%M:%S.%fZ')

    for job in lt.iterator(jobs):

        if exp.lower() == job['experience_level'] or exp.lower() == 'indiferente':

            # Obtener la fecha de la oferta para la comparacion
            current_date = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

            if min_date < current_date < max_date:

                # Obtener el salario promedio de la oferta
                salaries = me.getValue(get_data(employment_types, job['id']))
                job['salary'] = get_job_salary(salaries)

                # Obtener la cantidad de habilidades requeridas de la oferta
                job_skills = me.getValue(get_data(skills, job['id']))
                job['skills'] = data_size(job_skills, lt)

                # Buscar la pareja del pais de la oferta
                country = mp.get(countries, job['country_code'])

                if country:
                    # Si existe entonces obtenemos su valor
                    country = me.getValue(country)

                    # Agregar 1 a las ofertas de ese pais
                    country['offers'] += 1

                    # Agregar empresa con oferta al pais
                    mp.put(country['companies'], job['company_name'], None)
                    # Agregar ciudad con oferta al pais
                    mp.put(country['cities'], job['city'], None)

                    # Sumar al promedio de las habilidades del pais
                    country['average_skills'] += job['skills']

                    if job['salary'] != 0:
                        # Agregar al contador de ofertas con salario, tanto el general como el del pais
                        offers_with_salary += 1
                        country['offers_with_salary'] += 1
                        # Sumar al promedio de los salarios del pais
                        country['average_salary'] += job['salary']

                        if country['highest_salary'] < job['salary']:
                            # Actualizar mayor salario
                            country['highest_salary'] = job['salary']
                        if country['lowest_salary'] > job['salary']:
                            # Actualizar menor salario
                            country['lowest_salary'] = job['salary']                           

                    else:
                        # Sumar al contador de ofertas sin salario
                        offers_without_salary += 1

                else:
                    companies = mp.newMap(100,
                                          maptype='CHAINING',
                                          loadfactor=10)
                    mp.put(companies, job['company_name'], None)

                    cities = mp.newMap(100,
                                          maptype='CHAINING',
                                          loadfactor=10)
                    mp.put(cities, job['city'], None)

                    # Crear estructura para modelar los datos
                    country = {
                        'code': job['country_code'],
                        'average_salary': 0,
                        'companies': companies,
                        'cities': cities,
                        'offers': 1,
                        'offers_with_salary': 0,
                        'highest_salary': 0,
                        'lowest_salary': 1000000,
                        'average_skills': job['skills']
                    }

                    if job['salary'] != 0:
                        # Agregar al contador de ofertas con salario, tanto el general como el del pais
                        offers_with_salary += 1
                        country['offers_with_salary'] += 1
                        # Sumar al promedio de los salarios del pais
                        country['average_salary'] += job['salary']
                        #Agregar al mayor y menor salario
                        country['highest_salary'] = job['salary']
                        country['lowest_salary'] = job['salary']

                    else:
                        # Sumar al contador de ofertas sin salario
                        offers_without_salary += 1

                    # Agregar el pais a la tabla de hash de los paises
                    mp.put(countries, country['code'], country)

                # Agregar empresa para el conteo de empresas que publicaron al menos una oferta
                mp.put(total_companies, job['company_name'], None)

                # Agregar ciudad para el conteo de ciudades con ofertas
                mp.put(total_cities, job['city'], None)

    # Convertir la tabla de hash en una lista cn los valores
    countries = mp.valueSet(countries)

    for country in lt.iterator(countries):
        # Sumar el numero total de ofertas publicadas
        total_offers += country['offers']

        # Obtener el salario promedio del pais
        country['average_salary'] /= country['offers']
        # Obtener el numero de habilidades promedio del pais
        country['average_skills'] /= country['offers']

        # Obtener cuantas empresas publicaron al menos una oferta
        country['companies'] = data_size(country['companies'], mp)
        # Obtener cuantas ciudades publicaron al menos una oferta
        country['cities'] = data_size(country['cities'], mp)

    # Ordenar los paises de mayor a menor, por promedio salarial
    countries = sort(countries, sort_req_8)

    # Obtener el tamaño de las tablas para conocer la cantidad total de empresas y ciudades
    total_companies = data_size(total_companies, mp)
    total_cities = data_size(total_cities, mp)

    # Agregar la primera y la ultima oferta a sus respectivas listas
    lt.addLast(highest_country, lt.firstElement(countries))
    lt.addLast(lowest_country, lt.lastElement(countries))

    return countries, (total_offers, total_companies, total_cities, offers_with_salary, offers_without_salary, highest_country, lowest_country)


# Funciones de ordenamiento

def select_sort_algorithm(algorithm):
    """
    Permite seleccionar el algoritmo de ordenamiento.

    Args:
        algorithm (int): opcion de algoritmo de ordenamiento, las opciones son:
            1: Selection Sort
            2: Insertion Sort
            3: Shell Sort
            4: Merge Sort
            5: Quick Sort

    Returns:
        list: sort_algorithm (sort) la instancia del ordenamiento y
        msg (str) el texto que describe la configuracion del ordenamiento
    """
    sort_algorithm = None
    msg = None

    # opcion 1: Selection Sort
    if algorithm == 1:
        sort_algorithm = se
        msg = "Selection Sort"
    
    # opcion 2: Insertion Sort
    elif algorithm == 2:
        sort_algorithm = ins
        msg = "Insertion Sort"

    # opcion 3: Shell Sort
    elif algorithm == 3: 
        sort_algorithm = sa
        msg = "Shell Sort"

    # opcion 4: Merge Sort
    elif algorithm == 4:
        sort_algorithm = merg
        msg = "Merge Sort"

    # opcion 5: Quick Sort
    elif algorithm == 5:
        sort_algorithm = quk
        msg = "Quick Sort"

    return sort_algorithm, msg

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    dt_1 = datetime.fromisoformat(data_1['published_at'].replace("Z", "+00:00"))
    dt_2 = datetime.fromisoformat(data_2['published_at'].replace("Z", "+00:00"))

    if dt_1 > dt_2:
        return True
    
    elif dt_1 == dt_2:
        if data_1['company_name'] < data_2['company_name']:
            return True
        
    return False

def sort_req_4(city_1, city_2):
    """
    Criterio de ordenamiento para el requerimiento 4.
    """
    if city_1['offers'] > city_2['offers']:
        return True
    
    elif city_1['offers'] == city_2['offers']:
        if city_1['name'] < city_2['name']:
            return True

    return False

def sort_criteria_andres(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:   
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """    
    published_1 = datetime.fromisoformat(data_1['fecha publicacion'].replace("Z", "+00:00"))
    published_2 = datetime.fromisoformat(data_2['fecha publicacion'].replace("Z", "+00:00"))

    if published_1 > published_2:
        return False
        
    return True

def sort_req_5(city_1, city_2):
    """
    Criterio de ordenamiento para el requerimiento 4.
    """
    if city_1['total'] > city_2['total']:
        return True
    
    elif city_1['total'] == city_2['total']:
        if city_1['name'] < city_2['name']:
            return True

def sort_req_6(data_1, data_2):
    """
    Criterio de ordenamiento para el requerimiento 6.
    """
    if data_1['offers'] > data_2['offers']:
        return True
    
    elif data_1['offers'] == data_2['offers']:
        if data_1['name'] < data_2['name']:
            return True
        
    return False

def sort_req_8(data_1, data_2):
    """
    Criterio de ordenamiento para el requerimiento 8.
    """
    if data_1['average_salary'] > data_2['average_salary']:
        return True
        

    elif data_1['average_salary'] == data_2['average_salary']:
        if data_1['code'] < data_2['code']:
            return True
        
    return False


def sort_req_7(data_1, data_2):
    """
    Criterio de ordenamiento para el requerimiento 7.
    """
    if data_1['offers'] > data_2['offers']:
        return True
    
    elif data_1['offers'] == data_2['offers']:
        if data_1['name'] < data_2['name']:
            return True
        
    return False

def sort_req_3(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:   
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """    
    published_1 = datetime.fromisoformat(data_1['published_at'].replace("Z", "+00:00"))
    published_2 = datetime.fromisoformat(data_2['published_at'].replace("Z", "+00:00"))

    if published_1 > published_2:
        return False
        
    return True


def sort(catalog, sort_criteria=sort_criteria):
    """
    Función encargada de ordenar la lista con los datos
    """
    sorted_catalog = sort_algorithm.sort(catalog, sort_criteria)
    catalog = sorted_catalog

    return catalog