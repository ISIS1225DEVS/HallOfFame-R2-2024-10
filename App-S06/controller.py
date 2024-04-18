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
import tracemalloc
import config as cf
import model
import time
import csv
import tracemalloc
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from datetime import datetime as dt
from DISClib.DataStructures import mapentry as me
import sys
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
csv.field_size_limit(2147483647)

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

def load_data(control, memflag=True):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    loadSalarios(control)
    loadSkills(control)
    loadJobs(control)
    loadLocations(control)

    sort(control["model"]["jobs"],model.compFechas)

    paises = mp.keySet(control["model"]["por_pais"])
    niveles = ["junior","mid","senior"]
    
    for pais in lt.iterator(paises):
        for nivel in niveles:
            a_ordenar = mp.get(control["model"]["por_pais"],pais)
            valores = me.getValue(a_ordenar)
            sort(valores[nivel],model.compFechas)
    
    empresas = mp.keySet(control["model"]["por_empresa"])
    
    for empresa in lt.iterator(empresas):
        a_ordenar = mp.get(control["model"]["por_empresa"],empresa)
        valores = me.getValue(a_ordenar)
        sort(valores["ofertas"],model.compFechas)
        
    ciudades = mp.keySet(control["model"]["por_ciudad"])
    
    for ciudad in lt.iterator(ciudades):
        a_ordenar = mp.get(control["model"]["por_ciudad"],ciudad)
        valores = me.getValue(a_ordenar)
        sort(valores["all_jobs"],model.compFechas)
        
    stop_time = get_time()
    # calculando la diferencia en tiempo
    deltaTime = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return deltaTime, deltaMemory

    else:
        # respuesta sin medir memoria
        return deltaTime

def loadJobs(control):
    filename = cf.data_dir + 'large-jobs.csv'
    jobs_file = csv.DictReader(open(filename, encoding="utf-8"), delimiter=";")
    
    for job in jobs_file:
        job = cambiar_formato_trabajos(control,job)
        model.add_job(control["model"],job)
    
def loadSalarios(control):
    salarios = cf.data_dir + 'large-employments_types.csv'
    salary_file = csv.DictReader(open(salarios, encoding="utf-8"), delimiter=";")
     
    for salario in salary_file:      
        model.add_salary(control["model"],salario)
    
    
def loadSkills(control):
    skills = cf.data_dir + 'large-skills.csv'
    skills_file = csv.DictReader(open(skills, encoding="utf-8"), delimiter=";")
    
    for skill in skills_file: 
        model.add_skill(control["model"],skill)

def loadLocations(control):
    
    pass

# Funciones de ordenamiento

def cambiar_formato_trabajos(control,element):
    
    element["year"] = element["published_at"].split('-')[0]#Se crea la llave year para poder separarlos por año más adelante
    element["month"] =element["published_at"].split('-')[1]
    
    formato_fecha = "%Y-%m-%dT%H:%M:%S.%fZ" #2022-06-01T09:00:25.390Z
    fecha = element["published_at"]
    
    fecha = dt.strptime(fecha, formato_fecha)
    element["published_at"] = fecha 
    
    company = element["company_name"].lower()
    element["company_name"] = company
    
    info_salarios_dupla = mp.get(control["model"]["salarios"],element["id"])
    info_salarios = me.getValue(info_salarios_dupla)
    
    try:
        element["salary_from"] = int(info_salarios["salary_from"])
    except:
        element["salary_from"] = 0
    try:
        element["salary_to"] = int(info_salarios["salary_to"])
    except:
        element["salary_to"] = 0
    
    info_skills_dupla = mp.get(control["model"]["skills"],element["id"])
    info_skills = me.getValue(info_skills_dupla)
    
    element["ability"] = info_skills["name"]
    element["level"] = int(info_skills["level"])
    
    return element

def sort(control,criterio):
    """
    Ordena los datos del modelo
    """
    model.sort(control,criterio)


# Funciones de consulta sobre el catálogo
def prim_ult_tres(data_structs):
    filtro = ["published_at", "title", "company_name", "experience_level", "country_code", "city"]
    n = lt.size(data_structs)
    if n<6:
        return data_structs
    else: 
        prim = lt.subList(data_structs,1,3)
        last= lt.subList(data_structs, n-2,3)
        res= lt.newList()
        
        for job in lt.iterator(prim):
            filtered_values = [job[key] for key in filtro if key in job]
            lt.addLast(res,filtered_values)
      
        for job in lt.iterator(last):
            filtered_values = [job[key] for key in filtro if key in job]
            lt.addLast(res,filtered_values)

        return res  

def get_first_last_five(list):
    filtered = lt.newList("ARRAY_LIST")
    for i in range(1, 6):
        lt.addLast(filtered, lt.getElement(list, i))
    for i in range(-4, 1):
        lt.addLast(filtered, lt.getElement(list, i))
    return filtered

def req_1(control,pais,nivel,n,memflag=False):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    data_structs = control["model"]
    
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    lista, total_trabajos,total_ofertas_pais = model.req_1(data_structs,pais,nivel,n)
    

    filtro = ["published_at", "title", "company_name", "experience_level", "country_code", "city", 
              "company_size","workplace_type","open_to_hire_ukrainians"]
    respuesta = model.filtrar_llaves(lista,filtro)
    
    stop_time = get_time()
    # calculando la diferencia en tiempo
    deltaTime = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return respuesta,deltaTime,total_trabajos,total_ofertas_pais, deltaMemory

    else:
        # respuesta sin medir memoria
        return respuesta,deltaTime,total_trabajos,total_ofertas_pais

def req_2(control,empresa,ciudad,num_ofertas, memflag=False):
    """
    Retorna el resultado del requerimiento 2
    """
    data_structs = control["model"]
    
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    lista, total_ofertas = model.req_2(data_structs,empresa,ciudad,num_ofertas)

    filtro = ["published_at", "country_code", "city", "company_name", "title", "experience_level", 
              "remote_interview","workplace_type"]
    respuesta = model.filtrar_llaves(lista,filtro)
    
    stop_time = get_time()
    # calculando la diferencia en tiempo
    deltaTime = delta_time(start_time,stop_time)
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return respuesta,total_ofertas, deltaTime, deltaMemory
    else:
        return respuesta,total_ofertas, deltaTime

def req_3(control,empresa,fecha_inicial,fecha_final,memflag=False):
    """
    Retorna el resultado del requerimiento 3
    """
    
    data_struct = control["model"] 
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    start_time = get_time()
    
    lista,junior,mid,senior,total= model.req_3(data_struct,empresa,fecha_inicial,fecha_final)
    
    filtro = ["published_at", "title","experience_level","city","country_code", "company_size","workplace_type","open_to_hire_ukrainians"]
    
    lista_filtrada = model.filtrar_llaves(lista,filtro)
    
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return lista_filtrada, junior, mid, senior, total, deltaTime, deltaMemory
    else:
        return lista_filtrada, junior, mid, senior, total, deltaTime


def req_4(control,codigo,fechaInicio,fechaFin):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    data_struct = control["model"] 
    start_time = get_time()
    
    ofertas_en_pais,total_ofertas_final,total_empresas,total_ciudades,ciudad_mayor_ofertas,ciudad_menor_ofertas= model.req_4(data_struct,codigo,fechaInicio,fechaFin)
    
    filtro = ["published_at", "title", "experience_level", "company_name", "city", "workplace_type", "remote_interview", "open_to_hire_ukrainians"]
    
    lista_filtrada = model.filtrar_llaves(ofertas_en_pais,filtro)
    
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    
    return lista_filtrada,total_ofertas_final,total_empresas,total_ciudades,ciudad_mayor_ofertas,ciudad_menor_ofertas, deltaTime


def req_5(control, ciudad, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    data_struct = control["model"] 
    start_time = get_time()
    
    respuesta, n_empresas, empresa_mayor, mayor, empresa_menor, menor,n= model.req_5(data_struct, ciudad, fecha_inicial, fecha_final)
    
    filtro = ["published_at", "title","company_name", "company_size", "workplace_type"]
    
    lista_filtrada = model.filtrar_llaves(respuesta,filtro)
    
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    
    return lista_filtrada, n_empresas, empresa_mayor, mayor, empresa_menor, menor,n, deltaTime
    pass

def req_6(control,nivel,anio,num_ciudades,memflag=False):
    """
    Retorna el resultado del requerimiento 6
    """
    data_structs = control["model"] 
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    try:
        lista,total_ciudades_que_cumplen, total_empresas_que_cumplen, total_ofertas_que_cumplen, ciudad_mayor, ciudad_menor = model.req_6(data_structs,nivel,anio,num_ciudades)
        end_time = get_time()
        deltaTime = delta_time(start_time, end_time)
        if memflag is True:
            stop_memory = get_memory()
            tracemalloc.stop()
            # calcula la diferencia de memoria
            deltaMemory = delta_memory(stop_memory, start_memory)
        else:
            deltaMemory = 0
        return lista,total_ciudades_que_cumplen, total_empresas_que_cumplen, total_ofertas_que_cumplen, ciudad_mayor, ciudad_menor,deltaTime, deltaMemory
    except:
        lista,total_ciudades_que_cumplen, total_empresas_que_cumplen, total_ofertas_que_cumplen= model.req_6(data_structs,nivel,anio,num_ciudades)
    
        end_time = get_time()
        deltaTime = delta_time(start_time, end_time)
        if memflag is True:
            stop_memory = get_memory()
            tracemalloc.stop()
            # calcula la diferencia de memoria
            deltaMemory = delta_memory(stop_memory, start_memory)
        else:
            deltaMemory = 0
        
        return lista,total_ciudades_que_cumplen, total_empresas_que_cumplen, total_ofertas_que_cumplen,deltaTime,deltaMemory

def req_7(control,anio,mes,num_paises,memflag=False):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    data_structs = control["model"] 
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    lista,total_ofertas,mayor_pais, junior, mid, senior = model.req_7(data_structs,anio,mes,num_paises)
    
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return lista,total_ofertas,mayor_pais, junior, mid, senior, deltaTime, deltaMemory
    else:
        return lista,total_ofertas,mayor_pais, junior, mid, senior, deltaTime

def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


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
