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

def load_data(control, size):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    tracemalloc.start()
    start_memory = get_memory()

    data_structs = control['model']


    size_jobs = load_jobs(data_structs, size)
    size_paises = model.paises_size(data_structs)
    size_ciudades = model.ciudades_size(data_structs)
    size_empresas = model.empresas_size(data_structs)
    size_years = model.years_size(data_structs)
    
    size_skills = load_skills(data_structs, size)
    size_employment_types = load_emp(data_structs, size)
    size_multilocation = load_multilocations (data_structs, size)
    
    stop_time = get_time()
    deltaTime = delta_time(stop_time, start_time)
    
    stop_memory = get_memory()
    tracemalloc.stop()
    deltaMemory = delta_memory(stop_memory, start_memory)
    return size_jobs,size_paises,size_ciudades, size_empresas, size_years, size_skills, size_employment_types, size_multilocation, deltaTime, deltaMemory

def load_jobs(data_structs, size):
    if size == "large":
        archivo = "Kaggle/large-jobs.csv"
    elif size == "small":
        archivo = "Kaggle/small-jobs.csv"
    else:
        archivo = "Kaggle/"+str(size)+"-por-jobs.csv"
        
    jobs_file = cf.data_dir + archivo
    input_file = csv.DictReader(open(jobs_file, encoding= 'utf-8'), delimiter = ";")
    for job in input_file:
        model.add_job(data_structs,job)
    
    return model.job_size(data_structs)

def load_skills (data_structs, size):
    if size == "large":
        archivo = "Kaggle/large-skills.csv"
    elif size == "small":
        archivo = "Kaggle/small-skills.csv"
    else:
        archivo = "Kaggle/"+str(size)+"-por-skills.csv"
        
    skills_file = cf.data_dir + archivo
    input_file = csv.DictReader(open(skills_file, encoding= 'utf-8'), delimiter = ";")
    for skill in input_file:
        model.add_skill(data_structs,skill)
    
    return model.skills_size(data_structs) 
 
def load_emp (data_structs, size):
    if size == "large":
        archivo = "Kaggle/large-employments_types.csv"
    elif size == "small":
        archivo = "Kaggle/small-employments_types.csv"
    else:
        archivo = "Kaggle/"+str(size)+"-por-employments_types.csv"
        
    emp_file = cf.data_dir + archivo
    input_file = csv.DictReader(open(emp_file, encoding= 'utf-8'), delimiter = ";")
    for emp in input_file:
        model.add_employment_types(data_structs,emp)
    
    return model.emp_size(data_structs)

def load_multilocations (data_structs, size):
    if size == "large":
        archivo = "Kaggle/large-multilocations.csv"
    elif size == "small":
        archivo = "Kaggle/small-multilocations.csv" 
    else:
        archivo = "Kaggle/"+str(size)+"-por-multilocations.csv"
        
    mult_file = cf.data_dir + archivo
    input_file = csv.DictReader(open(mult_file, encoding= 'utf-8'), delimiter = ";")
    for mult in input_file:
        model.add_multilocation(data_structs,mult)
    
    return model.mult_size(data_structs) 


#Funciones de los requerimientos

def req_1(control,codigo, nivel):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1

    start_time = get_time()
    ofertas = model.req_1(control["model"], codigo, nivel)
    end_time = get_time()
    delt_time = delta_time(end_time, start_time)
    return ofertas, delt_time


def req_2(control, empresa, ciudad):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    ofertas = model.req_2(control["model"], empresa, ciudad)
    end_time = get_time()
    delt_time = delta_time(end_time, start_time)
    return ofertas, delt_time


def req_3(control, empresa, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()    
    ofertas = model.req_3(control["model"],empresa, fecha_inicial,fecha_final)
    end_time = get_time()
    delt_time = delta_time(end_time, start_time)
    return ofertas, delt_time


def req_4(control, codigo, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()    
    ofertas = model.req_4(control["model"], codigo, fecha_inicio, fecha_fin)
    end_time = get_time()
    delt_time = delta_time(end_time, start_time)
    return ofertas, delt_time


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control, n_ciudades, año, experticia):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()    
    ofertas = model.req_6(control["model"], n_ciudades, año, experticia)
    end_time = get_time()
    delt_time = delta_time(end_time, start_time)
    return ofertas, delt_time

def empresa_con_mas_ofertas(control, ofertas):
    data = model.empresa_con_mas_ofertas(control["model"], ofertas)
    return data


def req_7(control, n_paises, year, month):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()    
    result = model.req_7(control["model"],n_paises, year, month)
    end_time = get_time()
    delt_time = delta_time(end_time, start_time)
    return result, delt_time


def req_8(control, experticia, divisa, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_time = get_time()    
    result = model.req_8(control["model"],experticia, divisa, fecha_inicial, fecha_final)
    end_time = get_time()
    delt_time = delta_time(end_time, start_time)
    return result, delt_time


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(end, start):
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
