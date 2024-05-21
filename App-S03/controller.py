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
globalSufijo = "small"
prueba = "Rapidez"


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
                "model": None
                }
    control["model"] = model.new_data_structs()
    return control
    


# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    catalog = control['model']
    if prueba == "Rapidez":
        start_time = get_time()
    else:
        tracemalloc.start()
        start_memory = get_memory()

    
    loadEmployments_types(catalog)
    loadJobs(catalog)
    loadMultilocations(catalog)
    loadSkills(catalog)
    
    
    sorted_jobs = model.sort_th(control)
    
    if prueba == "Rapidez":
        end_time = get_time()
        return control, delta_time(start_time, end_time), prueba, sorted_jobs
    else:
        stop_memory = get_memory()
        tracemalloc.stop()
        A_memory = delta_memory(stop_memory, start_memory)
        return control, A_memory, prueba, sorted_jobs

    
    
    

def loadEmployments_types(catalog):
    file = cf.data_dir + 'data/'+globalSufijo+'-employments_types.csv'
    
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=";")
    
    for employment_type in input_file:
        fijo = False
        if employment_type["salary_from"] == "" or employment_type["salary_to"] == "":
            promedio_salarial = 0
            fijo = None
        else:
            if float(employment_type["salary_from"]) ==  float(employment_type["salary_to"]):
                fijo = True
            promedio_salarial = (float(employment_type["salary_from"]) + float(employment_type["salary_to"]))/2
        employment_type["fijo"] = fijo
        employment_type["promedio_salarial"] = promedio_salarial
        model.add_data(catalog,"employments_types", employment_type)
    return catalog

def loadJobs(catalog):
    file = cf.data_dir + 'data/'+globalSufijo+'-jobs.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=";")
    #conteo = 0
    for job in input_file:
        #conteo += 1
        model.add_data(catalog,"jobs", job)
    #    if conteo == 200:
    #        break
    return catalog



def loadMultilocations(catalog):
    file = cf.data_dir + 'data/'+globalSufijo+'-multilocations.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'),delimiter=";")
    for multilocation in input_file:
        model.add_data(catalog,"multilocations", multilocation)
    return catalog

def loadSkills(catalog):
    file = cf.data_dir + 'data/'+globalSufijo+'-skills.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=";")
    for skill in input_file:
        model.add_data(catalog,"skills", skill)
    return catalog

def cambiar_pruebas(respuesta):
    global prueba
    prueba = respuesta
    return prueba

def cambiarTamañoMuestra(sufijo):
    global globalSufijo
    globalSufijo = sufijo
        
def three_first_last(data_structs):
    first, last, size= model.three_first_last(data_structs)
    return first, last, size
# Funciones de ordenamiento

def sort(control, sort_crit):
    """
    Ordena los datos del modelo
    """
    
    #TODO: Llamar la función del modelo para ordenar los datos
    sorted_list = model.sort(control, sort_crit)
    return sorted_list
def get_sort_crit(tipo):
    sort_crit = model.get_sort_crit(tipo)
    return sort_crit


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,n,pais,experticia):
    """
    Retorna el resultado del requerimiento 1

    """
    global prueba
    prueba=prueba

    if prueba == "Rapidez":
        start_time = get_time()
    else:
        tracemalloc.start()
        start_memory = get_memory()
     
    final= model.req_1(control["model"],n,pais,experticia)

    if prueba == "Almacenamiento":

        stop_memory = get_memory()
        tracemalloc.stop()
        A_memory = delta_memory(stop_memory, start_memory)
        return final,A_memory,prueba
       
    else:
        
        end_time = get_time()
        return final, delta_time(start_time, end_time),prueba
    


def req_2(control, offer_number, company_name, city):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    catalog = control["model"]["specific_jobs"]
    function = model.req_2(catalog, offer_number, company_name, city)
    if function[1] !=None:
        size = function[1]
    else:
        size = 0
    end_time = get_time()
    time= delta_time(start_time, end_time)
    function = function[0]
    return size, function, time


def req_3(control,empresa,fecha1,fecha2):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    global prueba
    prueba=prueba

    if prueba == "Rapidez":
        start_time = get_time()
    else:
        tracemalloc.start()
        start_memory = get_memory()
     
    final= model.req_3(control["model"],empresa,fecha1,fecha2)

    if prueba == "Almacenamiento":

        stop_memory = get_memory()
        tracemalloc.stop()
        A_memory = delta_memory(stop_memory, start_memory)
        return final,A_memory,prueba
       
    else:
        
        end_time = get_time()
        return final, delta_time(start_time, end_time),prueba




def req_4(control, pais, fecha_inicial,fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    #model.req_4(control["model"]["specific_jobs"], pais, fecha_inicial,fecha_final)
    global prueba
    prueba = prueba
    if prueba == "Rapidez":
        start_time = get_time()
    else:
        tracemalloc.start()
        start_memory = get_memory()
    cant_empresas, cant_ciudades, cant_ofertas,max_city ,ofertas_max, min_city,ofertas_min, filtered_offers= model.req_4(control["model"]["specific_jobs"], pais, fecha_inicial,fecha_final)
    
    if prueba == "Rapidez":
        end_time = get_time()
        return cant_empresas, cant_ciudades, cant_ofertas,max_city ,ofertas_max, min_city,ofertas_min, filtered_offers, delta_time(start_time, end_time), prueba
    else:
        stop_memory = get_memory()
        tracemalloc.stop()
        A_memory = delta_memory(stop_memory, start_memory)
        return cant_empresas, cant_ciudades, cant_ofertas,max_city ,ofertas_max, min_city,ofertas_min, filtered_offers, A_memory, prueba
    
    return cant_empresas, cant_ciudades, cant_ofertas,max_city ,ofertas_max, min_city,ofertas_min, filtered_offers

def manipular_ofertas_filtradas(filtered_offers):
    firstf, lastf, cinco = model.manipular_ofertas_filtradas(filtered_offers)
    return firstf, lastf, cinco

def req_5(control, city, first_date, last_date):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    catalog = control["model"]["specific_jobs"]
    function = model.req_5(catalog, city, first_date, last_date)
    
    dicc_aux = {}
    cont = 0
    
    if function[1] !=None:
        size = function[1]
    else:
        size = 0
    #for i in model.lt.iterator(function):
    #for a in function["elements"]:
        #for i in a["elements"]:
    if function[0] != None:
        for i in model.lt.iterator(function[0]):
                if i["company_name"] not in dicc_aux:
                    dicc_aux[i["company_name"]] = 1 
                    cont +=1
                else:
                    dicc_aux[i["company_name"]] += 1  
    
        if len(dicc_aux)>0:
            upper_offer = max(dicc_aux.values())
            minor_offer = min(dicc_aux.values())


            for i in dicc_aux.items():
                if i[1] == upper_offer:
                    upper_offer0 = i[0]
                if i[1] == minor_offer: 
                    minor_offer0 = i[0]       
        else: 
            upper_offer = None
            minor_offer = None
            upper_offer0 =  None
            minor_offer0 = None
    else:
        upper_offer = None
        minor_offer = None
        upper_offer0 =  None
        minor_offer0 = None
    end_time = get_time()
    time= delta_time(start_time, end_time)
    function = function[0]
            
        
    return size, function, cont, upper_offer, minor_offer, upper_offer0, minor_offer0, time

def req_6(control,n,año,experticia):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    global prueba
    prueba=prueba

    if prueba == "Rapidez":
        start_time = get_time()
    else:
        tracemalloc.start()
        start_memory = get_memory()
     
    final= model.req_6(control["model"],n,año,experticia)

    if prueba == "Almacenamiento":

        stop_memory = get_memory()
        tracemalloc.stop()
        A_memory = delta_memory(stop_memory, start_memory)
        return final,A_memory,prueba
       
    else:
        
        end_time = get_time()
        return final, delta_time(start_time, end_time),prueba
    
    


def req_7(control, country_number, month, year):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    catalog = control["model"]
    function = model.req_7(catalog, country_number, month, year)
    dicc_aux = {}
    cont = 0
    dicc_skillsXExpertiz = {}
    dicc_skillsXExpertizLess = {}
    dicc_empresas = {}
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    size = model.lt.size(function[0]) #Sacamos el numero de ofertas totales
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    """
    Agregamos las ciudades y las veces que se repiten a un diccionario para luego contarlas
    y sacar la ciudad con mayor numero de ofertas
    """
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    for i in model.lt.iterator(function[0]):
        if i["city"] not in dicc_aux:
            dicc_aux[i["city"]] = 1 
            cont +=1

           
        else:
            dicc_aux[i["city"]] += 1
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    """
    Realizamos el mismo proceso pero con los paises, esta vez es mas facil 
    porque ya los habiamos tratado en el model
    """    
    if len(function[1])>0:
        max_country = max(function[1].values())
        for i in function[1].items():
            if i[1] == max_country:
                 max_country0 = i[0]
    else:
        max_country = None
        max_country0 = None
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    """
    Sacamos la ciudad con mayor y menor numero de ofertas
    """
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    if len(dicc_aux)>0:
        max_city = max(dicc_aux.values())       
        for i in dicc_aux.items():
            if i[1] == max_city:
                 max_city0 = i[0]   
    else:
        max_city = None
        max_city0 = None
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    """
    Sacamos la habilidad mas y menos solicitada por nivel de experticia
    """  
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    
    if len(function[2])>0:
        for i in function[2].items():
            mayores = max(i[1].values())
            menores = min(i[1].values())
            auxxx ={}
            auxx2 = {}
        
            for j in i[1].items():
                if j[1]==mayores:
                    auxxx[j[0]]= mayores
                if j[1]==menores:
                    auxx2[j[0]]=menores

            dicc_skillsXExpertiz[i[0]] = auxxx
            dicc_skillsXExpertizLess[i[0]] = auxx2
    
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    """
    Agregamos el numero de ofertas de trabajo por nivel de experticia
    --------OJO: como estoy utilizando diccionarios de diccionarios
                  no saco el mayor y menor aqui, sino en view para facilitarlo
    
    """
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    
    for i in model.lt.iterator(function[0]):
        aux = {}
        
        for j in function[2].items():
            if j[0] == i["experience_level"]:
                

                if i["company_name"] not in aux :
                    aux[i["company_name"]]=1
                else:
                    aux[i["company_name"]]=+1
            else:
                if i["company_name"] not in aux :
                    aux[i["company_name"]]=1
                else:
                    aux[i["company_name"]]=+1
            dicc_empresas[j[0]] = aux
            
    end_time = get_time()
    time= delta_time(start_time, end_time)
          
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    return int(size), function, cont, max_country, max_country0, max_city, max_city0, dicc_skillsXExpertiz, dicc_skillsXExpertizLess, dicc_empresas, time
    


def req_8(control, lvl_exp, divisa, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    global prueba
    prueba = prueba
    if prueba == "Rapidez":
        start_time = get_time()
    else:
        tracemalloc.start()
        start_memory = get_memory()
    
    
    cant_empresas, total_ofertas, cant_paises , cant_ciudades, cant_of_con_salario, cant_of_con_salario_fijo, cant_of_sin_salario, paises_orden, paises = model.req_8(control["model"], lvl_exp, divisa, fecha_inicial, fecha_final)
    if prueba == "Rapidez":
        end_time = get_time()
        return cant_empresas, total_ofertas, cant_paises , cant_ciudades, cant_of_con_salario, cant_of_con_salario_fijo, cant_of_sin_salario, paises_orden, paises, delta_time(start_time, end_time), prueba
    else:
        stop_memory = get_memory()
        tracemalloc.stop()
        A_memory = delta_memory(stop_memory, start_memory)
        return cant_empresas, total_ofertas, cant_paises , cant_ciudades, cant_of_con_salario, cant_of_con_salario_fijo, cant_of_sin_salario, paises_orden, paises, A_memory, prueba
    
    #return cant_empresas, total_ofertas, cant_paises , cant_ciudades, cant_of_con_salario, cant_of_con_salario_fijo, cant_of_sin_salario, paises_orden, paises

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
