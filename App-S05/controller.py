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

from genericpath import getatime
import config as cf
import model
import time
import csv
import tracemalloc
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt

from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as merg

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control

    #TODO:) Llamar la función del modelo que crea las estructuras de datos
    pass


# Funciones para la carga de datos

def load_data(control,muestra, memflag=True):
    """
    Carga los datos del reto
    """


    # TODO: lab 7, implementacion del catalogo midiendo el tiempo y memoria
    # toma el tiempo al inicio del proceso
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    data_struct = control['model']
    
   
    
    load_multilocations(data_struct,muestra)
    load_skills(data_struct, muestra)
    load_employmentTypes(data_struct, muestra)
    
    numjobs=load_tablasJobs(data_struct, muestra)
    primeros3, ultimos3=primeros3_ultimos3(data_struct)
    

    # toma el tiempo al final del proceso
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
        return [numjobs, [[delta_time, delta_memory], primeros3, ultimos3]]

    else:
        # respuesta sin medir memoria
        return [numjobs, [delta_time, primeros3, ultimos3]]
    
    
    
    #numero de trabajos cargados y los primeros y ultimos
    
    # TODO: Realizar la carga de datos
    
    

def load_tablasJobs(data_struct, muestra):
    jobfile = cf.data_dir + muestra+'-jobs.csv'
    input_file = csv.DictReader(open(jobfile, encoding='utf-8'),delimiter=';')
    sumatoria=0
    
    for job in input_file:
        model.add_tabla_paisxExpLevel(data_struct, job)
        model.add_tabla_empresas(data_struct, job)
        model.add_tabla_ciudades(data_struct, job)
        model.add_tabla_paises(data_struct, job)
        model.add_tabla_niveles_experiencia(data_struct,job)
        
        salarioJobPareja=mp.get(data_struct["tabla_employmentTypesID"], job["id"])
        salarioJobValue=me.getValue(salarioJobPareja)
        job["salary_from"]=salarioJobValue["salary_from"]
        job["salary_to"]=salarioJobValue["salary_to"]
        model.add_tabla_ciudadxExpLevel(data_struct, job)
        sumatoria+=1
        
    return sumatoria



def load_employmentTypes(data_struct, muestra):
    skillsFile = cf.data_dir + muestra + '-employments_types.csv'
    input_file = csv.DictReader(open(skillsFile, encoding='utf-8'),delimiter=';')
    prev=None
    
    for employmentType in input_file:
        current=employmentType
        if prev==None:
            model.add_tabla_employmentTypesID(data_struct, employmentType)
        elif prev["id"]==employmentType["id"]:
            NewEmploymentType=employmentType
            if prev["type"]=="b2b":
                NewEmploymentType["salary_to"]=prev["salary_to"]
            else:
                NewEmploymentType["salary_from"]=prev["salary_from"]
            model.add_tabla_employmentTypesID(data_struct, NewEmploymentType)
        else:
            model.add_tabla_employmentTypesID(data_struct, employmentType)
            
        prev=current

        
    return None


def load_multilocations(data_struct, muestra):
    skillsFile = cf.data_dir + muestra + '-multilocations.csv'
    input_file = csv.DictReader(open(skillsFile, encoding='utf-8'),delimiter=';')
    
    pre_prev={"id":None}
    prev={"id":None}
    
    for multilocation in input_file:
        current=multilocation
        
        #añado el elemento a multilocation si tiene más de una location y solo lo añado una vez
        if prev["id"]==pre_prev["id"] and current["id"]!=prev["id"] and prev["id"]!=None:
            model.add_tabla_multilocationID(data_struct, prev)
            
        pre_prev=prev
        prev=current
    
    return None


def load_skills(data_struct, muestra):
    skillsFile = cf.data_dir + muestra + '-skills.csv'
    input_file = csv.DictReader(open(skillsFile, encoding='utf-8'),delimiter=';')
    for skill in input_file:
        model.add_tabla_skillsID(data_struct, skill)
    
    return None

def primeros3_ultimos3(data_struct):
    #Saco las parejas de los años
    pareja2022=mp.get(data_struct["tabla_paisxExpLevel"], "2022")
    pareja2023=mp.get(data_struct["tabla_paisxExpLevel"], "2023")
    #Saco los keys del value de esas parejas que son la lista de meses
    keys2022=mp.keySet(me.getValue(pareja2022)["meses"])
    keys2023=mp.keySet(me.getValue(pareja2023)["meses"])

    #Sorteo para que queden ordenados la lista de keys de meses
    sortedKeys2022=model.sort_numeros_MenorMayor(keys2022)
    sortedKeys2023=model.sort_numeros_MayorMenor(keys2023)
    #Saco el primer mes y el ultimo mes del primer año y del ultimo año respectivamente
    primer_mesKey=lt.getElement(sortedKeys2022,1)
    ultimo_mesKey=lt.getElement(sortedKeys2023,1)
    
    #Cojo la pareja de ese ultimo mes y el primer mes
    parejaMes2022=mp.get(me.getValue(pareja2022)["meses"], primer_mesKey)
    parejaMes2023=mp.get(me.getValue(pareja2023)["meses"], ultimo_mesKey)
    #Saco el keyset de esos meses que sería la lista de paises
    keysPaisesMes2022=mp.keySet(me.getValue(parejaMes2022)["paises"])
    keysPaisesMes2023=mp.keySet(me.getValue(parejaMes2023)["paises"])
    
    #La lista que despues ordenare del primer mes
    listaJobs_PrimerMes=lt.newList(datastructure="ARRAY_LIST")

    #Para cada pais recorro sus exp_levels para sacar sus ofertas y los añado en una lista
    for pais in lt.iterator(keysPaisesMes2022):
        parejaPais=mp.get((me.getValue(parejaMes2022)["paises"]), pais)
        #La lista de exp levels de ese pais
        keys_expLevel=mp.keySet(me.getValue(parejaPais)["experience_levels"])
        
        #Recorro cada exp Level
        for exp_level in lt.iterator(keys_expLevel):
            #Saco la pareja de ese exp level
            pareja_expLevel=mp.get(me.getValue(parejaPais)["experience_levels"], exp_level)
            #Saco las ofertas de ese expLevel
            jobs=me.getValue(pareja_expLevel)
            
            #Añado cada uno de esos trabajo a la lista que va a ser sorteada
            for job in lt.iterator(jobs["jobs"]):
                lt.addLast(listaJobs_PrimerMes, job)
    
    
    #La lista que despues ordenare del ultimo mes
    listaJobs_UltimoMes=lt.newList(datastructure="ARRAY_LIST")

    #Para cada pais recorro sus exp_levels para sacar sus ofertas y los añado en una lista
    for pais in lt.iterator(keysPaisesMes2023):
        parejaPais=mp.get((me.getValue(parejaMes2023)["paises"]), pais)
        #La lista de exp levels de ese pais
        keys_expLevel=mp.keySet(me.getValue(parejaPais)["experience_levels"])
        
        #Recorro cada exp Level
        for exp_level in lt.iterator(keys_expLevel):
            #Saco la pareja de ese exp level
            pareja_expLevel=mp.get(me.getValue(parejaPais)["experience_levels"], exp_level)
            #Saco las ofertas de ese expLevel
            jobs=me.getValue(pareja_expLevel)
            
            #Añado cada uno de esos trabajo a la lista que va a ser sorteada
            for job in lt.iterator(jobs["jobs"]):
                lt.addLast(listaJobs_UltimoMes, job)
        
    sorted_listaJobs_PrimerMes=model.sortJobsDate_MenorMayor(listaJobs_PrimerMes)
    sorted_listaJobs_UltimoMes=model.sortJobsDate_MayorMenor(listaJobs_UltimoMes)

    primeros3=lt.subList(sorted_listaJobs_PrimerMes,1,5)
    ultimos3=lt.subList(sorted_listaJobs_UltimoMes,1,5)
    
    return primeros3, ultimos3

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


def req_1(control, pais, exp, n, memflag):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    
    a = model.req_1(control['model'], pais, exp, n)    
    
    # toma el tiempo al final del proceso
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
        return [a, [delta_time, delta_memory]]

    else:
        # respuesta sin medir memoria
        return [a, delta_time]




def req_2(control, city, emp, n, memflag):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    
    a = model.req_2_final(control["model"], city, emp, n)
    
    
    # toma el tiempo al final del proceso
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
        return [a, [delta_time, delta_memory]]

    else:
        # respuesta sin medir memoria
        return [a, delta_time]
    



def req_3(control,company_name,start_date, end_date, memflag):
    """
    Retorna el resultado del requerimiento 3

    """

    # toma el tiempo al inicio del proceso
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    resp = model.req_3(control["model"],company_name,start_date, end_date)


    # toma el tiempo al final del proceso
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
        return [resp, [delta_time, delta_memory]]

    else:
        # respuesta sin medir memoria
        return [resp, delta_time]

    



def req_4(control, pais, datei, datef, memflag):
    """
    Retorna el resultado del requerimiento 4
    """
    # toma el tiempo al inicio del proceso
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    
    a = model.req_4(control ["model"], pais, datei, datef)
    
    
    # toma el tiempo al final del proceso
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
        return [a, [delta_time, delta_memory]]

    else:
        # respuesta sin medir memoria
        return [a, delta_time]
    



def req_5(control,  ciudad, fechaInicial, fechaFinal, memflag):
    """
    Retorna el resultado del requerimiento 5
    """
    # toma el tiempo al inicio del proceso
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    
    ans = model.req_5(control["model"], ciudad, fechaInicial, fechaFinal)
    
    
    # toma el tiempo al final del proceso
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
        return [ans, [delta_time, delta_memory]]

    else:
        # respuesta sin medir memoria
        return [ans, delta_time]
    
    

def req_6(control,numCiudades,year,exp_level,memflag):
    """
    Retorna el resultado del requerimiento 6
    """
    # toma el tiempo al inicio del proceso
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    respreq6=model.req_6(control['model'],numCiudades,year,exp_level)



    # toma el tiempo al final del proceso
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
        return [respreq6, [delta_time, delta_memory]]

    else:
        # respuesta sin medir memoria
        return [respreq6, delta_time]

    


def req_7(control, numPaises, year, mes, memflag):
    """
    Retorna el resultado del requerimiento 7
    """
    # toma el tiempo al inicio del proceso
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
        
    ans=model.req_7(control["model"], numPaises, year, mes)

    # toma el tiempo al final del proceso
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
        return [ans, [delta_time, delta_memory]]

    else:
        # respuesta sin medir memoria
        return [ans, delta_time]

def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


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
