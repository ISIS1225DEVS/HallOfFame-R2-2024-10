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
    control ={'model':None}
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control, memflag=True):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    jobs=load_jobs(control)
    multilocations=load_multilocations(control)
    employments=load_employments(control)
    skills=load_skills(control)
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)

    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        respuesta= delta_time, delta_memory

    else:
        # respuesta sin medir memoria
        respuesta= delta_time
    
    return jobs, multilocations, employments, skills, respuesta

def load_jobs(data_struct):
    archivo_jobs = cf.data_dir + 'large-jobs.csv'
    input_file = csv.DictReader(open(archivo_jobs, encoding='utf-8'), delimiter=';')
    for data in input_file:
        model.add_jobs(data_struct['model'], data)
    return model.data_size_jobs(data_struct['model'])

def load_multilocations(data_struct):
    archivo_multilocations = cf.data_dir + 'large-multilocations.csv'
    input_file = csv.DictReader(open(archivo_multilocations, encoding='utf-8'), delimiter=';')
    for data in input_file:
        model.add_multilocations(data_struct['model'], data)
    return model.data_size_multilocations(data_struct['model'])

def load_employments(data_struct):
    archivo_employments = cf.data_dir + 'large-employments_types.csv'
    input_file = csv.DictReader(open(archivo_employments, encoding='utf-8'), delimiter=';')
    for data in input_file:
        model.add_employments(data_struct['model'], data)
    return model.data_size_employments(data_struct['model'])

def load_skills(data_struct):
    archivo_skills = cf.data_dir + 'large-skills.csv'
    input_file = csv.DictReader(open(archivo_skills, encoding='utf-8'), delimiter=';')
    for data in input_file:
        model.add_skills(data_struct['model'], data)
    return model.data_size_skills(data_struct['model'])

def tres_info(control):
    return model.tres_info(control['model'])
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
    return model.get_data(control,id)


def req_1(control,num_ofertas,codigo_pais,nivel_experticia):
    """
    Retorna el resultado del requerimiento 1
    """
    req1=model.req_1(control["model"]['jobs'],num_ofertas,codigo_pais,nivel_experticia)
    return req1


def req_2(control,num_ofertas,nom_empresa,ciudad_oferta):
    """
    Retorna el resultado del requerimiento 2
    """
    req2=model.req_2(control["model"]['jobs'],num_ofertas,nom_empresa,ciudad_oferta)
    return req2
    


def req_3(control,nom_empresa,fecha_inicial,fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    req3=model.req_3(control["model"],nom_empresa,fecha_inicial,fecha_final)
    return req3
    


def req_4(control,codigo_pais,fecha_inicial,fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    req4=model.req_4(control["model"],codigo_pais,fecha_inicial,fecha_final)
    return req4


def req_5(control,ciudad_oferta,fecha_inicial,fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    req5=model.req_5(control["model"],ciudad_oferta,fecha_inicial,fecha_final)
    return req5

def req_6(control,num_ciudades,nivel_experticia,ano_consulta):
    """
    Retorna el resultado del requerimiento 6
    """
    req6=model.req_6(control["model"],num_ciudades,nivel_experticia,ano_consulta)
    return req6


def req_7(control,num_paises,ano_consulta,mes_consulta):
    """
    Retorna el resultado del requerimiento 7
    """
    req7=model.req_7(control["model"],num_paises,ano_consulta,mes_consulta)
    return req7


def req_8(control,nivel_experticia,divisa,fecha_inicial,fecha_final):
    """
    Retorna el resultado del requerimiento 8
    """
    req8=model.req_8(control["model"],nivel_experticia,divisa,fecha_inicial,fecha_final)
    return req8


# Funciones para medir tiempos de ejecucion

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
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
