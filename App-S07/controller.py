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
import threading

import config as cf
import csv
import sys
import model
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
import time
import tracemalloc
from additional import consoleMethods as coco
from datetime import datetime as dt


csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*100)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control

# en el reto 1 se usan diferentes metodos de carga, aqui se selecciono uno solo para todos.
# En el caso de jobs se omite la primera linea para saltarses las llaves.

def load_data(control):
    ##! [LAB 7] QUITAR/DEBUG/REMOVER
    """
    Carga los datos del reto
    """
    
    """
    tracemalloc.start() ##! [LAB 7] QUITAR/DEBUG/REMOVER
    start_memory = getMemory() ##! [LAB 7] QUITAR / REMOVE
    """
    start_time = time.time() * 1000 ##! [LAB 7] QUITAR/DEBUG/REMOVER
    
    catalog = control['model']
    TempSkills = {}
    TempEmpTypes = {}
    TempMultiLocs = {}
    jobs = loadJobs(catalog) ##* Jobs es el tamaño cargado en el catálogo    skills = loadSkills(TempSkills) ##! Es lista
    skills = loadSkills(TempSkills)
    employmentTy= loadEmpTypes(TempEmpTypes) ##* Es lista
    multiloc = multiLocations(TempMultiLocs) ##* Es lista
    
    ## General el CSV madre de todos los CSVs. MOTHER OF ALL CSVs
    moa, moa2 = model.MOA_CSVs(catalog, TempSkills, TempEmpTypes, TempMultiLocs)
    
    
    stop_time = time.time() * 1000 ##! [LAB 7] QUITAR/DEBUG/REMOVERget time in sems 
    delta_time = stop_time - start_time ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    """
    stop_memory = getMemory() ##! [LAB 7] QUITAR/DEBUG/REMOVER
    tracemalloc.stop() ##! [LAB 7] QUITAR/DEBUG/REMOVER
    # calcula la diferencia de memoria 
    delta_memory = deltaMemory(stop_memory, start_memory) ##! [LAB 7] QUITAR/DEBUG/REMOVER
    # respuesta con los datos de tiempo y memoria
    """
    print("\033[94m TIEMPO DE CARGA: \033[0m")
    print("\033[94m"+ str(delta_time) + " - ms" + "\033[0m")
    """
    print("---------------------------------------------------")
    print("\033[95m USO DE MEMORIA: \033[0m")
    print("\033[95m " + str(delta_memory) + " - Kb " + "\033[0m")
    """

    return jobs, skills, employmentTy, multiloc

##! [LAB 7] QUITAR/DEBUG/REMOVER
def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()

##! [LAB 7] QUITAR/DEBUG/REMOVER
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


##! [LAB 7] QUITAR/DEBUG/REMOVER
def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

##! [LAB 7] QUITAR/DEBUG/REMOVERE
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



def loadJobs(catalog):
    jobsfile = cf.data_dir+"large-jobs.csv" 
    input_file = csv.DictReader(open(jobsfile, encoding='utf-8'), delimiter=";")
    for skill in input_file:
        model.addToCatalog('jobs',catalog, skill)
    return model.catSize('jobs', catalog)


def loadSkills(TempSkills):
    file_path = 'data\large-skills.csv'
    with open(file_path, newline='',encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            smallName= row[0]
            level = row[1]
            Id = row[2]
            if Id not in TempSkills:
                subdic = {'short_name': [],
                 'skill': []}
                TempSkills[Id] = subdic
            listaName = TempSkills[Id]['short_name']
            listaName.append(smallName)
            listaLevel = TempSkills[Id]['skill']
            listaLevel.append(level)
    return TempSkills

def loadEmpTypes(TempEmpTypes):
    file_path = 'data/large-employments_types.csv'

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            tipo_contrato= row[0]
            Id = row[1]
            currency_salary = row[2]
            salario_desde= row[3]
            salario_hasta= row[4] 

            if Id not in TempEmpTypes:
                subdic = {'tipo_contrato': [],
                 'currency_salary': [],
                 "salario_desde":[], 
                 "salario_hasta": []}
                TempEmpTypes[Id] = subdic

            lista_contrato = TempEmpTypes[Id]['tipo_contrato']
            lista_contrato.append(tipo_contrato)

            lista_currency_salary = TempEmpTypes[Id]['currency_salary']
            lista_currency_salary.append(currency_salary)

            lista_salario_desde = TempEmpTypes[Id]['salario_desde']
            lista_salario_desde.append(salario_desde)

            lista_salario_hasta = TempEmpTypes[Id]['salario_hasta']
            lista_salario_hasta.append(salario_hasta)
                
    return TempEmpTypes

def multiLocations(TempMultiLocs):
    locsFile = cf.data_dir+"large-multilocations.csv" 
    with open(locsFile, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:    
            city = row[0]
            street = row[1]
            Id = row[2]
            if Id not in TempMultiLocs:
                subdic = {'city': [],
                 'street': []}
                TempMultiLocs[Id] = subdic

            listaName = TempMultiLocs[Id]['city']
            listaName.append(city)
            listaLevel = TempMultiLocs[Id]['street']
            listaLevel.append(street)
    
    return TempMultiLocs

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


def req_1(catalog, country, exp, N):
    ret = model.req_1(catalog, country, exp)
    keep = ['published_at','title','company_name','experience_level','country_code','city','company_size',
                 'workplace_type', 'open_to_hire_ukrainians']
    fullInfos = ret[0]
    mostRecent = coco.DicKeepOnly(keep, fullInfos, N)
    NoJobsPerCountry = ret[1]
    NoJobsPerExperience = ret[2]
    ansSize = ret[3]
    return mostRecent, NoJobsPerCountry, NoJobsPerExperience, ansSize

def req_2(control, n, nombre_compañia, ciudad):
    """
    Retorna el resultado del requerimiento 2
    """
    total_ciudades, total_empresas, ofertas_info= model.req_2(control, nombre_compañia, ciudad)
    return total_ciudades, total_empresas, ofertas_info

def req_3(catalog, company, startDate, endDate, N):
    ret = model.req_3(catalog, company, startDate, endDate)
    # totaldeOffer, noByJunior, noByMid, noBySenior, dsfullInfos
    totaldeOffer = ret[0]
    noByJunior = ret[1]
    noByMid = ret[2]
    noBySenior = ret[3]
    dsfullInfos = ret[4]
    keep = ['published_at','title','experience_level','country_code','city','company_size',
            'workplace_type', 'open_to_hire_ukrainians']
    table = coco.DicKeepOnly(keep, dsfullInfos, N)
    table= table['elements']
    return totaldeOffer, noByJunior, noByMid, noBySenior, table




def req_4(control, CODpais, Ffirst, Flast):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    control=control["model"]
    start_time = time.time() * 1000 ##! [LAB 7] QUITAR/DEBUG/REMOVER
    res = model.req_4(control, CODpais, Ffirst, Flast)
    stop_time = time.time() * 1000 ##! [LAB 7] QUITAR/DEBUG/REMOVERget time in sems 
    delta_time = stop_time - start_time ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    print("\033[1m TIEMPO DE Req 4: \033[0m") ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    print("\033[1m"+ str(delta_time) + " - ms" + "\033[0m") ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    return res


def req_5(control, ciudad, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    fecha_inicial = dt.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final = dt.strptime(fecha_final, "%Y-%m-%d")
    
    total_ciudad, total_empresas, tupla_max, tupla_min, ofertas_sorted= model.req_5(control, ciudad, fecha_inicial, fecha_final)

    return total_ciudad, total_empresas, tupla_max, tupla_min, ofertas_sorted
    
def req_6(catalog, exp, year, N):
    ans = model.req_6(catalog, exp, year, N)
    return ans


def req_7(control, numeroPaises, año, mes):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    control=control["model"]
    start_time = time.time() * 1000 ##! [LAB 7] QUITAR/DEBUG/REMOVER
    res = model.req_7(control, numeroPaises, año, mes)
    stop_time = time.time() * 1000 ##! [LAB 7] QUITAR/DEBUG/REMOVERget time in sems 
    delta_time = stop_time - start_time ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    print("\033[1m TIEMPO DE Req 7: \033[0m") ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    print("\033[1m"+ str(delta_time) + " - ms" + "\033[0m") ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    junior=(("Cantidad habilidades diferentes solicitadas: "+str(res[4][0])),
            ("Habilidad más solicitada "+str(res[4][1]["key"])+" conteo: "+str(res[4][1]["value"])),
            ("Habilidad menos solicitada "+str(res[4][2]["key"])+" conteo: "+str(res[4][2]["value"])),
            ("Nivel mínimo promedio de las habilidades: "+str(res[4][3])),
            ("Cantidad empresas diferentes solicitadas: "+str(res[4][4])),
            ("Empresa mayor número ofertas "+str(res[4][5]["key"])+" conteo: "+str(res[4][5]["value"])),
            ("Empresa menor número ofertas "+str(res[4][6]["key"])+" conteo: "+str(res[4][6]["value"])),
            ("Cantidad empresas con 1 o más sedes: "+str(res[4][7]))
    )
    mid=(("Cantidad habilidades diferentes solicitadas: "+str(res[5][0])),
            ("Habilidad más solicitada "+str(res[5][1]["key"])+" conteo: "+str(res[5][1]["value"])),
            ("Habilidad menos solicitada "+str(res[5][2]["key"])+" conteo: "+str(res[5][2]["value"])),
            ("Nivel mínimo promedio de las habilidades: "+str(res[5][3])),
            ("Cantidad empresas diferentes solicitadas: "+str(res[5][4])),
            ("Empresa mayor número ofertas "+str(res[5][5]["key"])+" conteo: "+str(res[5][5]["value"])),
            ("Empresa menor número ofertas "+str(res[5][6]["key"])+" conteo: "+str(res[5][6]["value"])),
            ("Cantidad empresas con 1 o más sedes: "+str(res[5][7]))
    )
    senior=(("Cantidad habilidades diferentes solicitadas: "+str(res[6][0])),
            ("Habilidad más solicitada "+str(res[6][1]["key"])+" conteo: "+str(res[6][1]["value"])),
            ("Habilidad menos solicitada "+str(res[6][2]["key"])+" conteo: "+str(res[6][2]["value"])),
            ("Nivel mínimo promedio de las habilidades: "+str(res[6][3])),
            ("Cantidad empresas diferentes solicitadas: "+str(res[6][4])),
            ("Empresa mayor número ofertas "+str(res[6][5]["key"])+" conteo: "+str(res[6][5]["value"])),
            ("Empresa menor número ofertas "+str(res[6][6]["key"])+" conteo: "+str(res[6][6]["value"])),
            ("Cantidad empresas con 1 o más sedes: "+str(res[6][7]))
    )
    ans=False
    if lt.size(res[7])>10:
        ans=True
    #ans=coco.DicKeepOnly(keep=res[7],arrLi=res[7],N=5)
    return res[0],res[1],res[2],res[3],junior,mid,senior,res[7],ans


def req_8(control,Nivel_experticia,Divisa,Ffirst,Flast):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    control=control["model"]
    start_times = time.time() * 1000 ##! [LAB 7] QUITAR/DEBUG/REMOVER
    res=model.req_8(control,Nivel_experticia,Divisa,Ffirst,Flast)
    stop_times = time.time() * 1000 ##! [LAB 7] QUITAR/DEBUG/REMOVERget time in sems 
    delta_times = stop_times - start_times ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    print("\033[92m TIEMPO DE req_8: \033[0m") ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    print("\033[92m"+ str(delta_times) + " - ms" + "\033[0m") ##! [LAB 7] QUITAR/DEBUG/REMOVERE
    return res


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