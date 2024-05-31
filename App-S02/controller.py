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

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""



def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control, memflag=False):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()

    jobs_loaded = load_jobs(control)
    load_skills(control)
    load_employment_types(control)

    # toma el tiempo al final del proceso
    stop_time = get_time()
    # calculando la diferencia en tiempo
    delta_t = delta_time(start_time, stop_time)

    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_m = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return delta_t, delta_m , jobs_loaded

    else:
        # respuesta sin medir memoria
        return delta_t , jobs_loaded

def load_jobs(control):
    """_summary_

    Carga los trabajos del archivo. 
    """
    jobsfile = cf.data_dir + 'large-jobs.csv'
    input_file = csv.DictReader(open(jobsfile, encoding='utf-8'),delimiter=';')
    for job in input_file:
        model.add_joblist(control['model'],job)
        model.add_job(control['model'], job)
        model.add_city(control['model'], job)
        model.add_company(control['model'], job)
        model.add_country(control['model'],job)
        model.add_experience(control['model'],job)
        model.add_year(control['model'],job)

    model.sort(control['model']['jobs'],model.sort_by_date)
    return model.data_size(control['model']['jobs'])

def load_skills(control):
    skillsfile = cf.data_dir + 'large-skills.csv'
    input_file = csv.DictReader(open(skillsfile, encoding='utf-8'),delimiter=';',fieldnames=['name','level','id'])
    for skill in input_file:
        model.add_skill_by_id(control['model'],skill)
        
def load_employment_types(control):
    employmentsfile = cf.data_dir + 'large-employments_types.csv'
    input_file = csv.DictReader(open(employmentsfile, encoding='utf-8'),delimiter=';',fieldnames=['type','id','currency_salary','salary_from','salary_to'])
    for employment in input_file:
        model.add_employment_by_id(control['model'],employment)

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, n_offers, country_code, experience_level):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    info = model.req_1(control['model'], n_offers, country_code, experience_level)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return info, delta_t



def req_2(control, n, company, city):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    info = model.req_2(control['model'], n, company, city)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return info, delta_t


def req_3(control,empresa,fecha1,fecha2):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    info = model.req_3(control['model'],empresa,fecha1,fecha2)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return info, delta_t


def req_4(control,country,start,end):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    info = model.req_4(control['model'],country,start,end)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return info, delta_t


def req_5(control, city, starting_date, ending_date):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    info = model.req_5(control['model'],city,starting_date,ending_date)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return info, delta_t

def req_6(control,  amount_cities, level_expertise, year):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    answer = model.req_6(control['model'],amount_cities,level_expertise,year)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return answer, delta_t
    


def req_7(control,best_n_countries,start,end):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    info = model.req_7(control['model'],best_n_countries,start,end)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return info, delta_t


def req_8(control,experience,currency,start,end):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_time = get_time()
    info = model.req_8(control['model'],experience,currency,start,end)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return info, delta_t

def view_data(control, keys):
    return model.view_data(control,keys)

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