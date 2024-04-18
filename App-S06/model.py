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


import config as cf
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
import sys
from datetime import datetime as d
import csv
csv.field_size_limit(2147483647)

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
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
    
    data_structs = {"jobs":None,
                    "jobs_id":None,
                    "salarios": None,
                    "skills": None,
                    "locations": None,
                    "por_pais": None,
                    "por_ciudad":None,
                    "por_fecha":None,
                    "por_empresa":None,
                    }

    data_structs["jobs"] = lt.newList("ARRAY_LIST",compFechas)

    data_structs["jobs_id"] = mp.newMap(407131,
                                    maptype='PROBING',
                                    loadfactor=0.5,
                                    cmpfunction=compIDs)
    
    data_structs["salarios"] = mp.newMap(407131,
                                    maptype='PROBING',
                                    loadfactor=0.5,
                                    cmpfunction=compIDs)
    
    data_structs["skills"] = mp.newMap(577201,
                                    maptype='PROBING',
                                    loadfactor=0.9,
                                    cmpfunction=compIDs)
    
    data_structs["por_pais"] = mp.newMap(167,
                                    maptype='PROBING',
                                    loadfactor=0.5,
                                    )
    
    data_structs["por_ciudad"] = mp.newMap(357,
                                    maptype='PROBING',
                                    loadfactor=0.9,
                                    )
    
    data_structs["por_fecha"] = mp.newMap(189971,
                                    maptype='PROBING',
                                    loadfactor=0.5,
                                    )
    
    data_structs["por_empresa"] = mp.newMap(4000,
                                    maptype='PROBING',
                                    loadfactor=0.5,
                                    )

    return data_structs
    
# Funciones para agregar informacion al modelo

def add_job(data_structs, job):
    
    lt.addLast(data_structs["jobs"],job)
    id_job = job["id"]
    mp.put(data_structs['jobs_id'],id_job,job)
    
    pais = job["country_code"]
    #Se añaden los paises a un mapa
    add_por_pais(data_structs,pais,job)
    
    #Se añade cada ciudad como llave y su valor son las ofertas de la ciudad y la empresas que hay
    ciudad = job["city"].replace(" ","").lower()
    add_por_ciudad(data_structs,ciudad,job)
    
    #Se añade cada fecha como llave y su valor son las ofertas que hubo en esa fecha
    #fecha = job["published_at"]
    #add_fecha(data_structs,fecha,job)
    
    #Se añaden las empresas como llave y su valor son todas las ofertas que tiene
    empresa = job["company_name"]
    add_por_empresa(data_structs,empresa,job)

def add_salary(data_structs,job):
    mp.put(data_structs["salarios"],job["id"],job)
    
def add_skill(data_structs,job):
    mp.put(data_structs["skills"],job["id"],job)
        
def add_por_pais(data_structs,pais,job):
    
    paises = data_structs['por_pais'] 
    #Se busca si el pais ya tiene una estructura de datos creada, si no, se le crea
    existepais = mp.contains(paises, pais)
    if existepais:
        entry = mp.get(paises, pais)
        nombrepais = me.getValue(entry)
    else:
        nombrepais = new_country(pais)
        mp.put(paises, pais, nombrepais)
    
    #Se añaden todos los trabajos de un país a una lista
    lt.addLast(nombrepais["all_jobs"],job)
    
    #Se añaden los trabajos filtrados por nivel
    if job["experience_level"] == "junior":
        lt.addLast(nombrepais["junior"],job)
        
    elif job["experience_level"] == "mid":
        lt.addLast(nombrepais["mid"],job)
    
    elif job["experience_level"] == "senior":
        lt.addLast(nombrepais["senior"],job)
        
   
def add_por_ciudad(data_structs,ciudad,job):
    
    ciudades = data_structs["por_ciudad"]    
    existeciudad = mp.contains(ciudades,ciudad)
    #Se busca si la ciudad ya se encuentra en el mapa, si no, crea la ciudad
    if existeciudad:
        entry = mp.get(ciudades,ciudad)
        info_ciudad = me.getValue(entry)
    else:
        info_ciudad = new_city(ciudad)
        mp.put(ciudades, ciudad, info_ciudad)
    
    #Se añaden todos los trabajos que hay en esa ciudad a una lista
    lt.addLast(info_ciudad["all_jobs"],job)
    
    year = job["year"] 
    
    existeyear = mp.contains(info_ciudad["years"],year)
    if existeyear:
        entrada = mp.get(info_ciudad["years"],year)
        info_year = me.getValue(entrada)
    else:
        info_year = new_year(year)
        mp.put(info_ciudad["years"],year,info_year)
        
    lt.addLast(info_year["all_jobs"],job)
    
    if job["experience_level"] == "junior":
        lt.addLast(info_year["junior"],job)
        
    elif job["experience_level"] == "mid":
        lt.addLast(info_year["mid"],job)
    
    elif job["experience_level"] == "senior":
        lt.addLast(info_year["senior"],job)
    
    empresa = job["company_name"]
    
    empresas = info_ciudad["empresas"]
    existeempresa = mp.contains(empresas,empresa)
    if existeempresa:
        entrada = mp.get(empresas,empresa)
        info_empresa = me.getValue(entrada)
    else:
        info_empresa = new_empresa(empresa)
        mp.put(empresas,empresa,info_empresa)
    
    lt.addLast(info_empresa["ofertas"],job)

def add_fecha(data_structs,fecha,job):

    fechas = data_structs["por_fecha"]
    
    existefecha = mp.contains(fechas,fecha)
    if existefecha:
        entrada = mp.get(fechas,fecha)
        info_fecha = me.getValue(entrada)
    else: 
        info_fecha = new_fecha(fecha)
        mp.put(fechas,fecha,info_fecha)
    
    lt.addLast(info_fecha,job)

def add_por_empresa(data_structs,empresa,job):
    empresas = data_structs["por_empresa"]
    
    existeempresa = mp.contains(empresas,empresa)
    if existeempresa:
        entrada = mp.get(empresas,empresa)
        info_empresa = me.getValue(entrada)
    else:
        info_empresa = new_empresa(empresa)
        mp.put(empresas,empresa,info_empresa)
        
    lt.addLast(info_empresa["ofertas"],job)
    
def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def new_country(country):
    pais_info = {'name': "",
                 "all_jobs":None,
                 "junior": None,
                 "mid": None,
                 "senior": None}
    
    pais_info['name'] = country
    pais_info["all_jobs"] = lt.newList("ARRAY_LIST")
    pais_info['junior'] =lt.newList("ARRAY_LIST")
    pais_info['mid'] =lt.newList("ARRAY_LIST")  
    pais_info['senior'] =lt.newList("ARRAY_LIST")
    
    return pais_info

def new_city(city):
    city_info = {'name': "",
                 "all_jobs": None,
                 "years": None,
                 "empresas": None}
    
    city_info["name"] = city
    
    city_info["all_jobs"] = lt.newList("ARRAY_LIST")

    city_info["years"] = mp.newMap(5,
                                  maptype='PROBING',
                                  loadfactor=0.5,
                                  ) 
    
    city_info["empresas"] = mp.newMap(50,
                                      maptype='PROBING',
                                      loadfactor=0.9,
                                     ) 
    return city_info

def new_empresa(empresa):
    empresa_info = {'name': "",
                    "ofertas": None}
    
    empresa_info["name"] = empresa
    empresa_info["ofertas"] = lt.newList("ARRAY_LIST")
    
    return empresa_info

def new_fecha(fecha):
    fecha_info = lt.newList("ARRAY_LIST")
    
    return fecha_info

def new_year(year):
    year_info = {"all_jobs":None,
                 "junior":None,
                 "mid":None,
                 "senior":None
                 }
    
    year_info["all_jobs"] = lt.newList("ARRAY_LIST")
    year_info["junior"] = lt.newList("ARRAY_LIST")
    year_info["mid"] = lt.newList("ARRAY_LIST")
    year_info["senior"] = lt.newList("ARRAY_LIST")
    
    return year_info

# Funciones de consulta 

def filtrar_llaves(data_struct,filtro):
    
    lista_filtrada = lt.newList("ARRAY_LIST")
    
    for element in lt.iterator(data_struct):
        filtered_values = [element[key] for key in filtro if key in element]
        lt.addLast(lista_filtrada,filtered_values)
   
    return lista_filtrada

def req_1(data_structs,pais,nivel,num_elem):
    """
    Función que soluciona el requerimiento 1
    """
    #Usamos el mapa con todos los paises y sus trabajos
    paises = data_structs["por_pais"] 
    #Conseguimos solo las ofertas del pais buscado
    ofertas_pais = mp.get(paises,pais)
    #Usamos solo el valor de la llave, el cual es un dicc
    ofertas_filtradas = me.getValue(ofertas_pais)
    total_ofertas_pais = lt.size(ofertas_filtradas["all_jobs"])
    
    if lt.size(ofertas_filtradas[nivel]) > num_elem:
        lista = lt.subList(ofertas_filtradas[nivel],1,num_elem)
    else:
        lista = ofertas_filtradas[nivel]
    n = lt.size(lista)
    
    if n >10:
        respuesta = lt.newList("ARRAY_LIST")
        prim_5 = lt.subList(lista,1,5)
        ult_5 = lt.subList(lista,n-4,5)
        for job in lt.iterator(prim_5):
            lt.addLast(respuesta,job)
        for job in lt.iterator(ult_5):
            lt.addLast(respuesta,job)
        return respuesta,lt.size(ofertas_filtradas[nivel]),total_ofertas_pais
    else: 
        return lista,lt.size(ofertas_filtradas[nivel]),total_ofertas_pais

def req_2(data_structs,empresa,ciudad,num_ofertas):
    """
    Función que soluciona el requerimiento 2
    """
    empresas = data_structs["por_empresa"]
    
    empresa_dupla = mp.get(empresas,empresa)
    info_empresa = me.getValue(empresa_dupla)
    ofertas = info_empresa["ofertas"]
    
    ofertas_filtradas = lt.newList("ARRAY_LIST")
    
    for job in lt.iterator(ofertas):
        if job["city"] == ciudad:
            lt.addLast(ofertas_filtradas,job)
    if lt.size(ofertas_filtradas) > num_ofertas:
        ofertas_filtradas = lt.subList(ofertas_filtradas,1,num_ofertas)
        
    n = lt.size(ofertas_filtradas)
    if n >10:
        respuesta = lt.newList("ARRAY_LIST")
        prim_5 = lt.subList(ofertas_filtradas,1,5)
        ult_5 = lt.subList(ofertas_filtradas,n-4,5)
        for job in lt.iterator(prim_5):
            lt.addLast(respuesta,job)
        for job in lt.iterator(ult_5):
            lt.addLast(respuesta,job)
        return respuesta,n
    else: 
        return ofertas_filtradas,n
            

def req_3(data_structs,empresa,fecha_inicial,fecha_final):
    """
    Función que soluciona el requerimiento 3
    """
    try:
        fecha_inicial = d.strptime(fecha_inicial,"%Y-%m-%d")
        fecha_final = d.strptime(fecha_final,"%Y-%m-%d")
    except:
        return -1
    
    #Conseguimos los trabajos de una empresa
    dupla_empresa = mp.get(data_structs["por_empresa"],empresa)
    empresa = me.getValue(dupla_empresa)
    trabajos = empresa["ofertas"]
    
    #Creamos una lista para poner los trabajos que cumplan estén en el tiempo determinado
    lista = lt.newList("ARRAY_LIST")
    junior = 0
    mid = 0
    senior = 0
    
    for trabajo in lt.iterator(trabajos):
        fecha = trabajo["published_at"]
        if fecha >= fecha_inicial and fecha <= fecha_final:
            lt.addLast(lista,trabajo)
            if trabajo["experience_level"] == "junior":
                junior+=1
            elif trabajo["experience_level"] == "mid":
                mid+=1
            elif trabajo["experience_level"] == "senior":
                senior+=1
    #Si la lista tiene más de 10 elementos, se reduce y se toman los primeros 5 y últimos 5
    n = lt.size(lista)
    if n >10:
        respuesta = lt.newList("ARRAY_LIST")
        prim_5 = lt.subList(lista,1,5)
        ult_5 = lt.subList(lista,n-4,5)
        for job in lt.iterator(prim_5):
            lt.addLast(respuesta,job)
        for job in lt.iterator(ult_5):
            lt.addLast(respuesta,job)
        return respuesta, junior,mid,senior,n
    else:
        return lista,junior,mid,senior,n

def req_4(data_structs,codigo,fechaInicio,fechaFin):
    # TODO: Realizar el requerimiento 4
    """
    Función que soluciona el requerimiento 4
    """
    try:
        fecha_inicial = d.strptime(fechaInicio,"%Y-%m-%d")
        fecha_final = d.strptime(fechaFin,"%Y-%m-%d")
    except:
        return -1
    
    paises = data_structs["por_pais"]
    
    info_pais_dupla = mp.get(paises,codigo)
    info_pais = me.getValue(info_pais_dupla)
    trabajos_pais = info_pais["all_jobs"]
        
    ofertas_en_pais = lt.newList("ARRAY_LIST")
    empresas_en_pais = set()
    ciudades_en_pais = set()
    ciudades_ofertas = {}
    total_ofertas = 0
        
    for trabajo in lt.iterator(trabajos_pais):
            if fecha_inicial <= trabajo["published_at"] <= fecha_final:
                lt.addLast(ofertas_en_pais, trabajo)
                empresas_en_pais.add(trabajo["company_name"])
                ciudades_en_pais.add(trabajo["city"])
                if trabajo["city"] not in ciudades_ofertas:
                    ciudades_ofertas[trabajo["city"]] = 1
                else:
                    ciudades_ofertas[trabajo["city"]] +=1
                total_ofertas += 1
        
    total_ofertas_final=lt.size(ofertas_en_pais)
    total_empresas=len(empresas_en_pais)
    total_ciudades=len(ciudades_en_pais)
    ciudad_mayor_ofertas = llave_max_valor(ciudades_ofertas)
    ciudad_menor_ofertas = llave_min_valor(ciudades_ofertas)
    n = lt.size(ofertas_en_pais)
    if n >10:
        respuesta = lt.newList("ARRAY_LIST")
        prim_5 = lt.subList(ofertas_en_pais,1,5)
        ult_5 = lt.subList(ofertas_en_pais,n-4,5)
        for job in lt.iterator(ult_5):
            lt.addLast(respuesta,job)
        for job in lt.iterator(prim_5):
            lt.addLast(respuesta,job)
        return respuesta,total_ofertas_final,total_empresas,total_ciudades,ciudad_mayor_ofertas,ciudad_menor_ofertas
    else:
        return ofertas_en_pais,total_ofertas_final,total_empresas,total_ciudades,ciudad_mayor_ofertas,ciudad_menor_ofertas

def req_5(data_structs, ciudad,fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    try:
        fecha_inicial = d.strptime(fecha_inicial,"%Y-%m-%d")
        fecha_final = d.strptime(fecha_final,"%Y-%m-%d")
    except:
        return -1
    
    #Conseguimos los trabajos de una ciudad
    dupla_ciudad = mp.get(data_structs["por_ciudad"], ciudad)
    ciudad = me.getValue(dupla_ciudad)
    trabajos = ciudad["all_jobs"]
    
    #Creamos una lista para poner los trabajos que cumplan estén en el tiempo determinado
    lista = lt.newList("ARRAY_LIST")
    empresas_ofertas = {}
    for trabajo in lt.iterator(trabajos):
        fecha = trabajo["published_at"]
        if fecha >= fecha_inicial and fecha <= fecha_final:
            lt.addLast(lista,trabajo)
            if trabajo["company_name"] not in empresas_ofertas:
                empresas_ofertas[trabajo["company_name"]] = 1
            else:
                empresas_ofertas[trabajo["company_name"]] +=1
             
    empresa_menor, mayor = llave_max_valor(empresas_ofertas)
    empresa_mayor, menor = llave_min_valor(empresas_ofertas)
    n_empresas = len(empresas_ofertas)
    
            
    #Si la lista tiene más de 10 elementos, se reduce y se toman los primeros 5 y últimos 5
    n = lt.size(lista)
    if n > 10:
        respuesta = lt.newList("ARRAY_LIST")
        prim_5 = lt.subList(lista,1,5)
        ult_5 = lt.subList(lista,n-4,5)
        for job in lt.iterator(ult_5):
            lt.addLast(respuesta,job)
        for job in lt.iterator(prim_5):
            lt.addLast(respuesta,job)
            
        return respuesta, n_empresas, empresa_mayor, mayor, empresa_menor, menor,n
    else:
        return lista, n_empresas, empresa_mayor, mayor, empresa_menor, menor,n

def req_6(data_structs,nivel,anio,num_ciudades):
    """
    Función que soluciona el requerimiento 6
    """
    
    ciudades = mp.keySet(data_structs["por_ciudad"])
    ciudades_que_cumplen = lt.newList("ARRAY_LIST")
    
    
    if nivel == "indiferente":
        for ciudad in lt.iterator(ciudades):
            info_ciudad_dupla = mp.get(data_structs["por_ciudad"],ciudad)
            info_ciudad = me.getValue(info_ciudad_dupla)
            
            #verificamos si una ciudad tiene ofertas en el año
            existe_anio = mp.contains(info_ciudad["years"],anio)
            if existe_anio:
                ofertas_por_year = mp.get(info_ciudad["years"],anio)
                info_ofertas_por_year = me.getValue(ofertas_por_year)
                if lt.size(info_ofertas_por_year["all_jobs"]) != 0:
                    lt.addLast(ciudades_que_cumplen,{"ofertas":lt.size(info_ofertas_por_year["all_jobs"]),"ciudad":info_ciudad["name"],"lista":info_ofertas_por_year["all_jobs"]})
    
    else:
        #conseguimos la info de la ciudad
        for ciudad in lt.iterator(ciudades):
            info_ciudad_dupla = mp.get(data_structs["por_ciudad"],ciudad)
            info_ciudad = me.getValue(info_ciudad_dupla)
            
            #verificamos si una ciudad tiene ofertas en el año
            existe_anio = mp.contains(info_ciudad["years"],anio)
            if existe_anio:
                ofertas_por_year = mp.get(info_ciudad["years"],anio)
                info_ofertas_por_year = me.getValue(ofertas_por_year)
                if lt.size(info_ofertas_por_year[nivel]) != 0:
                    lt.addLast(ciudades_que_cumplen,{"ofertas":lt.size(info_ofertas_por_year[nivel]),"ciudad":info_ciudad["name"],"lista":info_ofertas_por_year[nivel]})
            
    sort(ciudades_que_cumplen,compSize) 
    ward = False
    if lt.size(ciudades_que_cumplen)>0:    
        ciudad_mayor = lt.firstElement(ciudades_que_cumplen)
        ciudad_menor = lt.lastElement(ciudades_que_cumplen)
    
        ciudad_mayor= {"ciudad":ciudad_mayor["ciudad"],"ofertas":ciudad_mayor["ofertas"]}
        ciudad_menor= {"ciudad":ciudad_menor["ciudad"],"ofertas":ciudad_menor["ofertas"]}
        ward = True
        
    if lt.size(ciudades_que_cumplen) < num_ciudades:
        lista_final = ciudades_que_cumplen
        
    else:
        lista_final = lt.subList(ciudades_que_cumplen,1,num_ciudades)
    
    total_ciudades_que_cumplen = lt.size(lista_final)
    total_ofertas_que_cumplen = 0
    total_empresas_que_cumplen = 0
    
    final = lt.newList("ARRAY_LIST")
    
    for key in lt.iterator(lista_final):
        lista = key["lista"]
        promedio_total = 0
        total_emp = {}
        mejor_oferta = {"info":None,"cantidad":0}
        peor_oferta = {"info":None,"cantidad":float("inf")}
        
        for job in lt.iterator(lista):
            promedio_salario = (job["salary_from"]+job["salary_to"])/2
            promedio_total += (promedio_salario)
            #Sacamos la mejor oferta
            if job["salary_to"] > mejor_oferta["cantidad"] and job["salary_to"] != 0:
                mejor_oferta["cantidad"] = job["salary_to"]
                mejor_oferta["info"] = job
            #Sacamos la peor oferta
            if job["salary_from"] < peor_oferta["cantidad"] and job["salary_from"] != 0:
                peor_oferta["cantidad"] = job["salary_from"]
                peor_oferta["info"] = job
                
            #Añadimos las empresas
            if job["company_name"] not in total_emp:
                total_emp[job["company_name"]] = 1
            else:
                total_emp[job["company_name"]] += 1
        
        total_ofertas_que_cumplen += lt.size(lista)
        total_empresas_que_cumplen += len(total_emp)
        
        filtro = ["title","country_code","company_name","experience_level","salary_from","salary_to","id"]
        
        mejor_oferta["info"] = filtrar_llaves_req6(mejor_oferta["info"],filtro)
        peor_oferta["info"] = filtrar_llaves_req6(peor_oferta["info"],filtro)
        
        max_empresa = llave_max_valor(total_emp)
        
        lt.addLast(final,{"ciudad":key["ciudad"],"total_ofertas":lt.size(lista),"promedio_total":promedio_total/lt.size(lista),"total_empresas":len(total_emp),
                        "mayor_empresa":max_empresa,"mejor_oferta":mejor_oferta["info"], "peor_oferta":peor_oferta["info"]})    
        
    if ward:
        return final, total_ciudades_que_cumplen, total_empresas_que_cumplen, total_ofertas_que_cumplen, ciudad_mayor, ciudad_menor
    else:
        return final, total_ciudades_que_cumplen, total_empresas_que_cumplen, total_ofertas_que_cumplen
         
def llave_max_valor(diccionario):
    if not diccionario:
        return None  # Devuelve None si el diccionario está vacío
    else:
        llave_max = max(diccionario, key=diccionario.get)
        # Obtener el valor correspondiente a la llave máxima
        valor_max = diccionario[llave_max]
        # Devolver la tupla (llave, valor)
        return llave_max, valor_max        

def llave_min_valor(diccionario):
    if not diccionario:
        return None  # Devuelve None si el diccionario está vacío
    else:
        llave_min = min(diccionario, key=diccionario.get)
        # Obtener el valor correspondiente a la llave máxima
        valor_min = diccionario[llave_min]
        # Devolver la tupla (llave, valor)
        return llave_min, valor_min
    
def filtrar_llaves_req6(data_struct,filtro):
    new_data = {}
    if data_struct is not None:
        for element,value in data_struct.items():
            if element in filtro:
                new_data[element] = value

    return new_data
    
def req_7(data_structs,anio,mes,num_paises):
    """
    Función que soluciona el requerimiento 7
    """
    
    paises = data_structs["por_pais"]
    nombre_paises = mp.keySet(data_structs["por_pais"])

    mapa_paises =  mp.newMap(87,
                            maptype='PROBING',
                            loadfactor=0.9,
                            )
    conteo_paises = {}
    
    #Recorremos todos los paises
    for pais in lt.iterator(nombre_paises):
        info_pais_dupla = mp.get(paises,pais)
        info_pais = me.getValue(info_pais_dupla)
        trabajos_pais = info_pais["all_jobs"]
        trabajos_cumplen =lt.newList("ARRAY_LIST")
        conteo_ciudades = {}
        #Si los trabajos de una pais están en el rango de fechas se añaden
        for job in lt.iterator(trabajos_pais):
            if job["year"] == anio and job["month"] == mes:
                lt.addLast(trabajos_cumplen,job)
                #Hacemos un conteo de los paises que cumplen las condiciones
                if job["country_code"] not in conteo_paises:
                    conteo_paises[job["country_code"]] = 1
                else:
                    conteo_paises[job["country_code"]] +=1
                #Hacemos un conteo de las ciudades que cumplen las condiciones dentro de cada país
                if job["city"] not in conteo_ciudades:
                    conteo_ciudades[job["city"]] = 1
                else:
                    conteo_ciudades[job["city"]] +=1

        total_ciudades = len(conteo_ciudades)
        ciudad_mayor = llave_max_valor(conteo_ciudades)
        
        #Agregamos al mapa cada país con su información correspondiente
        mp.put(mapa_paises,info_pais["name"],{"trabajos":trabajos_cumplen, "total_ciudades":total_ciudades,"ciudad_mayor":ciudad_mayor})

    conteo_paises = sortReq7(conteo_paises)
    
    primeras_n_llaves = {}
    contador = 1
    #Usamos solo los n primeros paises que nos piden
    for llave, valor in conteo_paises.items():
        if contador <= num_paises:
            primeras_n_llaves[llave] = valor
            contador += 1
        else:
            break
    
    lista_n_paises_cumplen = lt.newList("ARRAY_LIST")
    lista_info_todos_jobs = lt.newList("ARRAY_LIST")
    
    mayor_pais = {"conteo":0}
    total_ofertas = 0
        
    junior = {}
    mid = {}
    senior = {}
    
    cantidad_junior = 0
    junior_promedio_nivel = 0
    junior_ability = {}
    junior_emp = {}
    cantidad_mid = 0
    mid_promedio_nivel = 0
    mid_ability = {}
    mid_emp = {}
    cantidad_senior = 0
    senior_promedio_nivel = 0
    senior_ability = {}
    senior_emp = {}
    
    #Añadimos los n países que nos piden con su información correspondiente, esta se consigue con el mapa.
    for pais in primeras_n_llaves:
        trabajos_del_pais_dupla = mp.get(mapa_paises,pais)
        info_trabajos_del_pais = me.getValue(trabajos_del_pais_dupla)
        trabajos_del_pais = info_trabajos_del_pais["trabajos"]
        filtro = ["experience_level","ability","level","company_name"]
        trabajos_del_pais = filtrar_llaves(trabajos_del_pais,filtro)
        
        lt.addLast(lista_n_paises_cumplen,{"pais":pais,"total_ofertas":lt.size(trabajos_del_pais),"total_ciudades":info_trabajos_del_pais["total_ciudades"],
                                           "ciudad_mayor":info_trabajos_del_pais["ciudad_mayor"]})
        lt.addLast(lista_info_todos_jobs,trabajos_del_pais)
        
        total_ofertas += lt.size(trabajos_del_pais)
        if lt.size(trabajos_del_pais) > mayor_pais["conteo"]:
            mayor_pais["pais"] = pais
            mayor_pais["conteo"] = lt.size(trabajos_del_pais)
    
        for job in lt.iterator(trabajos_del_pais):
        #job = ['mid', 'FIGMA', '4', 'tp servglobal ltd']
        #job[0] = experience level, job[1]= ability, job[2] = level, job[3] = company name
            if job[0] == "junior":
                cantidad_junior +=1
                junior_promedio_nivel+= job[2]
                if job[1] not in junior_ability:
                    junior_ability[job[1]] = 1
                else:
                    junior_ability[job[1]] += 1
                if job[3] not in junior_emp:
                    junior_emp[job[3]] = 1
                else:
                    junior_emp[job[3]] += 1
                    
            elif job[0] == "mid":
                cantidad_mid +=1
                mid_promedio_nivel+= job[2]
                if job[1] not in mid_ability:
                    mid_ability[job[1]] = 1
                else:
                    mid_ability[job[1]] += 1
                
                if job[3] not in mid_emp:
                    mid_emp[job[3]] = 1
                else:
                    mid_emp[job[3]] += 1
                
            elif job[0] == "senior":
                cantidad_senior +=1
                senior_promedio_nivel+= job[2]
                if job[1] not in senior_ability:
                    senior_ability[job[1]] = 1
                else:
                    senior_ability[job[1]] += 1
                    
                if job[3] not in senior_emp:
                    senior_emp[job[3]] = 1
                else:
                    senior_emp[job[3]] += 1
   
    junior["total_ofertas"] = cantidad_junior
    junior["promedio_nivel"] = junior_promedio_nivel/cantidad_junior
    junior["mayor_habilidad"] = llave_max_valor(junior_ability) 
    junior["menor_habilidad"] = llave_min_valor(junior_ability)
    junior["total_empresas"] = len(junior_emp)
    junior["mayor_empresa"] = llave_max_valor(junior_emp)
    junior["menor_empresa"] = llave_min_valor(junior_emp)
    
    mid["total_ofertas"] = cantidad_mid
    mid["promedio_nivel"] = mid_promedio_nivel/cantidad_mid
    mid["mayor_habilidad"] = llave_max_valor(mid_ability) 
    mid["menor_habilidad"] = llave_min_valor(mid_ability)
    mid["total_empresas"] = len(mid_emp)
    mid["mayor_empresa"] = llave_max_valor(mid_emp)
    mid["menor_empresa"] = llave_min_valor(mid_emp)
    
    senior["total_ofertas"] = cantidad_senior
    senior["promedio_nivel"] = senior_promedio_nivel/cantidad_senior
    senior["mayor_habilidad"] = llave_max_valor(senior_ability) 
    senior["menor_habilidad"] = llave_min_valor(senior_ability)
    senior["total_empresas"] = len(senior_emp)
    senior["mayor_empresa"] = llave_max_valor(senior_emp)
    senior["menor_empresa"] = llave_min_valor(senior_emp)
    
    n = lt.size(lista_n_paises_cumplen)
    if n > 10:
        respuesta = lt.newList("ARRAY_LIST")
        prim_5 = lt.subList(lista_n_paises_cumplen,1,5)
        ult_5 = lt.subList(lista_n_paises_cumplen,n-4,5)
        for job in lt.iterator(prim_5):
            lt.addLast(respuesta,job)
        for job in lt.iterator(ult_5):
            lt.addLast(respuesta,job)
            
        return respuesta, total_ofertas,mayor_pais, junior, mid, senior
    else:
        return lista_n_paises_cumplen,total_ofertas,mayor_pais, junior, mid, senior


def sortReq7(dicc):
    diccionario_ordenado = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
    diccionario_ordenado = dict(diccionario_ordenado)
    
    return diccionario_ordenado
    
def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


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


def sort(data_structs,criterio):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    merg.sort(data_structs,criterio)


def compIDs(trabajo1,trabajo2):
    
    key = me.getKey(trabajo2)
    
    if trabajo1 > key:
        return 1
    if trabajo1 == key:
        return 0
    else: 
        return -1
    
def compFechas(fecha1,fecha2):

    if fecha1["published_at"] > fecha2["published_at"]:
        return True
    else:
        return False

def compSize(element1,element2):
    if element1["ofertas"] > element2["ofertas"]:
        return True
    else:
        return False
    
def compReq7(element1,element2):
    print(element1,element2)