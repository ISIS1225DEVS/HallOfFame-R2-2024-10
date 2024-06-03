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
from DISClib.Algorithms.Sorting import quicksort as quk
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(tipo, alfa, archivo):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {'model' : None}
    control['model'] = model.nuevo_catalogo(tipo, alfa, archivo)
    return control


# Funciones para la carga de datos

def load_data(control, filename, memory):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    tiempo_inicial=get_time()
    if memory == True:
        tracemalloc.start()
        memoria_inicial=get_memory()
    catalogo= control['model']
    jobs=loadjobs(catalogo, filename)
    skills=loadskills(catalogo, filename)
    employments=loademployments(catalogo, filename)
    multilocations=loadmultilocations(catalogo, filename)
    tiempo_final= get_time()
    tiempo_total=delta_time(tiempo_inicial, tiempo_final)
    memoria_total=None
    if memory == True:
        memoria_final= get_memory()
        tracemalloc.stop()
        memoria_total= delta_memory(memoria_final, memoria_inicial)
    return quk.sort(jobs, fecha), skills, employments, multilocations, tiempo_total, memoria_total

def load_map(catalogo, filename):
    jobfile=cf.data_dir + filename + 'jobs.csv'
    inputfile=csv.DictReader(open(jobfile,encoding='utf-8'), delimiter=';')
    for job in inputfile:
        model.add_job_map(catalogo,job)
        
#TODO_ IMPORTANTEEEEEEE

def loadjobs(catalogo, filename):
    jobfile=cf.data_dir + filename + 'jobs.csv'
    inputfile=csv.DictReader(open(jobfile,encoding='utf-8'), delimiter=';')
    for job in inputfile:
        model.add_job(catalogo,job)
    return catalogo['jobs_list']

def loadskills(catalogo, filename):
    skillsfile=cf.data_dir+ filename +'skills.csv'
    inputfile=csv.DictReader(open(skillsfile,encoding='utf-8'),delimiter=';',fieldnames=['name','level','id'])
    for skill in inputfile:
        model.add_skill(catalogo,skill)
    return catalogo['skills_list']

def loademployments(catalogo, filename):
    employmentsfile=cf.data_dir + filename +'employments_types.csv'
    inputfile=csv.DictReader(open(employmentsfile,encoding='utf-8'),delimiter=';',fieldnames=['type','id','currency_salary','salary_from','salary_to'])
    for employment in inputfile:
        model.add_employment(catalogo,employment)
    return catalogo['employments_list']

def loadmultilocations(catalogo, filename):
    multilocationfile=cf.data_dir + filename + 'multilocations.csv'
    inputfile=csv.DictReader(open(multilocationfile,encoding='utf-8'),delimiter=';',fieldnames=['city','street','id'])
    for multi in inputfile:
        model.add_multilocation(catalogo,multi)
    return catalogo['multilocations_list']

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data=model.get_data(control['model'], id)
    #TODO: Llamar la función del modelo para obtener un dato
    return data

#Requerimientos
def req_1(control, n, pais, exp):
    """
    Retorna el resultado del requerimiento 1
    """
    tiempo_inicial=get_time()
    rta=model.req_1(control['model'], n, pais, exp )
    tiempo_final=get_time()
    tiempo_total=delta_time(tiempo_inicial, tiempo_final)
    return tiempo_total, rta


def req_2(control,empresa,ciudad,n):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    tiempo_inicial=get_time()
    rta=model.req_2(control['model'],empresa,ciudad,n)
    tiempo_final=get_time()
    tiempo_total=delta_time(tiempo_inicial,tiempo_final)
    return tiempo_total,rta
    

def req_3(control, nombre, inicio, final):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    tiempo_inicial=get_time()
    
    #CÓDIGO
    rta = model.req_3(control['model'], nombre, inicio, final)
    tiempo_final=get_time()
    tiempo_total=delta_time(tiempo_inicial, tiempo_final)
    return tiempo_total,rta


def req_4(control,pais,fecha_inicio,fecha_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    tiempo_inicial=get_time()
    
    ans = model.req_4(control['model'],pais,fecha_inicio,fecha_fin)
    
    tiempo_final=get_time()
    tiempo_total=delta_time(tiempo_inicial, tiempo_final)
    return tiempo_total, ans


def req_5(control,ciudad,fecha_inicio,fecha_fin):
    
    tiempo_inicial=get_time()
    rta=model.req_5(control['model'],ciudad,fecha_inicio,fecha_fin)
    tiempo_final=get_time()
    tiempo_total=delta_time(tiempo_inicial, tiempo_final)
    return tiempo_total,rta

def req_6(control,n, exp, anio):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    tiempo_inicial=get_time()
    
    ans=model.req_6(control['model'],n, exp, anio)
    
    tiempo_final=get_time()
    tiempo_total=delta_time(tiempo_inicial, tiempo_final)
    return tiempo_total, ans


def req_7(control,n_paises,anio_mes):
    tiempo_inicial=get_time()
    rta=model.req_7(control['model'],n_paises,anio_mes)
    tiempo_final=get_time()
    tiempo_total=delta_time(tiempo_inicial, tiempo_final)
    return tiempo_total,rta


def req_8(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    tiempo_inicial=get_time()
    
    #CÓDIGO
    
    tiempo_final=get_time()
    tiempo_total=delta_time(tiempo_inicial, tiempo_final)
    return tiempo_total


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

#Funciones de ordenamiento

def fecha(dato1, dato2):
    return dato1['published_at'][:10]<dato2['published_at'][:10]

