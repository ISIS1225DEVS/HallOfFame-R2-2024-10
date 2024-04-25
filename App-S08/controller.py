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
    control={
        "model":None
    }
    #Se llama la función model.new_data_structs (Para crear las estructuras de datos vacias) y se guarda en la llave "model" para reemplazar el None.
    control["model"]=model.new_data_structs()
    #Se devuelve el dict completo con las estructuras
    return control


# Funciones para la carga de datos

def load_data(control, tamanio, memoria):
    """
    Carga los datos del reto
    """
    if memoria==True:
        tracemalloc.start()
        start_memory=get_memory()
    start_time=get_time()
    
    datos=control["model"]
    #Se asignan variables que corresponden a cada tipo de dato que se va a cargar
    full_jobs=datos["jobs"]
    full_skills=datos["skills"]
    full_employments=datos["employment"]
    multilocation=datos["multilocation"]
    #Se llama la función load_jobs que carga los datos del reto
    #Jobs es el diccionario que se va a llenar con los datos
    jobs_cargados=load_jobs(full_jobs, tamanio)
    multilocation=load_multilocation(multilocation, tamanio)
    skills_cargadas=load_skills(full_skills, tamanio)
    employment_cargados=load_employment_types(full_employments, tamanio)
    model.sort_jobs(full_jobs)
    end_time=get_time()
    if memoria==True:
        end_memory=get_memory()
        tracemalloc.stop()
        delta_mem=delta_memory(end_memory, start_memory)
    delta=delta_time(start_time, end_time)
    if memoria==True:
        return {"jobs":jobs_cargados,"skills":skills_cargadas, "employment":employment_cargados, "multilocation":multilocation }, delta, delta_mem
    else:
        return {"jobs":jobs_cargados,"skills":skills_cargadas, "employment":employment_cargados, "multilocation":multilocation }, delta
    


def load_jobs(full_jobs, tamanio):
    """
    Carga los datos de los trabajos en el modelo    de un archivo csv
    Args:
    full_jobs: diccionario con las llaves del archivo Jobs vacias
    tamanio: tamaño del archivo que se va a cargar (10,20,30,40,50,60,70,80,90,small,medium,large)
    Returns:
    full_jobs: diccionario con las llaves del archivo Jobs llenas con los datos del archivo csv
    """
    #Si el tamaño del archivo es small, medium o large se carga el archivo -jobs.csv al ser diferente de -por-jobs.csv
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
        formato_archivo = "-jobs.csv"
    else:
        formato_archivo = "-por-jobs.csv"
        #Se abre el archivo csv y se lee
    print(cf.data_dir)
    with open(cf.data_dir+tamanio+formato_archivo, mode="r", encoding="utf-8") as csvfile:
        data=csv.DictReader(csvfile, delimiter=";")
            #job son los datos del archivo csv en formato de diccionario
        for job in data:
            retorno=model.add_jobs(full_jobs, job)
    return retorno

def load_skills(full_skills, tamanio):
    """
    Carga los datos de las habilidades en el modelo de un archivo csv
    Args:
    full_skills: diccionario con las llaves del archivo Skills vacias
    tamanio: tamaño del archivo que se va a cargar (10,20,30,40,50,60,70,80,90,small,medium,large)
    Returns:
    full_skills: diccionario con las llaves del archivo Skills llenas con los datos del archivo csv
    """
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
        with open(cf.data_dir+tamanio+"-skills.csv", mode="r", encoding="utf-8") as csvfile:
            data=csv.reader(csvfile, delimiter=";")
            for skill in data:
                retorno=model.add_skills(full_skills, skill, tamanio)
    else:
        with open(cf.data_dir+tamanio+"-por-skills.csv", mode="r", encoding="utf-8") as csvfile:
            data=csv.DictReader(csvfile, delimiter=";")
            for skill in data:
                retorno=model.add_skills(full_skills, skill, tamanio)
    return retorno
def load_employment_types(full_employments,tamanio):
    """
    Carga los datos de los empleos por sus tipos del archivo csv
    Args:
        full_employment: diccionario con las llaves del archivo Employment_types vacias
        tamanio: tamaño del archivo que se va a cargar (10,20,30,40,50,60,70,80,90,small,medium,large)

    Returns:
        diccionario con las llaves del archivo Employments_types llenas con los datos del archivo csv
    """
    
    if tamanio in ["small","medium", "large"]:
        with open(cf.data_dir + f"{tamanio}-employments_types.csv", mode="r", encoding="utf-8") as csvfile:
            data = csv.reader(csvfile, delimiter=";")
            for employment in data:
                rta = model.add_employments(full_employments, employment, tamanio)
    else:
        with open(cf.data_dir + f"{tamanio}-por-employments_types.csv", mode="r", encoding="utf-8") as csvfile:
            data = csv.DictReader(csvfile, delimiter=";")
            for employment in data:
                rta = model.add_employments(full_employments, employment, tamanio)
    return rta

def load_multilocation(multilocation, tamanio):
    """
    Carga los datos de multilocation en el modelo de un archivo csv
    Args:
    multilocation: diccionario con las llaves del archivo Multilocation vacias
    tamanio: tamaño del archivo que se va a cargar (10,20,30,40,50,60,70,80,90,small,medium,large)
    Returns:
    multilocation: diccionario con las llaves del archivo multilocation llenas con los datos del archivo csv
    """
    #Si el tamaño del archivo es small, medium o large se carga el archivo -multilocation.csv al ser diferente de -por-multilocation.csv
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
        #Se abre el archivo csv y se lee
        with open(cf.data_dir+tamanio+"-multilocations.csv", mode="r", encoding="utf-8") as csvfile:
            data=csv.reader(csvfile, delimiter=";")
            #multi son los datos del archivo csv en formato de diccionario
            for multi in data:
                retorno=model.add_multilocation(multilocation, multi, tamanio)
    else:
        #Se abre el archivo csv y se lee
        with open(cf.data_dir+tamanio+"-por-multilocations.csv", mode="r", encoding="utf-8") as csvfile:
            data=csv.DictReader(csvfile, delimiter=";")
            #multi son los datos del archivo csv en formato de diccionario
            for multi in data:
                retorno=model.add_multilocation(multilocation, multi, tamanio)
    return retorno


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


def req_1(control, cantidad, cod_pais, experticia):
    start_time = get_time()
    mapa_ofertas, conteo_paises, conteo_experiencias = model.req_1(control["model"], cantidad, cod_pais, experticia)
    end_time = get_time()
    return mapa_ofertas, conteo_paises, conteo_experiencias, delta_time(start_time, end_time)


def req_2(control, num_ofertas, empresa, ciudad):
    """
    Función que resuelve el requerimiento 2.
    """
    start_time = get_time()  
    ofertas_resultado, conteo_empresa, conteo_ciudades = model.req_2(control["model"], num_ofertas, empresa, ciudad)
    end_time = get_time()
    return ofertas_resultado, conteo_empresa, conteo_ciudades, delta_time(start_time, end_time)

    

def req_3(control, nombre_empresa, fecha_ini, fecha_fin, memoria):
    """
    Retorna el resultado del requerimiento 3
    """

    # TODO: Modificar el requerimiento 3
    if memoria==True:
        tracemalloc.start()
        start_memory=get_memory()
    start_time=get_time()
    retorno=model.req_3(control["model"], nombre_empresa, fecha_ini, fecha_fin)
    end_time=get_time()
    if memoria==True:
        end_memory=get_memory()
        tracemalloc.stop()
        delta_mem=delta_memory(end_memory, start_memory)
        return retorno, delta_time(start_time, end_time), delta_mem
    else:
        return retorno, delta_time(start_time, end_time)


def req_4(control,codigo,fecha_inicial,fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    time_ini=get_time()
    retorno=model.req_4(control["model"],codigo,fecha_inicial,fecha_final)
    time_fin=get_time()
    delta=delta_time(time_ini,time_fin)
    return retorno,delta


def req_5(control,ciudad, fecha_ini, fecha_fin, memoria):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    if memoria==True:
        tracemalloc.start()
        start_memory=get_memory()
    start_time=get_time()
    retorno=model.req_5(control["model"], ciudad, fecha_ini, fecha_fin)
    end_time=get_time()
    if memoria==True:
        end_memory=get_memory()
        tracemalloc.stop()
        delta_mem=delta_memory(end_memory, start_memory)
        return retorno, delta_time(start_time, end_time), delta_mem
    else:
        return retorno, delta_time(start_time, end_time)

def req_6(control, num_ciudades, experticia, anio, memoria):
    """
    Retorna el resultado del requerimiento 6
    """
    if memoria==True:
        tracemalloc.start()
        start_memory=get_memory()
    start_time=get_time()
    retorno=model.req_6(control["model"], num_ciudades, experticia, anio)
    end_time=get_time()
    if memoria==True:
        end_memory=get_memory()
        tracemalloc.stop()
        delta_mem=delta_memory(end_memory, start_memory)
        return retorno, delta_time(start_time, end_time), delta_mem
    else:
        return retorno, delta_time(start_time, end_time)


def req_7(control, num_paises, anio_consulta, mes_consulta, memoria):
    """
    Retorna el resultado del requerimiento 7
    """
    if memoria==True:
        tracemalloc.start()
        start_memory=get_memory()
    start_time=get_time()
    retorno=model.req_7(control["model"], num_paises, anio_consulta, mes_consulta)
    end_time=get_time()
    if memoria==True:
        end_memory=get_memory()
        tracemalloc.stop()
        delta_mem=delta_memory(end_memory, start_memory)
        return retorno, delta_time(start_time, end_time), delta_mem
    else:
        return retorno, delta_time(start_time, end_time)


def req_8(control, nivel_experticia, divisa, fecha_ini, fecha_fin, memoria):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_time=get_time()
    if memoria==True:
        tracemalloc.start()
        start_memory=get_memory()
    retorno=model.req_8(control["model"], nivel_experticia, divisa, fecha_ini, fecha_fin)
    end_time=get_time()
    if memoria==True:
        end_memory=get_memory()
        tracemalloc.stop()
        delta_mem=delta_memory(end_memory, start_memory)
        return retorno, delta_time(start_time, end_time), delta_mem
    else:
        return retorno, delta_time(start_time, end_time)


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
