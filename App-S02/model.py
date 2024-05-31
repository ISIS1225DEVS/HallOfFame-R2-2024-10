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

from numpy import Infinity
import config as cf
from datetime import datetime as dt
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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {'jobs':None,
                    'id': None}

    data_structs['jobs'] = lt.newList('ARRAY_LIST',cmpfunction=compare, key=None)
    
    data_structs['id'] = mp.newMap(400000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_id)
    data_structs['city'] = mp.newMap(2000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_city)
    
    data_structs['company'] = mp.newMap(5000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_company)
    data_structs['country'] = mp.newMap(400,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_countries)
    
    data_structs['skill_id'] = mp.newMap(400000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_countries)
    
    data_structs['experience_level'] = mp.newMap(6,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_countries)
    
    data_structs['employment_id'] = mp.newMap(400000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_countries)
    
    data_structs['years'] = mp.newMap(6,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_countries)
    

    
    
    
    
    
    return data_structs
# Funciones para agregar informacion al modelo

def add_job(data_struct, job):
    mp.put(data_struct['id'], job['id'], job)
    
def add_city(data_struct, job):
    cities = data_struct['city']
    city_name = job['city']
    
    exist_city = mp.contains(cities, city_name)
    
    if exist_city:
        entry = mp.get(cities, city_name)
        city_list = me.getValue(entry)
    else:
        city_list = lt.newList(datastructure='ARRAY_LIST')
        mp.put(cities, city_name, city_list)

    lt.addLast(city_list, job)
 
    
def add_company(data_struct, job):
    companies = data_struct['company']
    company_name = job['company_name']
    
    exist_company = mp.contains(companies, company_name)
    
    if exist_company:
        entry = mp.get(companies, company_name)
        company_list = me.getValue(entry)
    else:
        company_list = lt.newList(datastructure='ARRAY_LIST')
        mp.put(companies, company_name, company_list)

    lt.addLast(company_list, job)

def add_country(data_struct, job):
    countries = data_struct['country']
    country_code = job['country_code']
    
    exist_country = mp.contains(countries, country_code)
    
    if exist_country:
        entry = mp.get(countries, country_code)
        dates_list = me.getValue(entry)
    else:
        dates_list = lt.newList(datastructure='ARRAY_LIST')
        mp.put(countries, country_code, dates_list)

    lt.addLast(dates_list, job)


def add_skill_by_id(data_struct, skill):
    add_key_to_aux_map(data_struct['skill_id'],skill['id'],skill)
    
def add_experience(data_struct, job):
    experiences = data_struct['experience_level']
    experience = job['experience_level']
    
    exist_exp = mp.contains(experiences, experience)
    
    if exist_exp:
        entry = mp.get(experiences, experience)
        exp_list = me.getValue(entry)
    else:
        exp_list = lt.newList(datastructure='ARRAY_LIST')
        mp.put(experiences, experience, exp_list)

    lt.addLast(exp_list, job)
    
def add_year(data_struct ,job):
    years = data_struct['years']
    year = job['published_at'][:4]
    
    exist_year = mp.contains(years, year)
    
    if exist_year:
        entry = mp.get(years, year)
        month_map = me.getValue(entry)
    else:
        month_map = mp.newMap(6,
                    maptype='PROBING',
                    loadfactor=0.5,
                    cmpfunction=compare_countries)         
        mp.put(years, year, month_map)

    month = job['published_at'][5:7]
    
    exist_month = mp.contains(month_map, month)
    
    if exist_month:
        entry = mp.get(month_map, month)
        job_list = me.getValue(entry)
    else:
        job_list = lt.newList(datastructure='ARRAY_LIST')
        mp.put(month_map, month, job_list)
    lt.addLast(job_list,job)
    
def add_employment_by_id(data_struct, employment):
     mp.put(data_struct['employment_id'], employment['id'], employment)
    
    

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista


def add_joblist(data_structs,data):
    lt.addLast(data_structs['jobs'],data)


    

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    data = {}
    for key in info:
        data[key] = id[key]
    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return mp.size(data_structs)


def req_1(data_structs,n_offers, country_code, experience_level):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    jobs = mp.get(data_structs['country'],country_code)
    job_offers = me.getValue(jobs)
    
    total_offers = lt.newList()
    offers_country= mp.newMap()
    offers_experience= mp.newMap()
        
    for job in lt.iterator(job_offers):
        add_counter(offers_country, job['title'])
        
        if job['experience_level'] == experience_level:
            add_counter(offers_experience, job['title'])
            
            lt.addLast(total_offers, job)
            
    offers_for_country = mp.size(offers_country)
    offers_for_experience = mp.size(offers_experience)
    sort(total_offers,sort_by_date)
    total_offers = lt.subList(total_offers, 0, n_offers)
        
    return total_offers, offers_for_country, offers_for_experience


def req_2(data_structs, n, company, city):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    cities = mp.get(data_structs['city'],city.title())
    city_list = me.getValue(cities)
    
    city_and_company = lt.newList()
    
    for job in lt.iterator (city_list):
        if job['company_name'] == company.title():
            lt.addLast(city_and_company,job)
    
    sort(city_and_company,sort_by_date_and_country)
    
    jobs_found = lt.size(city_and_company)
    
    if  jobs_found < n:
        n = jobs_found
    
    n_sublist = lt.subList(city_and_company,1,n)
    
    return jobs_found, n_sublist
        


def req_3(data_structs, empresa, fecha1, fecha2):
    """
    Función que soluciona el requerimiento 3
    """
    empresa=mp.get(data_structs['company'],empresa)
    ofertas_empresa= me.getValue(empresa)
    sort(ofertas_empresa,sort_by_company_and_date)
    jobs_in_dates = time_sublist(ofertas_empresa,fecha1,fecha2)
    if lt.isEmpty(jobs_in_dates):
        return None
    total_ofertas=lt.size(jobs_in_dates)
    
    junior=0
    mid=0
    senior=0
    
    for job in lt.iterator(jobs_in_dates):
        nivel=job["experience_level"]
        if nivel == "junior":
            junior+=1
        elif nivel == "mid":
            mid+=1
        elif nivel =="senior":
            senior+=1
        
    return total_ofertas,junior,mid,senior,jobs_in_dates


def req_4(data_structs,country,start,end):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    
    if not mp.contains(data_structs['country'],country.upper()):
        return None
    country_entry = mp.get(data_structs['country'],country.upper())
    country_list = me.getValue(country_entry)
    
    sort(country_list,sort_by_date_and_company)
    
    jobs_in_dates = time_sublist(country_list,start,end)
    
    if lt.isEmpty(jobs_in_dates):
        return None
    
    aux_company = mp.newMap(50,
                            maptype='PROBING',
                            loadfactor=0.7,
                            cmpfunction=compare_company)
    aux_city = mp.newMap(50,
                            maptype='PROBING',
                            loadfactor=0.7,
                            cmpfunction=compare_company)
    
    for job in lt.iterator(jobs_in_dates):
        city = job['city']
        company = job['company_name']
        
        add_counter(aux_city,city)
        add_counter(aux_company,company)
        
    companies = mp.size(aux_company)
    cities = mp.size(aux_city)
    
    city_max , city_n_max , city_min , city_n_min = map_max_and_min(aux_city)
    
    
    
    return lt.size(jobs_in_dates),companies,cities,city_max , city_n_max , city_min , city_n_min, jobs_in_dates
    
    


def req_5(data_structs, city, starting_date, ending_date):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    
    city_info = mp.get(data_structs['city'],city)
    city_list = me.getValue(city_info)
    sort(city_list,sort_by_company_and_date)
    
    offers_in_dates = time_sublist(city_list,starting_date,ending_date)
    
    if lt.isEmpty(offers_in_dates):
        return None
    
    company_offers = mp.newMap(50,
                            maptype='PROBING',
                            loadfactor=0.7,
                            cmpfunction=compare_company)
    total_offers = mp.newMap(50,
                            maptype='PROBING',
                            loadfactor=0.7,
                            cmpfunction=compare_company)
    
    
    for job in lt.iterator(offers_in_dates):
        company = job['company_name']
        offers_in_city = job['title']
        
        add_counter(company_offers,company)
        add_counter(total_offers,offers_in_city) 
        
        companies = mp.size(company_offers)
        n_offers = mp.size(total_offers)
   
    company_max , company_n_max , company_min , company_n_min = map_max_and_min(company_offers) 
    
    return companies, n_offers, company_max, company_n_max, company_min, company_n_min, offers_in_dates

#! REQUERIMIENTO 6

def req_6 (data_structs, amount_cities, level_expertise, year):
    
    cities = data_structs['city']
    map_companies = mp.newMap(5000, maptype='CHAINING', loadfactor=4)
    filter_cities = lt.newList('ARRAY_LIST')
    amount_offers = 0
    info_cities = mp.valueSet(cities)
    year = dt.strptime(year, '%Y')
    
    for city in lt.iterator(info_cities): # O(n)
        new_city = new_filtrated_city(data_structs, lt.getElement(city, 1)['city'])
        filtered_city = create_city(data_structs, city, new_city, year, level_expertise, map_companies, amount_offers)
        
        if lt.size(mp.get(filtered_city, 'offers')['value']) > 0:
            lt.addLast(filter_cities, filtered_city)
        
    sort_cities = merg.sort(filter_cities, sort_cities_by_num_offers_and_average_salarie) # Oclogc siendo c las ciudades 
    
    n_cities = lt.size(sort_cities)
    n_companies = mp.size(map_companies)
    
    if int(amount_cities) > lt.size(sort_cities):
        amount_cities = lt.size(sort_cities)
        
    best_city = lt.firstElement(sort_cities)
    worst_city = lt.lastElement(sort_cities)
    
    answer_sublist = lt.subList(sort_cities, 1, int(amount_cities))
    # -----------------------------------------------------------------------------------------------------
    tabular = []
    for city in lt.iterator(answer_sublist): # 0 (a)
        tabular_info, amount_offers = create_tabular_data(city, amount_offers)
        tabular.append(tabular_info)
    
    return tabular, n_cities, n_companies, best_city, worst_city, amount_offers
    

def create_city(data_structs, city_info, city_element, year, level_expertise=None, map_companies=None, amount_offers=0):
    
    for job in lt.iterator(city_info): # O(k) siendo k la cantridad de ofertas de la ciudad
        try:
            job['published_at'] = dt.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        except:
            job['published_at'] = job['published_at']
        if (level_expertise == job['experience_level'] or level_expertise is None) and year.year == job['published_at'].year:
            
            salary_info = mp.get(data_structs['employment_id'], job['id'])['value']
            
            job['salary_from'] = salary_info['salary_from']
            job['salary_to'] = salary_info['salary_to']
            
            if job['salary_from'] != "" and job['salary_to'] != "":
                job['salary_from'] = float(salary_info['salary_from'])
                job['salary_to'] = float(salary_info['salary_to'])
                average_salary = (job['salary_from'] + job['salary_to'])/2
                mp.get(city_element, 'amount_value_salaries')['value'] += average_salary
                mp.get(city_element, 'amount_offers_with_salary')['value'] += 1
                
                if mp.get(city_element, 'best_offer')['value']['salary_to'] < job['salary_to']:
                    mp.put(city_element, 'best_offer', job)
                
                if mp.get(city_element, 'worst_offer')['value']['salary_from'] > job['salary_from']:
                    mp.put(city_element, 'worst_offer', job)
            
            company = job['company_name']
            
            if mp.contains(mp.get(city_element, 'companies')['value'], company):
                company_element = mp.get(mp.get(city_element, 'companies')['value'], company)
                lt.addLast(company_element["value"], job)
            else:
                mp.put((mp.get(city_element, 'companies')['value']), company, lt.newList('ARRAY_LIST'))
                company_element = mp.get(mp.get(city_element, 'companies')['value'], company)
                lt.addLast(company_element["value"], job)
            
            if mp.contains(map_companies, company):
                company_element = mp.get(map_companies, company)
                lt.addLast(company_element["value"], job)
            else:
                mp.put(map_companies, company, lt.newList('ARRAY_LIST'))
                company_element = mp.get(map_companies, company)
                lt.addLast(company_element["value"], job)
                
            lt.addLast(mp.get(city_element, 'offers')['value'], job)
        
    
    if mp.get(city_element, 'amount_offers_with_salary')['value'] != 0:
        mp.put(city_element, 'average_salary', mp.get(city_element, 'amount_value_salaries')['value']/mp.get(city_element, 'amount_offers_with_salary')['value'])
    
    list_companies = mp.valueSet(mp.get(city_element, 'companies')['value'])
    merg.sort(list_companies, sort_companies_by_num_offers) # O(hlogh) siendo h la cantidad de compañias que hay en la ciudad
    mp.put(city_element, 'list_companies', list_companies)
    
    return city_element

def new_filtrated_city(data_structs, name_city):
    
    city = mp.newMap(8, maptype='PROBING', loadfactor=0.5)
    
    mp.put(city, 'city', name_city)
    mp.put(city, 'companies', mp.newMap(10, maptype='PROBING', loadfactor=0.5))
    mp.put(city, 'offers', lt.newList('ARRAY_LIST'))
    mp.put(city, 'amount_offers_with_salary', 0)
    mp.put(city, 'amount_value_salaries', 0)
    mp.put(city, 'best_offer', {'title': None, 'salary_to': -Infinity})
    mp.put(city, 'worst_offer', {'title': None ,'salary_from': Infinity})
    mp.put(city, 'average_salary', 0)
    
    return city

def sort_cities_by_num_offers_and_average_salarie(city1, city2):
    
    city1_amount_offers = lt.size(mp.get(city1, 'offers')['value'])
    city2_amount_offers = lt.size(mp.get(city2, 'offers')['value'])
    
    city1_average_salary = mp.get(city1, 'average_salary')['value']
    city2_average_salary = mp.get(city2, 'average_salary')['value']
    
    if city1_amount_offers == city2_amount_offers:
        return city1_average_salary > city2_average_salary
    else:
        return city1_amount_offers > city2_amount_offers

def sort_companies_by_num_offers(company1, company2):
    company1_size = lt.size(company1)
    company2_size = lt.size(company2)
    
    return company1_size > company2_size

def create_tabular_data(city, amount_offers):
    
    tabular_info = []
    tabular_info.append(mp.get(city, 'city')['value'])
    tabular_info.append(lt.firstElement(mp.get(city, 'offers')['value'])['country_code'])
    amount_offers += lt.size(mp.get(city, 'offers')['value'])
    tabular_info.append(lt.size(mp.get(city, 'offers')['value']))
    tabular_info.append(round((mp.get(city, 'average_salary')['value']), 2))
    tabular_info.append(lt.size(mp.get(city, 'list_companies')['value']))

    company_name = lt.firstElement(lt.firstElement(mp.get(city, 'list_companies')['value']))['company_name']
    company_offers = lt.size(lt.firstElement(mp.get(city, 'list_companies')['value']))
    
    tabular_info.append(f"Nombre: {company_name} | Ofertas: {company_offers}")
    best_offer = mp.get(city, 'best_offer')['value']
    worst_offer = mp.get(city, 'worst_offer')['value']
    tabular_info.append(f"Mejor oferta: {best_offer['title']} | Salario: {best_offer['salary_to']}")
    tabular_info.append(f"Peor oferta: {worst_offer['title']} | Salario: {worst_offer['salary_from']}")

    return tabular_info, amount_offers
    
    
    
    
    
    

def req_7(data_structs,best_n_countries,year,month):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    
    #Obtener las ofertas del año O(1)
    if not mp.contains(data_structs['years'],year):
        return None
    year_entry = mp.get(data_structs['years'],year)
    month_map = me.getValue(year_entry)
    
    #Obtener las ofertas del mes O(1)
    if not mp.contains(month_map,month):
        return None
    joblist_entry = mp.get(month_map,month)
    jobs_in_dates = me.getValue(joblist_entry)
    
    
    #Crear lista con parejas llave valor donde las llaves son los países para las ofertas en ese rango O(n)
    # El valor es otro mapa con llaves de nivel de experiencia y sus valores son la lista de las ofertas.
    list_of_countries = create_aux_countries(jobs_in_dates)
    
    # O(nlogn)
    sort(list_of_countries,sort_by_offers_req7)
    
    # Obtener las primeras n ofertas O(n)
    if lt.size(list_of_countries) < int(best_n_countries):
        best_n_countries = lt.size(list_of_countries)
    
    best_countries = lt.subList(list_of_countries,1,int(best_n_countries))
    
    #Hallar total de ofertas de la consulta O(1)
    total_offers = total_offers_best_n_countries(best_countries)
    
    #Crear un mapa con llaves de ciudades O(n)
    
    city_map = create_city_map(best_countries)
    
    #Encontrar el máximo y mínimo de las ciudades O(m)
    city_max, city_n_max, city_min, city_n_min = map_max_and_min_list_values(city_map)
    
    #Hallar el país con más ofertas O(1) ya está ordenado por ofertas
    max_country_entry = lt.getElement(best_countries,1)
    junior_max_country, mid_max_country, senior_max_country = get_experience_info(max_country_entry)
    key_max_country = me.getKey(max_country_entry)
    value_max_country = lt.size(junior_max_country) + lt.size(mid_max_country) + lt.size(senior_max_country)
    
    #Crear mapas para habilidades en cada nivel de experiencia O(n)    
    junior_skill_map,mid_skill_map,senior_skill_map,junior_level_map,mid_level_map,senior_level_map = create_skill_and_level_map(data_structs,best_countries)
    
    
    #Hallar máximo y minimo de las habilidades para cada nivel de experiencia O(m) cada uno
    junior_skill_max, junior_n_skill_max, junior_skill_min, junior_n_skill_min = map_max_and_min_list_values(junior_skill_map)
    mid_skill_max, mid_n_skill_max, mid_skill_min, mid_n_skill_min = map_max_and_min_list_values(mid_skill_map)
    senior_skill_max, senior_n_skill_max, senior_skill_min, senior_n_skill_min = map_max_and_min_list_values(senior_skill_map)
    
    #Calcular el nivel promedio de las habilidades para cada nivel de experiencia  O(1) cada uno
    
    junior_lvl_avg = lvl_avg(junior_level_map)
    mid_lvl_avg = lvl_avg(mid_level_map)
    senior_lvl_avg = lvl_avg(senior_level_map)
    

    #Se crean dos mapas en ambos las llaves son las empresas que tienen ofertas con el nivel promedio de habilidades.
    # El valor de company_map es la lista con las ofertas de trabajo
    # El valor de address_map es otro mapa donde las llaves son las sedes distintas de 'NOT DEFINED' y el valor es la cantidad de ofertas en esa sede
    # O(n)  
    junior_company_map, junior_address_map = create_company_map(junior_level_map,junior_lvl_avg)
    mid_company_map, mid_address_map = create_company_map(mid_level_map,mid_lvl_avg)
    senior_company_map, senior_address_map = create_company_map(senior_level_map,senior_lvl_avg)
    
    #Se halla el máximo y mínimo de las empresas O(m) cada uno
    
    junior_company_max, junior_n_company_max, junior_company_min, junior_n_company_min = map_max_and_min_list_values(junior_company_map)
    mid_company_max, mid_n_company_max, mid_company_min, mid_n_company_min = map_max_and_min_list_values(mid_company_map)
    senior_company_max, senior_n_company_max, senior_company_min, senior_n_company_min = map_max_and_min_list_values(senior_company_map)
    
    #Contar las empresas que tienen más de una dirección
    
    many_addresses_junior = count_companies_addresses(junior_address_map)
    many_addresses_mid = count_companies_addresses(mid_address_map)
    many_addresses_senior = count_companies_addresses(senior_address_map)
    
    #Organizar las respuestas por cada nivel de experiencia
    
    junior_ans = mp.size(junior_skill_map), junior_skill_max, junior_n_skill_max, junior_skill_min, junior_n_skill_min, junior_lvl_avg, mp.size(junior_company_map), junior_company_max, junior_n_company_max, junior_company_min, junior_n_company_min,many_addresses_junior
    mid_ans = mp.size(mid_skill_map), mid_skill_max, mid_n_skill_max, mid_skill_min, mid_n_skill_min, mid_lvl_avg, mp.size(mid_company_map), mid_company_max, mid_n_company_max, mid_company_min, mid_n_company_min,many_addresses_mid
    senior_ans = mp.size(senior_skill_map), senior_skill_max, senior_n_skill_max, senior_skill_min, senior_n_skill_min, senior_lvl_avg, mp.size(senior_company_map), senior_company_max, senior_n_company_max, senior_company_min, senior_n_company_min,many_addresses_senior
    
    return total_offers, mp.size(city_map), key_max_country, value_max_country, city_max, city_n_max, junior_ans, mid_ans, senior_ans
    

def req_8(data_structs,experience,currency,start,end):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    
    if experience.upper() != 'IND':
        entry = mp.get(data_structs['experience_level'],experience.lower())
        exp_list = me.getValue(entry)
        sort(exp_list,sort_by_date)
    else:
        exp_list = data_structs['jobs']
    
    jobs_in_dates = time_sublist(exp_list,start,end)
    
    aux_companies = mp.newMap(500,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_company)
    aux_cities = mp.newMap(500,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_company)
    
    aux_countries = mp.newMap(500,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_company)
    
    aux_skills = mp.newMap(500,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_company)
    
    aux_country_list = lt.newList(datastructure='ARRAY_LIST',cmpfunction=compare_names)
    
    total_companies = 0
    
    total_offers = 0
    range_salary = 0
    fixed_salary = 0
    no_salary = 0
    
    for job in lt.iterator(jobs_in_dates):
        job_id = job['id']
        employment_entry = mp.get(data_structs['employment_id'],job_id)
        employment = me.getValue(employment_entry)
        job_currency = employment['currency_salary']
        
        skills_list = me.getValue(mp.get(data_structs['skill_id'],job_id))
        if currency.lower() == job_currency or currency.lower() == '':
        
            total_offers +=1
            add_key_to_aux_map(aux_cities, job['city'], job)
            total_companies += add_company_country(aux_companies, job['company_name'], job['country_code'] , job )
            add_skills_country(aux_skills, job['country_code'],skills_list,job)
            sum_to_fixed, sum_to_range,sum_to_no_s = add_to_country_map_req8(aux_countries, aux_country_list,  job['country_code'],
                                    job,employment,job_currency)
            range_salary += sum_to_range
            fixed_salary += sum_to_fixed
            no_salary += sum_to_no_s
        

            
    for country in lt.iterator(mp.keySet(aux_countries)):
        
        country_entry = mp.get(aux_countries,country)
        country_map = me.getValue(country_entry)
        
        fixed_entry = mp.get(country_map,'fixed_salary')
        fixed_list = me.getValue(fixed_entry)
        
        range_entry = mp.get(country_map,'range_salary')
        range_list = me.getValue(range_entry)
        
        avg_entry = mp.get(country_map,'avg')
        avg_sum = me.getValue(avg_entry)
        
        avg = avg_sum/(lt.size(fixed_list)+lt.size(range_list))
        
        country_element = lt.getElement(aux_country_list,lt.isPresent(aux_country_list,country))
        country_element['avg'] = round(avg,2)
        
    sort(aux_country_list,sort_by_avg)
    
 
    
    countries_ans = create_ans_list(aux_countries,aux_country_list,currency,aux_companies,aux_skills)
    
    most_salary = lt.getElement(countries_ans, 1)
    least_salary= lt.getElement(countries_ans, lt.size(aux_country_list))
    
    part_2 = most_salary, least_salary       
              
    part_1 = total_companies, total_offers, mp.size(aux_countries), mp.size(aux_cities), range_salary, fixed_salary, no_salary, countries_ans
    return part_1, part_2
    
    
    

def view_data(data_structs, keys):
    """ Función para visualizar datos dada una lista de llaves
    Args:
        data_structs (_type_): _description_
        keys (_type_): _description_
    """
    show = []
    size = lt.size(data_structs)
    if size > 10:
        big = True
        show = [[],[]]
        i = 1
        while i < 6:
            show[0].append(new_data(lt.getElement(data_structs,i),keys))
            show[1].append(new_data(lt.getElement(data_structs,size-5+i),keys))
            i +=1
    else:
        big = False
        for data in lt.iterator(data_structs):
            show.append(new_data(data,keys))
    return show,big

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs,sort_crit):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    
    merg.sort(data_structs, sort_crit)
    
    

def sort_by_date (e1, e2):
    """
    Devuelve verdadero (True) si la empresa de la oferta1 es menor que en la oferta2,
    en caso de que sean iguales se analiza la fecha de publicación de la oferta laboral,
    de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "company_name" y "published_at"
    oferta2: información de la segunda oferta laboral que incluye
    "company_name" y "published_at"
    """
    
    published_at_1 = dt.strptime(e1['published_at'],'%Y-%m-%dT%H:%M:%S.%fZ')
    published_at_2 = dt.strptime(e2['published_at'],'%Y-%m-%dT%H:%M:%S.%fZ')
    
    if published_at_1 > published_at_2:
        return True
    else:
        return False

def sort_by_company_and_date(oferta1, oferta2):
    """
    Devuelve verdadero (True) si la empresa de la oferta1 es menor que en la oferta2,
    en caso de que sean iguales se analiza la fecha de publicación de la oferta laboral,
    de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "company_name" y "published_at"
    oferta2: información de la segunda oferta laboral que incluye
    "company_name" y "published_at"
    """
    
    company_name_1 = oferta1['company_name']
    company_name_2 = oferta2['company_name']
    
    published_at_1 = dt.strptime(oferta1['published_at'],'%Y-%m-%dT%H:%M:%S.%fZ')
    published_at_2 = dt.strptime(oferta2['published_at'],'%Y-%m-%dT%H:%M:%S.%fZ')
    
    if company_name_1 == company_name_2:
        if published_at_1 > published_at_2:
            return True
        else:
            return False
    elif company_name_1 < company_name_2:
        return True
    else:
        return False
    

def sort_by_date_and_country(oferta1, oferta2):
    """
    Devuelve verdadero (True) si la fecha de la oferta1 es menor que en la oferta2,
    en caso de que sean iguales se analiza el código del país de la oferta laboral,
    de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "country" y "published_at"
    oferta2: información de la segunda oferta laboral que incluye
    "country" y "published_at"
    """
    published_at_1 = dt.strptime(oferta1['published_at'],'%Y-%m-%dT%H:%M:%S.%fZ')
    published_at_2 = dt.strptime(oferta2['published_at'],'%Y-%m-%dT%H:%M:%S.%fZ')
    
    country1 = oferta1['country_code']
    country2 = oferta2['country_code']
    
    if published_at_1 == published_at_2:
        if country1 < country2:
            return True
        else:
            return False
    elif published_at_1 > published_at_2:
        return True
    else:
        return False

def sort_by_date_and_company(oferta1, oferta2):
    """
    Devuelve verdadero (True) si la fecha de la oferta1 es menor que en la oferta2,
    en caso de que sean iguales se analiza la fecha de publicación de la oferta laboral,
    de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "company_name" y "published_at"
    oferta2: información de la segunda oferta laboral que incluye
    "company_name" y "published_at"
    """
    
    company_name_1 = oferta1['company_name']
    company_name_2 = oferta2['company_name']
    
    published_at_1 = dt.strptime(oferta1['published_at'],'%Y-%m-%dT%H:%M:%S.%fZ')
    published_at_2 = dt.strptime(oferta2['published_at'],'%Y-%m-%dT%H:%M:%S.%fZ')
    
    if  published_at_1 == company_name_2:
        if company_name_1 < company_name_2:
            return True
        else:
            return False
    elif published_at_1 > published_at_2:
        return True
    else:
        return False

def sort_by_offers_req7(e1,e2):
    map_1 = me.getValue(e1)
    map_2 = me.getValue(e2)
    
    offers_1 = 0
    offers_2 = 0
    
    exps_1 = mp.keySet(map_1)
    
    for exp in lt.iterator(exps_1):
        entry = mp.get(map_1,exp)
        offers = me.getValue(entry)
        offers_1 += lt.size(offers)
        
    exps_2 = mp.keySet(map_2)
    
    for exp in lt.iterator(exps_2):
        entry = mp.get(map_2,exp)
        offers = me.getValue(entry)
        offers_2 += lt.size(offers)
    
    if offers_1 > offers_2:
        return True
    else:
        return False
    
def sort_by_avg(e1,e2):
    avg_1 = e1['avg']
    avg_2 = e2['avg']
    
    if avg_1 > avg_2:
        return True
    else:
        return False
    
def compare_id(Id, job):
    id_entry = me.getKey(job)
    if (Id == id_entry):
        return 0
    elif (Id > id_entry):
        return 1
    else:
        return -1
    
def compare_city(city, job):
    city_entry = me.getKey(job)
    if (city == city_entry):
        return 0
    elif (city > city_entry):
        return 1
    else:
        return -1
    
def compare_company(company, job):
    coompany_entry = me.getKey(job)
    if (company == coompany_entry):
        return 0
    elif (company > coompany_entry):
        return 1
    else:
        return -1

def compare_countries(country,job):
    country_entry = me.getKey(job)
    if (country == country_entry):
        return 0
    elif (country > country_entry):
        return 1
    else:
        return -1

def compare_dates(date, job):
    date_entry = me.getKey(job)
    date = date[:10]
    if (date == date_entry):
        return 0
    elif (date > date_entry):
        return 1
    else:
        return -1
    

#Funciones auxiliares REQ 4

def time_sublist(data_structs,start,end):
    
    jobs = data_structs 
    size = lt.size(jobs)
    start_date = dt.strptime(start,'%Y-%m-%d')
    end_date = dt.strptime(end,'%Y-%m-%d')
    
    #Encontrar el último (cronológicamente) que cumple con el requisito
    
    last_element = lt.firstElement(jobs)
    last_date = dt.strptime(last_element['published_at'][:10],'%Y-%m-%d')
    if end_date >= last_date:
        last = 1
    else:
        last_found = False
        last = 1
        
        while not(last_found) and last <= size :
            job = lt.getElement(jobs,last)
            date = dt.strptime(job['published_at'][:10],'%Y-%m-%d')
            
            if date <= end_date:
                last_found = True
                last -=1
                
            last += 1
    
    #Encontrar el primero (cronológicamente) que cumple con el requisito
    
    first_element = lt.lastElement(jobs)
    first_date = dt.strptime(first_element['published_at'][:10],'%Y-%m-%d')
    if start_date <= first_date:
        first = size
    else:
        first_found = False
        first = size
        
        while not(first_found) and first >= 1 :
            job = lt.getElement(jobs,first)
            date = dt.strptime(job['published_at'][:10],'%Y-%m-%d') #Solo se quiere información del año mes y dia por eso solo se toman los primeros 10 caracteres.
            if date >= start_date:
                first_found = True
                first +=1
            first -= 1
    
    #Como está ordenada según fechas, todos los datos entre esas posiciones cumplen la condición
    return lt.subList(jobs,last,first-last+1)


def add_counter(aux_map,key):
    if mp.contains(aux_map,key):
        entry = mp.get(aux_map,key)
        actual_count = me.getValue(entry)
        me.setValue(entry,actual_count+1)
    else:
        mp.put(aux_map,key,1)
        
def map_max_and_min(aux_map):
    """Encuentra el máximo y mínimo para mapas donde el valor es un entero

    """
    
    keys = mp.keySet(aux_map)
    max_key = ''
    max_value = 0
    min_key = ''
    min_value = float('inf')
    
    for key in lt.iterator(keys):
        value = me.getValue(mp.get(aux_map,key))
        if value > max_value:
            max_value = value
            max_key = key
        
        if value < min_value:
            min_value = value
            min_key = key 
    
    return max_key, max_value, min_key, min_value

def map_max_and_min_list_values(aux_map):
    """Encuentra el máximo y mínimo para mapas donde el valor es una lista

    """
    
    keys = mp.keySet(aux_map)
    max_key = ''
    max_value = 0
    min_key = ''
    min_value = float('inf')
    
    for key in lt.iterator(keys):
        value = me.getValue(mp.get(aux_map,key))
        size = lt.size(value)
        if size > max_value:
            max_value = size
            max_key = key
        
        if size < min_value:
            min_value = size
            min_key = key 
    
    return max_key, max_value, min_key, min_value

def create_aux_countries(jobs_in_dates):
    countries = mp.newMap(200,
                    maptype='PROBING',
                    loadfactor=4,
                    cmpfunction=compare_countries)
    
    for job in lt.iterator(jobs_in_dates):
        country_code = job['country_code']
        
        exist_country = mp.contains(countries, country_code)
        
        if exist_country:
            entry = mp.get(countries, country_code)
            experience_map = me.getValue(entry)
        else:
            experience_map = mp.newMap(5,
                    maptype='PROBING',
                    loadfactor=0.8,
                    cmpfunction=compare_countries)
            mp.put(experience_map, 'junior',lt.newList(datastructure='ARRAY_LIST'))
            mp.put(experience_map, 'mid',lt.newList(datastructure='ARRAY_LIST'))
            mp.put(experience_map, 'senior',lt.newList(datastructure='ARRAY_LIST'))
            
            mp.put(countries, country_code, experience_map)
            
        experience = job['experience_level']
        entry = mp.get(experience_map, experience)
        exp_list = me.getValue(entry)
        lt.addLast(exp_list, job)
        
    map_list = lt.newList(datastructure='ARRAY_LIST')
    
    keys = mp.keySet(countries)
    for country in lt.iterator(keys):
        lt.addLast(map_list,mp.get(countries,country))
    
    return map_list
    

def get_experience_info(country):
    exp_map = me.getValue(country)
        
    junior = me.getValue(mp.get(exp_map,'junior')) 
    mid = me.getValue(mp.get(exp_map,'mid')) 
    senior = me.getValue(mp.get(exp_map,'senior'))
    
    return junior,mid,senior

def total_offers_best_n_countries(best_countries):
    
    total_offers = 0
    
    for country in lt.iterator(best_countries):
         
        junior,mid,senior = get_experience_info(country)
       
        offers_in_country = lt.size(junior) + lt.size(mid) + lt.size(senior)
        
        total_offers += offers_in_country
    return total_offers


def create_city_map(best_countries):
    cities = mp.newMap(500,
                    maptype='CHAINING',
                    loadfactor=4,
                    cmpfunction=compare_countries)
    
    for country in lt.iterator(best_countries):
        
        junior,mid,senior = get_experience_info(country)
        
        for job in lt.iterator(junior):
            city_name = job['city']
    
            exist_city = mp.contains(cities, city_name)
            
            if exist_city:
                entry = mp.get(cities, city_name)
                city_list = me.getValue(entry)
            else:
                city_list = lt.newList(datastructure='ARRAY_LIST')
                mp.put(cities, city_name, city_list)

            lt.addLast(city_list, job)
        
        for job in lt.iterator(mid):
            city_name = job['city']
    
            exist_city = mp.contains(cities, city_name)
            
            if exist_city:
                entry = mp.get(cities, city_name)
                city_list = me.getValue(entry)
            else:
                city_list = lt.newList(datastructure='ARRAY_LIST')
                mp.put(cities, city_name, city_list)

            lt.addLast(city_list, job)
            
        for job in lt.iterator(senior):
            city_name = job['city']
    
            exist_city = mp.contains(cities, city_name)
            
            if exist_city:
                entry = mp.get(cities, city_name)
                city_list = me.getValue(entry)
            else:
                city_list = lt.newList(datastructure='ARRAY_LIST')
                mp.put(cities, city_name, city_list)

            lt.addLast(city_list, job)
            
    return cities

def create_skill_and_level_map(data_structs,best_countries):
    
    skills = data_structs['skill_id']
    
    junior_skill_map = mp.newMap(600,
                    maptype='PROBING',
                    loadfactor=0.5,
                    cmpfunction=compare_countries)
    
    mid_skill_map = mp.newMap(600,
                    maptype='PROBING',
                    loadfactor=0.5,
                    cmpfunction=compare_countries)
    
    senior_skill_map = mp.newMap(600,
                    maptype='PROBING',
                    loadfactor=0.5,
                    cmpfunction=compare_countries)
    
    junior_level_map = mp.newMap(8,
                    maptype='PROBING',
                    loadfactor=0.5,
                    cmpfunction=compare_countries)
    
    mid_level_map = mp.newMap(8,
                    maptype='PROBING',
                    loadfactor=0.5,
                    cmpfunction=compare_countries)
    
    senior_level_map = mp.newMap(8,
                    maptype='PROBING',
                    loadfactor=0.5,
                    cmpfunction=compare_countries)
    
    for country in lt.iterator(best_countries):
        
        junior,mid,senior = get_experience_info(country)
        
        for job in lt.iterator(junior):
            
            job_id = job['id']
            entry = mp.get(skills,job_id)
            skill_list = me.getValue(entry)
            
            for skill in lt.iterator(skill_list):
                skill_name = skill['name']
                
                exist_skill = mp.contains(junior_skill_map, skill_name)
                
                if exist_skill:
                    entry = mp.get(junior_skill_map, skill_name)
                    skill_list = me.getValue(entry)
                else:
                    skill_list = lt.newList(datastructure='ARRAY_LIST')
                    mp.put(junior_skill_map, skill_name, skill_list)

                lt.addLast(skill_list, job)
                
                level = skill['level']
                exist_level = mp.contains(junior_level_map, level)
                
                if exist_level:
                    entry = mp.get(junior_level_map, level)
                    level_list = me.getValue(entry)
                else:
                    level_list = lt.newList(datastructure='ARRAY_LIST')
                    mp.put(junior_level_map, level, level_list)

                lt.addLast(level_list, job)
            
        
        for job in lt.iterator(mid):
            
            job_id = job['id']
            entry = mp.get(skills,job_id)
            skill_list = me.getValue(entry)
            
            for skill in lt.iterator(skill_list):
                skill_name = skill['name']
                
                exist_skill = mp.contains(mid_skill_map, skill_name)
                
                if exist_skill:
                    entry = mp.get(mid_skill_map, skill_name)
                    skill_list = me.getValue(entry)
                else:
                    skill_list = lt.newList(datastructure='ARRAY_LIST')
                    mp.put(mid_skill_map, skill_name, skill_list)

                lt.addLast(skill_list, job)
                
                level = skill['level']
                exist_level = mp.contains(mid_level_map, level)
                
                if exist_level:
                    entry = mp.get(mid_level_map, level)
                    level_list = me.getValue(entry)
                else:
                    level_list = lt.newList(datastructure='ARRAY_LIST')
                    mp.put(mid_level_map, level, level_list)

                lt.addLast(level_list, job)
            
        for job in lt.iterator(senior):
            
            job_id = job['id']
            entry = mp.get(skills,job_id)
            skill_list = me.getValue(entry)
            
            for skill in lt.iterator(skill_list):
                skill_name = skill['name']
                
                exist_skill = mp.contains(senior_skill_map, skill_name)
                
                if exist_skill:
                    entry = mp.get(senior_skill_map, skill_name)
                    skill_list = me.getValue(entry)
                else:
                    skill_list = lt.newList(datastructure='ARRAY_LIST')
                    mp.put(senior_skill_map, skill_name, skill_list)

                lt.addLast(skill_list, job)
                
                level = skill['level']
                exist_level = mp.contains(senior_level_map, level)
                
                if exist_level:
                    entry = mp.get(senior_level_map, level)
                    level_list = me.getValue(entry)
                else:
                    level_list = lt.newList(datastructure='ARRAY_LIST')
                    mp.put(senior_level_map, level, level_list)

                lt.addLast(level_list, job)
            
    return junior_skill_map,mid_skill_map,senior_skill_map,junior_level_map,mid_level_map,senior_level_map
    
    
def lvl_avg(level_map):
    
    level_sum = 0
    levels = mp.keySet(level_map)
    total_offers = 0
    for level in lt.iterator(levels):
        level_list = me.getValue(mp.get(level_map,level))
        offers = lt.size(level_list)
        total_offers += offers
        level_sum += int(level)*offers
    if total_offers == 0:
        return 0
    
    level_avg = level_sum//total_offers
    
    return level_avg

def create_company_map(level_map,lvl_avg):
    
    companies = mp.newMap(500,
                            maptype='CHAINING',
                            loadfactor=4,
                            cmpfunction=compare_company)
    
    companies_address = mp.newMap(500,
                            maptype='CHAINING',
                            loadfactor=4,
                            cmpfunction=compare_company)
    
    if not(mp.contains(level_map,str(lvl_avg))):
        return companies,companies_address
    
    entry = mp.get(level_map,str(lvl_avg))
    avg_level_list = me.getValue(entry)
    
    
    
    for job in lt.iterator(avg_level_list):
        
        company_name = job['company_name']
        exist_company = mp.contains(companies, company_name)
        
        if exist_company:
            entry = mp.get(companies, company_name)
            company_list = me.getValue(entry)
            
            entry_2 = mp.get(companies_address, company_name)
            addresses_map = me.getValue(entry_2)
        else:
            company_list = lt.newList(datastructure='ARRAY_LIST')
            mp.put(companies, company_name, company_list)
             
            addresses_map = mp.newMap(50,
                            maptype='CHAINING',
                            loadfactor=4,
                            cmpfunction=compare_company)
            mp.put(companies_address, company_name, addresses_map)

        lt.addLast(company_list, job)
        
        address = job['address_text']
        
        if address != 'NOT DEFINED':
            exist_address = mp.contains(addresses_map, address)
            
            if exist_address:
                entry = mp.get(addresses_map, address)
                n_addrresses = me.getValue(entry)
            else:
                n_addrresses = 0
                mp.put(addresses_map,address,n_addrresses)
            n_addrresses += 1
        
        
    return companies,companies_address
        
def count_companies_addresses(address_map):
    count = 0 
    countries = mp.keySet(address_map)
    
    for country in lt.iterator(countries):
        entry = mp.get(address_map,country)
        addresses = me.getValue(entry)
        
        if lt.size(addresses) > 1:
            count += 1
    return count


def add_key_to_aux_map(aux_map, key, job):
    
    exist_key = mp.contains(aux_map, key)
    
    if exist_key:
        entry = mp.get(aux_map, key)
        value_list = me.getValue(entry)
    else:
        value_list = lt.newList(datastructure='SINGLE_LINKED')
        mp.put(aux_map, key, value_list)

    lt.addLast(value_list, job)

def add_company_country(aux_companies, company, country, job):
    sum_to_comp = 0
    exist_key = mp.contains(aux_companies, country)
    
    if exist_key:
        entry = mp.get(aux_companies, country)
        value_map = me.getValue(entry)
    else:
        value_map = mp.newMap(50,
                            maptype='PROBING',
                            loadfactor=4,
                            cmpfunction=compare_company)

        mp.put(aux_companies, country, value_map)
    
    exist_key = mp.contains(value_map, company)
    
    if exist_key:
        entry = mp.get(value_map, company)
        value_list = me.getValue(entry)
    else:
        value_list = lt.newList(datastructure='SINGLE_LINKED')
        mp.put(value_map, company, value_list)
        sum_to_comp += 1

    lt.addLast(value_list, job)
    
    return sum_to_comp
    
def add_skills_country(aux_skills, country,skills_list,job):
    for skill in lt.iterator(skills_list):
        
        exist_key = mp.contains(aux_skills, country)
        
        if exist_key:
            entry = mp.get(aux_skills, country)
            value_map = me.getValue(entry)
        else:
            value_map = mp.newMap(50,
                                maptype='PROBING',
                                loadfactor=4,
                                cmpfunction=compare_company)

            mp.put(aux_skills, country, value_map)
        
        skill_name = skill['name']
        exist_key = mp.contains(value_map, skill_name)
        
        if exist_key:
            entry = mp.get(value_map, skill_name)
            value_list = me.getValue(entry)
        
        else:
            value_list = lt.newList(datastructure='SINGLE_LINKED')
            mp.put(value_map, skill_name, value_list)

        lt.addLast(value_list, job)
        

    
def add_to_country_map_req8(aux_countries,aux_country_list, country_code, job,employment,job_currency):
    
    sum_to_fixed = 0
    sum_to_range = 0
    sum_to_no_s = 0
    
    exist_country = mp.contains(aux_countries, country_code)
    
    
    
    if exist_country:
        entry = mp.get(aux_countries, country_code)
        country_map = me.getValue(entry)
        
    else:
        country_map = mp.newMap(50,
                            maptype='PROBING',
                            loadfactor=4,
                            cmpfunction=compare_company)
        mp.put(country_map, 'range_salary',lt.newList(datastructure='ARRAY_LIST'))
        mp.put(country_map, 'fixed_salary',lt.newList(datastructure='ARRAY_LIST'))
        mp.put(country_map, 'no_salary',lt.newList(datastructure='ARRAY_LIST'))
        mp.put(country_map, 'avg',0)

        mp.put(aux_countries, country_code, country_map)
        
        country_list_element = new_country(country_code)
        lt.addLast(aux_country_list,country_list_element)
    
    if job_currency == '':
        entry = mp.get(country_map,'no_salary')
        no_salary_list = me.getValue(entry)
        lt.addLast(no_salary_list,job)
        sum_to_no_s +=1
        
    elif employment['salary_from'] == employment['salary_to']:
        entry = mp.get(country_map,'fixed_salary')
        fixed_salary_list = me.getValue(entry)
        lt.addLast(fixed_salary_list,job)
        sum_to_fixed +=1
        
    else:
        entry = mp.get(country_map,'range_salary')
        range_salary_list = me.getValue(entry)
        lt.addLast(range_salary_list,job)
        sum_to_range += 1
    
    if job_currency != '':  
        entry = mp.get(country_map,'avg' )
        avg = me.getValue(entry)
        mp.put(country_map,'avg', avg+ ((int(employment['salary_from']) + int(employment['salary_to']))/2))
        
    
    return sum_to_fixed, sum_to_range,sum_to_no_s
    
def new_country(country_code):

    country = {'name': '', 'jobs': None,'avg':0}
    country['name'] = country_code
    country['jobs'] = lt.newList(datastructure='SINGLE_LINKED')
    return country
    
def compare_names(name, info):
    if (name == info['name']):
        return 0
    elif (name > info['name']):
        return 1
    return -1

def create_ans_list(aux_countries,aux_country_list,currency,aux_companies,aux_skills):
    ans_list = lt.newList(datastructure='ARRAY_LIST')
    for country in lt.iterator(aux_country_list):
        code = country['name']
        avg =  country['avg']
        
        country_map = me.getValue(mp.get(aux_countries,code))
        
        fixed_list = me.getValue(mp.get(country_map,'fixed_salary'))
        range_list = me.getValue(mp.get(country_map,'range_salary'))
        no_salary_list = me.getValue(mp.get(country_map,'no_salary'))
        
        companies_map = me.getValue(mp.get(aux_companies,code))
        
        country_skills_map = me.getValue(mp.get(aux_skills,code))
        
        info = {'País': code,
                'Promedio de oferta salarial': str(avg) +' ' +currency,
                'Número de empresas que publicaron': mp.size(companies_map),
                'Numero de ofertas publicadas': lt.size(fixed_list) + lt.size(range_list)+ lt.size(no_salary_list),
                'Número de ofertas con salario': lt.size(fixed_list) + lt.size(range_list),
                'Número promedio de habilidades por oferta': round(mp.size(country_skills_map)/(lt.size(fixed_list) + lt.size(range_list)+ lt.size(no_salary_list)),3),
               }
        lt.addLast(ans_list,info)
    return ans_list
        
        
def change_to_usd(amount, currency):
    if currency == 'pln':
        usd = amount*1
    if currency == 'eur':
        usd = amount*1
    if currency == 'gbp':
        usd = amount*1
    if currency == 'pln':
        usd = amount*1
    if currency == 'pln':
        usd = amount*1
                

        