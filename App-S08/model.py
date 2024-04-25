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
from datetime import datetime
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
    #TODO: Inicializar las estructuras de datos
    datos={
        "jobs": None,
        "skills": None,
        "employment": None,
        "multilocation": None
    }
    datos["jobs"]=lt.newList("ARRAY_LIST")
    datos["skills"]=mp.newMap(200000, maptype='PROBING', loadfactor=0.7)
    datos["employment"]=mp.newMap(200000, maptype='PROBING', loadfactor=0.5)
    datos["multilocation"]=mp.newMap(200000, maptype='PROBING', loadfactor=0.7)
    return datos

def add_jobs(lista_jobs_actual, data):
    """
    Función para agregar nuevos elementos a la lista
    Args:
    lista_jobs_actual: lista de datos actual de los trabajos unicamente
    data: datos a agregar leidos del archivo csv
    Returns:
    lista_jobs_actual: lista de datos actual de los trabajos con los datos agregados
    """
    #TODO: Crear una funcion para arreglar esto mejor
    #Se añaden los datos a las listas que corresponden
    resultado_jobs = new_job(data["title"], data["street"], data["city"], data["country_code"], data["address_text"], data["marker_icon"], data["workplace_type"], data["company_name"], data["company_url"], data["company_size"], data["experience_level"], data["published_at"], data["remote_interview"], data["open_to_hire_ukrainians"], data["id"], data["display_offer"])
    lt.addLast(lista_jobs_actual, resultado_jobs)
    return lista_jobs_actual
def add_skills(mapa_skills_actual, data, tamanio):
    """
    Función para agregar nuevos elementos a la lista
    Args:
    mapa_skills_actual: lista de datos actual de las habilidades unicamente
    data: datos a agregar leidos del archivo csv
    Returns:
    mapa_skills_actual: lista de datos actual de las habilidades con los datos agregados
    """
    #Se añaden los datos a las listas que corresponden
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
       #Si al buscar el id no lo encuentra, crea una nueva lista con un nuevo skill
        if mp.get(mapa_skills_actual, data[2])==None:
            lista=lt.newList("ARRAY_LIST")
            lt.addLast(lista, new_skill(data[0], data[1], data[2]))
            #Se pone el nuevo skill en la lista de dicho ID
            mp.put(mapa_skills_actual, data[2], lista)
        #Sino se agrega el skill a la lista ya existente
        else:
            lt.addLast(me.getValue(mp.get(mapa_skills_actual, data[2])), new_skill(data[0], data[1], data[2]))
    else:
        #Lo mismo anterior pero con otro formato de diccionario
        if mp.get(mapa_skills_actual, data["id"])==None:
            lista=lt.newList("ARRAY_LIST")
            lt.addLast(lista, new_skill(data["name"], data["level"], data["id"]))
            mp.put(mapa_skills_actual, data["id"], lista)
        else:
            lt.addLast(me.getValue(mp.get(mapa_skills_actual, data["id"])), new_skill(data["name"], data["level"], data["id"]))
    return mapa_skills_actual
def add_employments(mapa_employments_actual, data, tamanio):
    #Mismo proceso que skills
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
        if mp.get(mapa_employments_actual, data[1])==None:
            lista=lt.newList("ARRAY_LIST")
            lt.addLast(lista, new_employment_type(data[0], data[1], data[2], data[3], data[4]))
            mp.put(mapa_employments_actual, data[1], lista)
        else:
            lt.addLast(me.getValue(mp.get(mapa_employments_actual, data[1])), new_employment_type(data[0], data[1], data[2], data[3], data[4]))
    else:
        if mp.get(mapa_employments_actual, data["id"])==None:
            lista=lt.newList("ARRAY_LIST")
            lt.addLast(lista, new_employment_type(data["type"], data["id"], data["currency_salary"], data["salary_from"], data["salary_to"]))
            mp.put(mapa_employments_actual, data["id"], lista)
        else:
            lt.addLast(me.getValue(mp.get(mapa_employments_actual, data["id"])), new_employment_type(data["type"], data["id"], data["currency_salary"], data["salary_from"], data["salary_to"]))
    return mapa_employments_actual
def add_multilocation(lista_multilocation, data, tamanio):
    """
    Función para agregar nuevos elementos a la lista
    Args:
    lista_multilocation: lista de datos actual de las habilidades unicamente
    data: datos a agregar leídos del archivo csv
    Returns:
    lista_multilocation: lista de datos actual de las habilidades con los datos agregados
    """
    #Mismo proceso de skill
    #Se añaden los datos a las listas que corresponden
    if tamanio=="small" or tamanio=="medium" or tamanio=="large":
        if mp.get(lista_multilocation, data[2])==None:
            lista=lt.newList("ARRAY_LIST")
            lt.addLast(lista, new_multilocation(data[0], data[1], data[2]))
            mp.put(lista_multilocation, data[2], lista)
        else:
            lt.addLast(me.getValue(mp.get(lista_multilocation, data[2])), new_multilocation(data[0], data[1], data[2]))
    else:
        if mp.get(lista_multilocation, data["id"])==None:
            lista=lt.newList("ARRAY_LIST")
            lt.addLast(lista, new_multilocation(data["city"], data["street"], data["id"]))
            mp.put(lista_multilocation, data["id"], lista)
        else:
            lt.addLast(me.getValue(mp.get(lista_multilocation, data["id"])), new_multilocation(data["city"], data["street"], data["id"]))
    return lista_multilocation
def sort_jobs(lista_jobs):
    """
    Función para ordenar los trabajos por fecha de publicación
    Args:
    lista_jobs: lista de trabajos a ordenar
    Returns:
    lista_jobs: lista de trabajos ordenada
    """
    merg.sort(lista_jobs, sort_dates)
    return lista_jobs
def new_job(title,street,city,country_code,address_text,marker_icon,workplace_type,company_name, company_url, company_size, experience_level, published_at, remote_interview, open_to_hire_ukranians, id_job, display_offer):
    """
    Crea una nueva estructura para modelar los datos
    """
    job = {
        "title": title,
        "street": street,
        "city": city,
        "country_code": country_code,
        "address_text": address_text,
        "marker_icon": marker_icon,
        "workplace_type": workplace_type,
        "company_name": company_name,
        "company_url": company_url,
        "company_size": company_size,
        "experience_level": experience_level,
        "published_at": published_at,
        "remote_interview": remote_interview,
        "open_to_hire_ukrainians": open_to_hire_ukranians,
        "id": id_job,
        "display_offer": display_offer
    }
    return job

def new_skill(name, level, id_job):
    """
    Crea una nueva estructura para modelar los datos
    """
    skill = {
        "name": name,
        "level": level,
        "id": id_job
    }
    return skill

def new_employment_type(type, id, currency_salary, salary_from, salary_to):
    employment = {
        "type": type,
        "id": id,
        "currency_salary": currency_salary,
        "salary_from": salary_from,
        "salary_to": salary_to
    }
    return employment

def new_multilocation(city, street, id):
    multilocation = {
        "city": city,
        "street": street,
        "id": id
    }
    return multilocation
    
# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

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

def compare_by_date(job1, job2):
    """
    Compara dos ofertas de trabajo por su fecha de publicación.
    Devuelve un valor negativo si job1 es más reciente que job2,
    cero si son igual de recientes, y un valor positivo si job1 es menos reciente que job2.
    """
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"  # Asegúrate de que este es el formato correcto para tus fechas
    date1 = datetime.strptime(job1['published_at'], date_format)
    date2 = datetime.strptime(job2['published_at'], date_format)
    return (date2 - date1).total_seconds()
    

def req_1(data_structs, num, cod_pais, experticia):
    """
    Función que soluciona el requerimiento 1
    """
    #Se crea un mapa de formato probing con un factor de carga de 0.7
    mapa = mp.newMap(200, maptype='PROBING', loadfactor=0.7)
    cantidad_pais=0
    cantidad_experticia=0
    #Se itera por toda la lista de trabajos
    for i in lt.iterator(data_structs["jobs"]):
        #Si el pais es igual al que se esta buscando se agrega a las cantidades
        if i["country_code"]==cod_pais:
            cantidad_pais+=1
        #Si la experiencia es igual a la que se esta buscando, se agrega
        if i["experience_level"]==experticia:
            cantidad_experticia+=1
        #Se crea una llave con forma de tupla de codigo de pais y nivel de experiencia
        key = (i["country_code"], i["experience_level"])
        #Se trata de buscar el valor en el mapa creado
        value = mp.get(mapa, key)
        #Si no existe, se crea una lista para almacenar la informacion
        if value == None:
            value = lt.newList("ARRAY_LIST")
            mp.put(mapa, key, value)
        #Se añade la informacion correspondiente a la lista que se encuentra con el key creado
        value=mp.get(mapa, key)
        lt.addLast(me.getValue(value), i)
    #Se busca el dato 
    dato=mp.get(mapa, (cod_pais, experticia))
    if dato != None:
        #Se obtiene el valor
        resultado=me.getValue(dato)
        #Si el valor ingresado por el usuario es mayor a la cantidad encontrada, se cambia
        if num > lt.size(resultado):
            num = lt.size(resultado)
        #La lista se corta hasta donde el usuario lo requiera
        lista = lt.subList(resultado, 1, num)
    else:
        #Sino se encuentra, retorna None
        lista=None
    return lista,cantidad_pais,cantidad_experticia


def req_2(data_structs, num, empresa,ciudad):
     #Se crea un mapa
    mapa = mp.newMap(200, maptype='PROBING', loadfactor=0.7)
    #Por cada elemento de los trabajos se recorre
    for i in lt.iterator(data_structs["jobs"]):
        #Se crea una llave con la información de la compañia y la ciudad
        key = (i["company_name"], i["city"])
        value = mp.get(mapa, key)
        #Si no existe, se crea una lista
        if value == None:
            value = lt.newList("ARRAY_LIST")
            mp.put(mapa, key, value)
        # Se obtiene el valor
        value=mp.get(mapa, key)
        #Se añade la información del trabajo
        lt.addLast(me.getValue(value), i)
    #Se obtiene el dato 
    dato=mp.get(mapa, (empresa, ciudad))
    #Si existe el dato en el mapa creado
    if dato != None:
        #Se obtiene el resultado (La lista creada en el valor)
        resultado=me.getValue(dato)
        # Si el numero ingresado por el usuario es mayor que el tamaño de la lista, se ambia
        if num > lt.size(resultado):
            num = lt.size(resultado)
        cantidad=lt.size(resultado)
        #Se hace una sublista con las cantidades necesitadas
        lista = lt.subList(resultado, 1, num)
    else:
        #Sino se encuentra, retorna None
        lista=None
    return lista,cantidad


def req_3(data_structs, nombre_empresa, fecha_ini, fecha_fin):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    mapa_junior=mp.newMap(200, maptype='PROBING', loadfactor=0.7)
    mapa_senior=mp.newMap(200, maptype='PROBING', loadfactor=0.7)
    mapa_mid=mp.newMap(200, maptype='PROBING', loadfactor=0.7)
    lista_ofertas=lt.newList("ARRAY_LIST")
    for i in lt.iterator(data_structs["jobs"]):
        if i["company_name"]==nombre_empresa and i["published_at"]>=date_to_iso(fecha_ini) and i["published_at"]<=date_to_iso(fecha_fin):
            lt.addLast(lista_ofertas, i)
            if i["experience_level"]=="junior":
                key=i["id"]
                if mp.contains(mapa_junior,key)==False:
                    mp.put(mapa_junior,key,i)
            elif i["experience_level"]=="mid":
                key=i["id"]
                if mp.contains(mapa_mid,key)==False:
                    mp.put(mapa_mid,key,i)
            elif i["experience_level"]=="senior":
                key=i["id"]
                if mp.contains(mapa_senior,key)==False:
                    mp.put(mapa_senior,key,i)
    lista_ofertas=merg.sort(lista_ofertas, sort_req_3)
    return lt.size(lista_ofertas),mp.size(mapa_junior),mp.size(mapa_mid),mp.size(mapa_senior),lista_ofertas

def compare_by_date_and_country(job1, job2):
    """
    Función de comparación para ordenar las ofertas por fecha y país.
    """
    fecha1 = datetime.strptime(job1['published_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
    fecha2 = datetime.strptime(job2['published_at'], "%Y-%m-%dT%H:%M:%S.%fZ")

    if fecha1 == fecha2:
        return -1 if job1['country_code'] < job2['country_code'] else 1
    else:
        return -1 if fecha1 < fecha2 else 1

def sort_req_3(oferta1, oferta2):
    if oferta1["published_at"] == oferta2["published_at"]:
        if oferta1["company_name"] > oferta2["company_name"]:
            return True
        else:
            return False
    elif oferta1["published_at"] > oferta2["published_at"]:
        return True
    else:
        return False


def req_4(data_structs,codigo,fecha_ini,fecha_fin):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    fecha_inicial=date_to_iso(fecha_ini)
    fecha_final= date_to_iso(fecha_fin)
    lista_nueva=lt.newList('ARRAY_LIST')
    mapa_empresas=mp.newMap (1000, maptype='PROBING', loadfactor=0.7)
    mapa_ciudades=mp.newMap(1000, maptype='PROBING', loadfactor=0.7)
    for i in lt.iterator(data_structs["jobs"]):
        if i["country_code"] == codigo and i["published_at"] >=fecha_inicial and i["published_at"] <= fecha_final :
            lt.addLast(lista_nueva, i)
            if mp.contains(mapa_empresas,i["company_name"])==False:
                mp.put(mapa_empresas,i["company_name"],1)
            else:
                 valor=me.getValue(mp.get(mapa_empresas,i["company_name"]))
                 valor+=1
                 mp.put(mapa_empresas,i["company_name"],valor)
            if mp.contains(mapa_ciudades,i["city"])==False:
                mp.put(mapa_ciudades,i["city"],1)
            else:
                 valorc=me.getValue(mp.get(mapa_ciudades,i["city"]))
                 valorc+=1
                 mp.put(mapa_ciudades,i["city"],valorc)

    llaves_ciudades= mp.keySet(mapa_ciudades)
    valores_ciudades=lt.newList('ARRAY_LIST')
    for i in lt.iterator(llaves_ciudades):
       datos= mp.get(mapa_ciudades,i)
       v= me.getValue(datos) 
       tupla= (i,v)
       lt.addLast(valores_ciudades,tupla)
    sorteado=merg.sort(lista_nueva, cmp_ofertas_by_fecha_y_nombre)
    sizee=mp.size(mapa_empresas)
    sorteado2=merg.sort(valores_ciudades, cmp_req_4)
  
    mayor = lt.firstElement(sorteado2)
    menor= lt.lastElement(sorteado2)
    total_ciu= lt.size(sorteado2)
    return sorteado,sizee,total_ciu,mayor,menor
def cmp_req_4(oferta1, oferta2):
    if oferta1 [1]==oferta2[1]:
            if oferta1[0]<oferta2[0]:
                return True
            else:
                return False
    elif oferta1[1]>oferta2[1]:
        return True
    else:
        return False

def cmp_ofertas_by_fecha_y_nombre(oferta1, oferta2):
    """
    Devuelve verdadero (True) si la fecha de la oferta 1 es menor que en la oferta ,
    en caso de que sean iguales se analiza la empresa de la oferta laboral, de lo contrario devuelva Falso

    Args:
        oferta1: información de la primera oferta laboral que incluye "company_name" y "published_at"
        oferta2: información de la segunda oferta laboral que incluye "company_name" y "published_at"
    """
    nombre1= oferta1["company_name"].lower()
    nombre2= oferta2["company_name"].lower()
    fecha1= oferta1["published_at"]
    fecha2= oferta2["published_at"]
    return (fecha1>fecha2) or (fecha1 == fecha2 and nombre1 < nombre2)

def req_5(data_structs,ciudad, fecha_ini, fecha_fin):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    #Se crea una nueva lista para almacenar los trabajos validos
    lista_jobs=lt.newList("ARRAY_LIST")
    #Se crean variables para almacenar los mayores y menores
    empresa_mayor=("a",0)
    empresa_menor=("a",100)
    #Se iteran los trabajos con las condiciones
    for i in lt.iterator(data_structs["jobs"]):
        if i["city"]==ciudad and i["published_at"]>=date_to_iso(fecha_ini) and i["published_at"]<=date_to_iso(fecha_fin):
            lt.addLast(lista_jobs, i)
    #Si no encuentra retorna None
    if lt.size(lista_jobs)==0:
        return None
    else:
        #Crea un mapa con las empresas
        mapa_empresas=mp.newMap(200, maptype='PROBING', loadfactor=0.7)
        lista_empresas=lt.newList("ARRAY_LIST")
        for i in lt.iterator(lista_jobs):
            key = i["company_name"]
            value = mp.get(mapa_empresas, key)
            #Si no encuentra crea una lista y la ingresa
            if value is None:
                value = lt.newList("ARRAY_LIST")
                mp.put(mapa_empresas, key, value)
                lt.addLast(lista_empresas, key)
            #Se ingresa el valor
            value=mp.get(mapa_empresas, key)
            lt.addLast(me.getValue(value), i)
        lista_final=lt.newList("ARRAY_LIST")
        #Se itera para encontrar el mayor y menor 
        for i in lt.iterator(lista_empresas):
            i=me.getValue(mp.get(mapa_empresas,i))
            for j in lt.iterator(i):
                if lt.size(me.getValue(mp.get(mapa_empresas,j["company_name"]))) > empresa_mayor[1]:
                    empresa_mayor=(j["company_name"],lt.size(me.getValue(mp.get(mapa_empresas,j["company_name"]))))
                if lt.size(me.getValue(mp.get(mapa_empresas,j["company_name"]))) < empresa_menor[1] or j["company_name"]>empresa_menor[0]:
                    empresa_menor=(j["company_name"],lt.size(me.getValue(mp.get(mapa_empresas,j["company_name"]))))
                lt.addLast(lista_final, j)
        #Se ordena
        merg.sort(lista_final, sort_dates_empresa)
        return lista_final,lt.size(lista_jobs),mp.size(mapa_empresas),empresa_mayor,empresa_menor


def req_6(data_structs, num_ciudades, experticia, anio):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    #Crea un mapa de ciudades por cantidad de trabajos
    #Estructura: mapa de ciudades -> (cantidad de trabajos, País)
    ciudades_cantidades=mp.newMap(num_ciudades, maptype='PROBING', loadfactor=0.7)
    #Crea una lista de trabajos que cumplan con los criterios de experticia y año
    lista_trabajos=lt.newList("ARRAY_LIST")    
    for i in lt.iterator(data_structs["jobs"]):
        if ((experticia.lower()!="indiferente" and i["experience_level"]==experticia) or (experticia.lower()=="indiferente")) and i["published_at"][:4]==anio :
                lt.addLast(lista_trabajos, i)
                key8=i["city"]
                value = mp.get(ciudades_cantidades, key8)
                if value is None:
                    value=(1,i["country_code"])
                    mp.put(ciudades_cantidades, key8, value)
                else:
                    value=me.getValue(mp.get(ciudades_cantidades,key8))
                    value=(value[0]+1,value[1])
                    mp.put(ciudades_cantidades, key8, value)
    if lt.size(lista_trabajos)==0:
        return None
    
    llaves_ciudades=mp.keySet(ciudades_cantidades)
    lista_ciudades_cantidades=lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(llaves_ciudades):
        value=mp.get(ciudades_cantidades, i)
        lt.addLast(lista_ciudades_cantidades, (i, me.getValue(value)[0], me.getValue(value)[1]))
        
    merg.sort(lista_ciudades_cantidades,sort_cantidades_ciudades)
    
    if num_ciudades>lt.size(lista_ciudades_cantidades):
        num_ciudades=lt.size(lista_ciudades_cantidades)
  
    lista_ciudades_cantidades=lt.subList(lista_ciudades_cantidades, 1, num_ciudades) 
    ciudades_cantidades=mp.newMap(lt.size(lista_ciudades_cantidades), maptype='PROBING', loadfactor=0.7)
    mapa_final=mp.newMap(20, maptype='PROBING', loadfactor=0.7)

    for i in lt.iterator(lista_ciudades_cantidades):
        key=i[0]
        value=(i[1],i[2])
        mp.put(ciudades_cantidades, key, value)
        mp.put(mapa_final, key, lt.newList("ARRAY_LIST")) 
        lt.addLast(me.getValue(mp.get(mapa_final,key)), key)
        lt.addLast(me.getValue(mp.get(mapa_final,key)), i[2])
        lt.addLast(me.getValue(mp.get(mapa_final,key)), i[1])
        lt.addLast(me.getValue(mp.get(mapa_final,key)), (0,0))
        lt.addLast(me.getValue(mp.get(mapa_final,key)), 0)
        lt.addLast(me.getValue(mp.get(mapa_final,key)), (0,0))
        lt.addLast(me.getValue(mp.get(mapa_final,key)), {"id_trabajo":"",
                                                         "title":"Ninguno",
                                                         "city":"",
                                                         "country_code":"",
                                                         "salario":0,
                                                         })
        lt.addLast(me.getValue(mp.get(mapa_final,key)), {"id_trabajo":"",
                                                         "title":"",
                                                         "city":"",
                                                         "country_code":"Ninguno",
                                                         "salario":100000,
                                                         })
    """
    Estructura Mapa final:
    llave: ciudad
    valor: Lista con los siguientes elementos:
    1: Ciudad
    2: País
    3: Cantidad de trabajos en la ciudad
    4[0]: Salario promedio de trabajos en la ciudad
    4[1]: Cantidad de ofertas con salario para calcular el promedio
    5: Cantidad de empresas en la ciudad
    6[0]: Empresa con mayor cantidad de trabajos
    6[1]: Cantidad de trabajos de la empresa con mayor cantidad de trabajos
    7: Informacion de la mejor oferta de trabajo
    8: Informacion de la peor oferta de trabajo
    """
    lista_trabajos_final=lt.newList("ARRAY_LIST") 
        
    for i in lt.iterator(lista_trabajos):
        if mp.get(ciudades_cantidades,i["city"])!=None:
            lt.addLast(lista_trabajos_final, i)
    #Crea un mapa de mapas para almacenar los salarios de trabajos por ID de trabajo y por país
    #Estructura: mapa de ciudad -> mapa de ID de trabajos -> salario
    salarios_ciudad_id=mp.newMap(lt.size(lista_ciudades_cantidades), maptype='PROBING', loadfactor=0.7)
    #Crea un mapa de empresas por cantidad de trabajos
    #Estructura: mapa de empresas -> cantidad de trabajos
    ciudades_empresas_cantidades=mp.newMap(200, maptype='PROBING', loadfactor=0.7)
    empresas_cantidades=mp.newMap(200, maptype='PROBING', loadfactor=0.7)
    for i in lt.iterator(lista_trabajos_final):
        key1=i["city"]
        value = mp.get(salarios_ciudad_id, key1)
        if value is None:
            value=mp.newMap(10, maptype='PROBING', loadfactor=0.7)
            mp.put(salarios_ciudad_id, key1, value)
        key2=i["id"]
        value = obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2)
        if value is None:
            value=i
            añadir_mapa_de_mapas(salarios_ciudad_id,key1,key2,value)
            salario=me.getValue(mp.get(data_structs["employment"], key2))
        if lt.size(salario)>1:
            salario_promedio=0
            cantidad=0
            for j in lt.iterator(salario):
                if j["salary_from"]!="" and j["salary_to"]!="":
                    salario_promedio+=(int(j["salary_from"])+int(j["salary_to"]))
                    cantidad+=2
            if cantidad!=0:
                salario_promedio=salario_promedio/cantidad
                value=salario_promedio
                me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]=value
                elemento=lt.getElement(me.getValue(mp.get(mapa_final,key1)),4)
                lt.changeInfo(me.getValue(mp.get(mapa_final,key1)),4,(elemento[0]+value,elemento[1]+1))
                if me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]>lt.getElement(me.getValue(mp.get(mapa_final,key1)),7)["salario"]:
                    lt.changeInfo(me.getValue(mp.get(mapa_final,key1)),7,{"id_trabajo":i["id"],
                                                                            "title":i["title"],
                                                                            "city":i["city"],
                                                                            "country_code":i["country_code"],
                                                                            "salario":me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]})
                if me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]<lt.getElement(me.getValue(mp.get(mapa_final,key1)),8)["salario"]:
                    lt.changeInfo(me.getValue(mp.get(mapa_final,key1)),8,{"id_trabajo":i["id"],
                                                                            "title":i["title"],
                                                                            "city":i["city"],
                                                                            "country_code":i["country_code"],
                                                                            "salario":me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]})
            else:
                me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]=0                    
    
        else:
            for j in lt.iterator(salario):
                if j["salary_from"]!="" and j["salary_to"]!="":
                    salario_promedio=(int(j["salary_from"])+int(j["salary_to"]))/2
                    value=salario_promedio
                    me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]=value
                    elemento=lt.getElement(me.getValue(mp.get(mapa_final,key1)),4)
                    lt.changeInfo(me.getValue(mp.get(mapa_final,key1)),4,(elemento[0]+value,elemento[1]+1))
                    if me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]>lt.getElement(me.getValue(mp.get(mapa_final,key1)),7)["salario"]:
                        lt.changeInfo(me.getValue(mp.get(mapa_final,key1)),7,{"id_trabajo":i["id"],
                                                                                "title":i["title"],
                                                                                "city":i["city"],
                                                                                "country_code":i["country_code"],
                                                                                "salario":me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]})
                    if me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]<lt.getElement(me.getValue(mp.get(mapa_final,key1)),8)["salario"]:
                        lt.changeInfo(me.getValue(mp.get(mapa_final,key1)),8,{"id_trabajo":i["id"],
                                                                            "title":i["title"],
                                                                            "city":i["city"],
                                                                            "country_code":i["country_code"],
                                                                            "salario":me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]})

                else:
                    me.getValue(obtener_mapa_de_mapas(salarios_ciudad_id,key1,key2))["salario"]=0
        key3=i["company_name"]
        value=mp.get(empresas_cantidades,key3)
        if value is None:
            value=0
            mp.put(empresas_cantidades, key3, value)
        value=mp.get(empresas_cantidades,key3)  
        value=me.getValue(value)
        value+=1
        mp.put(empresas_cantidades, key3, value)
        value = mp.get(ciudades_empresas_cantidades,key1)
        
        if value is None:
            value=mp.newMap(10, maptype='PROBING', loadfactor=0.7)
            mp.put(ciudades_empresas_cantidades, key1, value)
            value=obtener_mapa_de_mapas(ciudades_empresas_cantidades,key1,key3)
            if value is None:
                value=0
                añadir_mapa_de_mapas(ciudades_empresas_cantidades,key1,key3,value)
            else:
                value+=1
                añadir_mapa_de_mapas(ciudades_empresas_cantidades,key1,key3,value)
        value=me.getValue(mp.get(ciudades_empresas_cantidades,key1))
        if mp.get(value,key3)==None:
            añadir_mapa_de_mapas(ciudades_empresas_cantidades,key1,key3,1)
        else:
            value=me.getValue(obtener_mapa_de_mapas(ciudades_empresas_cantidades,key1,key3))
            value+=1
            añadir_mapa_de_mapas(ciudades_empresas_cantidades,key1,key3,value)         
    for i in lt.iterator(lista_ciudades_cantidades):
        key=i[0]
        value=me.getValue(mp.get(mapa_final,key))
        value=lt.getElement(value,4)
        if value[1]!=0:
            value=value[0]/value[1]
        else:
            value=0
        lt.changeInfo(me.getValue(mp.get(mapa_final,key)),4,value)
        lt.changeInfo(me.getValue(mp.get(mapa_final,key)),5,mp.size(me.getValue(mp.get(ciudades_empresas_cantidades,key))))
        llave_empresas=mp.keySet(me.getValue(mp.get(ciudades_empresas_cantidades,key)))
        empresa_mayor=("a",0)
        for i in lt.iterator(llave_empresas):
            if me.getValue(obtener_mapa_de_mapas(ciudades_empresas_cantidades,key,i))>empresa_mayor[1]:
                empresa_mayor=(i,me.getValue(obtener_mapa_de_mapas(ciudades_empresas_cantidades,key,i)))
                lt.changeInfo(me.getValue(mp.get(mapa_final,key)),6,empresa_mayor)
       
            
    lista_retorno=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista_ciudades_cantidades):
        key=i[0]
        value=me.getValue(mp.get(mapa_final,key))
        lt.addLast(lista_retorno, value)
            
    return (lt.size(lista_ciudades_cantidades),
                mp.size(empresas_cantidades),
                lt.size(lista_trabajos_final),
                lt.getElement(lista_ciudades_cantidades,1),
                lt.getElement(lista_ciudades_cantidades,lt.size(lista_ciudades_cantidades)), 
                lista_retorno)


def req_7(data_structs, num_paises, anio_consulta, mes_consulta):
    """
    Función que soluciona el requerimiento 7
    """
    paises_cantidades=mp.newMap(num_paises, maptype='PROBING', loadfactor=0.7)
    # TODO: Realizar el requerimiento 7
    llaves_paises=lt.newList("ARRAY_LIST")
    lista_trabajos=lt.newList("ARRAY_LIST")    
    for i in lt.iterator(data_structs["jobs"]):
        if i["published_at"][:7]==anio_consulta+"-"+mes_consulta:
                lt.addLast(lista_trabajos, i)
                key_2=i["country_code"]
                value = mp.get(paises_cantidades, key_2)
                if value is None:
                    value=1
                    mp.put(paises_cantidades, key_2, value)
                    lt.addLast(llaves_paises, key_2)
                else:
                    value=me.getValue(mp.get(paises_cantidades,key_2))
                    value+=1
                    mp.put(paises_cantidades, key_2, value)
                    
    if lt.size(lista_trabajos)==0:
        return None
    
    lista_paises_cantidades=lt.newList("ARRAY_LIST")
    for i in lt.iterator(llaves_paises):
        value=mp.get(paises_cantidades, i)
        lt.addLast(lista_paises_cantidades, (i, me.getValue(value)))
    merg.sort(lista_paises_cantidades,sort_cantidades_ciudades)
    
    if num_paises>lt.size(lista_paises_cantidades):
        num_paises=lt.size(lista_paises_cantidades)
    lista_paises_cantidades=lt.subList(lista_paises_cantidades, 1, num_paises)
    paises_cantidades=mp.newMap(lt.size(lista_paises_cantidades), maptype='PROBING', loadfactor=0.7)
    for i in lt.iterator(lista_paises_cantidades):
        key=i[0]
        value=i[1]
        mp.put(paises_cantidades, key, value)
    lista_trabajos_final=lt.newList("ARRAY_LIST")
    ciudades_cantidades=mp.newMap(100, maptype='PROBING', loadfactor=0.7)
    id_empresas=mp.newMap(100, maptype='PROBING', loadfactor=0.7)
    llaves_ciudades=mp.keySet(ciudades_cantidades)

    for i in lt.iterator(lista_trabajos):
        if mp.get(paises_cantidades,i["country_code"])!=None:
            lt.addLast(lista_trabajos_final, i)
            key=i["city"]
            value = mp.get(ciudades_cantidades, key)
            if value is None:
                value=1
                mp.put(ciudades_cantidades, key, value)
                lt.addLast(llaves_ciudades, key)
            else:
                value=me.getValue(mp.get(ciudades_cantidades,key))
                value+=1
                mp.put(ciudades_cantidades, key, value)
            key=i["id"]
            value = mp.get(id_empresas, key)
            if value is None:
                value=i["company_name"]
                mp.put(id_empresas, key, value)
            else:
                value=me.getValue(mp.get(id_empresas,key))
                value=i["company_name"]
                mp.put(id_empresas, key, value)

    lista_ciudades_cantidades=lt.newList("ARRAY_LIST")
    for i in lt.iterator(llaves_ciudades):
        value=mp.get(ciudades_cantidades, i)
        lt.addLast(lista_ciudades_cantidades, (i, me.getValue(value)))
    merg.sort(lista_ciudades_cantidades,sort_cantidades_ciudades)
    
    mapa_final=mp.newMap(num_paises, maptype='PROBING', loadfactor=0.7)
    for i in lt.iterator(lista_trabajos_final):
        key1=i["country_code"]
        value = mp.get(mapa_final, key1)
        if value is None:
            value=mp.newMap(7, maptype='PROBING', loadfactor=0.7)
            mp.put(mapa_final, key1, value)
        key2=i["experience_level"]
        value = obtener_mapa_de_mapas(mapa_final,key1,key2)
        if value is None:
            value=mp.newMap(10, maptype='PROBING', loadfactor=0.7)
            mp.put(me.getValue(mp.get(mapa_final,key1)), key2, value)
            mp.put(value, "habilidades", mp.newMap(10, maptype='PROBING', loadfactor=0.7))
            mp.put(value, "habilidad_mayor", ("No existe",0))
            mp.put(value, "habilidad_menor", ("No existe",100))
            mp.put(value, "promedio_habilidad", (0,0))
            mp.put(value,"empresas",mp.newMap(10, maptype='PROBING', loadfactor=0.7))
            mp.put(value, "empresa_mayor", ("No existe",0))
            mp.put(value, "empresa_menor", ("No existe",100))
            mp.put(value, "empresas_mas_localizaciones",mp.newMap(100, maptype='PROBING', loadfactor=0.7))
        
        #Obtiene el mapa de retorno por país y experticia
        value=mp.get(me.getValue(mp.get(mapa_final,key1)),key2)
        #Obtiene la entrada de habilidades
        habilidades=me.getValue(mp.get(data_structs["skills"], i["id"]))
        #Para cada habilidad en la entrada de habilidades
        for j in lt.iterator(habilidades):
            key3=j["name"]
            value1 = mp.get(me.getValue(mp.get(me.getValue(value), "habilidades")), key3)
            if value1 is None:
                value2=(j["name"],1,int(j["level"]))
                mp.put(me.getValue(mp.get(me.getValue(value),"habilidades")), key3, value2)
                promedio=me.getValue(mp.get(me.getValue(value), "promedio_habilidad"))
                promedio=(promedio[0]+int(value2[2]),promedio[1]+1)
                mp.put(me.getValue(value), "promedio_habilidad", promedio)
            else:
                value2=me.getValue(value1)
                level=value2[2]+int(j["level"])
                value2=(j["name"],value2[1]+1,level)
                mp.put(me.getValue(mp.get(me.getValue(value),"habilidades")), key3, value2)
            if value2[1]>me.getValue(mp.get(me.getValue(value), "habilidad_mayor"))[1]:
                mp.put(me.getValue(value), "habilidad_mayor", value2)
            if value2[1]<me.getValue(mp.get(me.getValue(value), "habilidad_menor"))[1]:
                mp.put(me.getValue(value), "habilidad_menor", value2)
                promedio=me.getValue(mp.get(me.getValue(value), "promedio_habilidad"))
                promedio=(promedio[0]+int(value2[2]),promedio[1]+1)
                mp.put(me.getValue(value), "promedio_habilidad", promedio)
        empresa=mp.get(me.getValue(mp.get(me.getValue(value), "empresas")),i["company_name"])
        if empresa == None:
            mp.put(me.getValue(mp.get(me.getValue(value), "empresas")),i["company_name"],1)
        else:
            empresa=me.getValue(empresa)
            empresa+=1
            mp.put(me.getValue(mp.get(me.getValue(value), "empresas")),i["company_name"],empresa)
        empresa=mp.get(me.getValue(mp.get(me.getValue(value), "empresas")),i["company_name"])
        #TODO: Terminar de implementar el requerimiento
        if me.getValue(empresa)>me.getValue(mp.get(me.getValue(value), "empresa_mayor"))[1]:
            mp.put(me.getValue(value), "empresa_mayor", (i["company_name"],me.getValue(empresa)))
        elif me.getValue(empresa)==me.getValue(mp.get(me.getValue(value), "empresa_mayor"))[1]:
            if me.getValue(mp.get(me.getValue(value), "empresa_mayor"))[0]>i["company_name"]:
                mp.put(me.getValue(value), "empresa_mayor", (i["company_name"],me.getValue(empresa)))
        if me.getValue(empresa)<me.getValue(mp.get(me.getValue(value), "empresa_menor"))[1]:
            mp.put(me.getValue(value), "empresa_menor", (i["company_name"],me.getValue(empresa)))
        elif me.getValue(empresa)==me.getValue(mp.get(me.getValue(value), "empresa_menor"))[1]:
            if me.getValue(mp.get(me.getValue(value), "empresa_menor"))[0]>i["company_name"]:
                mp.put(me.getValue(value), "empresa_menor", (i["company_name"],me.getValue(empresa)))
        multilocation=mp.get(data_structs["multilocation"],i["id"])
        empresas_mas_localizaciones=me.getValue(mp.get(me.getValue(value), "empresas_mas_localizaciones"))
        if multilocation!=None and mp.contains(empresas_mas_localizaciones,i["company_name"])==False:
            if lt.size(me.getValue(multilocation))>1:
                mp.put(empresas_mas_localizaciones,i["company_name"],lt.size(me.getValue(multilocation)))         
    lista_final=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista_paises_cantidades):
        lista_temporal=lt.newList("ARRAY_LIST")
        key=i[0]
        value=me.getValue(mp.get(mapa_final,key))
        for j in lt.iterator(mp.keySet(value)):
            lt.addLast(lista_temporal, key)
            value1=me.getValue(mp.get(value,j))
            lt.addLast(lista_temporal, j)
            
            for k in ("habilidades","habilidad_mayor","habilidad_menor","promedio_habilidad","empresas","empresa_mayor","empresa_menor","empresas_mas_localizaciones"):
                value2=me.getValue(mp.get(value1,k))
                if k=="habilidades" or k=="empresas" or k=="empresas_mas_localizaciones":
                    lt.addLast(lista_temporal, mp.size(value2))
                elif k=="promedio_habilidad":
                    if value2[1]!=0:
                        value2=value2[0]/value2[1]
                    else:
                        value2=0
                    lt.addLast(lista_temporal, value2)
                elif k=="habilidad_mayor" or k=="habilidad_menor":
                    lt.addLast(lista_temporal, (value2[0],value2[1]))
                else:
                    lt.addLast(lista_temporal, value2)
        
        lt.addLast(lista_final, lista_temporal)
    return lt.size(lista_trabajos_final),mp.size(ciudades_cantidades),lt.getElement(lista_paises_cantidades,1),lt.getElement(lista_ciudades_cantidades,1),lista_final



def req_8(data_structs, nivel_experticia, divisa, fecha_ini, fecha_fin):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    lista_jobs=lt.newList("ARRAY_LIST")
    mapa_final_parte1=mp.newMap(15, maptype='PROBING', loadfactor=0.7)
    mp.put(mapa_final_parte1, "empresas", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    mp.put(mapa_final_parte1, "id_ofertas", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    mp.put(mapa_final_parte1, "paises", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    mp.put(mapa_final_parte1, "ciudades", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    mp.put(mapa_final_parte1, "pais_salario", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    mp.put(mapa_final_parte1, "salario",mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    mp.put(mapa_final_parte1, "valor_fijo", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    mp.put(mapa_final_parte1, "valor_nulo", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    mp.put(mapa_final_parte1, "pais_oferta_salarial",mp.newMap(100, maptype='PROBING', loadfactor=0.7))
    for i in lt.iterator(data_structs["jobs"]):
        if (i["experience_level"] == nivel_experticia.lower() and i["published_at"] >= date_to_iso(fecha_ini) and i["published_at"] <= date_to_iso(fecha_fin)) or (nivel_experticia.lower() == "indiferente" and i["published_at"] >= date_to_iso(fecha_ini) and i["published_at"] <= date_to_iso(fecha_fin)):
            salario = me.getValue(mp.get(data_structs["employment"], i["id"]))
            suma = 0
            contador=0
            divisa_salario=None
            valor_fijo=False
            if obtener_mapa_de_mapas(mapa_final_parte1, "pais_oferta_salarial", i["country_code"])==None:
                añadir_mapa_de_mapas(mapa_final_parte1, "pais_oferta_salarial", i["country_code"], (i["country_code"],
                                                                                                    0,
                                                                                                    mp.newMap(20,maptype="PROBING",loadfactor=0.7),
                                                                                                    mp.newMap(20,maptype="PROBING",loadfactor=0.7),
                                                                                                    mp.newMap(20,maptype="PROBING",loadfactor=0.7),
                                                                                                    0))
            
            tupla_mapa=me.getValue(obtener_mapa_de_mapas(mapa_final_parte1, "pais_oferta_salarial", i["country_code"]))
            
            if mp.contains(tupla_mapa[2],i["company_name"])==False:
                mp.put(tupla_mapa[2], i["company_name"], 1)
            if mp.contains(tupla_mapa[3],i["id"])==False:
                mp.put(tupla_mapa[3], i["id"], 1)
            valor=lt.size(me.getValue(mp.get(data_structs["skills"], i["id"])))+tupla_mapa[5]
            tupla=(tupla_mapa[0],tupla_mapa[1],tupla_mapa[2],tupla_mapa[3],tupla_mapa[4],valor)
            añadir_mapa_de_mapas(mapa_final_parte1, "pais_oferta_salarial", i["country_code"], tupla)
             
            for j in lt.iterator(salario):
                divisa_salario=j["currency_salary"]
                if divisa_salario==divisa:
                    if j["salary_from"] != "" and j["salary_to"] != "":
                        suma += int(j["salary_from"]) + int(j["salary_to"])
                        contador += 2
                    elif j["salary_from"] == j["salary_to"] and j["salary_from"] != "":
                        suma += int(j["salary_from"])
                        contador += 1
                        valor_fijo=True
                    else:
                        añadir_mapa_de_mapas(mapa_final_parte1, "valor_nulo", i["id"], 0)
                    
                        
            if divisa_salario!=None and contador!=0 and valor_fijo==False:
                salario = conversor_divisas(suma/contador, divisa_salario)
                lt.addLast(lista_jobs, i)
                i["salary"]=salario
                añadir_mapa_de_mapas(mapa_final_parte1, "id_ofertas", i["id"], i)
                añadir_mapa_de_mapas(mapa_final_parte1, "salario", i["id"], salario)
                if obtener_mapa_de_mapas(mapa_final_parte1, "paises", i["country_code"])==None:
                    añadir_mapa_de_mapas(mapa_final_parte1, "paises", i["country_code"], 1)
                else:
                    añadir_mapa_de_mapas(mapa_final_parte1, "paises", i["country_code"], me.getValue(obtener_mapa_de_mapas(mapa_final_parte1, "paises", i["country_code"]))+1)
                if obtener_mapa_de_mapas(mapa_final_parte1, "ciudades", i["city"])==None:
                    añadir_mapa_de_mapas(mapa_final_parte1, "ciudades", i["city"], 1)
                else:
                    añadir_mapa_de_mapas(mapa_final_parte1, "ciudades", i["city"], me.getValue(obtener_mapa_de_mapas(mapa_final_parte1, "ciudades", i["city"]))+1)
                if obtener_mapa_de_mapas(mapa_final_parte1, "empresas", i["company_name"])==None:
                    añadir_mapa_de_mapas(mapa_final_parte1, "empresas", i["company_name"], 1)
                else:
                    añadir_mapa_de_mapas(mapa_final_parte1, "empresas", i["company_name"], me.getValue(obtener_mapa_de_mapas(mapa_final_parte1, "empresas", i["company_name"]))+1)
                mapa_final=obtener_mapa_de_mapas(mapa_final_parte1, "pais_oferta_salarial", i["country_code"])
                mapa_final=me.getValue(mapa_final)
                mp.put(mapa_final[4], i["id"], salario)
                valor=mapa_final[1]+salario
                mapa_final=(mapa_final[0],valor,mapa_final[2],mapa_final[3],mapa_final[4],mapa_final[5])
                añadir_mapa_de_mapas(mapa_final_parte1, "pais_oferta_salarial", i["country_code"], mapa_final)
            elif divisa_salario!=None and contador==0:
                añadir_mapa_de_mapas(mapa_final_parte1, "valor_nulo", i["id"], 0)
            elif valor_fijo==True:
                salario=conversor_divisas(suma/contador, divisa_salario)
                añadir_mapa_de_mapas(mapa_final_parte1, "valor_fijo", i["id"], salario)
    lista_1=lt.newList("ARRAY_LIST")
    llaves_paises=mp.keySet(me.getValue(mp.get(mapa_final_parte1, "pais_oferta_salarial")))
    lista_1_sin_0=lt.newList("ARRAY_LIST")
    for i in lt.iterator(llaves_paises):
        value=me.getValue(obtener_mapa_de_mapas(mapa_final_parte1, "pais_oferta_salarial", i))
        if mp.size(value[4])!=0:
            value_1=value[1]/mp.size(value[4])
        else:
            value_1=0
        if mp.size(value[3])!=0:
            value_5=value[5]/mp.size(value[3])
        else:
            value_5=0
        lt.addLast(lista_1, (i,value_1,mp.size(value[2]),mp.size(value[3]),mp.size(value[4]),value_5))
        if mp.size(value[4])!=0:
            lt.addLast(lista_1_sin_0, (i,value_1,mp.size(value[2]),mp.size(value[3]),mp.size(value[4]),value_5))
    #TODO: LISTADO DE MAYOR A MENOR PARTE 1
    lista_1=merg.sort(lista_1_sin_0,sort_req8)
    retorno_parte_1=(mp.size(me.getValue(mp.get(mapa_final_parte1, "empresas"))),
                     lt.size(lista_jobs),
                     mp.size(me.getValue(mp.get(mapa_final_parte1, "paises"))),
                     mp.size(me.getValue(mp.get(mapa_final_parte1, "ciudades"))),
                     mp.size(me.getValue(mp.get(mapa_final_parte1, "salario"))),
                     mp.size(me.getValue(mp.get(mapa_final_parte1, "valor_fijo"))),
                     mp.size(me.getValue(mp.get(mapa_final_parte1, "valor_nulo"))),
                     lista_1)
    mayor_menor=(lt.firstElement(lista_1_sin_0),lt.lastElement(lista_1_sin_0))
    mapa_mayor=mp.newMap(20, maptype='PROBING', loadfactor=0.7)
    mapa_menor=mp.newMap(20, maptype='PROBING', loadfactor=0.7)
    for i in lt.iterator(lista_jobs):
        if i["country_code"]==mayor_menor[0][0]:
            print("hola")
            if mp.contains(mapa_mayor,"pais")==False:
                mp.put(mapa_mayor, "pais",mayor_menor[0][0])
            if mp.contains(mapa_mayor,"total",)==False:
                mp.put(mapa_mayor, "total", mayor_menor[0][3])
            if mp.contains(mapa_mayor,"salario")==False:
                mp.put(mapa_mayor, "salario", mayor_menor[0][1])
            if mp.contains(mapa_mayor,"ciudades")==False:
                mp.put(mapa_mayor, "ciudades", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
            if obtener_mapa_de_mapas(mapa_mayor,"ciudades",i["city"])==None:
                añadir_mapa_de_mapas(mapa_mayor,"ciudades",i["city"],0)
            añadir_mapa_de_mapas(mapa_mayor,"ciudades",i["city"],me.getValue(obtener_mapa_de_mapas(mapa_mayor,"ciudades",i["city"]))+1)
            if mp.contains(mapa_mayor,"empresas")==False:
                mp.put(mapa_mayor, "empresas", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
            if obtener_mapa_de_mapas(mapa_mayor,"empresas",i["company_name"])==None:
                añadir_mapa_de_mapas(mapa_mayor,"empresas",i["company_name"],0)
            añadir_mapa_de_mapas(mapa_mayor,"empresas",i["company_name"],me.getValue(obtener_mapa_de_mapas(mapa_mayor,"empresas",i["company_name"]))+1)
            salario_actual=0
            cantidad=0
            for j in lt.iterator(me.getValue(mp.get(data_structs["employment"],i["id"]))):
                 if j["salary_from"]!="" and j["salary_to"]!="":
                     salario_actual=int(j["salary_from"])+int(j["salary_to"])
                     cantidad+=2
                 elif j["salary_from"]!="" and j["salary_to"]=="":
                        salario_actual=int(j["salary_from"])
                        cantidad+=1
            print(salario_actual)
            if cantidad!=0:
                salario_actual=salario_actual/cantidad
            print(salario_actual)
            if mp.contains(mapa_mayor,"salario_mayor")==False:
                mp.put(mapa_mayor, "salario_mayor", 0)
            if me.getValue(mp.get(mapa_mayor,"salario_mayor"))<salario_actual:
                mp.put(mapa_mayor, "salario_mayor", salario_actual)
            if mp.contains(mapa_mayor,"salario_menor")==False:
                mp.put(mapa_mayor, "salario_menor", 10000)
            if me.getValue(mp.get(mapa_mayor,"salario_menor"))>salario_actual and salario_actual!=0:
                mp.put(mapa_mayor, "salario_menor", salario_actual)
            if mp.contains(mapa_mayor,"habilidades")==False:
                mp.put(mapa_mayor, "habilidades", lt.size(me.getValue(mp.get(data_structs["skills"], i["id"]))))
        elif i["country_code"]==mayor_menor[1][0]:
            if mp.contains(mapa_menor,"pais")==False:
                mp.put(mapa_menor, "pais", mayor_menor[1][0])
            if mp.contains(mapa_menor,"total",)==False:
                mp.put(mapa_menor, "total", mayor_menor[1][3])
            if mp.contains(mapa_menor,"salario")==False:
                mp.put(mapa_menor, "salario", mayor_menor[1][1])
            if mp.contains(mapa_menor,"ciudades")==False:
                mp.put(mapa_menor, "ciudades", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
            if obtener_mapa_de_mapas(mapa_menor,"ciudades",i["city"])==None:
                añadir_mapa_de_mapas(mapa_menor,"ciudades",i["city"],0)
            añadir_mapa_de_mapas(mapa_menor,"ciudades",i["city"],me.getValue(obtener_mapa_de_mapas(mapa_menor,"ciudades",i["city"]))+1)
            if mp.contains(mapa_menor,"empresas")==False:
                mp.put(mapa_menor, "empresas", mp.newMap(100, maptype='PROBING', loadfactor=0.7))
            if obtener_mapa_de_mapas(mapa_menor,"empresas",i["company_name"])==None:
                añadir_mapa_de_mapas(mapa_menor,"empresas",i["company_name"],0)
            añadir_mapa_de_mapas(mapa_menor,"empresas",i["company_name"],me.getValue(obtener_mapa_de_mapas(mapa_menor,"empresas",i["company_name"]))+1)
            salario_actual=0
            cantidad=0
            for j in lt.iterator(me.getValue(mp.get(data_structs["employment"],i["id"]))):
                 if j["salary_from"]!="" and j["salary_to"]!="":
                     salario_actual=int(j["salary_from"])+int(j["salary_to"])
                     cantidad+=2
                 elif j["salary_from"]!="" and j["salary_to"]=="":
                        salario_actual=int(j["salary_from"])
                        cantidad+=1
            if cantidad!=0:
                salario_actual=salario_actual/cantidad
            if mp.contains(mapa_menor,"salario_mayor")==False:
                mp.put(mapa_menor, "salario_mayor", 0)
            if me.getValue(mp.get(mapa_menor,"salario_mayor"))<salario_actual:
                mp.put(mapa_menor, "salario_mayor", salario_actual)
            if mp.contains(mapa_menor,"salario_menor")==False:
                mp.put(mapa_menor, "salario_menor", 10000)
            if me.getValue(mp.get(mapa_menor,"salario_menor"))>salario_actual and salario_actual!=0:
                mp.put(mapa_menor, "salario_menor", salario_actual)
            if mp.contains(mapa_menor,"habilidades")==False:
                mp.put(mapa_menor, "habilidades", lt.size(me.getValue(mp.get(data_structs["skills"], i["id"]))))
    lista_mayor=lt.newList("ARRAY_LIST")
    lista_menor=lt.newList("ARRAY_LIST")
    contador=0
    llaves=("pais","total","salario","ciudades","empresas","salario_mayor","salario_menor","habilidades")
    for i in llaves:
        if i=="ciudades" or i=="empresas":
            lt.addLast(lista_mayor,mp.size(me.getValue(mp.get(mapa_mayor,i))))
        else:
            lt.addLast(lista_mayor,me.getValue(mp.get(mapa_mayor,i)))
    for i in llaves:
        if i=="ciudades" or i=="empresas":
            lt.addLast(lista_menor,mp.size(me.getValue(mp.get(mapa_menor,i))))
        else:
            lt.addLast(lista_menor,me.getValue(mp.get(mapa_menor,i)))
    retorno_parte_2=(lista_mayor,lista_menor)
    return retorno_parte_1,retorno_parte_2
            
            
        
def conversor_divisas(salary, divisa):
    if divisa.lower() == "usd":
        return salary * 1
    elif divisa.lower() == "eur":
        return salary * 1.19
    elif divisa.lower() == "gbp":
        return salary * 1.27
    elif divisa.lower() == "pln":
        return salary * 0.25
    elif divisa.lower() == "chf":
        return salary * 1.11
    else:
        return None

def sort_req8(data_1, data_2):
    if data_1[1]==data_2[1]:
        if data_1[0]>data_2[0]:
            return True
        else:
            return False
    else:
        return data_1[1]>data_2[1]

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

def date_to_iso(fecha:str):
    return fecha+"T00:00:00.000Z"
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

def añadir_mapa_de_mapas(mapa, key1, key2, value):
    """
    Función que añade un valor a un mapa de mapas
    mapa: mapa de mapas
    key1: llave del mapa grande
    key2: llave del mapa pequeño
    value: valor a añadir
    """
    return mp.put(me.getValue(mp.get(mapa,key1)), key2, value)
def obtener_mapa_de_mapas(mapa, key1, key2):
    """
    Función que obtiene un valor de un mapa de mapas
    mapa: mapa de mapas
    key1: llave del mapa grande
    key2: llave del mapa pequeño
    """
    return mp.get(me.getValue(mp.get(mapa,key1)),key2)
def sort_dates_empresa(empresa1, empresa2):
    if empresa1["published_at"]==empresa2["published_at"]:
        if empresa1["company_name"]>empresa2["company_name"]:
            return True
        else:
            return False
    else:
        return empresa1["published_at"]>empresa2["published_at"]
        
def sort_dates(fecha_1:int, fecha_2:int):
    """
    Función encargada de comparar dos fechas
    """
    fechas1=fecha_1["published_at"]
    fechas2=fecha_2["published_at"]
    return fechas1>fechas2
    
def date_to_unix(fecha:str):
    """
    Función que convierte una fecha en formato "%Y-%m-%dT%H:%M:%S.%fZ" a un entero en tiempo unix
    """ 
    timestamp_dt = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%fZ")
    unix_timestamp = timestamp_dt.timestamp()
    timestamp_int = int(unix_timestamp)
    return timestamp_int

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
def sort_cantidades_ciudades(pais1, pais2):
    if pais1[1]==pais2[1]:
        if pais1[0]>pais2[0]:
            return True
        else:
            return False
    else:
        return pais1[1]>pais2[1]
