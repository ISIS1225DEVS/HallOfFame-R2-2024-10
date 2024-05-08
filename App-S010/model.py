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
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

import model
from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""
# =========================
# Construccion de modelos
# ========================= 

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    
    #En el archivo "large" hay:
    #Paises: 81
    #Ciudades: 1453
    #Empresas: 6321
    
    data_structs = {'jobs': None,
                    'skills': None,
                    'employement_types': None,
                    'multilocation': None,
                    'paises': None,
                    'ciudades': None,
                    'empresas': None,
                    'years': None,
                    'p': {},
                    'numero_p':0,
                    'c': {},
                    'numero_c': 0,
                    'e': {},
                    'numero_e': 0,
                    'lst_paises': lt.newList("ARRAY_LIST", compareCountryCodeInList),
                    'lst_ciudades': lt.newList("ARRAY_LIST", compareCityInList),
                    'lst_empresas': lt.newList("ARRAY_LIST", compareCompanyInList)  
                    }
    #id unico: sin cmpfunction
    data_structs['jobs'] = mp.newMap(205001,
                                   maptype='CHAINING',
                                   loadfactor=4)

    data_structs["lst_jobs"] = lt.newList("ARRAY_LIST")
    
    data_structs['skills'] = mp.newMap(205001,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=compareSkillsById)
    #id unico: sin cmpfunction
    data_structs['employment_types'] = mp.newMap(260001,
                                   maptype='CHAINING',
                                   loadfactor=4)
    
    data_structs['multilocations'] = mp.newMap(245001,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=compareMultById)
    
    data_structs['paises'] = mp.newMap(101,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=compareCountryCode)

    data_structs['ciudades'] = mp.newMap(1501,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=compareCity)
    
    data_structs['empresas'] = mp.newMap(6501,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=compareCompanyName)
    
    data_structs["years"] = mp.newMap(2,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=compareYear)
     
    return data_structs


# ==================================================
#Funciones para agregar elementos a las listas TAD. 
# ==================================================

def add_lista_paises (lst_paises, job):
    pos = lt.isPresent(lst_paises, job["country_code"])
    if pos == 0:    #No se encuentra en la lista
        new_pais = {'pais': job["country_code"],
                    'n_ofertas': 1
                    }
        lt.addLast(lst_paises, new_pais)
    else:
        pais = lt.getElement(lst_paises, pos)
        pais["n_ofertas"] += 1
        
        
def add_lista_ciudades_req7 (lst_ciudades, job):
    pos = lt.isPresent(lst_ciudades, job["city"])
    if pos == 0:    #No se encuentra en la lista
        new_ciudad = {'ciudad': job["city"],
                    'n_ofertas': 1
                    }
        lt.addLast(lst_ciudades, new_ciudad)
    else:
        ciudad = lt.getElement(lst_ciudades, pos)
        ciudad["n_ofertas"] += 1

def add_lista_empresas_req7 (lst_empresas, job):
    pos = lt.isPresent(lst_empresas, job["company_name"])
    if pos == 0:    #No se encuentra en la lista
        new_empresa = {'empresa': job["company_name"],
                    'n_ofertas': 1
                    }
        lt.addLast(lst_empresas, new_empresa)
    else:
        empresa = lt.getElement(lst_empresas, pos)
        empresa["n_ofertas"] += 1

def add_lista_ciudades_req6 (data_structs, job):
    pos = lt.isPresent(data_structs["lst_ciudades"], job["city"])
    if pos == 0:    #No se encuentra en la lista
        new_ciudad = {'ciudad': job["city"],
                    'n_ofertas': 0
                    }
        lt.addLast(data_structs["lst_ciudades"], new_ciudad)
    ciudad = lt.getElement(data_structs["lst_ciudades"], pos)
    ciudad["n_ofertas"] += 1

def add_lista_empresas_req6 (data_structs, job):
    pos = lt.isPresent(data_structs["lst_empresas"], job["company_name"])
    if pos == 0:    #No se encuentra en la lista
        new_empresa = {'empresa': job["company_name"],
                    'n_ofertas': 0
                    }
        lt.addLast(data_structs["lst_empresas"], new_empresa)
    empresa = lt.getElement(data_structs["lst_empresas"], pos)
    empresa["n_ofertas"] += 1


def add_lista_skills (lst_skills, skill):
    pos = lt.isPresent(lst_skills, skill["name"])
    if pos == 0:    #No se encuentra en la lista
        new_skill = {'name': skill["name"],
                    'cantidad': 0
                    }
        lt.addLast(lst_skills, new_skill)
    else:
        skill_pos = lt.getElement(lst_skills, pos)
        skill_pos["cantidad"] += 1
        
def add_lista_skills (lst_skills, skill):
    pos = lt.isPresent(lst_skills, skill["name"])
    if pos == 0:    #No se encuentra en la lista
        new_skill = {'name': skill["name"],
                    'cantidad': 0
                    }
        lt.addLast(lst_skills, new_skill)
    else:
        skill_pos = lt.getElement(lst_skills, pos)
        skill_pos["cantidad"] += 1
        
def add_lista_paises_req8 (lst_paises, job, emp, skills):
    pos = lt.isPresent(lst_paises, job["country_code"])
    if pos == 0:    #No se encuentra en la lista
        new_pais = {'pais': job["country_code"],   
                    'ofertas' : 0, #
                    'ofertas_rango_salarial': 0,#
                    'empresas': lt.newList("ARRAY_LIST"),#
                    'ciudades': lt.newList("ARRAY_LIST"),#
                    'salario_mayor': 0,#  #Elements: str
                    'salario_menor': 100000000000000000000000000000000000000,
                    'sum_salary': 0, #
                    'average_salary': 0, #
                    'sum_skills' : 0,   #             #Elements: str
                    'average_skills': 0 #
                    }
        lt.addLast(lst_paises, new_pais)

    pais_pos = lt.getElement(lst_paises, pos)
    pais_pos["ofertas"] += 1
    
    #Se insertan los salarios para determinar cual es el mayor
    if emp["salary_from"] != "" and emp["salary_to"] != "":
        pais_pos["ofertas_rango_salarial"] += 1
        
        local_average = round(( float(emp["salary_from"]) + float(emp["salary_to"]) )/2 , 2)
        pais_pos["sum_salary"] += local_average
        
        if local_average > pais_pos["salario_mayor"]:
            pais_pos["salario_mayor"] = local_average
        
        if local_average < pais_pos["salario_menor"]:
            pais_pos["salario_menor"] = local_average
            
    elif emp["salary_from"] == "" or emp["salary_to"] == "" or emp["salary_to"] == emp["salary_from"]:
        
        if emp["salary_from"] == "":
                
            if float(emp["salary_to"]) > pais_pos["salario_mayor"]:
                pais_pos["salario_mayor"] = float(emp["salary_to"])
            
            if float(emp["salary_to"]) < pais_pos["salario_menor"]:
                pais_pos["salario_menor"] = float(emp["salary_to"])
            
            pais_pos["sum_salary"] += float(emp["salary_to"])
            
        elif emp["salary_to"] == "":


            if float(emp["salary_from"]) > pais_pos["salario_mayor"]:
                pais_pos["salario_mayor"] = float(emp["salary_from"])
            
            if float(emp["salary_from"]) < pais_pos["salario_menor"]:
                pais_pos["salario_menor"] = float(emp["salary_from"])

            pais_pos["sum_salary"] += float(emp["salary_from"])
            
        elif emp["salary_to"] == emp["salary_from"]:
            
            if float(emp["salary_from"]) > pais_pos["salario_mayor"]:
                pais_pos["salario_mayor"] = float(emp["salary_from"])
            
            if float(emp["salary_from"]) < pais_pos["salario_menor"]:
                pais_pos["salario_menor"] = float(emp["salary_from"])
            
            pais_pos["sum_salary"] += float(emp["salary_from"])
    
    #Se insertan las diversas empresas
    if lt.isPresent(pais_pos["empresas"], job["company_name"]) == 0:
        lt.addLast(pais_pos["empresas"], job["company_name"])
    
    #Se insertan las diversas ciudades
    if lt.isPresent(pais_pos["ciudades"], job["city"]) == 0:
        lt.addLast(pais_pos["ciudades"], job["city"])
    
    #Se insertan las skills
    pais_pos["sum_skills"] += lt.size(skills["skills"])
    
    #Promedio salario
    if pais_pos["ofertas"] > 0:
        pais_pos["average_salary"] = pais_pos["sum_salary"] / pais_pos["ofertas_rango_salarial"]
    
    #Promedio skills
    if pais_pos["sum_skills"] > 0:
        pais_pos["average_skills"] = pais_pos["sum_skills"] / pais_pos["ofertas"]
            
    
# ==============================================
# Funciones para agregar informacion al modelo
# ==============================================

def add_job(data_structs, job):
    """
    Función para agregar nuevos elementos al mapa de jobs, 
    paises, ciudades y empresas. 
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    #Add_job 
    mp.put(data_structs["jobs"], job["id"], job)
    lt.addLast(data_structs["lst_jobs"], job)
    
    #Add_pais
    paises = data_structs["paises"]
    existe_pais = mp.contains(paises, job["country_code"])
    #print(existe_pais)
    if existe_pais:
        entry = mp.get(paises,job["country_code"])
        ofertas_pais = me.getValue(entry)

    else:
        ofertas_pais = lt.newList("ARRAY_LIST", compareCountryCode)
        mp.put(paises,job["country_code"],ofertas_pais)
        #print(existe_pais)
        
    lt.addLast(ofertas_pais,job)

    #Add_ciudad
    ciudades = data_structs["ciudades"]
    existe_ciudad = mp.contains(ciudades, job["city"])
    if existe_ciudad:
        entry = mp.get(ciudades,job["city"])
        ofertas_ciudad = me.getValue(entry)
    else:
        ofertas_ciudad = lt.newList("ARRAY_LIST", compareCity)
        mp.put(ciudades,job["city"],ofertas_ciudad)    
    
    lt.addLast(ofertas_ciudad,job)
    
    #Add_empresa
    empresas = data_structs["empresas"]
    existe_empresa = mp.contains(empresas, job["company_name"])
    if existe_empresa:
        entry = mp.get(empresas,job["company_name"])
        ofertas_empresa= me.getValue(entry)
    else:
        ofertas_empresa = lt.newList("ARRAY_LIST", compareCompanyName)
        mp.put(empresas,job["company_name"],ofertas_empresa)
        
    lt.addLast(ofertas_empresa,job)
    
    #Add_year
    
    years = data_structs["years"]
    job_year = job["published_at"][0:4]
    existe_year = mp.contains(years, job_year)
    
    if existe_year:
        entry = mp.get(years,job_year)
        ofertas_year= me.getValue(entry)
    else:
        ofertas_year = lt.newList("ARRAY_LIST", compareYear)
        mp.put(years,job_year,ofertas_year)
        
    lt.addLast(ofertas_year,job)
    

def add_skill (data_structs, skill):
    """
    Función para agregar nuevos elementos al mapa de skills.
    """
    skills = data_structs["skills"]
    existe_job = mp.contains(skills, skill["id"])
    #print(existe_job)
    if existe_job:
        entry = mp.get(skills,skill["id"])
        skills_job = me.getValue(entry)

    else:
        skills_job = newSkill(skill["id"])
        mp.put(skills,skill["id"],skills_job)
        
    lt.addLast(skills_job["skills"],skill)
    
    skills_job["average"] += float(skill['level'])
    total_skills = lt.size(skills_job["skills"])
    if total_skills > 0:
        skills_job['average_level'] = skills_job["average"] / total_skills
    
    
def add_employment_types (data_structs, emp):
    """
    Función para agregar nuevos elementos al mapa de employment types.
    """
    mp.put(data_structs["employment_types"], emp["id"], emp)    
    
    
def add_multilocation (data_structs, mult):
    """
    Función para agregar nuevos elementos al mapa de employment types.
    """
    multilocations = data_structs["multilocations"]
    existe_job = mp.contains(multilocations, mult["id"])
    #print(existe_job)
    if existe_job:
        entry = mp.get(multilocations,mult["id"])
        mult_job = me.getValue(entry)

    else:
        mult_job = newMult(mult["id"])
        mp.put(multilocations,mult["id"],mult_job)
        
    lt.addLast(mult_job["multilocations"],mult)
    
# =================================
# Funciones para creacion de datos
# =================================

def newSkill (id):
    """
    Crea una nueva estructura para modelar las skills de un trabajo y el nivel
    promedio requerido. Se crea una lista TAD para guardar dichas skills.

    """
    skill = {'id': None,
             'skills': None,
             'average': 0,
             'average_level': None
    }
    skill['id'] = id
    skill['skills'] = lt.newList("ARRAY_LIST", compareSkillsById)
    return skill

def newMult (id):
    """
    Crea una nueva estructura para modelar las multilocations de un trabajo. 
    Se crea una lista TAD para guardar dichas multilocations.

    """
    mult = {'id': None,
             'multilocations': None
    }
    mult['id'] = id
    mult['multilocations'] = lt.newList("ARRAY_LIST", compareMultById)
    return mult


# ==============================
# Size de los mapas
# ==============================

def job_size(data_structs):
    return mp.size(data_structs["jobs"])

def paises_size(data_structs):
    return mp.size(data_structs["paises"])

def ciudades_size(data_structs):
    return mp.size(data_structs["ciudades"])
    
def empresas_size(data_structs):
    return mp.size(data_structs["empresas"])

def years_size(data_structs):
    return mp.size(data_structs["years"])

def skills_size(data_structs):
    return mp.size(data_structs["skills"])

def emp_size(data_structs):
    return mp.size(data_structs["employment_types"])

def mult_size(data_structs):
    return mp.size(data_structs["multilocations"])

# ====================================
# Funciones de Comparacion para MAPAS
# ====================================

def compareCountryCode (keyname, country):
    countryentry = me.getKey(country)
    if (keyname == countryentry):
        return 0
    elif (keyname > countryentry):
        return 1
    else:
        return -1

def compareCity (keyname, city):
    cityentry = me.getKey(city)
    if (keyname == cityentry):
        return 0
    elif (keyname > cityentry):
        return 1
    else:
        return -1

def compareCompanyName (keyname, company):
    companyentry = me.getKey(company)
    if (keyname == companyentry):
        return 0
    elif (keyname > companyentry):
        return 1
    else:
        return -1

def compareSkillsById (keyname, skill):
    skillentry = me.getKey(skill)
    if (keyname == skillentry):
        return 0
    elif (keyname > skillentry):
        return 1
    else:
        return -1
    
def compareMultById (keyname, mult):
    multentry = me.getKey(mult)
    if (keyname == multentry):
        return 0
    elif (keyname > multentry):
        return 1
    else:
        return -1
    
def compareYear (keyname, year):
    yearentry = me.getKey(year)
    if (keyname == yearentry):
        return 0
    elif (keyname > yearentry):
        return 1
    else:
        return -1
    
def compareSkillName (keyname, skill):
    skillentry = me.getKey(skill)
    if (keyname == skillentry):
        return 0
    elif (keyname > skillentry):
        return 1
    else:
        return -1

def compareExperienceLevel (keyname, experience_level):
    skillentry = me.getKey(experience_level)
    if (keyname == skillentry):
        return 0
    elif (keyname > skillentry):
        return 1
    else:
        return -1
    
# ====================================
#Funciones de comparacion para LISTAS
# ====================================

def compareCountryCodeInList (keyname, el2):
    if keyname == el2["pais"]:
        return 0
    elif keyname > el2["pais"]:
        return 1
    else:
        return -1 

def compareCityInList (keyname, el2):
    if keyname == el2["ciudad"]:
        return 0
    elif keyname > el2["ciudad"]:
        return 1
    else:
        return -1

def compareSkillsInList (keyname, el2):
    if keyname == el2["name"]:
        return 0
    elif keyname > el2["name"]:
        return 1
    else:
        return -1

def compareCompanyInList (keyname, el2):
    if keyname == el2["empresa"]:
        return 0
    elif keyname > el2["empresa"]:
        return 1
    else:
        return -1
    

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def req_1(data_structs, codigo, nivel):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    entry = mp.get(data_structs["paises"], codigo)
    jobs_pais = me.getValue(entry)
    
    lst_ofertas = lt.newList("ARRAY_LIST")
    
    for job in lt.iterator(jobs_pais):
        if codigo == job["country_code"] and nivel == job["experience_level"]:
            lt.addLast(lst_ofertas, job)
    
    ordenada = sort(data_structs, lst_ofertas, "date_crit")
    
    return ordenada


def req_2(data_structs, empresa, ciudad):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    entry = mp.get(data_structs["ciudades"], ciudad)
    jobs_ciudad = me.getValue(entry)
    
    lst_ofertas = lt.newList("ARRAY_LIST")
    
    for job in lt.iterator(jobs_ciudad):
        if empresa == job["company_name"]:
            lt.addLast(lst_ofertas, job)
    
    ordenada = sort(data_structs, lst_ofertas, "date_crit")
    
    return ordenada


def req_3(data_structs, empresa, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    entry = mp.get(data_structs["empresas"], empresa)
    jobs_empresa = me.getValue(entry)
    
    ofertas = lt.newList("ARRAY_LIST")
    
    #inicio contadores de tipos de experticia
    junior = 0
    mid = 0
    senior = 0
    
    for oferta in lt.iterator(jobs_empresa):
        large_date = datetime.strptime(oferta["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        date = str(large_date.date())
        if date>=fecha_inicial and date<=fecha_final:
            lt.addLast(ofertas,oferta)
            if oferta["experience_level"] == "junior":
                junior += 1
            elif oferta["experience_level"] == "mid":
                mid += 1
            elif oferta["experience_level"] == "senior":
                senior += 1
        
    ordenada = sort(data_structs,ofertas,"country_range_date_crit")
    elements = [ordenada,lt.size(ordenada), junior, mid, senior]
    
    return elements


def req_4(data_structs, codigo, fecha_inicio, fecha_fin):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pais_filtrado = mp.get(data_structs["paises"], codigo)
    pais = me.getValue(pais_filtrado)
    ofertas = lt.newList("ARRAY_LIST")
    
    for job in lt.iterator(pais):
        large_date = datetime.strptime(job["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        date = str(large_date.date())
        if date>=fecha_inicio and date<=fecha_fin:
            lt.addLast(ofertas, job)
    
    ordenada = sort(data_structs, ofertas, "date_company_crit")
    return ordenada


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs, n_ciudades, año, experticia):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    año_filtrado = mp.get(data_structs["years"], año)
    year = me.getValue(año_filtrado)
    ofertas = lt.newList("ARRAY_LIST") #ofertas que cumplen con las condiciones
    
    if experticia == "indiferente":
        for job in lt.iterator(year):
            add_lista_ciudades_req6(data_structs, job) #ciudades que cumplen con las condiciones de año
            lt.addLast(ofertas, job) #ofertas que cumplen con las condiciones de año
    else: 
        for job in lt.iterator(year):
            if job["experience_level"] == experticia:
                add_lista_ciudades_req6(data_structs, job) #ciudades que cumplen con las condiciones de año y experticia
                lt.addLast(ofertas, job) #ofertas que cumplen con las condiciones de año y experticia
    
    ranked_ciudades = sort(data_structs, data_structs["lst_ciudades"], "CiudadesListElementsCrit") #ciudades ordenadas de mayor a menor ofertas

    if lt.size(data_structs["lst_ciudades"]) > int(n_ciudades):
        top_ranked_ciudades = lt.subList(ranked_ciudades,1, int(n_ciudades)) #sublista de las primeras N ciudades
    else:
        top_ranked_ciudades = ranked_ciudades
    
    total_ciudades = lt.size(top_ranked_ciudades)
    
    ofertas_filtrado = lt.newList("ARRAY_LIST")
    salarios = lt.newList("ARRAY_LIST")
    city_map = mp.newMap(1501,
                        maptype='CHAINING',
                        loadfactor=4)
    for city in lt.iterator(top_ranked_ciudades):
        ciudad = city["ciudad"]
        ofertas_ciudad = lt.newList("ARRAY_LIST")
        for job in ofertas["elements"]:
            if job["city"] == ciudad:
                lt.addLast(ofertas_ciudad, job) #se agrega la oferta a la lista que va en el mapa
                lt.addLast(salarios, employment_types(data_structs, job["id"])) #se agrega la info del salario enlazado al id del elemento
                lt.addLast(ofertas_filtrado, job) #se agrega la oferta a la lista general de ofertas
        mp.put(city_map, ciudad, ofertas_ciudad) #se agrega al mapa toda la informacion
    
    total_ofertas = lt.size(ofertas_filtrado)
    
    company_list = lt.newList("ARRAY_LIST")
    for company in ofertas_filtrado["elements"]:
        if lt.isPresent(company_list, company["company_name"]) == 0:
            lt.addLast(company_list, company["company_name"])    
    total_empresas = lt.size(company_list)
    
    mayor_ciudad = lt.firstElement(top_ranked_ciudades)
    nombre_mayor_ciudad = mayor_ciudad["ciudad"]
    conteo_mayor_ciudad = mayor_ciudad["n_ofertas"]
    
    menor_ciudad = lt.lastElement(top_ranked_ciudades)
    nombre_menor_ciudad = menor_ciudad["ciudad"]
    conteo_menor_ciudad = menor_ciudad["n_ofertas"]
    
    info = [city_map, total_ciudades, total_empresas, total_ofertas, nombre_mayor_ciudad, conteo_mayor_ciudad,
            nombre_menor_ciudad, conteo_menor_ciudad, salarios, top_ranked_ciudades, data_structs]
    
    return info
    
def employment_types(data_structs, id):
    id_filtrado = mp.get(data_structs["employment_types"], id)
    id_elem = me.getValue(id_filtrado)
    return id_elem

def empresa_con_mas_ofertas(data_structs, ofertas):
    for job in ofertas["elements"]:
        add_lista_empresas_req6(data_structs, job)
    ranked_empresas = sort(data_structs, data_structs["lst_empresas"], "EmpresasListElementsCrit")
    mayor_empresa = lt.firstElement(ranked_empresas)
    nombre_mayor_empresa = mayor_empresa["empresa"]
    conteo_mayor_empresa = mayor_empresa["n_ofertas"]
    
    return nombre_mayor_empresa, conteo_mayor_empresa


def req_7(data_structs, n_paises, year, month):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    
    #Resultado: total_ofertas, total_ciudades, pais_mayor_ofertas, ciudad_mayor_ofertas, 
    
    #Inicializacion de variables y ADTs
    total_ofertas = 0
    total_ciudades = 0
    
    ofertas_experticias = mp.newMap(10, 
                                    maptype='CHAINING', 
                                    loadfactor=4, 
                                    cmpfunction=compareExperienceLevel)
        
    lst_ciudades = lt.newList("ARRAY_LIST", compareCityInList)
    lst_paises = lt.newList("ARRAY_LIST", compareCountryCodeInList)
    
    #Listas de habilidades por experticia
    lst_habilidades_junior = lt.newList("ARRAY_LIST", compareSkillsInList)
    lst_habilidades_mid = lt.newList("ARRAY_LIST", compareSkillsInList)
    lst_habilidades_senior = lt.newList("ARRAY_LIST", compareSkillsInList)
    
    #Listas de habilidades por empresa
    lst_empresas_junior = lt.newList("ARRAY_LIST", compareCompanyInList)
    lst_empresas_mid = lt.newList("ARRAY_LIST", compareCompanyInList)
    lst_empresas_senior = lt.newList("ARRAY_LIST", compareCompanyInList)
    
    #Variables para almacenar el numero de trabajos con multilocation.
    lst_empresas_multilocation_junior = lt.newList("ARRAY_LIST")
    lst_empresas_multilocation_mid = lt.newList("ARRAY_LIST")
    lst_empresas_multilocation_senior = lt.newList("ARRAY_LIST")
    
    total_skills_junior = 0
    sum_level_junior = 0
    
    total_skills_mid = 0
    sum_level_mid = 0
    
    total_skills_senior = 0
    sum_level_senior = 0
    
    if mp.contains(data_structs["years"], year):
        entry = mp.get(data_structs["years"],year)
        ofertas_year = me.getValue(entry)
    else:
        return "NONE_YEAR"
    
    for job in lt.iterator(ofertas_year):
        if job["published_at"][5:7] == month:
            total_ofertas += 1
            add_lista_paises(lst_paises, job)
    
    if lt.size(lst_paises) == 0:
        return "NONE_ELEMENTS"
    
    ranked_paises = sort(data_structs, lst_paises, "CountryListElementsCrit")
    
    if lt.size(lst_paises) > n_paises:
        top_ranked_paises = lt.subList(ranked_paises,1, n_paises)
    else:
        top_ranked_paises = ranked_paises
        
    for job in lt.iterator(ofertas_year):
        if lt.isPresent(top_ranked_paises, job["country_code"]) and job["published_at"][5:7] == month:
            
            add_lista_ciudades_req7 (lst_ciudades, job)
            
            #Add_expertiece
            existe_experticia = mp.contains(ofertas_experticias, job["experience_level"])
            
            if existe_experticia:
                entry = mp.get(ofertas_experticias,job["experience_level"])
                ofertas_exp= me.getValue(entry)
            else:
                ofertas_exp = lt.newList("ARRAY_LIST", compareYear)
                mp.put(ofertas_experticias,job["experience_level"],ofertas_exp)
                
            lt.addLast(ofertas_exp,job)
            
            
            #Add_empresa
            if job["experience_level"] == "junior":
                #Add_empresa_junior
                add_lista_empresas_req7 (lst_empresas_junior, job)
                
                entry = mp.get(data_structs["multilocations"], job["id"])
                value = me.getValue(entry)
                multilocations = value["multilocations"]
                
                if lt.isPresent(lst_empresas_multilocation_junior, job["company_name"]) == 0 and lt.size(multilocations) > 1:
                    lt.addLast(lst_empresas_multilocation_junior, job["company_name"])
                
            elif job["experience_level"] == "mid":
                #Add_empresa_mid 
                add_lista_empresas_req7 (lst_empresas_mid, job)
                
                entry = mp.get(data_structs["multilocations"], job["id"])
                value = me.getValue(entry)
                multilocations = value["multilocations"]
                
                if lt.isPresent(lst_empresas_multilocation_mid, job["company_name"]) == 0 and lt.size(multilocations) > 1:
                    lt.addLast(lst_empresas_multilocation_mid, job["company_name"])
                    
            else:
                #Add_empresa_senior
                add_lista_empresas_req7 (lst_empresas_senior, job)
                
                entry = mp.get(data_structs["multilocations"], job["id"])
                value = me.getValue(entry)
                multilocations = value["multilocations"]
                
                if lt.isPresent(lst_empresas_multilocation_senior, job["company_name"]) == 0 and lt.size(multilocations) > 1:
                    lt.addLast(lst_empresas_multilocation_senior, job["company_name"])

            #Add_skills by expertiece
            entry = mp.get(data_structs["skills"], job["id"])
            lst_skills = me.getValue(entry)
            
            for skill in lt.iterator(lst_skills["skills"]):
                if job["experience_level"] == "junior":
                    #Add_junior
                    add_lista_skills (lst_habilidades_junior, skill)
                    total_skills_junior += 1
                    sum_level_junior += int(skill["level"])
                elif job["experience_level"] == "mid":
                    #Add_mid 
                    add_lista_skills (lst_habilidades_mid, skill)
                    total_skills_mid += 1
                    sum_level_mid += int(skill["level"])
                else:
                    #Add_senior
                    add_lista_skills (lst_habilidades_senior, skill)
                    total_skills_senior += 1
                    sum_level_senior += int(skill["level"])
                    
    #Pais con mayor ofertas
    pais_mayor_ofertas = lt.firstElement(top_ranked_paises)
    
    #Ciudad con mayor ofertas
    ranked_ciudades = sort(data_structs, lst_ciudades,"CiudadesListElementsCrit")
    ciudad_mayor_ofertas = lt.firstElement(ranked_ciudades)
    
    #Total ciudades
    total_ciudades = lt.size(lst_ciudades)
    
    
    #Junior info
    n_skills_junior = lt.size(lst_habilidades_junior)
    ranked_skills_junior = sort(data_structs, lst_habilidades_junior, "SkillsListElementsCrit" )
    
    while ranked_skills_junior["elements"][-1]["cantidad"] == 0:
        lt.deleteElement(ranked_skills_junior, lt.size(ranked_skills_junior))
    
    skill_mas_solicitada_junior = lt.firstElement(ranked_skills_junior)
    skill_menos_solicitada_junior = lt.lastElement(ranked_skills_junior)
    
    promedio_level_junior = round(sum_level_junior / total_skills_junior, 2)
    numero_empresas_junior = lt.size(lst_empresas_junior)
    
    ranked_empresas_junior = sort(data_structs, lst_empresas_junior, "EmpresasListElementsCrit" )
    empresa_mayor_ofertas_junior = lt.firstElement(ranked_empresas_junior)
    empresa_menor_ofertas_junior = lt.lastElement(ranked_empresas_junior)

    n_empresas_sedes_junior = lt.size(lst_empresas_multilocation_junior)
    
    
    #Mid info
    n_skills_mid = lt.size(lst_habilidades_mid)
    ranked_skills_mid = sort(data_structs, lst_habilidades_mid, "SkillsListElementsCrit" )
    
    while ranked_skills_mid["elements"][-1]["cantidad"] == 0:
        lt.deleteElement(ranked_skills_mid, lt.size(ranked_skills_mid))
    
    skill_mas_solicitada_mid = lt.firstElement(ranked_skills_mid)
    skill_menos_solicitada_mid = lt.lastElement(ranked_skills_mid)
    
    promedio_level_mid = round(sum_level_mid / total_skills_mid, 2)
    numero_empresas_mid = lt.size(lst_empresas_mid)
    
    ranked_empresas_mid = sort(data_structs, lst_empresas_mid, "EmpresasListElementsCrit" )
    empresa_mayor_ofertas_mid = lt.firstElement(ranked_empresas_mid)
    empresa_menor_ofertas_mid = lt.lastElement(ranked_empresas_mid)

    n_empresas_sedes_mid = lt.size(lst_empresas_multilocation_mid)
    
    
    #Senior info
    n_skills_senior = lt.size(lst_habilidades_senior)
    ranked_skills_senior = sort(data_structs, lst_habilidades_senior, "SkillsListElementsCrit" )
    
    while ranked_skills_senior["elements"][-1]["cantidad"] == 0:
        lt.deleteElement(ranked_skills_senior, lt.size(ranked_skills_senior))
    
    skill_mas_solicitada_senior = lt.firstElement(ranked_skills_senior)
    skill_menos_solicitada_senior = lt.lastElement(ranked_skills_senior)
    
    promedio_level_senior = round(sum_level_senior / total_skills_senior, 2)
    numero_empresas_senior = lt.size(lst_empresas_senior)
    
    ranked_empresas_senior = sort(data_structs, lst_empresas_senior, "EmpresasListElementsCrit" )
    empresa_mayor_ofertas_senior = lt.firstElement(ranked_empresas_senior)
    empresa_menor_ofertas_senior = lt.lastElement(ranked_empresas_senior)

    n_empresas_sedes_senior = lt.size(lst_empresas_multilocation_senior)
    
    #               int            int             dict                dict
    general_info = [total_ofertas, total_ciudades, pais_mayor_ofertas, ciudad_mayor_ofertas]
    
    #              int              dict                         dict                           float                  int                     dict                          dict                          int
    junior_info = [n_skills_junior, skill_mas_solicitada_junior, skill_menos_solicitada_junior, promedio_level_junior, numero_empresas_junior, empresa_mayor_ofertas_junior, empresa_menor_ofertas_junior, n_empresas_sedes_junior]
    mid_info = [n_skills_mid, skill_mas_solicitada_mid, skill_menos_solicitada_mid, promedio_level_mid, numero_empresas_mid, empresa_mayor_ofertas_mid, empresa_menor_ofertas_mid, n_empresas_sedes_mid]
    senior_info = [n_skills_senior, skill_mas_solicitada_senior, skill_menos_solicitada_senior, promedio_level_senior, numero_empresas_senior, empresa_mayor_ofertas_senior, empresa_menor_ofertas_senior, n_empresas_sedes_senior]
    
    expertiece_level_info = [junior_info, mid_info, senior_info]
    
    result =[general_info, expertiece_level_info]
    
    return result


def req_8(data_structs, experticia, divisa, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    
    total_ofertas = 0

    lst_ciudades = lt.newList("ARRAY_LIST", compareCityInList)
    lst_paises = lt.newList("ARRAY_LIST", compareCountryCodeInList)
    lst_empresas = lt.newList("ARRAY_LIST", compareCompanyInList)
    
    n_ofertas_rango_salarial = 0
    n_ofertas_salario_fijo = 0
    n_ofertas_sin_salario = 0
    
    
    jobs = data_structs["lst_jobs"]
    
    if experticia == "indiferente":
        
        for job in lt.iterator(jobs):
            
            year = job["published_at"][0:4]
            month =job["published_at"][5:7]
            day =job["published_at"][8:10]
            date = year+"-"+month+"-"+day
            
            #Se obtiene el tipo de empleo de la oferta y la skill
            entry = mp.get(data_structs["employment_types"], job["id"])
            emp = me.getValue(entry)
            
            entry = mp.get(data_structs["skills"], job["id"])
            skills = me.getValue(entry)
            
            if date >= fecha_inicial and date <= fecha_final and emp["currency_salary"] == divisa:
                
                total_ofertas += 1
                
                #Se añade a la lista de salarios
                if emp["salary_from"] != "" and emp["salary_to"] != "":
                    n_ofertas_rango_salarial += 1
                elif emp["salary_from"] == "" and emp["salary_to"] == "":
                    n_ofertas_sin_salario += 1
                elif emp["salary_from"] == "" or emp["salary_to"] == "" or emp["salary_to"] == emp["salary_from"]:
                    n_ofertas_salario_fijo += 1
                
                #Se añaden al conteo de ciudades, paises y empresas de la consulta
                add_lista_ciudades_req7 (lst_ciudades, job)
                add_lista_empresas_req7 (lst_empresas, job)
                
                #Se añade a la estructrua de paises con
                add_lista_paises_req8(lst_paises, job, emp, skills)
        
    else:
        
        for job in lt.iterator(jobs):
            
            year = job["published_at"][0:4]
            month =job["published_at"][5:7]
            day =job["published_at"][8:10]
            date = year+"-"+month+"-"+day
            
            #Se obtiene el tipo de empleo de la oferta y la skill
            entry = mp.get(data_structs["employment_types"], job["id"])
            emp = me.getValue(entry)
            
            entry = mp.get(data_structs["skills"], job["id"])
            skills = me.getValue(entry)
            
            if date >= fecha_inicial and date <= fecha_final and job["experience_level"] == experticia and emp["currency_salary"] == divisa:
                
                total_ofertas += 1
                
                #Se añade a la lista de salarios
                if emp["salary_from"] != "" and emp["salary_to"] != "":
                    n_ofertas_rango_salarial += 1
                elif emp["salary_from"] == "" and emp["salary_to"] == "":
                    n_ofertas_sin_salario += 1
                elif emp["salary_from"] == "" or emp["salary_to"] == "" or emp["salary_to"] == emp["salary_from"]:
                    n_ofertas_salario_fijo += 1
                
                #Se añaden al conteo de ciudades, paises y empresas de la consulta
                add_lista_ciudades_req7 (lst_ciudades, job)
                add_lista_empresas_req7 (lst_empresas, job)
                
                #Se añade a la estructrua de paises con
                add_lista_paises_req8(lst_paises, job, emp, skills)
    
    
    ranked_paises = sort(data_structs, lst_paises, "country_average_salary_crit")
    
    result = [ranked_paises, total_ofertas, lst_ciudades, lst_empresas, n_ofertas_rango_salarial, n_ofertas_salario_fijo, n_ofertas_sin_salario]
    
    return result
    
    
    
    

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# ==============================
# Funciones de ordenamiento
# ==============================

def date_crit(data_1,data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (dict): oferta de trabajo
        data2 (dict): oferta de trabajo

    Returns:
        Bool: Si el data_1 es mas reciente que el data_2
    """
    date_1 = datetime.strptime(data_1["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_2 = datetime.strptime(data_2["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    
    return str(date_1) > str(date_2)

def country_range_date_crit(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (dict): oferta de trabajo
        data2 (dict): oferta de trabajo

    Returns:
        Bool: Si el data_1 es mas reciente que el data_2
    """
    date_1 = datetime.strptime(data_1["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    
    date_2 = datetime.strptime(data_2["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    
    if str(date_1) < str(date_2):
        return True
    elif str(date_1) == str(date_2):
        return data_1["country_code"] < data_2["country_code"]
    else:
        return False
    
def date_company_crit(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    
    large_date_1 = datetime.strptime(data_1["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_1 = large_date_1.date()
    
    large_date_2 = datetime.strptime(data_2["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_2 = large_date_2.date()
    
    if str(date_1) > str(date_2):
        return True
    elif str(date_1) == str(date_2):
        return data_1["company_name"] < data_2["company_name"] 
    else:
        return False
    
def country_average_salary_crit (data_1, data_2):

    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    
    average_salary_1 = data_1["average_salary"]
    average_salary_2 = data_2["average_salary"]
    
    if average_salary_1 > average_salary_2:
        return True
    elif average_salary_1 == average_salary_2:
        return data_1["pais"] < data_2["pais"] 
    else:
        return False
    
    

    
def CountryListElementsCrit (el1, el2):
    return el1["n_ofertas"] > el2["n_ofertas"]

def CiudadesListElementsCrit (el1, el2):
    return el1["n_ofertas"] > el2["n_ofertas"]

def EmpresasListElementsCrit (el1, el2):
    return el1["n_ofertas"] > el2["n_ofertas"]

def SkillsListElementsCrit (el1, el2):
    return el1["cantidad"] > el2["cantidad"]


def sort(data_structs,list,ord_crit):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    
    crit_ordenamiento = getattr(model, ord_crit)   #Obtenido de la Doc Oficial de Python: https://docs.python.org/3/library/functions.html#getattr  
    sorted_elements = merg.sort(list,crit_ordenamiento)

    return sorted_elements
