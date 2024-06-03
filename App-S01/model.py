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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def nuevo_catalogo(tipo, alfa, tamano):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalogo={'jobs_list':None,
              'skills_list':None,
              'employments_list':None,
              'multilocations_list':None,
              'jobs':None,
              'skills':None,
              'employments':None,
              'multilocations':None,
              'paises':None,
              'empresas':None,
              'ciudades':None}

    if tamano == "10-por-":
        tamano_jobs = 34470
        tamano_skills = 96865
        tamano_employments = 43846
        tamano_multilocations = 80692
    elif tamano == "20-por-":
        tamano_jobs = 67100
        tamano_skills = 189073
        tamano_employments = 856617
        tamano_multilocations = 127300
    elif tamano == "30-por-":
        tamano_jobs = 103710
        tamano_skills = 293557
        tamano_employments = 132296
        tamano_multilocations = 164326
    elif tamano == "40-por-":
        tamano_jobs = 137874
        tamano_skills = 391054
        tamano_employments = 176280
        tamano_multilocations = 197720
    elif tamano == "50-por-":
        tamano_jobs = 167990
        tamano_skills = 476730
        tamano_employments = 214713
        tamano_multilocations = 226984
    elif tamano == "60-por-":
        tamano_jobs = 187521
        tamano_skills = 532004
        tamano_employments = 239775
        tamano_multilocations = 244228
    elif tamano == "70-por-":
        tamano_jobs = 193695
        tamano_skills = 549515
        tamano_employments = 247479
        tamano_multilocations = 246181
    elif tamano == "80-por-":
        tamano_jobs = 198120
        tamano_skills = 561992
        tamano_employments = 253082
        tamano_multilocations = 246241
    elif tamano == "90-por-":
        tamano_jobs = 201174
        tamano_skills = 570503
        tamano_employments = 256915
        tamano_multilocations = 245159
    elif tamano == "large-":
        tamano_jobs = 203563
        tamano_skills = 577165
        tamano_employments = 259837
        tamano_multilocations = 244937
    elif tamano == "medium-":
        tamano_jobs = 191568
        tamano_skills = 543484
        tamano_employments = 244829
        tamano_multilocations = 245726
    elif tamano == "small-":
        tamano_jobs = 114710
        tamano_skills = 324760
        tamano_employments = 146449
        tamano_multilocations = 175111
    catalogo['jobs_list']=lt.newList('ARRAY_LIST')
    catalogo['skills_list']=lt.newList('ARRAY_LIST')
    catalogo['employments_list']=lt.newList('ARRAY_LIST')
    catalogo['multilocations_list']=lt.newList('ARRAY_LIST')    
    catalogo['jobs']=mp.newMap(tamano_jobs,maptype=tipo, loadfactor=alfa)
    catalogo['skills']=mp.newMap(tamano_skills, maptype='CHAINING', loadfactor=1.5)
    catalogo['employments']=mp.newMap(tamano_employments, maptype='PROBING', loadfactor=0.5)
    catalogo['multilocations']=mp.newMap(tamano_multilocations, maptype='CHAINING', loadfactor=1.5)
    catalogo['paises']=mp.newMap(maptype='CHAINING', loadfactor=1.5)
    catalogo['empresas']=mp.newMap(maptype='CHAINING',loadfactor=1.5)
    catalogo['ciudades']=mp.newMap(maptype='CHAINING',loadfactor=1.5)
    catalogo["anios"]=mp.newMap(maptype='CHAINING',loadfactor=1.5)
    catalogo["anio_mes"]=mp.newMap(maptype='CHAINING',loadfactor=1.5)
    catalogo["experiencia"]=mp.newMap(maptype='CHAINING',loadfactor=1.5)
    catalogo["locaciones"]=mp.newMap(maptype='CHAINING',loadfactor=1.5)
    
    
    return catalogo

# Funciones para agregar informacion al modelo




def add_job (data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Para añadir trabajos por ID
    key= data['id']
    mp.put(data_structs['jobs'],key,data)
    lt.addLast(data_structs['jobs_list'], data)
    #Para añadir trabajos por país
    
    key_pais=data['country_code']
    pais=mp.get(data_structs['paises'], key_pais)
    if pais:
        pais=me.getValue(pais)
    else:
        pais=new_entry_list(key_pais)
        mp.put(data_structs['paises'],key_pais, pais)
    lt.addLast(pais, data)
    
    key_empresa=data['company_name']
    empresa=mp.get(data_structs['empresas'],key_empresa)
    if empresa:
        empresa=me.getValue(empresa)
    else:
        empresa=new_entry_list(key_empresa)
        mp.put(data_structs['empresas'],key_empresa,empresa)
    lt.addLast(empresa,data)
    
    key_ciudad=data['city']
    ciudad=mp.get(data_structs['ciudades'],key_ciudad)
    if ciudad:
        ciudad=me.getValue(ciudad)
    else:
        ciudad=new_entry_list(key_ciudad)
        mp.put(data_structs['ciudades'],key_ciudad,ciudad)
    lt.addLast(ciudad,data)
    
    key_exp=data['experience_level']
    key_anio_exp=data["published_at"][0:4]
    exp=mp.get(data_structs['experiencia'], key_exp)
    if exp:
        exp=me.getValue(exp)
        anio_exp=mp.get(exp, key_anio_exp)
        if anio_exp:
            anio_exp=me.getValue(anio_exp)
        else:
            anio_exp=new_entry_list(key_anio_exp)
            mp.put(exp, key_anio_exp, anio_exp)
    else:
        exp=mp.newMap()
        mp.put(data_structs['experiencia'],key_exp, exp)
        anio_exp=mp.get(exp, key_anio_exp)
        if anio_exp:
            anio_exp=me.getValue(anio_exp)
        else:
            anio_exp=new_entry_list(key_anio_exp)
            mp.put(exp, key_anio_exp, anio_exp)
    
    lt.addLast(anio_exp, data)
    
    key_anios=data['published_at'][0:4]
    anio=mp.get(data_structs['anios'], key_anios)
    if anio:
        anio=me.getValue(anio)
    else:
        anio=new_entry_list(key_anios)
        mp.put(data_structs['anios'],key_anios, anio)
    lt.addLast(anio, data)
    
    #=====================REQ7=================================
    key_anio_mes=data["published_at"][0:7]
    key_pais=data['country_code']
    anio_mes=mp.get(data_structs['anio_mes'], key_anio_mes)
    if anio_mes:
        anio_mes=me.getValue(anio_mes)
        pais=mp.get(anio_mes, key_pais)
        if pais:
            pais=me.getValue(pais)
        else:
            pais=new_entry_list(key_pais)
            mp.put(anio_mes, key_pais, pais)
    else:
        anio_mes=mp.newMap()
        mp.put(data_structs['anio_mes'],key_anio_mes, anio_mes)
        pais=mp.get(anio_mes, key_pais)
        if pais:
            pais=me.getValue(pais)
        else:
            pais=new_entry_list(pais)
            mp.put(anio_mes, key_pais, pais)
            
    lt.addLast(pais, data)
    
    return data_structs

def add_skill(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Añade skills por ID.
    id=data['id']
    trabajo=mp.get(data_structs['skills'], id)
    if trabajo:
        trabajo=me.getValue(trabajo)
    else:
        trabajo=new_entry_list(id)
        mp.put(data_structs['skills'],id, trabajo)
    lt.addLast(trabajo, data)
    lt.addLast(data_structs['skills_list'], data)
    
    
    return data_structs

    
    
        

def add_employment(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Añade empleos por ID
    key= data['id']
    mp.put(data_structs['employments'],key,data)
    lt.addLast(data_structs['employments_list'], data)
    
    
    return data_structs

def add_multilocation(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #Añade multilocaciones por ID.
    id=data['id']
    multilocation=mp.get(data_structs['multilocations'], id)
    if multilocation:
        multilocation=me.getValue(multilocation)
    else:
        multilocation=new_entry_list(id)
        mp.put(data_structs['multilocations'],id, multilocation)
    lt.addLast(multilocation, data)
    lt.addLast(data_structs['multilocations_list'], id)
    
    
    key_ids=data['id']
    loca=mp.get(data_structs['locaciones'], key_ids)
    if loca:
        loca=me.getValue(loca)
    else:
        loca=new_entry_list(key_ids)
        mp.put(data_structs['locaciones'],key_ids, loca)
    lt.addLast(loca, data)
    
    return data_structs

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def new_entry_list(id):
    id=lt.newList('ARRAY_LIST')
    return id
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pareja_trabajo=mp.get(data_structs['jobs'], id)
    pareja_skill=mp.get(data_structs['skills'], id)
    pareja_employment=mp.get(data_structs['employments'], id)
    pareja_multi=mp.get(data_structs['multilocations'], id)
    return me.getValue(pareja_trabajo), me.getValue(pareja_skill), me.getValue(pareja_employment), me.getValue(pareja_multi)


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, n, pais, exp):
    """
    Función que soluciona el requerimiento 1
    """
    paises=mp.get(data_structs['paises'], pais)
    lista_ofertas=me.getValue(paises)
    tamanio_pais=lt.size(lista_ofertas)
    filtrados=lt.newList('ARRAY_LIST')
    for oferta in lt.iterator(lista_ofertas):
        if oferta['experience_level']==exp:
            lt.addLast(filtrados, oferta)
    tamanio_exp=lt.size(filtrados)
    filtrados=sa.sort(filtrados, fecha)
    if lt.size(filtrados)==0:
        return None
    elif lt.size(filtrados)>n:
        return lt.subList(filtrados, 1, n), tamanio_pais, tamanio_exp
    else:
        return filtrados, tamanio_pais, tamanio_exp


def req_2(data_structs,empresa,ciudad,n):
    """
    Función que soluciona el requerimiento 2
    """
    
    empresa_seleccionada=mp.get(data_structs['empresas'],empresa)
    lista_ofertas=me.getValue(empresa_seleccionada)
    empresa_y_ciudad = lt.newList("ARRAY_LIST")
    for oferta in lt.iterator(lista_ofertas):
        if oferta["city"] == ciudad:
            lt.addLast(empresa_y_ciudad, oferta)
    if lt.size(empresa_y_ciudad)==0:
        return None
    elif lt.size(empresa_y_ciudad)<n:
        tamanio_ofertas_empresa_ciudad=lt.size(empresa_y_ciudad)
        return (tamanio_ofertas_empresa_ciudad,sa.sort(empresa_y_ciudad, fecha))
    else:
        sublista=lt.subList(empresa_y_ciudad,lt.size(empresa_y_ciudad)-n,n)
        tamanio_ofertas_empresa_ciudad=lt.size(empresa_y_ciudad)
        return (tamanio_ofertas_empresa_ciudad,sa.sort(sublista, fecha))
    


def req_3(data_structs, nombre, inicio, f_final):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    n_ofertas = 0
    junior = 0
    mid = 0
    senior = 0 
    trabajos=mp.get(data_structs['empresas'], nombre)
    lista= me.getValue(trabajos)
    final=lt.newList("ARRAY_LIST")
    for t in lt.iterator(lista):
        fecha_oferta=t["published_at"][:10]
        if fecha_oferta>=inicio and fecha_oferta<=f_final:
            n_ofertas += 1
            if t["experience_level"] == "junior":
                junior += 1
            if t["experience_level"] == "mid":
                mid += 1
            if t["experience_level"] == "senior":
                senior += 1
            diccionario = {"fecha de la oferta": t['published_at'][:10], "titulo de la oferta": t["company_name"], "nivel de experiencia requerido": t["experience_level"], "ciudad de la empresa": t["city"], "pais de la empresa": t["country_code"], "tamaño de la empresa": t["company_size"], "tipo de lugar de trabajo": t["workplace_type"], "disponibilidad de ucranianos": t["open_to_hire_ukrainians"]}
            lt.addLast(final, diccionario)
            
    return n_ofertas, junior, mid, senior, final
    

def req_4(data_structs,pais,fecha_inicio,fecha_fin):
    """
    Función que soluciona el requerimiento 4
    """
    empresas=lt.newList()
    ciudades=mp.newMap()
    ofertas=mp.get(data_structs['paises'], pais)
    lista_ofertas=me.getValue(ofertas)
    filtrados=lt.newList('ARRAY_LIST')
    for oferta in lt.iterator(lista_ofertas):
        fecha_oferta=oferta['published_at'][:10]
        nombre_empresa=oferta['company_name']
        if fecha_fin>=fecha_oferta>=fecha_inicio:
            lt.addLast(filtrados, oferta)
            if lt.isPresent(empresas, nombre_empresa):
                pass
            else:
                lt.addLast(empresas, nombre_empresa)
            ciudad=oferta['city']
            lista_ciudades=mp.get(ciudades, ciudad)
            if lista_ciudades:
                lista_ciudades=me.getValue(lista_ciudades)
            else:
                lista_ciudades=new_entry_list(ciudad)
                mp.put(ciudades, ciudad, lista_ciudades)
            lt.addLast(lista_ciudades, oferta)       
    city_list=mp.keySet(ciudades)
    offers_list=mp.valueSet(ciudades)
    mayor_ciudad=(None, 0)
    menor_ciudad= (None, 100000000000)
    i=1
    for oferta in lt.iterator(offers_list):
        tamanio=lt.size(oferta)
        if tamanio>mayor_ciudad[1]:
            mayor_ciudad= (lt.getElement(city_list, i), tamanio)
        if tamanio<menor_ciudad[1]:
            menor_ciudad= (lt.getElement(city_list, i), tamanio)
        if tamanio==mayor_ciudad[1]:
            mayor_ciudad= (comparar_promedios_ciudad(data_structs, ciudades, mayor_ciudad[0], (lt.getElement(city_list, i))), tamanio)
        if tamanio==menor_ciudad[1]:
            menor_ciudad= (comparar_promedios_ciudad(data_structs, ciudades, menor_ciudad[0], (lt.getElement(city_list, i))), tamanio)
        i+=1
        
    return lt.size(filtrados), lt.size(empresas), mp.size(ciudades), mayor_ciudad, menor_ciudad, sa.sort(filtrados, fecha_empresa)


def req_5(data_structs,ciudad,fecha_inicio,fecha_fin):
    
    ofertas=mp.get(data_structs['ciudades'],ciudad)
    ofertas_ciudad=me.getValue(ofertas)
    filtrados=mp.newMap(maptype='PROBING',loadfactor=0.5)
    lista_ofertas_filtrados=lt.newList('ARRAY_LIST')
    totales_ofertas=0
    for oferta in lt.iterator(ofertas_ciudad):
        fecha_oferta=oferta['published_at'][:10]
        if (fecha_inicio<=fecha_oferta) and (fecha_oferta<=fecha_fin):
            totales_ofertas+=1
            lt.addLast(lista_ofertas_filtrados,oferta)
            if not mp.contains(filtrados,oferta['company_name']):
                mp.put(filtrados,oferta['company_name'],lt.newList('ARRAY_LIST'))
            empresa=mp.get(filtrados,oferta['company_name'])
            lt.addLast(me.getValue(empresa),oferta)
    total_empresas=mp.size(filtrados)
    
    menor=(None,1000000000000)
    mayor=(None,0)
    for empresa in lt.iterator(mp.keySet(filtrados)):
        lista_empresa = mp.get(filtrados, empresa)
        if lista_empresa is not None:
            num_ofertas = lt.size(me.getValue(lista_empresa))
            if menor is None or num_ofertas < menor[1]:
                menor = (empresa, num_ofertas)
            if mayor is None or num_ofertas > mayor[1]:
                mayor = (empresa, num_ofertas)
                
    if menor[1]==1000000000000:
        menor=(None,0)
    
        
    
    return totales_ofertas,total_empresas,mayor,menor,sa.sort(lista_ofertas_filtrados,fecha_empresa)
        



def req_6(data_structs,n, exp, anio):
    """
    Función que soluciona el requerimiento 6
    """
    rta=None
    if exp != "indiferente":
        mapa_exp_anios= data_structs["experiencia"]
        mapa_anios= me.getValue(mp.get(mapa_exp_anios, exp))
        if mp.get(mapa_anios, anio) == None:
            return rta
        lista_ofertas= me.getValue(mp.get(mapa_anios, anio))
        
    else:
        mapa=data_structs['anios']
        lista_ofertas= me.getValue(mp.get(mapa, anio))
        if lista_ofertas == None:
            return rta
    
    mapa_ciudades=mp.newMap()
    lista_empresas=lt.newList()
    for oferta in lt.iterator(lista_ofertas):
        key_ciudad=oferta['city']
        ciudad=mp.get(mapa_ciudades,key_ciudad)
        if ciudad:
            ciudad=me.getValue(ciudad)
        else:
            ciudad=new_entry_list(key_ciudad)
            mp.put(mapa_ciudades,key_ciudad,ciudad)
        lt.addLast(ciudad,oferta)
        if lt.isPresent(lista_empresas, oferta['company_name'])==0:
            lt.addLast(lista_empresas, oferta['company_name'])
            
    mapa_counter_ciudades= mp.newMap()
    llaves_ciudad= mp.keySet(mapa_ciudades)
    valores_ciudad= mp.valueSet(mapa_ciudades)
    i = 1
    for ciudad in lt.iterator(llaves_ciudad):
        size = lt.size(lt.getElement (valores_ciudad, i))
        promedio=promedio_por_ciudad(data_structs, mapa_ciudades, ciudad)
        mp.put(mapa_counter_ciudades, ciudad, (ciudad, size, promedio))
        i += 1
    lista_sorteada_ciudades=lt.newList()
    valores_ciudad_pre= mp.valueSet(mapa_counter_ciudades)
    sa.sort(valores_ciudad_pre, numero_ofertas)
    if lt.size(valores_ciudad_pre)==0:
        return None
    elif lt.size(valores_ciudad_pre)<n:
        lista_sorteada=valores_ciudad_pre
    else:
        lista_sorteada=lt.subList(valores_ciudad_pre, 1, n)
    i=1
    for city in lt.iterator(lista_sorteada):
        lista_ofertas_city=me.getValue(mp.get(mapa_ciudades, city[0]))
        pais=lt.getElement(lista_ofertas_city, 1)['country_code']
        total_empresas, mayor_empresa = calcular_empresas(mapa_ciudades, city[0])
        mejor_oferta , peor_oferta = calcular_mejor_peor_oferta(data_structs, mapa_ciudades, city[0])
        lt.addLast(lista_sorteada_ciudades, [city[0], pais, city[1], city[2], total_empresas, mayor_empresa, mejor_oferta, peor_oferta])

    numero_ciudades=lt.size(lista_sorteada)
    numero_empresas=lt.size(lista_empresas)
    mejor_ciudad=(lt.getElement(lista_sorteada, 1)[0], lt.getElement(lista_sorteada, 1)[1])
    menor_ciudad=(lt.getElement(lista_sorteada, numero_ciudades)[0], lt.getElement(lista_sorteada, numero_ciudades)[1])
    rta=(numero_ciudades, numero_empresas, lt.size(lista_ofertas), mejor_ciudad, menor_ciudad, lista_sorteada_ciudades)
    
    return rta


def req_7(data_structs,n_paises,anio_mes):
    """
    Función que soluciona el requerimiento 7
    """
    mapa=data_structs['anio_mes']
    mapa_exp= data_structs["skills"]
    lst_sedes=data_structs['multilocations_list']
    mayores_paises=mp.newMap(maptype='CHAINING',loadfactor=1.5)
    mapa_anio_mes_pais= me.getValue(mp.get(mapa, anio_mes))
    #####Tomamos varias estructuras que necesitaremos para las operaciones
    mapa_counter_pais= mp.newMap()
    llaves_pais= mp.keySet(mapa_anio_mes_pais)
    valores_pais= mp.valueSet(mapa_anio_mes_pais)
    #Se llena el mapa_counter_pais con el nombre del pais y su tamaño de ofertas
    i = 1
    for pais in lt.iterator(llaves_pais):
        size = lt.size(lt.getElement (valores_pais, i))
        mp.put(mapa_counter_pais, pais, (pais,size))
        i += 1
    #Se sortea y se toman las n ofertas con mayor numero de ofertas
    valores_pais_pre= mp.valueSet(mapa_counter_pais)
    sa.sort(valores_pais_pre, oferta_nombre_pais )
    lista_sorteada=lt.subList(valores_pais_pre, 1, n_paises)
    mayor_pais=lt.getElement(lista_sorteada,1)
    num_ofertas=0
    #Se itera sobre la lista sorteada para llenar el mapa mayores_paises y poder trabajar sobre las ofertas filtradas
    for pais in lt.iterator(lista_sorteada):
        num_ofertas+=pais[1]
        pais=pais[0]
        ofertas_fecha=mp.get(mapa_anio_mes_pais,pais)
        ofertas=me.getValue(ofertas_fecha)
        mp.put(mayores_paises,pais,ofertas)
    
    mayores_ciudades=mp.newMap()
    llaves_pais_mayores=mp.keySet(mayores_paises)
    #Se itera para sacar un mapa de ciudades y calcular la información requerida
    total_ofertas_sorteadas=lt.newList('ARRAY_LIST')
    for pais in lt.iterator(llaves_pais_mayores):
        ofertas_pais=mp.get(mayores_paises,pais)
        for oferta in lt.iterator(me.getValue(ofertas_pais)):
            lt.addLast(total_ofertas_sorteadas,oferta)
            if not mp.contains(mayores_ciudades,oferta['city']):
                mp.put(mayores_ciudades,oferta['city'],(oferta['city'],0))
            valor=me.getValue(mp.get(mayores_ciudades,oferta['city']))
            mp.put(mayores_ciudades,oferta['city'],(oferta['city'],valor[1]+1))
    ciudades_totales=mp.valueSet(mayores_ciudades)
    sa.sort(ciudades_totales,oferta_nombre_pais)
    num_ciudades=lt.size(ciudades_totales)
    mayor_ciudad=lt.getElement(ciudades_totales,1)
    
    #Se crean mapas y se llenan con las diferentes habilidades 
    habilidades_junior=mp.newMap()
    habilidades_mid=mp.newMap()
    habilidades_senior=mp.newMap()
    
    level_j=0
    level_m=0
    level_s=0
    
    empresas_j=mp.newMap()
    empresas_m=mp.newMap()
    empresas_s=mp.newMap()
    
    sedes_j=0
    sedes_m=0
    sedes_s=0
    
    emp_multi_j=lt.newList('ARRAY_LIST')
    emp_multi_m=lt.newList('ARRAY_LIST')
    emp_multi_s=lt.newList('ARRAY_LIST')
    
    num_of_j=0
    num_of_m=0
    num_of_s=0
    
    for oferta in lt.iterator(total_ofertas_sorteadas):
        id=oferta['id']
        ofer_habilidad=me.getValue(mp.get(mapa_exp,id))
        nom_empresa=oferta['company_name']
        
        if oferta['experience_level']=='junior':
            if not mp.contains(empresas_j,nom_empresa) :
                mp.put(empresas_j,nom_empresa,(nom_empresa,0))
            valor=me.getValue(mp.get(empresas_j,nom_empresa))
            mp.put(empresas_j,nom_empresa,(nom_empresa,valor[1]+1))
            for habilidad in lt.iterator(ofer_habilidad):
                if not mp.contains(habilidades_junior,habilidad['name']):
                    mp.put(habilidades_junior,habilidad['name'],(habilidad['name'],0))
                valor=me.getValue(mp.get(habilidades_junior,habilidad['name']))
                mp.put(habilidades_junior,habilidad['name'],(habilidad['name'],valor[1]+1))
                level_j+=int(habilidad['level'])
                num_of_j+=1
            if lt.isPresent(lst_sedes,id) and not lt.isPresent(emp_multi_j,nom_empresa):
                sedes_j+=1
                lt.addLast(emp_multi_j,nom_empresa)
                
                
        
        elif oferta['experience_level']=='mid':
            if not mp.contains(empresas_m,nom_empresa) :
                mp.put(empresas_m,nom_empresa,(nom_empresa,0))
            valor=me.getValue(mp.get(empresas_m,nom_empresa))
            mp.put(empresas_m,nom_empresa,(nom_empresa,valor[1]+1))
            for habilidad in lt.iterator(ofer_habilidad):
                if not mp.contains(habilidades_mid,habilidad['name']):
                    mp.put(habilidades_mid,habilidad['name'],(habilidad['name'],0))
                valor=me.getValue(mp.get(habilidades_mid,habilidad['name']))
                mp.put(habilidades_mid,habilidad['name'],(habilidad['name'],valor[1]+1))
                level_m+=int(habilidad['level'])
                num_of_m+=1
            if lt.isPresent(lst_sedes,id) and not lt.isPresent(emp_multi_m,nom_empresa):
                sedes_m+=1
                lt.addLast(emp_multi_m,nom_empresa)
                
        
        elif oferta['experience_level']=='senior':
            if not mp.contains(empresas_s,nom_empresa) :
                mp.put(empresas_s,nom_empresa,(nom_empresa,0))
            valor=me.getValue(mp.get(empresas_s,nom_empresa))
            mp.put(empresas_s,nom_empresa,(nom_empresa,valor[1]+1))
            for habilidad in lt.iterator(ofer_habilidad):
                if not mp.contains(habilidades_senior,habilidad['name']):
                    mp.put(habilidades_senior,habilidad['name'],(habilidad['name'],0))
                valor=me.getValue(mp.get(habilidades_senior,habilidad['name']))
                mp.put(habilidades_senior,habilidad['name'],(habilidad['name'],valor[1]+1))
                level_s+=int(habilidad['level'])
                num_of_s+=1
            if lt.isPresent(lst_sedes,id) and not lt.isPresent(emp_multi_s,nom_empresa):
                sedes_s+=1
                lt.addLast(emp_multi_s,nom_empresa)
                
    
    #Se calcula el tamaño, mayor, menor y el promedio de las habilidades 
 
    menor_hab_j,mayor_hab_j=calcular_mayor_y_menor(mp.valueSet(habilidades_junior))
    menor_hab_m,mayor_hab_m=calcular_mayor_y_menor(mp.valueSet(habilidades_mid))
    menor_hab_s,mayor_hab_s=calcular_mayor_y_menor(mp.valueSet(habilidades_senior))
    
    tamanio_hab_junior=mp.size(habilidades_junior)
    tamanio_hab_mid=mp.size(habilidades_mid)
    tamanio_hab_senior=mp.size(habilidades_senior)
    
    prom_j=promedio(num_of_j,level_j)
    prom_m=promedio(num_of_m,level_m)
    prom_s=promedio(num_of_s,level_s)
    
    tamanio_emp_junior=mp.size(empresas_j)
    tamanio_emp_mid=mp.size(empresas_m)
    tamanio_emp_senior=mp.size(empresas_s) 
    
    menor_emp_j,mayor_emp_j=calcular_mayor_y_menor(mp.valueSet(empresas_j))
    menor_emp_m,mayor_emp_m=calcular_mayor_y_menor(mp.valueSet(empresas_m))
    menor_emp_s,mayor_emp_s=calcular_mayor_y_menor(mp.valueSet(empresas_s))
    
    junior=[tamanio_hab_junior,mayor_hab_j,menor_hab_j,prom_j,tamanio_emp_junior,mayor_emp_j,menor_emp_j,sedes_j]
    mid=[tamanio_hab_mid,mayor_hab_m,menor_hab_m,prom_m,tamanio_emp_mid,mayor_emp_m,menor_emp_m,sedes_m]
    senior=[tamanio_hab_senior,mayor_hab_s,menor_hab_s,prom_s,tamanio_emp_senior,mayor_emp_s,menor_emp_s,sedes_s]
    
    return num_ofertas,num_ciudades,mayor_pais,mayor_ciudad,junior,mid,senior
     


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

#Funciones auxiliares

def calcular_mayor_y_menor(lst):
    lista=sa.sort(lst,oferta_nombre_pais)
    menor=lt.getElement(lista,lt.size(lista)-1)
    mayor=lt.getElement(lista,1)
    return menor,mayor
    

def calcular_empresas(mapa, item):
    lista_ofertas=me.getValue(mp.get(mapa, item))
    mapa_empresas=mp.newMap()
    for oferta in lt.iterator(lista_ofertas):
       if mp.contains(mapa_empresas, oferta['company_name']):
           mp.put(mapa_empresas, oferta['company_name'], (oferta['company_name'], me.getValue(mp.get(mapa_empresas, oferta['company_name']))[1]+1))
       else:
           mp.put(mapa_empresas, oferta['company_name'], (oferta['company_name'],1))
    valores=mp.valueSet(mapa_empresas)
    sa.sort(valores, oferta_nombre_pais)
    return mp.size(mapa_empresas), lt.getElement(valores, 1)

def comparar_promedios_ciudad(data_structs, mapa_ciudades, ciudad1, ciudad2):
    ganador=None
    mapa_salarios=data_structs['employments']
    city1=me.getValue(mp.get(mapa_ciudades, ciudad1))
    city2=me.getValue(mp.get(mapa_ciudades, ciudad2))
    con_oferta1=0
    con_oferta2=0
    total1=0
    total2=0
    promedio1=0
    promedio2=0
    for oferta1 in lt.iterator(city1):
        id=oferta1['id']
        actual=me.getValue(mp.get(mapa_salarios, id))
        if actual['salary_from'] != '' and actual['salary_to'] != '':
            salario=(int(actual['salary_from'])+int(actual['salary_to']))/2
            con_oferta1+=1
            total1+=salario
            
    for oferta2 in lt.iterator(city2):
        id=oferta2['id']
        actual=me.getValue(mp.get(mapa_salarios, id))
        if actual['salary_from'] != '' and actual['salary_to'] != '':
            salario=(int(actual['salary_from'])+int(actual['salary_to']))/2
            con_oferta2+=1
            total2+=salario
            
            
    if con_oferta1==0:
        promedio1=0
        if con_oferta2==0:
            promedio2=0
        else:
            promedio2 = total2/con_oferta2
    elif con_oferta2==0:
        promedio2=0
        promedio1 =  total1/con_oferta1
    else:
        promedio1 =  total1/con_oferta1
        promedio2 = total2/con_oferta2
   
    if promedio1>promedio2:
        ganador=ciudad1
    else:
        ganador=ciudad2
    return ganador

def promedio_por_ciudad(data_structs, mapa_ciudades, ciudad):
    promedio=0
    mapa_salarios=data_structs['employments']
    city=me.getValue(mp.get(mapa_ciudades, ciudad))
    con_oferta=0
    total=0
    for oferta in lt.iterator(city):
        id=oferta['id']
        actual=me.getValue(mp.get(mapa_salarios, id))
        if actual['salary_from'] != '' and actual['salary_to'] != '':
            salario=(int(actual['salary_from'])+int(actual['salary_to']))/2
            con_oferta+=1
            total+=salario
            
    if con_oferta==0:
        promedio=0
    else:
        promedio=total/con_oferta
    return promedio

def calcular_mejor_peor_oferta(data_structs, mapa, item):
    lista_ofertas=me.getValue(mp.get(mapa, item))
    mapa_salarios=data_structs['employments']
    ofertas_oredenadas_max=lt.newList()
    ofertas_oredenadas_min=lt.newList()
    for oferta in lt.iterator(lista_ofertas):
        id=oferta['id']
        actual=me.getValue(mp.get(mapa_salarios, id))
        if actual['salary_from'] != '' and actual['salary_to'] != '':
            high=int(actual['salary_to'])
            low=int(actual['salary_from'])
            lt.addLast(ofertas_oredenadas_max, (oferta, high))
            lt.addLast(ofertas_oredenadas_min, (oferta, low))
    sa.sort(ofertas_oredenadas_max, mayor_salario)
    sa.sort(ofertas_oredenadas_min, mayor_salario)
            
        
    mejor_oferta=lt.firstElement(ofertas_oredenadas_max)
    peor_oferta=lt.lastElement(ofertas_oredenadas_min)
    
    return mejor_oferta, peor_oferta
    
def promedio(denominador,numerador):
    if denominador>0:
        return(numerador/denominador)
    else: 
        return 0
# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass


        
    

# Funciones de ordenamiento

def fecha(dato1, dato2):
    return dato1['published_at'][:10]<dato2['published_at'][:10]

def salario(dato1, dato2):
    if dato1['salary_from'] != '' and dato1['salary_to'] != '':
        salario1=round((int(dato1['salary_from'])+int(dato1['salary_to']))/2, 2)
    else:
        salario1=0
    if dato2['salary_from'] != '' and dato2['salary_to'] != '':
        salario2=round((int(dato2['salary_from'])+int(dato2['salary_to']))/2, 2)
    else:
        salario2=0
          
    return salario1<salario2

def fecha_empresa(dato1, dato2):
    if dato1['published_at'][:10]<dato2['published_at'][:10]:
        return True
    elif dato1['published_at'][:10]>dato2['published_at'][:10]:
        return False
    else:
        return dato1['company_name']<dato2['company_name']
    
def numero_ofertas(data_1, data_2):
    if data_1[1]==data_2[1]:
        return data_1[2]>data_2[2]    
    else:
        return data_1[1]>data_2[1]

def oferta_nombre_pais(data_1, data_2):
    if data_1[1]==data_2[1]:
        return data_1[0]<data_2[0]    
    else:
        return data_1[1]>data_2[1]

def mayor_salario(data_1, data_2):
    return data_1[1]>data_2[1]

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


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
