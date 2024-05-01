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
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

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
    data_struct = {"tabla_paisxExpLevel": None,
                'tabla_ciudadxExpLevel': None,
               'tabla_skillsID': None,
               'tabla_employmentTypesID': None,
               "tabla_multilocationID":None,
               }
    
        
    data_struct['tabla_ciudadxExpLevel'] = mp.newMap(3,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_anios)
    
    data_struct["tabla_paisxExpLevel"] = mp.newMap(3,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_anios)
    
    data_struct["tabla_ciudades"]=mp.newMap(2000,
                                    maptype="PROBING",
                                    loadfactor=0.5,
                                    cmpfunction=compare_cities)
    
    data_struct["tabla_niveles_experiencias"]=mp.newMap(3,
                                    maptype="PROBING",
                                    loadfactor=0.5,
                                    cmpfunction=compare_cities)
    
    
    data_struct["tabla_empresas"]=mp.newMap(7000,
                                    maptype="CHAINING",
                                    loadfactor=4,
                                    cmpfunction=compare_empresas)
    
    data_struct["tabla_paises"]=mp.newMap(200,
                                    maptype="CHAINING",
                                    loadfactor=4,
                                    cmpfunction=compare_paises)

    data_struct["tabla_skillsID"] = mp.newMap(400000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_mapId)

    data_struct['tabla_multilocationID'] = mp.newMap(200937,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   cmpfunction=compare_mapId)
    
    data_struct['tabla_employmentTypesID'] = mp.newMap(244937,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=compare_mapId)
    

    return data_struct



#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤
# Funciones para agregar informacion al modelo
#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    pass

def add_tabla_ciudades(data_struct, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Saco la ciudad que va a ser la llave
    city=job["city"]
    
    #Chequeo si el la ciudad que quiero añadir existe
    existCity = mp.contains(data_struct["tabla_ciudades"], city)
    #Si si existe cojo esa ciudad
    if existCity:
        entryCity = mp.get(data_struct["tabla_ciudades"], city)
        #Cojo el value de ese entry
        cityValue = me.getValue(entryCity)
    #Si no existe creo un nuevo key, value pair
    else:
        cityValue = newCityJobsValue(city)
        mp.put(data_struct["tabla_ciudades"], city, cityValue)
    #Añado a la lista de trabajos de esa ciudad
    lt.addLast(cityValue['jobs'], job)
    
    pass

def add_tabla_paises(data_struct, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Saco la pais que va a ser la llave
    pais=job["country_code"]
    
    #Chequeo si el pais que quiero añadir existe
    existPais = mp.contains(data_struct["tabla_paises"], pais)
    #Si si existe cojo ese pais
    if existPais:
        entryPais = mp.get(data_struct["tabla_paises"], pais)
        #Cojo el value de ese entry
        paisValue = me.getValue(entryPais)
    #Si no existe creo un nuevo key, value pair
    else:
        paisValue = newPaisJobsValue(pais)
        mp.put(data_struct["tabla_paises"], pais, paisValue)
    #Añado a la lista de trabajos de ese pais
    lt.addLast(paisValue['jobs'], job)
    
    pass


def add_tabla_niveles_experiencia(data_struct, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Saco la pais que va a ser la llave
    expLevel=job["experience_level"]
    
    #Chequeo si el pais que quiero añadir existe
    expLevelExists = mp.contains(data_struct["tabla_niveles_experiencias"], expLevel)
    #Si si existe cojo ese pais
    if expLevelExists:
        entryExp = mp.get(data_struct["tabla_niveles_experiencias"], expLevel)
        #Cojo el value de ese entry
        expValue = me.getValue(entryExp)
    #Si no existe creo un nuevo key, value pair
    else:
        expValue = newExpLevelValue(expLevel)
        mp.put(data_struct["tabla_niveles_experiencias"], expLevel, expValue)
    #Añado a la lista de trabajos de ese pais
    lt.addLast(expValue['jobs'], job)
    
    pass

def add_tabla_empresas(data_struct, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Saco la empresa que va a ser la llave
    empresa=job["company_name"]
    
    #Chequeo si la empresa que quiero añadir existe
    existEmpresa = mp.contains(data_struct["tabla_empresas"], empresa)
    #Si si existe cojo ese pais
    if existEmpresa:
        entryEmpresa = mp.get(data_struct["tabla_empresas"], empresa)
        #Cojo el value de ese entry
        empresaValue = me.getValue(entryEmpresa)
    #Si no existe creo un nuevo key, value pair
    else:
        empresaValue = newEmpresaValue(empresa)
        mp.put(data_struct["tabla_empresas"], empresa, empresaValue)
    #Añado a la lista de trabajos de ese pais
    lt.addLast(empresaValue['jobs'], job)
    
    pass

def add_tabla_paisxExpLevel(data_struct, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Saco el nivel de experiencia y el pais que van a ser dos keys
    exp_level = job["experience_level"]
    pais = job["country_code"]
    #Para que no vaya a sacar error con los trabajos que no tienen nada en pais
    if pais == "":
        pais="Undefined"
    
    #Hago estos splits para sacar el anio y mes por su propia cuenta
    fechaSinHoras=job["published_at"].split("T")
    fechaAnioMesDia=fechaSinHoras[0].split("-")
    #Saco el mes y anio que van a ser otras dos keys
    mes=fechaAnioMesDia[1]
    anio=fechaAnioMesDia[0]
    
    #Chequeo si existe el año en la tabla
    existAnio = mp.contains(data_struct["tabla_paisxExpLevel"], anio)
    #Si si existe cojo el value de ese año
    if existAnio:
        entry = mp.get(data_struct["tabla_paisxExpLevel"], anio)
        anioValue = me.getValue(entry)
    #Si no existe creo una nueva key,value pair
    else:
        anioValue = newAnioValue(anio)
        mp.put(data_struct["tabla_paisxExpLevel"], anio, anioValue)
    
    
    #Chequeo si existe el mes en la tabla del año
    existMes= mp.contains(anioValue["meses"], mes)
    #Si si existe cojo el value de ese mes
    if existMes:
        entry = mp.get(anioValue["meses"], mes)
        mesValue = me.getValue(entry)
    #Si no existe creo una nueva key,value pair
    else:
        mesValue = newMesValue(mes)
        mp.put(anioValue["meses"], mes, mesValue)
    
    
    #Chequeo si existe el pais en la tabla del mes
    existPais=mp.contains(mesValue["paises"], pais)
    #Si ya existe el pais cojo el value de ese pais
    if existPais:
        entryPais = mp.get(mesValue["paises"], pais)
        paisValue = me.getValue(entryPais)
    #Si no existe creo un nuevo key, value pair 
    else:
        paisValue = newPaisValue(pais)
        mp.put(mesValue["paises"], pais, paisValue)
        
    
    #Chequeo si el nivel que quiero añadir existe dentro de ese pais
    existExpLevel = mp.contains(paisValue["experience_levels"], exp_level)
    #Si si existe cojo ese experience level
    if existExpLevel:
        entryExpLevel = mp.get(paisValue["experience_levels"], exp_level)
        #Cojo el value de ese entry
        exp_levelValue = me.getValue(entryExpLevel)
    #Si no existe creo un nuevo key, value pair
    else:
        exp_levelValue = newExpLevelValue(exp_level)
        mp.put(paisValue["experience_levels"], exp_level, exp_levelValue)
    #Añado a la lista de trabajos de ese experience level 
    lt.addLast(exp_levelValue['jobs'], job)
        

def add_tabla_ciudadxExpLevel(data_struct, job):
    """
    Función para agregar nuevos elementos a la lista
"""
    #Saco el nivel de experiencia y el pais que van a ser dos keys
    exp_level = job["experience_level"]
    ciudad = job["city"]
    #Para que no vaya a sacar error con los trabajos que no tienen nada en ciudad
    if ciudad == "":
        ciudad="Undefined"
    
    #Hago estos splits para sacar el anio por su propia cuenta
    fechaSinHoras=job["published_at"].split("T")
    fechaAnioMesDia=fechaSinHoras[0].split("-")
    #Saco el mes que va a ser otra key
    anio=fechaAnioMesDia[0]
    
    #Chequeo si existe el año en la tabla
    existAnio = mp.contains(data_struct["tabla_ciudadxExpLevel"], anio)
    #Si si existe cojo el value de ese año
    if existAnio:
        entry = mp.get(data_struct["tabla_ciudadxExpLevel"], anio)
        anioValue = me.getValue(entry)
    #Si no existe creo una nueva key,value pair
    else:
        anioValue = newAnioxCiudadValue(anio)
        mp.put(data_struct["tabla_ciudadxExpLevel"], anio, anioValue)
    
    
    #Chequeo si existe la ciudad en la tabla del año
    existPais=mp.contains(anioValue["ciudades"], ciudad)
    #Si ya existe el pais cojo el value de ese pais
    if existPais:
        entryCity = mp.get(anioValue["ciudades"], ciudad)
        cityValue = me.getValue(entryCity)
    #Si no existe creo un nuevo key, value pair 
    else:
        cityValue = newCityValueExpLevel(ciudad)
        mp.put(anioValue["ciudades"], ciudad, cityValue)
        
    
    #Chequeo si el nivel que quiero añadir existe dentro de ese pais
    existExpLevel = mp.contains(cityValue["experience_levels"], exp_level)
    #Si si existe cojo ese experience level
    if existExpLevel:
        entryExpLevel = mp.get(cityValue["experience_levels"], exp_level)
        #Cojo el value de ese entry
        exp_levelValue = me.getValue(entryExpLevel)
    #Si no existe creo un nuevo key, value pair
    else:
        exp_levelValue = newExpLevelValue(exp_level)
        mp.put(cityValue["experience_levels"], exp_level, exp_levelValue)
    #Añado a la lista de trabajos de ese experience level 
    lt.addLast(exp_levelValue['jobs'], job)
        
    pass
    

def add_tabla_multilocationID(data_struct, job):
    mp.put(data_struct['tabla_multilocationID'], job['id'], job)


def searchJob_byID(data_struct, job):

    value = mp.get(data_struct['tabla_employmentTypesID'], (job['id'], None))
    if value is not None:
        return value
    else:
        return "el jobID no se encuentra en el archivo de employment types"



def add_tabla_employmentTypesID(data_struct, employType):
    #Cambio de divisa
    if  employType["currency_salary"] == "usd":
        employType["salary_from"] = round(float(employType["salary_from"]) * 3.98,2)
        employType["salary_to"] = round(float(employType["salary_from"]) * 3.98,2)


    elif  employType["currency_salary"] == "gbp":
        employType["salary_from"] = round(float(employType["salary_from"]) * 5.05,2)
        employType["salary_to"] = round(float(employType["salary_to"]) * 5.05,2)


    elif  employType["currency_salary"] == "eur":
        employType["salary_from"] =round(float(employType["salary_from"]) * 4.32,2)
        employType["salary_to"] = round(float(employType["salary_from"]) * 4.32,2)


    elif  employType["currency_salary"] == "chf":
        employType["salary_from"] =round(float(employType["salary_from"]) * 4.49,2)
        employType["salary_to"] = round(float(employType["salary_from"]) * 4.49,2)   
        
    mp.put(data_struct['tabla_employmentTypesID'], employType['id'], employType)



def add_tabla_skillsID(data_struct, skill):
    id = skill["id"]

    if mp.contains(data_struct["tabla_skillsID"], id):
        entrySkill = mp.get(data_struct["tabla_skillsID"], id)
        listSkills = me.getValue(entrySkill)
        lt.addLast(listSkills["skills"], skill)
    else:
        listSkills=newSkillsValue(id)
        mp.put(data_struct["tabla_skillsID"], id, listSkills)
        lt.addLast(listSkills["skills"], skill)





#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤
# Funciones para creacion de datos
#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤


    
def newExpLevelValue(exp_level):
    """
    Esta funcion crea la estructura de ofertas asociados
    a un nivel de experiencia.
    """
    entry = {'exp_level': "", "jobs": None}
    entry['exp_level'] = exp_level
    entry['jobs'] = lt.newList('ARRAY_LIST')
    return entry

def newEmpresaValue(empresa):
    """
    Esta funcion crea la estructura de ofertas asociados
    a una empresa.
    """   
    entry = {'empresa': "", "jobs": None}
    entry['empresa'] = empresa
    entry['jobs'] = lt.newList('ARRAY_LIST')
    
    return entry

def newCityJobsValue(city):
    entry = {'city': "", "jobs": None}
    entry['city'] = city
    entry['jobs'] = lt.newList('ARRAY_LIST')
    
    return entry

def newPaisJobsValue(pais):
    entry = {'pais': "", "jobs": None}
    entry['pais'] = pais
    entry['jobs'] = lt.newList('ARRAY_LIST')
    
    return entry

def newEmpresaValue(empresa):
    """
    Esta funcion crea la estructura de ofertas asociados
    a una empresa.
    """   
    entry = {'empresa': "", "jobs": None}
    entry['empresa'] = empresa
    entry['jobs'] = lt.newList('ARRAY_LIST')
    
    return entry

def newCityJobsValue(city):
    entry = {'city': "", "jobs": None}
    entry['city'] = city
    entry['jobs'] = lt.newList('ARRAY_LIST')
    
    return entry

def newPaisJobsValue(pais):
    entry = {'pais': "", "jobs": None}
    entry['pais'] = pais
    entry['jobs'] = lt.newList('ARRAY_LIST')
    
    return entry


def newCityValueExpLevel(city):
    entry = {'city': "", "experience_levels": None}
    entry['city'] = city
    entry['experience_levels'] = mp.newMap(numelements=3, maptype="PROBING", loadfactor=0.5, 
                            cmpfunction=compare_exp_level)
    return entry


def newCityValue(city):
    entry = {"city": "", "empresas": None}
    entry["city"] = city
    
    ciudades10000=["Warszawa", "Wroclaw","Roznan","Gdansk","Katowice","Krakow"]
    ciudades5000=["Szczecin","Rzeszow","Zielona Gora","Lublin","Bialystok","Bydgoszcz","Lodz"]
    ciudades2000=["Torun","Opole","Olsztyn","Bielsko-Biala","Czestochowa","Gliwice","Gorzow Wielkopolski","Kielce"]
    
    if city in ciudades10000:
        elements=700
    elif city in ciudades5000:
        elements=300
    elif city in ciudades2000:
        elements=150
    else:
        elements=50
        
    entry["empresas"] = mp.newMap(numelements=elements, 
                                    maptype= "PROBING",
                                    loadfactor=0.5, 
                                    cmpfunction=compare_empresas)
    
    return entry

def newPaisValue(pais):
    entry = {'pais': "", "experience_levels": None}
    entry['pais'] = pais
    entry['experience_levels'] = mp.newMap(numelements=3, maptype="PROBING", loadfactor=0.5, 
                            cmpfunction=compare_exp_level)
    return entry

def newMesValue(mes):
    entry = {'mes': "", "paises": None}
    entry['mes'] = mes
    entry['paises'] = mp.newMap(numelements=100, maptype="CHAINING", loadfactor=4,
                                cmpfunction=compare_ciudades)
    return entry
 
def newMesValueCities(mes):
    entry = {'mes': "", "cities": None}
    entry['mes'] = mes
    entry['cities'] = mp.newMap(numelements=800, maptype="PROBING", loadfactor=0.5,
                                cmpfunction=compare_cities)
    return entry
 

def newAnioValue(anio):
    entry = {'anio': "", "meses": None}
    entry['anio'] = anio
    
    entry['meses'] = mp.newMap(numelements=12, maptype="PROBING", loadfactor=0.5,
                                cmpfunction=compare_meses)
    return entry

def newAnioxCiudadValue(anio):
    entry = {'anio': "", "ciudades": None}
    entry['anio'] = anio
    
    entry['ciudades'] = mp.newMap(numelements=1700, maptype="PROBING", loadfactor=0.5,
                                cmpfunction=compare_exp_level)
    return entry

def newSkillsValue(id):
    entry = {'id': "", "skills": None}
    entry['id'] = id
    
    entry['skills'] = lt.newList('SINGLE_LINKED')
    
    return entry



def contador_newSkillValue(skill, level):
    entry = {"name": "", "times": 0, "average":0}
    entry["name"]=skill
    entry["average"]=int(level)
    
    return entry

def contador_newEmpresaValue(empresa):
    entry = {"name": "", "times": 0}
    entry["name"]=empresa
    
    return entry

def contador_newCityValue(city):
    entry = {"name": "", "times": 0}
    entry["name"]=city
    
    return entry



#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤
# Funciones de consulta
#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤


def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, pais, exp, n):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
        
    parejaPais = mp.get(data_structs["tabla_paises"], pais)
    ofertasPais = (me.getValue(parejaPais))["jobs"]

    parejaExplevel = mp.get(data_structs["tabla_niveles_experiencias"], exp)
    ofertasExp = (me.getValue(parejaExplevel))["jobs"]

    sizePais = lt.size(ofertasPais)  
    sizeExp = lt.size(ofertasExp)   
    
    ofertasAmbos = lt.newList("ARRAY_LIST")
    
    if sizePais <= sizeExp:
        for job in lt.iterator(ofertasPais):
            if job["experience_level"] == exp:
                lt.addLast(ofertasAmbos, job)
    
    else:
        for job in lt.iterator(ofertasExp):
            if job["country_code"] == pais:
                lt.addLast(ofertasAmbos, job)        

    ofertas_ord = sortJobsDate_MayorMenor(ofertasAmbos)
    ofertasN = lt.newList("ARRAY_LIST")

    size = lt.size(ofertas_ord)

    i = 1 
    while i < size and lt.size(ofertasN)< n: 
        lt.addLast(ofertasN, lt.getElement(ofertas_ord, i))
        i += 1

    ans = [sizePais, sizeExp, ofertasN]

    return ans

def req_2_final(data_structs, city, emp, n):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2

    parejaCity = mp.get(data_structs["tabla_ciudades"], city)
    ofertasCity = (me.getValue(parejaCity))["jobs"]

    parejaEmp = mp.get(data_structs["tabla_empresas"], emp)
    ofertasEmp = (me.getValue(parejaEmp))["jobs"]

    sizeCity = lt.size(ofertasCity)  
    sizeEmp = lt.size(ofertasEmp)   
    
    ofertasAmbos = lt.newList("ARRAY_LIST")
    
    if sizeCity <= sizeEmp:
        for job in lt.iterator(ofertasCity):
            if job["company_name"] == emp:
                lt.addLast(ofertasAmbos, job)
    
    else:
        for job in lt.iterator(ofertasEmp):
            if job["city"] == city:
                lt.addLast(ofertasAmbos, job)        

    ofertas_ord = sortJobsDate_MayorMenor(ofertasAmbos)
    ofertasN = lt.newList("ARRAY_LIST")

    sizeList = lt.size(ofertas_ord)

    i = 1 
    while i < sizeList and lt.size(ofertasN)< n: 
        lt.addLast(ofertasN, lt.getElement(ofertas_ord, i))
        i += 1

    ans = [sizeList, ofertasN]    
    
    return ans


def req_3(data_struct,company_name, start_date, end_date):
    """
    Función que soluciona el requerimiento 3
    """
    company_info = mp.get(data_struct['tabla_empresas'], company_name)

    company_offers = me.getValue(company_info)['jobs']

    # mapa para contadores de ofertas por nivel de experiencia
    tabla_experience_levels = mp.newMap(numelements=3,
                                  maptype='PROBING',
                                  loadfactor=0.5)

    # Inicializar contadores en el mapa
    mp.put(tabla_experience_levels, 'junior', 0)
    mp.put(tabla_experience_levels, 'mid', 0)
    mp.put(tabla_experience_levels, 'senior', 0)

    # Lista para almacenar los detalles de las ofertas
    offers_details = lt.newList('ARRAY_LIST')

    # Filtrar y contar ofertas en el rango de fechas
    for offer in lt.iterator(company_offers):
        if start_date <= offer['published_at'] <= end_date:
            # Contar las ofertas por nivel de experiencia
            exp_level = offer['experience_level']
            current_count = mp.get(tabla_experience_levels, exp_level)
            if current_count:
                mp.put(tabla_experience_levels, exp_level, me.getValue(current_count) + 1)
            # Agregar detalles de la oferta a la lista
            lt.addLast(offers_details,offer)

    offers_sorted_alfabetico=sa.sort(offers_details, sort_critJobs_pais_MenorMayor)
    offers_details_sorted=merg.sort(offers_sorted_alfabetico,sortCrit_Fechas_MenorMayor)

    # Construir la respuesta

    junior_entry = mp.get(tabla_experience_levels, 'junior')
    if junior_entry is not None:
    # Usar getValue para obtener el valor asociado a la entrada
        ofertas_junior = me.getValue(junior_entry)
    else:
        ofertas_junior = 0

    mid_entry = mp.get(tabla_experience_levels, 'mid')
    if mid_entry is not None:
    # Usar getValue para obtener el valor asociado a la entrada
        ofertas_mid = me.getValue(mid_entry)
    else:
        ofertas_mid = 0


    senior_entry = mp.get(tabla_experience_levels, 'senior')
    if senior_entry is not None:
    # Usar getValue para obtener el valor asociado a la entrada
        ofertas_senior = me.getValue(senior_entry)
    else:
        ofertas_senior = 0

    total_ofertas=int(ofertas_junior) +int(ofertas_mid)+int(ofertas_senior)

    offer_details_company=offers_details_sorted


    response = [total_ofertas,ofertas_junior, ofertas_mid, ofertas_senior,offer_details_company]

    return response 



def req_4(data_structs, pais, datei, datef):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    
    #Obtener las ofertas de ese país específico
    parejaPais = mp.get(data_structs["tabla_paises"], pais)
    ofertasPais = me.getValue(parejaPais)["jobs"]
    ofertas_rango = lt.newList("ARRAY_LIST")

    #Calcular las fechas
    dateFinal = datef + "T99:99:99.999Z"
    dateInicial = datei + "T00:00:00.000Z"

    #Obtiene las ofertas en dicho rango de fechas
    for job in lt.iterator(ofertasPais):
        if job["published_at"] >= dateInicial and job["published_at"] <= dateFinal:
         lt.addLast(ofertas_rango, job)

    #Crea un map que contiene todas las empresas diferentes     
    empresas = mp.newMap(numelements=6000,
                         maptype="PROBING", 
                         loadfactor=0.5)
    
    #Si la empresa no está, se añade al mapa
    for job in lt.iterator(ofertas_rango):
        if not(mp.contains(empresas, job["company_name"])):
            mp.put(empresas, job["company_name"], None)

    #Obtiene el número de empresas diferentes
    size_emp = mp.size(empresas)

    #Crea mapa que contiene todas las ciudades diferentes y cuántas veces aparecen
    ciudades = mp.newMap(numelements=910,
                         maptype="PROBING", 
                         loadfactor=0.5)
    
    for job in lt.iterator(ofertas_rango):

        if mp.contains(ciudades, job["city"]):
            parejaCity = mp.get(ciudades, job["city"])
            valueCity = me.getValue(parejaCity)
            mp.put(ciudades, job["city"], valueCity+1)
        else:
            mp.put(ciudades, job["city"], 1)

    size_city = mp.size(ciudades)
    
    #Busca la ciudad con mayor y menor número de ofertas
    if not(mp.isEmpty(ciudades)):
        mayor = 0
        keyCity = mp.keySet(ciudades)
        
        for city in lt.iterator(keyCity):
            parejaCity = mp.get(ciudades, city)
            if parejaCity != None:
                valueCity  = me.getValue(parejaCity)
                if valueCity > mayor: 
                    mayor = valueCity
                    city_may = city

        menor = mayor 
        for city in lt.iterator(keyCity):
            parejaCity = mp.get(ciudades, city)
            if parejaCity != None:
                valueCity  = me.getValue(parejaCity) 
                if  valueCity < menor:
                    menor = valueCity
                    city_men = city 
        if menor == mayor:
            menor = mayor
            city_men = city_may

    else: 
        city_may = 0
        mayor = 0
        city_men = 0
        menor = 0    

    #primero se ordena con Shell Sort las ofertas por orden alfabético
    rango_ord = sa.sort(ofertas_rango, sort_critJobs_EmpName_MenorMayor)
    #Se ordena por fechas con merge dado que es in situ, las  ofertas con la misma fecha mantendrán el orden previo (alfabético)
    rango_ordenado = merg.sort(rango_ord, sortCrit_JobDates_MenorMayor)

    #Guarda todos los datos para imprimir
    ans = [rango_ordenado, size_emp, size_city, city_may, mayor, city_men, menor]
    
    return ans


def req_5(data_structs, ciudad, fechaInicial, fechaFinal):
    """
    Consulta las ofertas que se publicaron en una ciudad durante un periodo de tiempo
    
    Args:
       data_structs: data structure
       ciudad: Nombre de la ciudad.
       fecha_inicial: La fecha inicial del periodo a consultar (con formato "%Y-%m-%d").
       fecha_final: La fecha final del periodo a consultar (con formato "%Y-%m-%d").
       
    Returns:
        Una lista [sublistCities_final_sort, mayorNombre, mayorNum, menorNombre, menorNum, total_empresas]
        sublistCities_final_sort: Sublista de las ofertas que se publicaron en una ciudad durante un periodo de tiempo
        mayorNombre: empresa con más ofertas
        mayorNum: numero de ofertas de esa empresa
        menorNombre: empresa con menos ofertas
        menorNum: numero de ofertas de esa empresa
        total_empresas: numero de empresas totales
        totalOfertasCiudad: numero de ofertas en la ciudad

    """
    
    # TODO: Realizar el requerimiento 5
    
    #Saco los trabajos de la ciudad
    parejaCity=mp.get(data_structs["tabla_ciudades"], ciudad)
    cityJobs=me.getValue(parejaCity)["jobs"]
    
    #Voy a contar las empresas en esa ciudad
    #Creo contador para las empresas de la ciudad, su tamaño lo ajusto si es de las ciudades más grandes
    ciudades10000=["Warszawa", "Wroclaw","Roznan","Gdansk","Katowice","Krakow"]
    ciudades5000=["Szczecin","Rzeszow","Zielona Gora","Lublin","Bialystok","Bydgoszcz","Lodz"]
    ciudades2000=["Torun","Opole","Olsztyn","Bielsko-Biala","Czestochowa","Gliwice","Gorzow Wielkopolski","Kielce"]
    
    if ciudad in ciudades10000:
        elements=1000
    elif ciudad in ciudades5000:
        elements=600
    elif ciudad in ciudades2000:
        elements=450
    else:
        elements=100
        
    contador_empresas=mp.newMap(numelements=elements, maptype="PROBING", loadfactor=0.5)
    
    sublistJobs=lt.newList("ARRAY_LIST")
    #Busco los trabajos que están dentro del rango de fechas
    fechaFinal_forma2=fechaFinal+"T99:99:99.999Z"
    fechaInicial_forma2=fechaInicial+"T00:00:00.000Z"
    for job in lt.iterator(cityJobs):
        if job["published_at"]>=fechaInicial_forma2 and job["published_at"]<=fechaFinal_forma2:
            lt.addLast(sublistJobs, job)
            
            empresa=job["company_name"]
            #Vou a añadir su empresa al contador
            #Chequeo si la empresa ya existe dentro del contador
            existEmpresa = mp.contains(contador_empresas, empresa)
            #Si si existe cojo ese entry de skill
            if existEmpresa:
                entryEmpresa= mp.get(contador_empresas, empresa)
                #Cojo el value de ese entry
                contador_empresaValue = me.getValue(entryEmpresa)
            #Si no existe creo un nuevo key, value pair
            else:
                contador_empresaValue = contador_newEmpresaValue( empresa)
                mp.put(contador_empresas, empresa, contador_empresaValue)
            #Sumo 1 a las veces que aparece esa empresa
            contador_empresaValue["times"]+=1
        
    #Busco la empresa con menos y más ofertas
    companiesValue=mp.valueSet(contador_empresas)
    menorNum=300000
    mayorNum=0
    
    for company in lt.iterator(companiesValue):
        if company["times"]>mayorNum:
            mayorNum=company["times"]
            mayorNombre=company["name"]
        if company["times"]<menorNum:
            menorNum=company["times"]
            menorNombre=company["name"]
            
    
    #Ordeno alfabéticamente
    sublistCities_alfabetica=sa.sort(sublistJobs, sort_critJobs_EmpName_MenorMayor)
    #Ordeno otra vez por fechas pero esta vez usando merge que es estable para mantener el orden alfabético
    sublistCities_final_sort=merg.sort(sublistCities_alfabetica, sortCrit_JobDates_MenorMayor)
    
    #Saco el numero de ofertas totales en la ciudad en el rango de tiempo
    totalOfertasCiudad=lt.size(sublistCities_final_sort)
    
        
    answer=[sublistCities_final_sort, mayorNombre, mayorNum, menorNombre, menorNum, mp.size(contador_empresas), totalOfertasCiudad]
    
    return answer

def req_6(data_struct, numCiudades, year, exp_level):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    """
     Función que soluciona el requerimiento 6: Clasificar las N ciudades con mayor número de ofertas de trabajo.
    
    Args:
        data_struct (dict): Estructura de datos con la información de las ofertas de trabajo.
        numCiudades (int): Número de ciudades para la consulta.
        year (str): Año de la consulta.
        mes (str): Mes de la consulta.

    Returns:
        'listado_ciudades'
                Una lista 'city stats' donde esta:

                'Nombre de la ciudad'
                'País de la ciudad'
                'Total de ofertas'
                'Numero de empresas'
                'Empresa con mayor número de ofertas'
                'Número de ofertas de la empresa con mayor número de ofertas'
                'Promedio de salario ofertado'
                'Mejor oferta por salario'
                'Peor oferta por salario'

        'total_ofertas'
        'ciudad_con_mas_ofertas'
        'ciudad_con_menos_ofertas'
        'pais_con_mas_ofertas'
     
    """
    parejaYear = mp.get(data_struct['tabla_ciudadxExpLevel'], year)
    yearValue=me.getValue(parejaYear)
    
    
    if parejaYear is None:
        return "Año o mes no encontrado en los datos."
    
    cityStats = lt.newList(datastructure='ARRAY_LIST')
    total_ofertas = 0
    ciudad_con_mas_ofertas = ('', 0)
    ciudad_con_menos_ofertas = ('', float('inf'))
    sumatoria_empresas_totales=0
    

    
    #Saco los nombres de las N ciudades con más trabajos
    conteo_jobs_cities=lt.newList("ARRAY_LIST")
    for ciudad in lt.iterator(mp.keySet(yearValue['ciudades'])):
        ofertasCiudad=0
        ciudadValue=me.getValue(mp.get(yearValue["ciudades"], ciudad))
        if exp_level=="indiferente":

            #Sumo todos los trabajos de esas ciudad
            for exp_levelIt in lt.iterator(mp.keySet(ciudadValue['experience_levels'])):
                expLevelValue = me.getValue(mp.get(ciudadValue['experience_levels'], exp_levelIt))
                ofertasCiudad+=lt.size(expLevelValue['jobs'])

            lt.addLast(conteo_jobs_cities, [ciudad, ofertasCiudad])
        else:
            #Si no es indiferente solo tomo en cuenta las ofertas del nivel de experiencia pedido
            expLevelPareja=mp.get(ciudadValue['experience_levels'], exp_level)
            if expLevelPareja!=None:
                expLevelValue1=me.getValue(expLevelPareja)
                ofertasCiudad=lt.size(expLevelValue1["jobs"])
                lt.addLast(conteo_jobs_cities, [ciudad, ofertasCiudad])
    
    # Ordenamos las ciudades por número de ofertas
    sorted_ciudades = sa.sort(conteo_jobs_cities, sort_crit_cityJobSize)
    ciudad_con_menos_ofertas=lt.lastElement(sorted_ciudades)
    ciudad_con_mas_ofertas=lt.firstElement(sorted_ciudades)

    # Recortamos la lista a las N ciudades
    if lt.size(sorted_ciudades) > numCiudades:
        sorted_Nciudades = lt.subList(sorted_ciudades, 1, numCiudades)
        
    #Saco los datos de las N ciudades 
    for ciudad in lt.iterator(sorted_Nciudades):
        ciudadValue = me.getValue(mp.get(yearValue['ciudades'], ciudad[0]))
        pais_ciudad = None 
        empresas_ciudad = mp.newMap(numelements=100, maptype='PROBING', loadfactor=0.5)
        num_ofertas_ciudad = ciudad[1]
        total_salario = 0
        contador_salarios = 0
        mejor_oferta = (None, 0)
        peor_oferta = (None, float('inf'))
        
        if exp_level!="indiferente":
            expLevelValue = me.getValue(mp.get(ciudadValue['experience_levels'], exp_level))
            empresas_ciudad, total_salario, contador_salarios, mejor_oferta, peor_oferta, pais_ciudad=info_ciudad_req6(expLevelValue, empresas_ciudad, total_salario, contador_salarios, mejor_oferta, peor_oferta)
            
            # Encuentro la empresa con más ofertas en la ciudad
            empresa_con_mas_ofertas = None
            max_ofertas_empresa = -1
            keys_empresas = mp.keySet(empresas_ciudad)
            for key_empresa in lt.iterator(keys_empresas):
                sumatoria_empresas_totales+=1
                num_ofertas = me.getValue(mp.get(empresas_ciudad, key_empresa))
                if num_ofertas > max_ofertas_empresa:
                    max_ofertas_empresa = num_ofertas
                    empresa_con_mas_ofertas = key_empresa

            # Calculo el salario promedio si hay salarios disponibles
            if contador_salarios>0:
                promedio_salario = round(total_salario / contador_salarios,2)

            lt.addLast(cityStats, {
            'Nombre de la ciudad': ciudad[0],
            'País de la ciudad': pais_ciudad,
            'Total de ofertas': num_ofertas_ciudad,
            'Numero de empresas':mp.size(empresas_ciudad),
            'Empresa con mayor número de ofertas': empresa_con_mas_ofertas + " "+ str(max_ofertas_empresa) if empresa_con_mas_ofertas else 'No disponible',
            'Número de ofertas de la empresa con mayor número de ofertas': max_ofertas_empresa,
            'Promedio de salario ofertado': promedio_salario if promedio_salario else 'No disponible',
            'Mejor oferta por salario': mejor_oferta if mejor_oferta[0] else 'No disponible',
            'Peor oferta por salario': peor_oferta if peor_oferta[0] else 'No disponible'
             })

        else: 
            for exp_levelIt in lt.iterator(mp.keySet(ciudadValue['experience_levels'])):
                expLevelValue = me.getValue(mp.get(ciudadValue['experience_levels'], exp_levelIt))
                empresas_ciudad, total_salario, contador_salarios, mejor_oferta, peor_oferta, pais_ciudad=info_ciudad_req6(expLevelValue, empresas_ciudad, total_salario, contador_salarios, mejor_oferta, peor_oferta)
            # Encuentro la empresa con más ofertas en la ciudad
            empresa_con_mas_ofertas = None
            max_ofertas_empresa = -1
            keys_empresas = mp.keySet(empresas_ciudad)
            for key_empresa in lt.iterator(keys_empresas):
                sumatoria_empresas_totales+=1
                num_ofertas = me.getValue(mp.get(empresas_ciudad, key_empresa))
                if num_ofertas > max_ofertas_empresa:
                    max_ofertas_empresa = num_ofertas
                    empresa_con_mas_ofertas = key_empresa

            # Calculo el salario promedio si hay salarios disponibles
            if contador_salarios>0:
                promedio_salario = round(total_salario / contador_salarios,2)

            lt.addLast(cityStats, {
            'Nombre de la ciudad': ciudad[0],
            'País de la ciudad': pais_ciudad,
            'Total de ofertas': num_ofertas_ciudad,
            'Numero de empresas':mp.size(empresas_ciudad),
            'Empresa con mayor número de ofertas': empresa_con_mas_ofertas + " "+ str(max_ofertas_empresa) if empresa_con_mas_ofertas else 'No disponible',
            'Promedio de salario ofertado': promedio_salario if promedio_salario else 'No disponible',
            'Mejor oferta por salario': mejor_oferta if mejor_oferta[0] else 'No disponible',
            'Peor oferta por salario': peor_oferta if peor_oferta[0] else 'No disponible'
             })
            
        total_ofertas += num_ofertas_ciudad


    # Ordenamos las ciudades por número de ofertas y promedio de salario
    sorted_ciudades = sa.sort(cityStats, sort_crit_city_MayorMenor)

    respuesta = {
        'listado_ciudades': sorted_ciudades,
        'total_ofertas': total_ofertas,
        'ciudad_con_mas_ofertas': ciudad_con_mas_ofertas,
        'ciudad_con_menos_ofertas': ciudad_con_menos_ofertas,
        "total_empresas": sumatoria_empresas_totales,
    }
    
    return respuesta

def info_ciudad_req6 (expLevelValue, empresas_ciudad, total_salario, contador_salarios, mejor_oferta, peor_oferta):
    for job in lt.iterator(expLevelValue['jobs']):
        pais_ciudad = job['country_code']
                    
        #Añado su empresa al contador de empresas
        empresa = job['company_name']
        if mp.contains(empresas_ciudad, empresa):
            mp.put(empresas_ciudad, empresa, me.getValue(mp.get(empresas_ciudad, empresa)) + 1)
        else:
            mp.put(empresas_ciudad, empresa, 1)
        
        salario_from = job['salary_from']
        salario_to = job['salary_to']
        
        # Proceso los salarios
        if salario_from and salario_to:
            salario_promedio = (float(salario_from) + float(salario_to)) / 2
            total_salario += salario_promedio
            contador_salarios += 1

                # Proceso los salarios para la mejor y peor oferta
            if salario_to:  # Para la mejor oferta uso salary_to
                salario_to_float = float(salario_to)
                if salario_to_float > mejor_oferta[1]:
                    mejor_oferta = (job['title'], salario_to_float)

            if salario_from:  # Para la peor oferta uso salary_from
                salario_from_float = float(salario_from)
                if salario_from_float < peor_oferta[1]:
                    peor_oferta = (job['title'], salario_from_float)
    
    return empresas_ciudad, total_salario, contador_salarios, mejor_oferta, peor_oferta, pais_ciudad

def req_7(data_struct, numPaises, year, mes):
    """
    Función que soluciona el requerimiento 7
    
    Returns:
        ans=[lista para imprimir, 
            numero de ofertas totales, 
            numero de ciudades totales,
            [nombre de la ciudad con más puestos,  numero ofertas], 
            [nombre del pais con más puestos,  numero ofertas]
    """
     #Saco las parejas de los años
     
    #Cojo la pareja del año pedido
    try:
        parejaYear=mp.get(data_struct["tabla_paisxExpLevel"], year)
    except:
        print("No es un año que está en los datos. Error")
        return None

    #Cojo la pareja del mes pedido
    try:
        parejaMes=mp.get(me.getValue(parejaYear)["meses"], mes)
    except:
        print("No es un mes que está en los datos. Error")
        return None
    
    #Saco el keyset de ese mes que sería los keys de paises
    keysPaises=mp.keySet(me.getValue(parejaMes)["paises"])
    
    #La lista que tendra los países
    listaxPaises=lt.newList(datastructure="ARRAY_LIST")

    #Para cada pais recorro sus exp_levels para sacar sus ofertas y los añado en una lista de listas
    for pais in lt.iterator(keysPaises):
        parejaPais=mp.get((me.getValue(parejaMes)["paises"]), pais)
        #La lista de exp levels de ese pais
        keys_expLevel=mp.keySet(me.getValue(parejaPais)["experience_levels"])
        
        #La lista temporal del país individual
        tempList_Pais=lt.newList(datastructure="ARRAY_LIST")
        
        #Recorro cada exp Level
        for exp_level in lt.iterator(keys_expLevel):
            
            #La lista temporal que ira dentro de la lista del país individual
            tempList_expLevel=lt.newList(datastructure="ARRAY_LIST")
            
            #Saco la pareja de ese exp level
            pareja_expLevel=mp.get(me.getValue(parejaPais)["experience_levels"], exp_level)
            #Saco las ofertas de ese expLevel
            jobs=me.getValue(pareja_expLevel)
            
            #Añado cada uno de esos trabajo a la lista temporal de ese nivel
            for job in lt.iterator(jobs["jobs"]):
                lt.addLast(tempList_expLevel, job)
                
            #Añado la lista del nivel a la lista del pais individual
            lt.addLast(tempList_Pais, tempList_expLevel)
        
        #Añado la lista del país individual a la lista de paises
        lt.addLast(listaxPaises, tempList_Pais)
    
    #Sort de mayor a menor ofertas 
    sorted_listPaises=sa.sort(listaxPaises, sort_crit_numJobsxPais_MayorMenor)
    
    #Saco los N paises con mayores ofertas
    #Si los paises quqe aplican a los criterios son menor que N, añado todas las que aplican
    if lt.size(sorted_listPaises)<numPaises:
        sublist_NPaises=lt.subList(sorted_listPaises,1,lt.size(sorted_listPaises))
    #Saco los primeros N paises con mayorees ofertas
    else:
        sublist_NPaises=lt.subList(sorted_listPaises,1,numPaises)
        
    
    #Creo esta lista que va a ser utilizada para imprimir
    listImpresion=lt.newList("ARRAY_LIST")
    #Variable que necesito contar para todas las ofertas totales
    ofertasTotales=0
    #Contador de ciudades
    contador_ciudades=mp.newMap(maptype="PROBING", loadfactor=0.5, numelements=800)
    
    for pais in lt.iterator(sublist_NPaises):
        paisImpresion=lt.newList("ARRAY_LIST")
        
        for expLevel_List in lt.iterator(pais):
        
            #Cada expLevelImpresion va a ser una fila en la tabla que le printea al usuario
            expLevelImpresion={"País": None, "Nivel de experiencia": None, "Numero_habilidades_solicitadas":None, "Habilidad_mas_solicitada":[0,1], "Habilidad_menos_solicitada":[0,1], 
                      "Promedio_nivel_mínimo_de_hablidades":None, "Numero_empresas_totales":None, "Empresa_mayor_ofertas":[0,1],
                      "Empresa_menor_ofertas":[0,1], "Numero_empresas_multisedes":None
                      }
        
            #Contadores, uso de chaining porque tiene menos buckets para después hacer value set
            temp_ContadorSkills=mp.newMap(maptype="CHAINING", loadfactor=4, numelements=1000)
            temp_ContadorEmpresas=mp.newMap(maptype="CHAINING", loadfactor=4, numelements=1000)
            numEmpresasMultisede=0
            

            #Recorro cada trabajo
            for job in lt.iterator(expLevel_List):
                #Busco si el job tiene multilocation
                existsMultilocation=mp.contains(data_struct["tabla_multilocationID"], job["id"])
                if existsMultilocation:
                    numEmpresasMultisede+=1
                    
                #Busco sus skills
                parejaSkills=mp.get(data_struct["tabla_skillsID"], job["id"])
                lista_skillsJob=(me.getValue(parejaSkills))["skills"]
                
                for skill in lt.iterator(lista_skillsJob):
                    
                    #Chequeo si la skill que quiero añadir ya existe dentro del contador
                    existSkill = mp.contains(temp_ContadorSkills, skill["name"])
                    #Si si existe cojo ese entry de skill
                    if existSkill:
                        entrySkill= mp.get(temp_ContadorSkills, skill["name"])
                        #Cojo el value de ese entry
                        skillValue = me.getValue(entrySkill)
                    #Si no existe creo un nuevo key, value pair
                    else:
                        skillValue = contador_newSkillValue(skill["name"], skill["level"])
                        mp.put(temp_ContadorSkills, skill["name"], skillValue)
                        
                    #Sumo 1 a las veces que aparece esa skill
                    skillValue["times"]+=1
                    
                    #Actualizo el promedio de esa skill
                    if existSkill:
                        avg_prev=skillValue["average"]
                        avg_current= (avg_prev+int(skill["level"]))/2
                        skillValue["average"]=avg_current
                
                
                #Añado su empresa al contador
                #Chequeo si la empresa ya existe dentro del contador
                existEmpresa = mp.contains(temp_ContadorEmpresas, job["company_name"])
                #Si si existe cojo ese entry de skill
                if existEmpresa:
                    entryEmpresa= mp.get(temp_ContadorEmpresas, job["company_name"])
                    #Cojo el value de ese entry
                    empresaValue = me.getValue(entryEmpresa)
                #Si no existe creo un nuevo key, value pair
                else:
                    empresaValue = contador_newEmpresaValue( job["company_name"])
                    mp.put(temp_ContadorEmpresas, job["company_name"], empresaValue)
                #Sumo 1 a las veces que aparece esa empresa
                empresaValue["times"]+=1
                
                
                #Añado su ciudad al contador
                #Chequeo si la ciudad ya existe dentro del contador
                existCity = mp.contains(contador_ciudades, job["city"])
                #Si si existe cojo ese entry de skill
                if existCity:
                    entryCity= mp.get(contador_ciudades, job["city"])
                    #Cojo el value de ese entry
                    cityValue = me.getValue(entryCity)
                #Si no existe creo un nuevo key, value pair
                else:
                    cityValue = contador_newCityValue( job["city"])
                    mp.put(contador_ciudades, job["city"], cityValue)
                #Sumo 1 a las veces que aparece esa ciudad
                cityValue["times"]+=1
                
                
                #Añado a la suma de ofertas totales
                ofertasTotales+=1
                
                
                
            #Busco la habilidad más y menos pedida y el promedio     
            skillsValues=mp.valueSet(temp_ContadorSkills)
            
            topSkill_Num=0
            topSkill_Name=None
            lastSkill_Num=90000
            lastSkill_Name=None
            sum_skillLevel=0
            
            for skillxExpLevels in lt.iterator(skillsValues):
                if skillxExpLevels["times"]>topSkill_Num:
                    topSkill_Num=skillxExpLevels["times"]
                    topSkill_Name=skillxExpLevels["name"]
                if skillxExpLevels["times"]<lastSkill_Num:
                    lastSkill_Num=skillxExpLevels["times"]
                    lastSkill_Name=skillxExpLevels["name"]
                sum_skillLevel+=skillxExpLevels["average"]
                    
                
            #Busco la empresa con más y menos ofertas     
            empresasValues=mp.valueSet(temp_ContadorEmpresas)
            
            topEmp_Num=0
            topEmp_Name=None
            lastEmp_Num=90000
            lastEmp_Name=None
            #listas si hay empresas con mismo numero de ofertas:
            listTopEmps=lt.newList(datastructure="ARRAY_LIST")
            listLastEmps=lt.newList(datastructure="ARRAY_LIST")

            
            for empresasxExpLevels in lt.iterator(empresasValues):
                if empresasxExpLevels["times"]>topEmp_Num:
                    topEmp_Num=empresasxExpLevels["times"]
                    topEmp_Name=empresasxExpLevels["name"]
                    #Borro la lista de empresas pasadas
                    listTopEmps=lt.newList(datastructure="ARRAY_LIST")
                elif empresasxExpLevels["times"]==topEmp_Num:
                    #Si la lista está vacia añado la empresa que estaba con mayor ofertas
                    if lt.isEmpty(listTopEmps):
                        lt.addLast(listTopEmps, [topEmp_Name, topEmp_Num])
                    #Añado la nueva ciudad
                    NewEmp=[empresasxExpLevels["name"], topEmp_Num]
                    lt.addLast(listTopEmps, NewEmp)
                    
                if empresasxExpLevels["times"]<lastEmp_Num:
                    lastEmp_Num=empresasxExpLevels["times"]
                    lastEmp_Name=empresasxExpLevels["name"]
                    #Borro la lista de empresas pasadas
                    listLastEmps=lt.newList(datastructure="ARRAY_LIST")
                elif empresasxExpLevels["times"]==lastEmp_Num:
                    #Si la lista está vacia añado la empresa que estaba con menor ofertas
                    if lt.isEmpty(listLastEmps):
                        lt.addLast(listLastEmps, [lastEmp_Name, lastEmp_Num])
                    #Añado la nueva empresa
                    NewEmp=[empresasxExpLevels["name"], lastEmp_Num]
                    lt.addLast(listLastEmps, NewEmp)                    
            
            #Si solo hubo una empresa con mayor ofertas
            if lt.isEmpty(listTopEmps):
                TopEmpInd=[topEmp_Name,topEmp_Num]
            else:
                #Sorteo la lista de empresas alfabeticamente
                merg.sort(listTopEmps, sort_crit_EmpName_MenorMayor)
                #Saco la primera empresa  
                topEmp=lt.firstElement(listTopEmps)
                TopEmpInd=topEmp[0], topEmp[1] 

            #Si solo hubo una empresa con menos ofertas
            if lt.isEmpty(listLastEmps):
                LastEmpInd=[lastEmp_Name,lastEmp_Num]
            else:
                #Sorteo la lista de empresas alfabeticamente
                merg.sort(listLastEmps, sort_crit_EmpName_MenorMayor)
                #Saco la primera empresa  
                lastEmp=lt.firstElement(listLastEmps)
                LastEmpInd=lastEmp[0], lastEmp[1] 
                    
            #Añado al diccionario
            expLevelImpresion["Promedio_nivel_mínimo_de_hablidades"]=round(sum_skillLevel/mp.size(temp_ContadorSkills),2)
            expLevelImpresion["Habilidad_mas_solicitada"]=[topSkill_Name, topSkill_Num]
            expLevelImpresion["Habilidad_menos_solicitada"]=[lastSkill_Name, lastSkill_Num]
            expLevelImpresion["Numero_habilidades_solicitadas"]=mp.size(temp_ContadorSkills)

            expLevelImpresion["Nivel de experiencia"] = (lt.firstElement(expLevel_List))["experience_level"]
            expLevelImpresion["País"] = (lt.firstElement(expLevel_List))["country_code"]
            
            expLevelImpresion["Numero_empresas_multisedes"]=numEmpresasMultisede
            
            expLevelImpresion["Numero_empresas_totales"]=mp.size(temp_ContadorEmpresas)
            expLevelImpresion["Empresa_mayor_ofertas"]=TopEmpInd
            expLevelImpresion["Empresa_menor_ofertas"]=LastEmpInd



            lt.addLast(paisImpresion, expLevelImpresion)
            
        lt.addLast(listImpresion, paisImpresion)
    
   
    
    #Lista paisMayorOfertas: [0]=nombre del pais con más ofertas, [1] su numero de ofertas
    paisMayor=lt.firstElement(sublist_NPaises)
    #Saco el nombre del pais
    expPaisMayor=lt.firstElement(paisMayor)
    trabajoMayor=lt.firstElement(expPaisMayor)
    #Sumo las ofertas del mayor pais
    ofertasTot_MayorPais=0
    for exp_level in lt.iterator(paisMayor):
        ofertasTot_MayorPais+=lt.size(exp_level)
    paisMayorOfertas=[trabajoMayor["country_code"], ofertasTot_MayorPais]
    
    #Busco la ciudad con más y menos ofertas     
    cityValues=mp.valueSet(contador_ciudades)
    
    topCity_Num=0
    topCity_Name=None
    
    for cities in lt.iterator(cityValues):
        if cities["times"]>topCity_Num:
            topCity_Num=cities["times"]
            topCity_Name=cities["name"]
            
    cityMayorOfertas=[topCity_Name, topCity_Num]

                                        
    answer= [listImpresion, ofertasTotales, mp.size(contador_ciudades), cityMayorOfertas, paisMayorOfertas,]
    
    """
    ans=[lista para imprimir, 
        numero de ofertas totales, 
        numero de ciudades totales,
        [nombre de la ciudad con más puestos,  numero ofertas], 
        [nombre del pais con más puestos,  numero ofertas] :)
    """
    
    return answer


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass



#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤
# Funciones utilizadas para comparar elementos dentro de una lista
#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    pass

def compare_exp_level(exp_level, entry):
    """
    Compara dos niveles de experiencia. El primero es una cadena
    y el segundo un entry de un map
    """
    exp_level_key= me.getKey(entry)
    if (exp_level == exp_level_key):
        return 0
    elif (exp_level > exp_level_key):
        return 1
    else:
        return -1

def compare_empresas(empresa, entry):
    """
    Compara dos empresas. El primero es una cadena
    y el segundo un entry de un map
    """
    empresa_key= me.getKey(entry)
    if (empresa == empresa_key):
        return 0
    elif (empresa > empresa_key):
        return 1
    else:
        return -1

def compare_ciudades(ciudad, entry):

    ciudad_key= me.getKey(entry)
    if (ciudad == ciudad_key):
        return 0
    elif (ciudad > ciudad_key):
        return 1
    else:
        return -1
    
def compare_cities(city, entry):

    city_key= me.getKey(entry)
    if (city == city_key):
        return 0
    elif (city > city_key):
        return 1
    else:
        return -1
        
def compare_meses(mes, entry):
  
    mes_key= me.getKey(entry)
    if (int(mes) == int(mes_key)):
        return 0
    elif (int(mes) > int(mes_key)):
        return 1
    else:
        return -1


def compare_anios(anio, entry):
  
    anio_key= me.getKey(entry)
    if (int(anio) == int(anio_key)):
        return 0
    elif (int(anio) > int(anio_key)):
        return 1
    else:
        return -1


def compare_mapId(ID, entry):

    ID_key= me.getKey(entry)
    if (ID == ID_key):
        return 0
    elif (ID > ID_key):
        return 1
    else:
        return -1
    
def compare_paises(pais, entry):

    pais_key= me.getKey(entry)
    if (pais == pais_key):
        return 0
    elif (pais > pais_key):
        return 1
    else:
        return -1

#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤
# Funciones de ordenamiento
#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    pass

    
def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    pass

def sort_crit_city_MayorMenor(ciudad1, ciudad2):
    if ciudad1['Total de ofertas'] > ciudad2['Total de ofertas']:
        return True
    elif ciudad1['Total de ofertas'] < ciudad2['Total de ofertas']:
        return False
    else:
        # En caso de empate, se ordena por salario
        try:
            return ciudad1['Promedio de salario ofertado'] > ciudad2['Promedio de salario ofertado']
        except:
            if ciudad1['Promedio de salario ofertado']=="No diponible":
              return False
            else:
              return True
    
def sort_crit_cityJobSize(ciudad1, ciudad2):
    if ciudad1[1]>ciudad2[1]:
        return True
    elif ciudad1[1]<ciudad2[1]:
        return False
    
def sortCrit_num_MenorMayor(num1, num2):
    if num1< num2:
        return True
    elif num1> num2:
        return False
    

def sort_numeros_MenorMayor(lista):
    sorted_lista=merg.sort(lista, sortCrit_num_MenorMayor)
    return sorted_lista

def sortCrit_num_MayorMenor(num1, num2):
    if int(num1)> int(num2):
        return True
    elif int(num1)<int(num2):
        return False

def sortCrit_JobDates_MenorMayor(job1,job2):
    """Ordena de menor a mayor"""
    if job1['published_at']< job2['published_at']:
        return True
    elif job1['published_at']> job2['published_at']:
        return False

def sortCrit_JobDates_MayorMenor(job1,job2):
    """Ordena de mayor a menor"""
    if job1['published_at']> job2['published_at']:
        return True
    elif job1['published_at']< job2['published_at']:
        return False

def sortJobsDate_MayorMenor(lista):
    sorted_lista=sa.sort(lista, sortCrit_JobDates_MayorMenor)
    return sorted_lista

def sortJobsDate_MenorMayor(lista):
    sorted_lista=sa.sort(lista, sortCrit_JobDates_MenorMayor)
    return sorted_lista


def sort_numeros_MayorMenor(lista):
    sorted_lista=merg.sort(lista, sortCrit_num_MayorMenor)
    return sorted_lista

def sort_crit_sizeListas_MayorMenor(list1,list2):
    """El sort crit de los tamaños de listas"""
    if list1['size']> list2['size']:
        return True
    elif list1['size']< list2['size']:
        return False
    
def sort_crit_numJobsxPais_MayorMenor(pais1,pais2):
    """El sort crit de paises por numero de ofertas siendo los paises una lista de listas de los exp level"""

    jobs_pais1=0
    jobs_pais2=0
    
    for expLevel in lt.iterator(pais1):
        ofertas=lt.size(expLevel)
        jobs_pais1+=ofertas
        
    for expLevel in lt.iterator(pais2):
        ofertas=lt.size(expLevel)
        jobs_pais2+=ofertas
        
    if jobs_pais1> jobs_pais2:
        return True
    elif jobs_pais1< jobs_pais2:
        return False
    
def sort_crit_EmpName_MenorMayor(city1, city2):
    """El sort crit alfabetico de nombre de emppresa"""
    if city1[0].lower()< city2[0].lower():
        return True
    elif city1[0].lower()> city2[0].lower():
        return False

def sort_critJobs_EmpName_MenorMayor(job1, job2):
    """El sort crit alfabetico de nombre de emppresa"""
    if job1['company_name']< job2['company_name']:
        return True
    elif job1['company_name']> job2['company_name']:
        return False
    
def sort_critJobs_pais_MenorMayor(offer1, offer2):
    """
    el sort crit alfabetico para pais rq3
    """
    country1 = offer1['country_code']
    country2 = offer2['country_code']

    # Compara alfabéticamente los códigos de país.
    if country1 < country2:
        return -1
    elif country1 > country2:
        return 1
    else:
        return 0
    
def sortCrit_Fechas_MenorMayor(job1,job2):
    """Ordena de menor a mayor"""
    if job1['published_at']< job2['published_at']:
        return True
    elif job1['published_at']> job2['published_at']:
        return False


#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤
# Funciones de busqueda
#◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤

def searchFecha(lista, fecha, primera):
    """searchFecha es la MASCARA para la busqueda recursiva, recibe el
    data structure y la fecha a buscar y prepara las condiciones para la recursion

    Args:
        data_struct (dict): el data_struct
        fecha (str): la fecha buscada
        primera (bool): si True, da el primer trabajo de esa fecha. si False, da el último trabajo de ese fecha 

    Returns:
        pos: posición del diccionario que cumple con la fecha
    """
    
    idx=recursiveSearchFecha(lista, fecha, 1, (lt.size(lista)-1), primera)
    
    if idx==-1:
        return None
    else:
        return idx
    


def recursiveSearchFecha(jobs, fecha, low, high, primera):
    """recursiveSearchFecha ejecuta recursivamente la busqueda binaria
    de la fecha en la lista, si no lo encuentra retorna -1, utiliza la
    llave "published_at" para la comparacion

    Args:
        jobs (ADT List): lista de trabajos 
        fecha (str): fecha de la oferta que se busca
        low (int): rango inferior de busqueda
        high (int): rango superior de busqueda
        primera (bool): si True, te da el primer trabajo de esa fecha. si False, te da el último trabajo de esa fecha

    Returns:
        int: indice del trabajo en la lista. 
        Si primera=True, el primero de esa fecha si se encuentra, si no se encuentra el primer trabajo de la fecha después
        Si primera=False, el último de esa fecha si se encuentra, si no se encuentra el ultimo trabajo de la fecha antes
    """

    pos=(high+low)//2
    
    current_date= jobs['elements'][pos]['published_at'].split("T")
    current_dateSimpl= current_date[0]

    if low<=high:
        
        if fecha==current_dateSimpl:
            if primera:
                while fecha in (jobs['elements'][pos-1]['published_at']):
                    pos=pos-1
                return pos
            else:
                while fecha in (jobs['elements'][pos+1]['published_at']):
                    pos=pos+1
                return pos
        
        elif current_dateSimpl > fecha:
            high=pos-1
            return recursiveSearchFecha(jobs, fecha, low, high, primera)
            
        elif current_dateSimpl < fecha:
            low=pos+1
            return recursiveSearchFecha(jobs, fecha, low, high, primera)

    else: 
        if primera:
            return pos+1
        else:
            return pos   