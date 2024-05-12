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
 """

import config as cf
import model
import time
import csv
import tracemalloc

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def new_controller(data_size, data_structure, load_factor):
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs(data_size, data_structure, load_factor)

    return control


# Funciones para la carga de datos

def load_data(control, filename, memflag):
    """
    Carga los datos del reto
    """
    start_time = get_time()

    if memflag:
        tracemalloc.start()
        start_memory = get_memory()

    catalog = control['model']

    load_jobs(catalog, filename)
    load_skills(catalog, filename)
    load_employment_types(catalog, filename)
    load_multilocations(catalog, filename)

    sort(catalog['jobs'])

    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    deltaMemory = 0

    if memflag:
        stop_memory = get_memory()
        tracemalloc.stop()
        deltaMemory = delta_memory(stop_memory, start_memory)
        
    return catalog['jobs'], deltaTime, deltaMemory

def load_jobs(catalog, filename):
    """
    Carga las caracteristicas de las ofertas de empleo
    """
    jobs_file = cf.data_dir + 'JobFiles/' + filename + '-jobs.csv'
    input_file = csv.DictReader(open(jobs_file, encoding='utf-8'), delimiter=';')
    for job in input_file:
        model.new_job(catalog, job)

def load_skills(catalog, filename):
    """
    Carga las habilidades requeridas de cada oferta
    """
    skills_file = cf.data_dir + 'JobFiles/' + filename + '-skills.csv'
    input_file = csv.DictReader(open(skills_file, encoding='utf-8'), delimiter=';')
    for skill in input_file:
        model.new_data(catalog['skills'], skill)

def load_employment_types(catalog, filename):
    """
    Carga los tipos de contratacion de cada oferta
    """
    employment_file = cf.data_dir + 'JobFiles/' + filename + '-employments_types.csv'
    input_file = csv.DictReader(open(employment_file, encoding='utf-8'), delimiter=';')
    for types in input_file:
        model.new_employment_type(catalog['employment_types'], types)

def load_multilocations(catalog, filename):
    """
    Carga los datos de las sedes de cada oferta 
    """
    multilocations_file = cf.data_dir + 'JobFiles/' + filename + '-multilocations.csv'
    input_file = csv.DictReader(open(multilocations_file, encoding='utf-8'), delimiter=';')
    for multilocation in input_file:
        model.new_data(catalog['multilocations'], multilocation)


# Funciones de ordenamiento

def set_sort_algorithm(algorithm):
    """
    Configura el algoritmo de ordenamiento que se va a utilizar en el
    modelo y lo retorna.
    """
    selected, msg = model.select_sort_algorithm(algorithm)
    model.sort_algorithm = selected

    return msg

def sort(control):
    """
    Ordena los datos del modelo
    """
    catalog = model.sort(control)

    return catalog


# Funciones de consulta sobre el catálogo

def req_1(control, num, country, exp, memflag):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()

    if memflag:
        tracemalloc.start()
        start_memory = get_memory()

    catalog = control['model']
    filtered_jobs, stadistics = model.req_1(catalog, num, country, exp)

    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    deltaMemory = 0

    if memflag:
        stop_memory = get_memory()
        tracemalloc.stop()
        deltaMemory = delta_memory(stop_memory, start_memory)

    return filtered_jobs, stadistics, deltaTime, deltaMemory

def req_2(control, num, company_name, city, memflag):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time = get_time()

    if memflag:
        tracemalloc.start()
        start_memory = get_memory()

    catalog = control['model']
    filtered_jobs = model.req_2(catalog, num, company_name, city)

    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    deltaMemory = 0

    if memflag:
        stop_memory = get_memory()
        tracemalloc.stop()
        deltaMemory = delta_memory(stop_memory, start_memory)

    return filtered_jobs, deltaTime, deltaMemory

def req_3(control,nombre_empresa, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()

    catalog = control["model"]
    num_offers, num_junior, num_mid, num_senior, res = model.req_3(catalog, nombre_empresa, fecha_inicial, fecha_final)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)

    return num_offers, num_junior, num_mid, num_senior, res, deltatime

def req_4(control, country, min_date, max_date, memflag):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()

    if memflag:
        tracemalloc.start()
        start_memory = get_memory()

    catalog = control['model']
    filtered_jobs, cities, companies = model.req_4(catalog, country, min_date, max_date)

    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    deltaMemory = 0
    
    if memflag:
        stop_memory = get_memory()
        tracemalloc.stop()
        deltaMemory = delta_memory(stop_memory, start_memory)

    return filtered_jobs, cities, companies, deltaTime, deltaMemory

def req_5(control, ciudad, fecha_inicio, fecha_fin, memflag):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()

    if memflag:
        tracemalloc.start()
        start_memory = get_memory()

    catalog = control["model"]
    offerr_ciudad, empresas, maximo, minimo, res = model.req_5(catalog, ciudad, fecha_inicio, fecha_fin)
    
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    deltaMemory = 0
    
    if memflag:
        stop_memory = get_memory()
        tracemalloc.stop()
        deltaMemory = delta_memory(stop_memory, start_memory)
    
    return offerr_ciudad, empresas, maximo, minimo, res, deltaTime, deltaMemory

def req_6(control, num_cities, exp, year, memflag):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()

    if memflag:
        tracemalloc.start()
        start_memory = get_memory()

    catalog = control['model']
    filtered_cities, stadistics = model.req_6(catalog, num_cities, exp, year)

    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    deltaMemory = 0
    
    if memflag:
        stop_memory = get_memory()
        tracemalloc.stop()
        deltaMemory = delta_memory(stop_memory, start_memory)

    return filtered_cities, stadistics, deltaTime, deltaMemory

def req_7(control,num_countries, year, month):
    """
    Retorna el resultado del requerimiento 7
    """
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()

    catalog = control['model']
    filtered_offers = model.req_7(catalog, num_countries, year, month)

    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)

    stop_memory = get_memory()
    tracemalloc.stop()
    deltaMemory = delta_memory(stop_memory, start_memory)

    return filtered_offers, deltaTime, deltaMemory

def req_8(control, exp, min_date, max_date, memflag):
    """
    Retorna el resultado del requerimiento 8
    """
    start_time = get_time()

    if memflag:
        tracemalloc.start()
        start_memory = get_memory()

    catalog = control['model']
    filtered_countries, stadistics = model.req_8(catalog, exp, min_date, max_date)

    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    deltaMemory = 0
    
    if memflag:
        stop_memory = get_memory()
        tracemalloc.stop()
        deltaMemory = delta_memory(stop_memory, start_memory)

    return filtered_countries, stadistics, deltaTime, deltaMemory


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()

def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory