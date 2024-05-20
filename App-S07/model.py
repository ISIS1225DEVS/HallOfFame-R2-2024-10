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
from datetime import datetime as dt
from datetime import datetime as dt
from datetime import datetime as dt
import csv
import sys
import sys
import sys
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
from additional import additionalMethods as adi
from additional import ilegalHandling as ile

assert cf
import time 
from datetime import datetime as dt

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*100)


def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    
    catalog = {'jobs': None, ##Mapa Grabnde de los Ids con TODOS los valores. El resto son filtros
               'published_at': None,
               'country_code': None,
               'experience_level': None,
               'company_name': None,
               'city': None}
    
    #? [Fgutep] Igual que en el ejemplo, creramos una lista single linked para los trabajos.
    catalog['jobs'] = lt.newList('ARRAY_LIST')
    
    
    catalog['published_at'] = mp.newMap(numelements= 203562,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        #cmpfunction=CompareDatesISO8601
                                        )
    
    catalog['country_code'] = mp.newMap(numelements= 80,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        #cmpfunction=CompareCountry
                                        )
    
    catalog['experience_level'] = mp.newMap(numelements= 3,
                                            maptype='PROBING',
                                            loadfactor=0.5,
                                            #cmpfunction=CompareExperience
                                            )
    
    catalog['company_name'] = mp.newMap(numelements= 6322,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        #cmpfunction=CompareCompany
                                        )
    
    catalog['city'] = mp.newMap(numelements= 1453,
                                maptype='PROBING',
                                loadfactor=0.5,
                                #cmpfunction=CompareCity
                                )
    
    return catalog

def addToCatalog(key, catalog, item):
    lt.addLast(catalog[key], item)
    return catalog

# Sizes
def catSize(key, catalog):
    return lt.size(catalog['jobs'])


def addToCatalog(key, catalog, item):
    lt.addLast(catalog[key], item)
    return catalog

# Sizes
def catSize(key, catalog):
    return lt.size(catalog['jobs'])


def addToCatalog(key, catalog, item):
    lt.addLast(catalog[key], item)
    return catalog

# Sizes
def catSize(key, catalog):
    return lt.size(catalog['jobs'])


# Construccion de modelos
def MOA_CSVs(catalog, TempSkills, TempEmpTypes, TempMultiLocs):
    ##* Acceder a Jobs
    jobs = catalog['jobs']['elements'] ##* Jobs es una lista de diccionarios
    ##* Sacar los Ids desde Jobs
    Ids = lt.newList("ARRAY_LIST")
    for job in jobs:
        identificator = job['id']
        lt.addLast(Ids, identificator)
    
    moal2 = mp.newMap(numelements=203562,maptype="CHAINING",loadfactor=4)
    
    # Ahora tenemos una lista con todos los IDs (Primer nLog(N))
    moal = lt.newList("ARRAY_LIST")
    ##* Para cada ID sacado, buscar en los otros 3 CSVs.
    for singleID in lt.iterator(Ids):
        ##* 1) Crean una lista de diccionarios con cada ID
        ## Buscar todas las congruencias
        lt.addLast(moal, {singleID: {'title': None,
                'street': None,
                'city': None,
                'country_code': None,
                'address_text': None,
                'marker_icon': None,
                'workplace_type': None,
                'company_name': None,
                'company_url': None,
                'company_size': None,
                'experience_level': None,
                'published_at': None,
                'remote_interview': None,
                'open_to_hire_ukrainians': None,
                'id': singleID,
                'display_offer': None,
                'contract_type': None,
                'currency_salary': None,
                'salary_from': None,
                'salary_to': None,
                'skill': None,
                'short_name': None}})
        
    TempJobs = {}
    for dic in jobs:
        idJob = dic['id']
        subdic = {
            'title': dic['title'],
            'country_code': dic['country_code'],
            'address_text': dic['address_text'],
            'marker_icon': dic['marker_icon'],
            'workplace_type': dic['workplace_type'],
            'company_name': dic['company_name'],
            'experience_level': dic['experience_level'],
            'company_size': dic['company_size'],
            'published_at': dic['published_at'],
            'remote_interview': dic['remote_interview'],
            'open_to_hire_ukrainians': dic['open_to_hire_ukrainians'],
            'display_offer': dic['display_offer'],
            'company_url': dic['company_url'] 
            }
        TempJobs[idJob] = subdic
        
        
    ##? Funciona hasta acá
    ##* Ahora MOAL tiene todos los Ids con todo el resto de llaves
    for idi in lt.iterator(moal): ## Para cada uno de los diccionarios en moal
        identificator = list(idi.keys())[0] ## Sacar la llave (Id)
        #? Jobs [identificator] ----------------------------------------------------
        idi[identificator]['title'] = TempJobs[identificator]['title']
        idi[identificator]['country_code'] = TempJobs[identificator]['country_code']
        idi[identificator]['address_text'] = TempJobs[identificator]['address_text']
        idi[identificator]['marker_icon'] = TempJobs[identificator]['marker_icon']
        idi[identificator]['workplace_type'] = TempJobs[identificator]['workplace_type']
        idi[identificator]['company_name'] = TempJobs[identificator]['company_name']
        idi[identificator]['experience_level'] = TempJobs[identificator]['experience_level']
        idi[identificator]['company_size'] = TempJobs[identificator]['company_size']
        idi[identificator]['company_url'] = TempJobs[identificator]['company_url']
        idi[identificator]['published_at'] = TempJobs[identificator]['published_at']
        idi[identificator]['remote_interview'] = TempJobs[identificator]['remote_interview']
        idi[identificator]['open_to_hire_ukrainians'] = TempJobs[identificator]['open_to_hire_ukrainians']
        idi[identificator]['display_offer'] = TempJobs[identificator]['display_offer']
        #? Skills ------------------------------------------------------------------
        idi[identificator]['short_name'] = TempSkills[identificator]['short_name']
        idi[identificator]['skill'] = TempSkills[identificator]['skill']
        #? MultiLoc ------------------------------------------------------------------
        idi[identificator]['city'] = TempMultiLocs[identificator]['city'][0]
        idi[identificator]['street'] = TempMultiLocs[identificator]['street'][0]
        #? EmpTypes ------------------------------------------------------------------
        idi[identificator]['contract_type'] = TempEmpTypes[identificator]['tipo_contrato']
        idi[identificator]['currency_salary'] = TempEmpTypes[identificator]['currency_salary']
        idi[identificator]['salary_from'] = TempEmpTypes[identificator]['salario_desde']
        idi[identificator]['salary_to'] = TempEmpTypes[identificator]['salario_hasta']
        
        mp.put(moal2,identificator,idi)
        addDate(catalog,identificator,TempJobs[identificator]['published_at'])
        addCountry(catalog,identificator,TempJobs[identificator]['country_code'])
        addExperience(catalog,identificator,TempJobs[identificator]['experience_level'])
        addCompany(catalog,identificator,TempJobs[identificator]['company_name'])
        addCity(catalog,identificator,TempMultiLocs[identificator]['city'][0])
    
    #? Ejemplo
    """
    aa= mp.valueSet(moal2)
    listaord = sa.sort(aa,CompareCountry)
    for i in listaord:
        mp.get(catalog["countrycode"],listaord["countrycode"])
        mp.put(catalog["countrycode"],listaord["countrycode"],[listaord[0]["id"],listaord[3]["id"]])
    
    #ejemplo requerimiento
    caso1
    oferta=mp.get(catalog["countrycode"],"PL")
    datos=mp.get(moal2,oferta[0]["value"][oferta["key"]])
    caso2
    oferta=mp.get(catalog["countrycode"],"PL")
    id=oferta["key"]
    datos=oferta[oferta["value"][oferta["key"]]]
    """
    catalog['jobs'] = moal2 ##! Agregar moal2 al catálogo bajo la llave de 'JOBS'
    return moal, moal2

    
    
    '''
    Queremos que se vea algo así:
    {...., info:{ID1: {title: Titulo, street: Calle ...., 'Experience': [MismoId1, MismoId2, MismoIdn]}}}
    
    
    
    '''
def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    pass

"""
NUEVAS ESTRUCTURAS PARA LA CREACIÓN DE DATOS
"""
def newStructure(Value):
    Structure = {Value:None}
    Structure[Value] = lt.newList("ARRAY_LIST")
    return Structure


#!! title;street;city;country_code;address_text;marker_icon;workplace_type;company_name;
#!! company_url;company_size;experience_level;published_at;remote_interview;open_to_hire_ukrainians;
#!! id;display_offer
"""
FUNCIONES DE COMPARACIONES DE MAPAS
"""
def CompareDates(date1, dates): 
    date2 = me.getValue(dates)
    """
    date1 = dt.fromisoformat(date1)
    date2 = dt.fromisoformat(date2)
    """
    if date1 == date2:
        return 0
    elif date1 > date2:
        return 1
    elif date1 < date2:
        return -1
    
def CompareCountry(country1,countries):
    country2 = me.getValue(countries)
    if country1 == country2:
        return 0
    elif country1 > country2:
        return 1
    else:
        return -1
    
def CompareExperience(experience1,experience):
    experience2 = me.getValue(experience)
    if experience1 == experience2:
        return 0
    elif experience1 > experience2:
        return 1
    else:
        return -1

def CompareCompany(company1,company):
    company2 = me.getValue(company)
    if company1 == company2:
        return 0
    elif company1 > company2:
        return True
    else:
        return False

def CompareCity(city1,city):
    city2 = me.getValue(city)
    if city1 == city2:
        return 0
    elif city1 > city2:
        return 1
    else:
        return -1

def Compare_fecha_nombre(dic1, dic2):
    date1 = dt.fromisoformat(dic1['published_at'])
    date2 = dt.fromisoformat(dic2['published_at'])
    
def Compare_fecha_nombre(dic1, dic2):
    date1 = dt.fromisoformat(dic1['published_at'])
    date2 = dt.fromisoformat(dic2['published_at'])
    
    if date1 == date2:
        if dic1['company_name'] == dic2['company_name']:
            return False
        elif dic1['company_name'] > dic2['company_name']:
            return True
        else:
            return False
    elif date1 > date2:
        return True
    else:
        return False

def CompareValuesMapTuple(Dic1,Dic2):
    value1=Dic1["value"]
    value2=Dic2["value"]
    if value1 == value2:
        return None
    elif value1 > value2:
        return True
    elif value1 < value2:
        return False

def CompareKeysMapTuple(Dic1,Dic2):
    value1=Dic1["key"]
    value2=Dic2["key"]
    if value1 == value2:
        return None
    elif value1 > value2:
        return True
    elif value1 < value2:
        return False

#borrar si no se usa al final
def Compare_fechas_sin_dict(date1, date2):
    date1_dt = dt.fromisoformat(str(date1))
    date2_dt = dt.fromisoformat(str(date2))
    
    if date1_dt < date2_dt:
        return -1
    elif date1_dt == date2_dt:
        return 0
    else:
        return 1


    
def CompareCompanies(Dic1,Dic2):
    company1=Dic1["company_name"]
    company2=Dic2["company_name"]
    if company1 == company2:
        return 0
    elif company1 > company2:
        return True
    else:
        return False

"""
FUNCIONES PARA AÑADIR DATOS A LOS MAPAS
"""
def addDate(catalog,ID,date):
    dates=catalog["published_at"]
    existdate = mp.contains(dates, date)
    if existdate:
        entry = mp.get(dates, date)
        fecha = me.getValue(entry)
    else:
        fecha = lt.newList("ARRAY_LIST")
        mp.put(dates,date,fecha)
    lt.addLast(fecha,ID)
    
def addCountry(catalog,ID,country):
    countries=catalog["country_code"] ## ESto es un MAPA
    existcountry = mp.contains(countries, country)
    if existcountry:
        entry = mp.get(countries, country)
        pais = me.getValue(entry)
    else:
        pais = lt.newList("ARRAY_LIST")
        mp.put(countries,country,pais)
    lt.addLast(pais,ID)

    
def addExperience(catalog,ID,experience):
    experiences=catalog["experience_level"]
    existexperience = mp.contains(experiences, experience)
    if existexperience:
        entry = mp.get(experiences, experience)
        experiencia = me.getValue(entry)
    else:
        experiencia = lt.newList("ARRAY_LIST")
        mp.put(experiences,experience,experiencia)
    lt.addLast(experiencia,ID)
    
def addCompany(catalog,ID,company):
    companies=catalog["company_name"]
    existcompany = mp.contains(companies, company)
    if existcompany:
        entry = mp.get(companies, company)
        compania = me.getValue(entry)
    else:
        compania = lt.newList("ARRAY_LIST")
        mp.put(companies,company,compania)
    lt.addLast(compania,ID)

def addCity(catalog,ID,city):
    cities=catalog["city"]
    existcity = mp.contains(cities, city)
    if existcity:
        entry = mp.get(cities, city)
        ciudad = me.getValue(entry)
    else:
        ciudad = lt.newList("ARRAY_LIST")
        mp.put(cities,city,ciudad)
    lt.addLast(ciudad,ID)

def CompareDatesISO8601(Dic1, Dic2): 
    date1 = Dic1['published_at']
    date2 = Dic2['published_at']
    #date1 = dt.fromisoformat(date1)
    #date2 = dt.fromisoformat(date2)
    if date1 == date2:
        return None
    elif date1 > date2:
        return True
    elif date1 < date2  :
        return False
    
def CompareDatesNAscii(Dic1, Dic2): 
    date1 = Dic1['published_at']
    date2 = Dic2['published_at']
    comp1 = Dic1['country_code'].upper()
    comp2 = Dic2['country_code'].upper()
    #date1 = dt.fromisoformat(date1)
    #date2 = dt.fromisoformat(date2)
    if date1 == date2:
        if comp1 > comp2:
            return True
        else:
            return False
    elif date1 > date2:
        return True
    elif date1 < date2  :
        return False
    
def CompareDatesCountryNAscii(Dic1, Dic2): 
    date1 = Dic1['published_at']
    date2 = Dic2['published_at']
    comp1 = Dic1['country_code'].upper()
    comp2 = Dic2['country_code'].upper()
    #date1 = dt.fromisoformat(date1)
    #date2 = dt.fromisoformat(date2)
    if date1 == date2:
        if comp1 > comp2:
            return True
        else:
            return False
    elif date1 > date2:
        return True
    elif date1 < date2  :
        return False
    
    
def DateSort(DebonedJobs):
    #* SOLVED : Known issue: No retorna los primeros, problemas de estabilidad.
    '''
    Dónde los más recientes (i.e. Los más cercanos al día actual) estarán de primeras (Indices más bajos del ARRAY_LIST)
    '''
    SortedLOD = merg.sort(DebonedJobs, CompareDatesISO8601)
    return SortedLOD  ## Actualizar lista inicial
    
def DateAsciiSort(DebonedJobs, sort_crit):
    #* SOLVED : Known issue: No retorna los primeros, problemas de estabilidad.
    '''
    Dónde los más recientes (i.e. Los más cercanos al día actual) estarán de primeras (Indices más bajos del ARRAY_LIST)
    '''
    SortedLOD = merg.sort(DebonedJobs, sort_crit)
    return SortedLOD  ## Actualizar lista inicial
    

def req_1(catalog, country, exp):
    ##* Acceder el mapa de país
    countryMap = catalog['country_code']
    byCountry = mp.get(countryMap, country)
    ##* Acceder la lista de IDs por Pais byCountry es una ARRAY_LIST
    byCountry = byCountry['value'] # (Esto es una ARRAY_LIST con todos los IDs)
    #* Ahora que tenemos una lista de todos los IDs de ese país, debemos sacar los IDs correspondientes al nivel de experiencia
    expMap = catalog['experience_level']
    byExp = mp.get(expMap, exp) # Acceder al mapa
    byExp = byExp['value'] # (Esto es una ARRAY_LIST con todos los IDs)
    ##* Ahora hacemos la substracción de conjuntos para sacar sólo los elementos en común:
    meetsCriterias = adi.getIdentical(byCountry, byExp) # Usamos la función
    #* Tenemos que sacar la infromación completa asociada a todos los IDs que obtuvimos
    jobsMap = catalog['jobs']
    fullInfos = adi.getFullInfos(jobsMap, meetsCriterias) ## Usamos una función para iterar sobre la lista de IDs e ir sacando su info completa de Jobs
    ##! Puede que aquí se tengaque incluir el método de Debone para el dateSort
    fullInfos = adi.deboneIds(fullInfos)
    dsfullInfos = DateSort(fullInfos)
    ##* Ahora sacamos la información para el retorno
    NoJobsPerCountry = lt.size(byCountry) ## El total de ofertas de trabajo ofrecidas según el país
    NoJobsPerExperience = lt.size(byExp) ## El total de ofertas de trabajo ofrecidas según la condición (junior, mid o senior).
    ansSize = lt.size(dsfullInfos)
    return dsfullInfos, NoJobsPerCountry, NoJobsPerExperience, ansSize


def req_2(catalog, nombre_compañia, ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    #Organizar datos
    #Organizar datos
    moam_c= catalog["model"]["city"]
    moam_e= catalog["model"]["company_name"]
    
    #Obtener ids de ciudad y compañia especifica
    lista_id_ciudad= mp.get(moam_c, ciudad)
    lista_id_ciudad= lista_id_ciudad["value"]["elements"]
    lista_id_empresa= mp.get(moam_e, nombre_compañia)
    lista_id_empresa= lista_id_empresa["value"]["elements"]
    
    #Total de ofertas ofrecidas por empresa y ciudad especifica
    total_ciudades= (len(lista_id_ciudad))
    total_empresas= (len(lista_id_empresa))
    
    #Encontrar ids comunes entre empresa y ciudad
    lista_ciudad_empresas= adi.getIdentical(lista_id_ciudad, lista_id_empresa)["elements"]
    
    #Sacar info de los ids comunes
    ofertas_info= lt.newList("ARRAY_LIST")
    for offer in lista_ciudad_empresas:
        oferta= mp.get(catalog["model"]["jobs"], offer)
        oferta= oferta["value"][offer]
        oferta_info= {"Fecha": oferta["published_at"] ,
                 "Pais": oferta["country_code"] ,
                 "Ciudad":oferta["city"] ,
                 "Titulo_oferta": oferta["title"] ,
                 "Nivel_experiencia": oferta["experience_level"] ,
                 "Formato_aplicación": oferta["contract_type"], 
                 "Tipo_trabajo": oferta["workplace_type"]}
        oferta= oferta["value"][offer]
        oferta_info= {"Fecha": oferta["published_at"] ,
                 "Pais": oferta["country_code"] ,
                 "Ciudad":oferta["city"] ,
                 "Titulo_oferta": oferta["title"] ,
                 "Nivel_experiencia": oferta["experience_level"] ,
                 "Formato_aplicación": oferta["contract_type"], 
                 "Tipo_trabajo": oferta["workplace_type"]}
        lt.addLast(ofertas_info, oferta_info)
    
    
    return total_ciudades, total_empresas, ofertas_info["elements"]


def req_3(catalog, company, startDate, endDate):
    start = time.time()*1000
    ##* Acceder el mapa de empresa
    compMap = catalog['company_name']
    byCompany = mp.get(compMap, company)
    ##* Acceder la lista de IDs por Pais byCompany es una ARRAY_LIST
    byCompany = byCompany['value'] # (Esto es una ARRAY_LIST con todos los IDs)
    ##* Sacar rango de fechas
    dateMap = catalog['published_at']
    dateKeysInRange = adi.getKeyRangeByFullDates(dateMap, startDate, endDate)
    ##* Sacar IDs correspondientes a esas fechas
    dateIds = lt.newList('ARRAY_LIST')
    for dateId in lt.iterator(dateKeysInRange):
        IdSubli = mp.get(dateMap, dateId)
        IdSubli = IdSubli['value']
        for idi in lt.iterator(IdSubli):
            lt.addLast(dateIds, idi)
    ##* Sacar los Ids que cumplen con ambos criterios Compañía ^ Rango
    meetsCriteria = adi.getIdentical(byCompany, dateIds)
     #* Tenemos que sacar la infromación completa asociada a todos los IDs que obtuvimos
    jobsMap = catalog['jobs']
    fullInfos = adi.getFullInfos(jobsMap, meetsCriteria) ## Usamos una función para iterar sobre la lista de IDs e ir sacando su info completa de Jobs
    fullInfos = adi.deboneIds(fullInfos)
    ##* Total de Ofertas
    totaldeOffer = lt.size(meetsCriteria)
    ##* Por experiencia:
    expMap = catalog['experience_level']
    ##* Número total de ofertas con experticia junior.
    byJunior = mp.get(expMap, 'junior') # Acceder al mapa
    byJunior = byJunior['value'] # (Esto es una ARRAY_LIST con todos los IDs)
    juniorandmeets =  adi.getIdentical(meetsCriteria, byJunior)
    noByJunior = lt.size(juniorandmeets)
    ##* Número total de ofertas con experticia mid
    bymid = mp.get(expMap, 'mid') # Acceder al mapa
    bymid = bymid['value'] # (Esto es una ARRAY_LIST con todos los IDs)
    Midandmeets =  adi.getIdentical(meetsCriteria, bymid)
    noByMid = lt.size(Midandmeets)
    ##* Número total de ofertas con experticia senior.
    bysenior = mp.get(expMap, 'senior') # Acceder al mapa
    bysenior = bysenior['value'] # (Esto es una ARRAY_LIST con todos los IDs)
    Seniorandmeets =  adi.getIdentical(meetsCriteria, bysenior)
    noBySenior= lt.size(Seniorandmeets)
    # El listado de ofertas de la empresa ordenados cronológicamente por fecha y país 
    dsfullInfos = DateSort(fullInfos)
    end = time.time()*1000
    delta = start - end
    print("DeltaTime" + str(delta))
    # TODO Controller del 3
    return totaldeOffer, noByJunior, noByMid, noBySenior, dsfullInfos
    
    
def req_4(control, CODpais, Ffirst, Flast):
    """
    Función que soluciona el requerimiento 4
    """
    # jacome: Realizar el requerimiento 4
    mapcountries=control["country_code"]
    keyscountries=mp.keySet(mapcountries)
    moal2=control["jobs"]
    listaIDsSBCountry=lt.newList("ARRAY_LIST")
    for i in lt.iterator(keyscountries):
        if i == CODpais:
            dato=mp.get(mapcountries,i)
            lt.addLast(listaIDsSBCountry,dato["value"])
    
    valuesSBCountry=lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(listaIDsSBCountry):
        for j in lt.iterator(i):
            dato = mp.get(moal2,j)
            lt.addLast(valuesSBCountry,dato["value"][j])
    DateSort(valuesSBCountry)
    valuesSBCountryANDDate=lt.newList("ARRAY_LIST")
    for i in lt.iterator(valuesSBCountry):
        fecha=i["published_at"][0:10]
        if Ffirst <= fecha and fecha <= Flast:
            lt.addLast(valuesSBCountryANDDate,i)
    
    NUMofertas = lt.size(valuesSBCountryANDDate)
    CompanieswithOfertas = ContadorMapasNOList(valuesSBCountry,"company_name")
    NUMcompanies = mp.size(CompanieswithOfertas)
    CitieswithOfertas = ContadorMapasNOList(valuesSBCountry,"city")
    NUMcities = mp.size(CitieswithOfertas)
    keyscities = mp.keySet(CitieswithOfertas)
    MAXofertasCity = mp.get(CitieswithOfertas,lt.getElement(keyscities,1))
    MINofertasCity = mp.get(CitieswithOfertas,lt.getElement(keyscities,1))
    for i in lt.iterator(keyscities):
        dato = mp.get(CitieswithOfertas,i)
        if MAXofertasCity["value"] < dato["value"]:
            MAXofertasCity = dato
        if MINofertasCity["value"] > dato["value"]:
            MINofertasCity = dato
    sa.sort(valuesSBCountryANDDate,CompareCompanies)
    DateSort(valuesSBCountryANDDate)
    
    return NUMofertas, NUMcompanies, NUMcities, MAXofertasCity, MINofertasCity, valuesSBCountryANDDate


def req_5(catalog, ciudad, fecha_inicial, fecha_final):
    
    #Organizar datos
    
    #Organizar datos
    moam_c= catalog["model"]["city"]
    moam_p= catalog["model"]["published_at"]
    moam_e= catalog["model"]["company_name"]
    moam_j= catalog["model"]["jobs"]

    lista_empresas= mp.keySet(moam_e)  
    lista_id_empresas= mp.valueSet(moam_e)
    
    #Transformar lista_id_empresas a array
    lista_id_empresas_array= lt.newList("ARRAY_LIST")
    for id in lt.iterator(lista_id_empresas):
        lt.addLast(lista_id_empresas_array, id["elements"][0])
    lista_id_empresas_array= lista_id_empresas_array["elements"]
    
    #Obtener ids de una ciudad especifica
    lista_id_ciudad= mp.get(moam_c, ciudad)["value"]["elements"]
    
    lista_id_fechas= mp.valueSet(moam_p)
    
    #Volver lista_id_fechas a array
    fecha_array= lt.newList("ARRAY_LIST")
    for id in lt.iterator(lista_id_fechas):
        lt.addLast(fecha_array, id["elements"][0])
    fecha_array= fecha_array["elements"]
    
    #Sorteo por fechas
    fullinfo= adi.getFullInfos(moam_j, fecha_array)
    fullinfo= adi.deboneIds(fullinfo)["elements"]
    
    #Filtro por rango de fechas
    lista_id_tiempo_filtradas= lt.newList("ARRAY_LIST")
    for offer in fullinfo:
        published_at = dt.fromisoformat(offer['published_at'][:-5])
        id= offer["id"]
        if fecha_inicial <= published_at <= fecha_final:
            lt.addLast(lista_id_tiempo_filtradas, id)
    lista_id_tiempo_filtradas= lista_id_tiempo_filtradas["elements"]
    
    #Filtro especifico por ciudad y por empresas
    id_repetidas_ciudad_tiempo= adi.getIdentical(lista_id_tiempo_filtradas, lista_id_ciudad)["elements"]  
    id_repetidas_empresa= adi.getIdentical(lista_id_ciudad, lista_id_empresas_array)["elements"]
    
    total_ciudad= len(id_repetidas_ciudad_tiempo)
    total_empresas= len(id_repetidas_empresa)
    
    #Empresas max y min y sus contadores
    #Empresas max y min y sus contadores
    empresas_dict= {}
    for empresa in lt.iterator(lista_empresas): 
        ids= mp.get(moam_e, empresa)["value"]
        longitud= lt.size(ids)

        empresas_dict[empresa]= longitud
        
    if (max(empresas_dict, key=empresas_dict.get)) == 1:
        empresas_dict[empresa]= longitud
        
    if (max(empresas_dict, key=empresas_dict.get)) == 1:
        empresa_max = max(empresas_dict, key=empresas_dict.get)
        empresa_min= empresa_max
    else:       
        empresa_max = max(empresas_dict, key=empresas_dict.get)
        empresa_min = min(empresas_dict, key=empresas_dict.get)
    
    #Organizacion y filtro para sortear primero por fecha y luego nombre
    fullinfo2= adi.getFullInfos(moam_j, id_repetidas_ciudad_tiempo)
    fullinfo2= adi.deboneIds(fullinfo2)["elements"]
    
    fullinfo2_1= lt.newList("ARRAY_LIST")
    for dict in fullinfo2:
        lt.addLast(fullinfo2_1, dict)
    
    lista_organizada_todo= (merg.sort(fullinfo2_1, Compare_fecha_nombre))["elements"]
    
    #Sacar informacion de lista sorteada
    ofertas_sorted= lt.newList("ARRAY_LIST")
    for oferta in lista_organizada_todo:
        oferta_info= {"Fecha": oferta["published_at"],
                      "Titulo": oferta["title"],
                      "Nombre_empresa_oferta": oferta["company_name"],
                      "Tipo_lugar": oferta["workplace_type"],
                      "Tamaño_empresa": oferta["company_size"] 
        }
        lt.addLast(ofertas_sorted, oferta_info)
    
    tupla_max= empresa_max, empresas_dict[empresa_max]
    tupla_min= empresa_min, empresas_dict[empresa_min]
    
    return total_ciudad, total_empresas, tupla_max, tupla_min, ofertas_sorted["elements"]


def req_6(catalog, exp, year, N):
    start = time.time()*1000
    #* EdgeCases
    if exp != 'indiferente':
        #* 1) Debemos sacar todos los IDs correspondientes al nivel de experiencia ~(1/3 N)
        expMap = catalog['experience_level']
        byExp = mp.get(expMap, exp) # Acceder al mapa
        byExp = byExp['value'] # (Esto es una ARRAY_LIST con todos los IDs)
    elif exp == 'indiferente':
        byExp = mp.valueSet(expMap)
    ##* Ahora debemos acceder a los elementos del año indicado.
    datemap = catalog['published_at']
    keysByYear = adi.getKeysByYear(datemap, year)
    IdsByYear = lt.newList("ARRAY_LIST")
    for key in lt.iterator(keysByYear):
        # Acá tenemos que sacar los IDs asociados a la llave y ver si también pertenecen a el nivel
        InternalIds = mp.get(datemap, key)
        InternalIds = InternalIds['value']
        for idi in lt.iterator(InternalIds):
            lt.addLast(IdsByYear, idi)
    meetsCriterias = adi.getIdentical(byExp, IdsByYear) # Usamos la función para encontrar similares
    ##* Hasta acá el tiempo es aceptable ~6s Listokas, ya sacamos los comunes que tienen la experiencia Y el año.

    ##* Ahora vamos a pedirle a Jobs que nos dé la lista con todo. Ya es una lista N/k dónde k>N<<0
    jobsMap = catalog['jobs']
    jobsCrit = adi.getFullInfos(jobsMap, meetsCriterias)
    jobsCrit = adi.deboneIds(jobsCrit) # listo tenemos una lista con [{Att1: Ans1, Att2: Ans2, Att3, Ans3, ...}, {Att1: Ans1, Att2: Ans2, Att3, Ans3, ...}]
    ## TODO Sacar stats de conteo según requiere basado en buscar esos IDs en JObs 
    cityCount = adi.ContadorMapasNOList(jobsCrit, 'city')
    companyCount = adi.ContadorMapasNOList(jobsCrit, 'company_name')
    #*Total de ciudades
    cityTotal = mp.size(cityCount)
    #* Total de empresas
    compTotal = mp.size(companyCount)
    #* Total de ofertas
    totalOffers = lt.size(jobsCrit)
    ##* Ciudad con mayor cantidad de ofertas y su conteo
    maxCity = adi.getMapStats(cityCount, 'max')
    maxCityName = maxCity['key']
    maxCityCount= maxCity['value']
    ##* Ciudad con menor cantidad de ofertas y su conteo
    minCity = adi.getMapStats(cityCount, 'min')
    minCityName = minCity['key']
    minCityCount= minCity['value']
    ##* Jodidísimo, sacar promedios de ciudad
    # Clasificar las N ciudades con mayor cantidad de ofertas de trabajo
    NCities = adi.sortC_MapValues(cityCount, N)
    # Hacer un mapa con las 20 ciudades
    # Sacar una versión reducida de Jobs para sólo las que contengan las ciudadesN
    #Preludio: Hacer un mapa conNcities
    NCitiesMap = mp.newMap(numelements= (lt.size(NCities)),
                        maptype='PROBING',
                        loadfactor=0.5)
    for dic in lt.iterator(NCities):
        Dkey = list(dic.keys())
        Dvalue = list(dic.values())
        Dkey, Dvalue = Dkey[0], Dvalue[0]
        mp.put(NCitiesMap, Dkey, Dvalue)
    
    reducedJobs = lt.newList('ARRAY_LIST')
    for job in lt.iterator(jobsCrit):
        #Para cada dic dentro de jobsCrit
        if mp.contains(NCitiesMap, job['city']):
            lt.addLast(reducedJobs, job)
    
    CityAvrg = mp.newMap(numelements= (lt.size(NCities)),
                        maptype='PROBING',
                        loadfactor=0.5)
    moneyFromMap = mp.newMap(numelements= (lt.size(NCities)),
                    maptype='PROBING',
                    loadfactor=0.5)
    moneyToMap =  mp.newMap(numelements= (lt.size(NCities)),
                    maptype='PROBING',
                    loadfactor=0.5)
    for dic in lt.iterator(NCities):
        Dkey = list(dic.keys())
        Dvalue = list(dic.values())
        Dkey, Dvalue = Dkey[0], Dvalue[0]
        for job in lt.iterator(reducedJobs):
            if job['city'] == Dkey:
                if type(job['salary_from']) == list:
                    existsMFM = mp.contains(moneyFromMap, Dkey)
                    if existsMFM:
                        entry = mp.get(moneyFromMap, Dkey)
                        dato = me.getValue(entry)
                    else:
                        datoF = lt.newList("ARRAY_LIST")
                        for salaryyy in job['salary_from']:
                            lt.addLast(datoF, salaryyy)
                        
                    existsMTM = mp.contains(moneyToMap, Dkey)
                    if existsMTM:
                        entry = mp.get(moneyToMap, Dkey)
                        dato = me.getValue(entry)
                    else:
                        datoT = lt.newList("ARRAY_LIST")
                        for salaryyy in job['salary_to']:
                            lt.addLast(datoT, salaryyy)
                else:
                    existsMFM = mp.contains(moneyFromMap, Dkey)
                    if existsMFM:
                        entry = mp.get(moneyFromMap, Dkey)
                        datoF = me.getValue(entry)
                    else:
                        datoF = lt.newList("ARRAY_LIST")
                        lt.addLast(datoF, job['salary_from'])
                        
                    existsMTM = mp.contains(moneyToMap, Dkey)
                    if existsMTM:
                        entry = mp.get(moneyToMap, Dkey)
                        datoT = me.getValue(entry)
                    else:
                        datoT = lt.newList("ARRAY_LIST")
                        lt.addLast(datoT, job['salary_to'])
                    
                mp.put(moneyFromMap, Dkey, datoF)
                mp.put(moneyToMap, Dkey, datoT)
    
    #? Tiempo hasta acá (en el maquinón) 8.4 s
    # Sacando promedios y metiendolos al mapa CityAvrg
    # Primero promediemos listas internas
    def getArrLiAvrg(Arrli): 
        lstpy = Arrli['elements']
        if lt.size(Arrli) == 1:
            try:
                prom = int(lstpy[0])
            except:
                prom = 0
            return prom
        elif lt.size(Arrli) > 1:
            try:
                canti = int(lt.size(Arrli))
                suma = 0
                for element in lstpy:
                    element = int(element)
                    suma = suma + element
                prom = int(suma/canti)
                return prom
            except:
                prom = 0
                return prom

    moneyFromMapKeys = mp.keySet(moneyFromMap)
    for key in lt.iterator(moneyFromMapKeys):
        val = mp.get(moneyFromMap, key)
        val = val['value']
        if len(val) > 1:
            avrg = getArrLiAvrg(val)
            # Actualizar el valor
            mp.remove(moneyFromMap, key)
            mp.put(moneyFromMap, key, avrg)

    moneyToMapkeys = mp.keySet(moneyToMap)
    for key in lt.iterator(moneyToMapkeys):
        val = mp.get(moneyToMap, key)
        val = val['value']
        if len(val) > 1:
            avrg = getArrLiAvrg(val)
            # Actualizar el valor
            mp.remove(moneyToMap, key)
            mp.put(moneyToMap, key, avrg)
            
    #* Sacar promedio total promTot = (from+to)/2
    for dic in lt.iterator(NCities):
        Dkey = list(dic.keys())
        Dvalue = list(dic.values())
        Dkey, Dvalue = Dkey[0], Dvalue[0]
        
        fromValue = mp.get(moneyFromMap, Dkey)
        toValue = mp.get(moneyToMap, Dkey)
        fromValue, toValue = fromValue['value'], toValue['value']
        
        finalAverage = (int(fromValue) + int(toValue)) / 2
        
        mp.put(CityAvrg, Dkey, finalAverage)
        
        # Listo, ya tenemos todos los promedios    
                    
    #* Done Sacar promedios dados los dos mapas anteriores.
    #* Return: City, Country, TotalOffers, AvrgSalary, NumberOfCompanies, CompanyMostOffers, BestOffer, WorstOffer, 
    GreatreturnList = lt.newList('ARRAY_LIST') ##! Estas fueron medidas de ultimo recurso
    ReturnMap = mp.newMap(numelements= (lt.size(NCities)),
                        maptype='PROBING',
                        loadfactor=0.5)
    ReturnFinal = mp.newMap(numelements= (lt.size(NCities)),
                        maptype='PROBING',
                        loadfactor=0.5)
    ReturnFinal = mp.newMap(numelements= (lt.size(NCities)),
                        maptype='PROBING',
                        loadfactor=0.5)
    #Inicializar. Meter llaves y valor acá
    eDic = {}##! Estas fueron medidas de ultimo recurso
    for city in lt.iterator(NCities):
        for i in city:
            city = list(city.keys())
            city = str(city[0])
            

            Dkey = list(dic.keys())
            Dkey = Dkey[0]
            exists = mp.contains(ReturnMap, i)
            mp.put(ReturnMap, i, {'City': i})
            eDic['city'] = str(city)
        
    for city in lt.iterator(mp.keySet(ReturnMap)):
        eDic['city'] = str(city)
        # Acceder al Nuevo Dic
        Dic = mp.get(ReturnMap, city)
        Dic = Dic['value']
        # Sacar el pais de la ciudad (a lo fuerza bruta, fuckit)
        for job in lt.iterator(reducedJobs):
            furtherReducedJobs = lt.newList('ARRAY_LIST')
            if job['city'] == city:
                country = job['country_code']
                lt.addLast(furtherReducedJobs, job)
        #*Aprovechando el loop para sacar los conteos de Jobs NumberOfCompanies, CompanyMostOffers
        CitycompanyCount = adi.ContadorMapasNOList(furtherReducedJobs, 'company_name')
        numberOfCompanies = lt.size(mp.keySet(CitycompanyCount))
        CompanyMostOffers = adi.getMapStats(CitycompanyCount, 'max')

        #*Aprovechando el loop para sacar los conteos de  BestOffer, WorstOffer
        try:
            KCompanyMostOffers = CompanyMostOffers['key']
            VCompanyMostOffers = CompanyMostOffers['value']
            bestSalaryCounter = adi.ContadorMapasNOList(furtherReducedJobs, 'salary_to')
            bestSalaryValue = adi.getMapStats(bestSalaryCounter, 'max')
            WorstSalaryCounter = adi.ContadorMapasNOList(furtherReducedJobs, 'salary_from')
            WorstSalaryValue = adi.getMapStats(WorstSalaryCounter, 'min')
        except:
            KCompanyMostOffers = None
            VCompanyMostOffers = None
            bestSalaryValue = 0
            WorstSalaryValue = 0
        dic['country_code'] = country
        eDic['country_code'] = country
        # Aprovechando que estamos en el loop, saquemos la info que está en otros mapas y metámosla de una
        # Total de ofertas (conteo)
        CitytotalOffers = mp.get(NCitiesMap, city)
        CitytotalOffers = CitytotalOffers['value']
        dic['Total_offers'] = CitytotalOffers
        eDic['Total_offers'] = CitytotalOffers
        # Salario promedio
        AvrgSalary = mp.get(CityAvrg, city)
        AvrgSalary = AvrgSalary['value']
        dic['Average_salary'] = AvrgSalary
        eDic['Average_salary'] = AvrgSalary

    #* Dar los valores previamente asignados de NumberOfCompanies, CompanyMostOffers
        dic['NumberOfCo'] = int(numberOfCompanies)
        eDic['NumberOfCo'] = int(numberOfCompanies)
        dic['MostOffersCo'] = (KCompanyMostOffers, VCompanyMostOffers)
        eDic['MostOffersCo']  = (KCompanyMostOffers, VCompanyMostOffers)
    #* , BestOffer, WorstOffer
    # Livin'on a prayer de Bon Jovi por que puede que sí cómo puede que nó. Faltaron Mapas ya que.
    # Sacar el salario mejory peor de la ciudad (a lo fuerza bruta, fuckit)
        for job in lt.iterator(reducedJobs):
            fullInfoWorst, fullInfobest = None, None
            furtherReducedJobs = lt.newList('ARRAY_LIST')
            if job['salary_from'] == WorstSalaryValue:
                fullInfoWorst = job
            if job['salary_to'] == bestSalaryValue:
                fullInfobest = job

        # Meterle esos últimos dos datos:
        dic['Best_Offer'] = fullInfobest
        eDic['Best_Offer']  = fullInfobest
        dic['Worst_Offer'] = fullInfoWorst
        eDic['Worst_Offer']  = fullInfoWorst
        lt.addLast(GreatreturnList, dic)
        finalEdic = dict(eDic)
        mp.put(ReturnFinal, city, finalEdic)
    end = time.time()*1000
    delta = start - end
    print("DeltaTime" + str(delta))
    
    # Retornazo:
    #! Ojo, toca en controller sacar una lista de todo lo del return Map, luego DEbone, luego pasar a view para Tabulate
    return cityTotal, compTotal, totalOffers, maxCityName, maxCityCount, minCityName, minCityCount, GreatreturnList



def req_7(control, numeroPaises, año, mes):
    """
    Función que soluciona el requerimiento 7
    """    
    
    moal2=control["jobs"]
    #filtrar por fecha
    fecha=año+"-"+mes
    mapa_date=control["published_at"]
    lista_fechas = mp.keySet(mapa_date)
    # IDsSWD = datos Shorten With Date
    IDsSWD=lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(lista_fechas):
        if i[0:7]==fecha:
            IDs=mp.get(mapa_date,i)
            lt.addLast(IDsSWD,IDs["value"])
    # sacar elemento de moal2 con IDsSWD
    # values = valores Shorten With Date
    valuesSWD=lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(IDsSWD):
        for j in lt.iterator(i):
            dato = mp.get(moal2,j)
            lt.addLast(valuesSWD,dato["value"][j])
    
    #Organizar la lista IDsSWD
    valuesSWD=DateSort(valuesSWD)
    
    # Solo dejar los que tengan los paises pedidos
    #MAcountriesCount = Max Amount of countries Count
    MAcountriesCount = mp.newMap(numelements=3,maptype="PROBING",loadfactor=0.5)
    for i in lt.iterator(valuesSWD):
        i=i["country_code"]
        existcountry = mp.contains(MAcountriesCount,i)
        if existcountry:
            entry = mp.get(MAcountriesCount,i)
            pais = me.getValue(entry)
        else:
            pais = 0
        pais = pais + 1
        mp.put(MAcountriesCount,i,pais)
    
    listcountries=mp.keySet(MAcountriesCount)
    # MAcountries = Max Amount of countries
    MAcountries = lt.newList(datastructure="ARRAY_LIST")
    listMAcountriesCount = lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(listcountries):
        dato=mp.get(MAcountriesCount,i)
        lt.addLast(listMAcountriesCount,dato)
    
    merg.sort(listMAcountriesCount,CompareValuesMapTuple)
    
    for i in lt.iterator(listMAcountriesCount):
        key=mp.get(MAcountriesCount,i["key"])["key"]
        present = lt.isPresent(MAcountries,key)
        if lt.size(MAcountries) == numeroPaises:
            break
        elif present == 0:
            lt.addLast(MAcountries,key)   
    
    #valuesFbCs = values Filtered by Countries
    valuesFbCs = lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(valuesSWD):
        for j in lt.iterator(MAcountries):
            icountry=i["country_code"]
            if icountry == j:
                lt.addLast(valuesFbCs,i)
    
    #* total de ofertas
    NUMofertas=lt.size(valuesFbCs)
    
    #* Número ciudades donde se ofertó en los países resultantes
    #CitiesCount = número de ofertas por ciudad
    CitiesCount = mp.newMap(numelements=11,maptype="PROBING",loadfactor=0.5)
    for i in lt.iterator(valuesFbCs):
        city = i["city"]
        existcity = mp.contains(CitiesCount,city)
        if existcity:
            entry = mp.get(CitiesCount, city)
            ciudad = me.getValue(entry)
        else:
            ciudad = 0
        ciudad = ciudad + 1
        mp.put(CitiesCount,city,ciudad)
    
    NUMofertasCities=mp.size(CitiesCount)
    
    listCities=mp.keySet(CitiesCount) 
    listCitiesCount = lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(listCities):
        dato=mp.get(CitiesCount,i)
        lt.addLast(listCitiesCount,dato)
    
    merg.sort(listCitiesCount,CompareValuesMapTuple) 
    
    MAcities = lt.getElement(listCitiesCount,1)
    
    #* País con mayor cantidad de ofertas
    MAXNUMofertasCountry = lt.getElement(listMAcountriesCount,1)
    for i in lt.iterator(listMAcountriesCount):
        value=i["value"]
        if MAXNUMofertasCountry["value"]<value:
            MAXNUMofertasCountry=i
        
    
    juniorinfo= manejoinfoExperience(valuesFbCs,"junior")
    middleinfo= manejoinfoExperience(valuesFbCs,"mid")
    seniorinfo= manejoinfoExperience(valuesFbCs,"senior")
    
    """valuesFbCs = todos los elements"""
    return  NUMofertas, MAXNUMofertasCountry, MAcities, NUMofertasCities, juniorinfo, middleinfo, seniorinfo, valuesFbCs


def manejoinfoExperience(datos,tipoexperticia):
    listdatosreducida=lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(datos):
        dato=i["experience_level"]
        if dato == tipoexperticia:
            lt.addLast(listdatosreducida,i)
    
    Habilidadpromedio = lt.newList(datastructure="ARRAY_LIST")
    HabilidadCount = mp.newMap(numelements=11,maptype="PROBING",loadfactor=0.5)
    for i in lt.iterator(listdatosreducida):
        hab = i["short_name"]
        hab_num = i["skill"]
        suma=0
        for j in range(0,len(hab)):
            habil=hab[j]
            habil_num=int(hab_num[j])
            existhab = mp.contains(HabilidadCount,habil)
            if existhab:
                entry = mp.get(HabilidadCount,habil)
                habilidad = me.getValue(entry)
            else:
                habilidad = 0
            habilidad = habilidad + 1
            mp.put(HabilidadCount,habil,habilidad)
            suma=suma+ habil_num
        promedio=suma/len(hab)
        lt.addLast(Habilidadpromedio,round(promedio,3))
    
    #! ARREGLAR
    #merg.sort(HabilidadCount,CompareKeysMapTuple)
    #! ARREGLAR
    
    CompanyCount = ContadorMapasNOList(listdatosreducida,"company_name")
    SedesCount = mp.newMap(numelements=11,maptype="PROBING",loadfactor=0.5)
    for i in lt.iterator(listdatosreducida):
        sublist = i["company_name"]
        existdato = mp.contains(SedesCount,sublist)
        if existdato:
            entry = mp.get(SedesCount, sublist)
            dato = me.getValue(entry)
        else:
            dato = lt.newList("ARRAY_LIST")
        lt.addLast(dato,i["street"])
        mp.put(SedesCount,sublist,dato)
    keyssedescount=mp.keySet(SedesCount)
    CountCompanyplussede=lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(keyssedescount):
        dato=mp.get(SedesCount,i)
        if lt.size(dato["value"]) > 1:
            lt.addLast(CountCompanyplussede,dato)
        
    sizehabilidades=mp.size(HabilidadCount)
    keyhabilidades=mp.keySet(HabilidadCount)
    maxhabilidad=mp.get(HabilidadCount,lt.getElement(keyhabilidades,1))
    minhabilidad=mp.get(HabilidadCount,lt.getElement(keyhabilidades,1))
    for i in lt.iterator(keyhabilidades):
        dato= mp.get(HabilidadCount,i)
        if dato["value"]>maxhabilidad["value"]:
            maxhabilidad=dato
        if dato["value"]<minhabilidad["value"]:
            minhabilidad=dato
    sizecompanies=mp.size(CompanyCount)
    keycompanies=mp.keySet(CompanyCount)
    maxcompany=mp.get(CompanyCount,lt.getElement(keycompanies,1))
    mincompany=mp.get(CompanyCount,lt.getElement(keycompanies,1))
    for i in lt.iterator(keycompanies):
        dato= mp.get(CompanyCount,i)
        if dato["value"]>maxcompany["value"]:
            maxcompany=dato
        if dato["value"]<mincompany["value"]:
            mincompany=dato
    sizesedes=0
    keyssedes=mp.keySet(SedesCount)
    for i in lt.iterator(keyssedes):
        dato=mp.get(SedesCount,i)
        if lt.size(dato["value"])>1:
            sizesedes=sizesedes+1
    return sizehabilidades, maxhabilidad, minhabilidad, min(HabilidadCount), sizecompanies, maxcompany, mincompany, sizesedes
    
def ContadorMapasNOList(lista,llave:str):
    Mapcontador = mp.newMap(numelements=11,maptype="PROBING",loadfactor=0.5)
    for i in lt.iterator(lista):
        sublist = i[llave]
        existdato = mp.contains(Mapcontador,sublist)
        if existdato:
            entry = mp.get(Mapcontador, sublist)
            dato = me.getValue(entry)
        else:
            dato = 0
        dato = dato + 1
        mp.put(Mapcontador,sublist,dato)
    return Mapcontador

def ContadorMapasList(lista,llave:str):
    Mapcontador = mp.newMap(numelements=11,maptype="PROBING",loadfactor=0.5)
    for i in lt.iterator(lista):
        sublist = i[llave]
        for j in range(0,len(sublist)):
            subsublist=sublist[j]
            existdato = mp.contains(Mapcontador,subsublist)
            if existdato:
                entry = mp.get(Mapcontador,subsublist)
                dato = me.getValue(entry)
            else:
                dato = 0
            dato = dato + 1
            mp.put(Mapcontador,subsublist,dato)
    return Mapcontador

def req_8(control,Nivel_experticia,Divisa,Ffirst,Flast):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    mapaexperience = control["experience_level"]
    moal2 = control["jobs"]
    # IDsSWEx = Ids Shorten With Experience
    IDsSWEx = lt.newList(datastructure="ARRAY_LIST")
    if Nivel_experticia != "indiferente":
        experience=mp.get(mapaexperience,Nivel_experticia)["value"]
        lt.addLast(IDsSWEx,experience)
    else:
        junior = mp.get(mapaexperience,"junior")["value"]
        mid = mp.get(mapaexperience,"mid")["value"]
        senior = mp.get(mapaexperience,"senior")["value"]
        lt.addLast(IDsSWEx,junior)
        lt.addLast(IDsSWEx,mid)
        lt.addLast(IDsSWEx,senior)
    valuesSWEx = lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(IDsSWEx):
        for j in lt.iterator(i):
            dato = mp.get(moal2,j)
            lt.addLast(valuesSWEx,dato["value"][j])
    DateSort(valuesSWEx)
    valuesSWExANDDate = lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(valuesSWEx):
        fecha=i["published_at"][0:10]
        if Ffirst <= fecha and fecha <= Flast:
            lt.addLast(valuesSWExANDDate,i)
    
    valuesSWExANDDateANDCurrency=lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(valuesSWExANDDate):
        currency=i["currency_salary"]
        salary_from=i["salary_from"]
        salary_to=i["salary_to"]
        keepcurren=[]
        keepsalaryf=[]
        keepsalaryt=[]
        for j in range(0,len(currency)):
            if currency[j] == Divisa:
                keepcurren.append(currency[j])
                keepsalaryf.append(salary_from[j])
                keepsalaryt.append(salary_to[j])
        if Divisa in keepcurren:
            i["currency_salary"]=keepcurren
            i["salary_from"]=keepsalaryf
            i["salary_to"]=keepsalaryt
            lt.addLast(valuesSWExANDDateANDCurrency,i)
    
    empresas = ContadorMapasNOList(valuesSWExANDDateANDCurrency,"company_name")
    NUMempresas = mp.size(empresas)
    NUMofertas = lt.size(valuesSWExANDDateANDCurrency)
    paises = ContadorMapasNOList(valuesSWExANDDateANDCurrency,"country_code")
    NUMpaises = mp.size(paises)
    ciudades = ContadorMapasNOList(valuesSWExANDDateANDCurrency,"city")
    NUMciudades = mp.size(ciudades)
    currency = ContadorMapasList(valuesSWExANDDateANDCurrency,"currency_salary")
    keyscurrency = mp.keySet(currency)
    #NUMcurrency = mp.get(lt.getElement(keyscurrency,1))["value"]
    salaryfrom = ContadorMapasList(valuesSWExANDDateANDCurrency,"salary_from")
    salaryto = ContadorMapasList(valuesSWExANDDateANDCurrency,"salary_to")
    
    valuesSWExANDDateANDCurrency
    return NUMempresas, NUMofertas, NUMpaises, NUMciudades