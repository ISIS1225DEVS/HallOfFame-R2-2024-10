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
import datetime
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
from currency_converter import CurrencyConverter

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

prueba = "Rapidez"

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog= { "jobs"  : None,
              "specific_jobs":None,
              "employments_types" : None,
              "multilocations" : None,
              "skills" : None
              }

    catalog['employments_types'] = mp.newMap(numelements=203560,maptype="CHAINING", loadfactor= 4)
    catalog['jobs'] = mp.newMap(numelements = 259837, maptype="CHAINING", loadfactor= 4)
    catalog['multilocations'] = mp.newMap(numelements=244937, maptype="CHAINING", loadfactor= 4)
    catalog['skills'] = mp.newMap(numelements=577165, maptype="CHAINING", loadfactor= 4)
    catalog['specific_jobs'] = mp.newMap(numelements=259837, maptype="CHAINING", loadfactor= 4)
    
    return catalog




# Funciones para agregar informacion al modelo

def add_data(data_structs, part, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    #TODO: Crear la función para agregar elementos a una lista
    if part == "employments_types":
        #key = f"{data['id']}"
        #fijo = False
        #if data["salary_from"] == "" or data["salary_to"] == "":
        #    promedio_salarial = 0
        #    fijo = None
        #else:
        #    if float(data["salary_from"]) ==  float(data["salary_to"]):
        #        fijo = True
        #    promedio_salarial = (float(data["salary_from"]) + float(data["salary_to"]))/2
        
        
        
        #key= f"{data['id']};{promedio_salarial};{data["currency_salary"]};{fijo}"
        key= f"{data['id']}"
       
    elif part == "jobs":
        key = f"{data['id']}"
        #key= f"{data['id']}_{data['country_code']}_{data['city']}_{data['experience_level']}_{data['company_name']}"
        keyS = f"{data['country_code']};{data['city']};{data['company_name']};{data['experience_level']};{data['published_at'][:10]}"
        existkeyS = mp.contains(data_structs["specific_jobs"],keyS)
        if not existkeyS:
            mp.put(data_structs["specific_jobs"], keyS ,  lt.newList("ARRAY_LIST"))
        """  
        entry = mp.get(data_structs["specific_jobs"], keyS)
        existkey = mp.contains(me.getValue(entry),key)
        if not existkey:
            mp.put(data_structs["specific_jobs"], keyS , lt.newList("ARRAY_LIST"))
        """
        entry = mp.get(data_structs["specific_jobs"], keyS)
        lt.addLast(me.getValue(entry), data) 
            
            
       
        
        
    elif part == "multilocations":
        #key = f"{data['id']}"
        key = f"{data['id']};{data['city']}"
        
    
    else:
        #key = f"{data['id']}"
        key = f"{data['id']}"
    
    
    existkey = mp.contains(data_structs[part],key)
    if not existkey:
        mp.put(data_structs[part], key, lt.newList("ARRAY_LIST"))
        
    entry = mp.get(data_structs[part], key)
    
    lt.addLast(me.getValue(entry), data)
    


    
# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs,part,  id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    if mp.contains(data_structs[part], id):
        entry = mp.get(data_structs[part], id)
        return me.getValue(entry)
    else:
        return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass

def three_first_last(data_structs):
    size = lt.size(data_structs)
    first_three = lt.subList(data_structs, 1, 3)
    last_three = lt.subList(data_structs,size-3,3)
    
    return first_three, last_three, size

def get_sort_crit(tipo):
    if tipo  == "mayor_a_menor_fecha":
        return sort_crit_mayor_a_menor_fecha
    if tipo == "req4":
        return sort_crit_req4

def sort_crit_mayor_a_menor_fecha(oferta1, oferta2):
    
    """
    fecha0= datetime.strptime(lt.getElement(oferta1,1)["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    fecha1= datetime.strptime(lt.getElement(oferta2,1)["published_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    if fecha0.year > fecha1.year:
        return True
    elif fecha0.year < fecha1.year:
        return False
    else:
        if fecha0.month > fecha1.month:
            return True
        elif fecha0.month < fecha1.month:
            return False
        else:
            if fecha0.day > fecha1.day:
                return True
            elif fecha0.day < fecha1.day:
                return False
            else:
                if fecha0.hour > fecha1.hour:
                    return True
                elif fecha0.hour < fecha1.hour:
                    return False
                else:
                    if fecha0.minute > fecha1.minute:
                        return True
                    elif fecha0.minute < fecha1.minute:
                        return False
                    else:
                        return True
    """
    
    Y1,M1,D1 = lt.getElement(oferta1,1)["published_at"].split("-")
    Y1 = int(Y1)
    M1 = int(M1)
    D1 = int(D1[:2])
    Y2,M2,D2 = lt.getElement(oferta2,1)["published_at"].split("-")
    Y2 = int(Y2)
    M2 = int(M2)
    D2 = int(D2[:2])
    if Y1 > Y2:
        return True
    elif Y1<Y2:
        return False
    else:
        if M1 > M2:
            return True
        elif M1 < M2:
            return False
        else:
            if D1 > D2:
                return True
            elif D1 < D2:
                return False
            else:
                return True

def sort_recientes_req1(oferta1, oferta2):
    date1=datetime.strptime(oferta1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
    date2= datetime.strptime(oferta2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
    if date1>date2:
        return True
    elif date1<date2:
        return False
    else:
        return None

def sort_crit_req3(oferta1,oferta2):
    date1=datetime.strptime(oferta1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
    date2= datetime.strptime(oferta2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
    if date1>date2:
        return True
    elif date1<date2:
        return False
    else: 
        if oferta1["country_code"]>oferta2["country_code"]:
            return True
        elif oferta1["country_code"]<=oferta2["country_code"]:
            return False

            
def sort_crit_req4(oferta1, oferta2):
    
    Y1,M1,D1 = oferta1["published_at"].split("-")
    Y1 = int(Y1)
    M1 = int(M1)
    D1 = int(D1[:2])
    Y2,M2,D2 = oferta2["published_at"].split("-")
    Y2 = int(Y2)
    M2 = int(M2)
    D2 = int(D2[:2])
    if Y1 > Y2:
        return False
    elif Y1<Y2:
        return True
    else:
        if M1 > M2:
            return False
        elif M1 < M2:
            return True
        else:
            if D1 > D2:
                return False
            elif D1 < D2:
                return True
            else:
                if oferta1["company_name"] > oferta2["company_name"]:
                    return False
                elif oferta1["company_name"] < oferta2["company_name"]:
                    return True
                else:
                    return False
                
def sort_crit_req6(oferta1,oferta2):
    total1= oferta1["total_ofertas"]
    total2=oferta2["total_ofertas"]
    if total1>total2:
        return True
    elif total1<total2:
        return False
    else:
        None
   
    
    
    
    
def sort_th(data):
            
    
    
    sort_crit = get_sort_crit("mayor_a_menor_fecha")
    lst  = mp.valueSet(data["model"]["jobs"])
    lst1 = lt.newList("ARRAY_LIST")
    for i in lt.iterator(lst):
        lt.addLast(lst1, i)
            
    sorted_list = sort(lst1, sort_crit)
    return sorted_list
    
def sort_crit_req8(pais1, pais2):
    if pais1[1] > pais2[1]:
        return True
    elif pais1[1] < pais2[1]:
        return False
    else:
        return True
    
    
def req_1(data_structs,n,pais,experticia):
    """
    Función que soluciona el requerimiento 1

    """
    catalogo= mp.keySet(data_structs["specific_jobs"])
    lista= lt.newList("ARRAY_LIST")
    conteo_pais= 0
    
    

    for key in lt.iterator(catalogo):
        keysplit= key.split(";")
        if experticia == keysplit[3] and pais == keysplit[0]:
            pareja=mp.get(data_structs["specific_jobs"],key)
            valor=me.getValue(pareja)
            for element in lt.iterator(valor):
                lt.addLast(lista, element)
        if pais==keysplit[0]:
            pareja=mp.get(data_structs["specific_jobs"],key)
            valor=me.getValue(pareja)
            for element in lt.iterator(valor):
                conteo_pais +=1
                 
    
        
    lista_final=merg.sort(lista,sort_recientes_req1)
    if lt.size(lista_final) == 0:
    
        sublista = None
    if lt.size(lista_final) < n:
        sublista = lista_final
    else:
        sublista = lt.subList(lista_final,1,n)
    return sublista,lt.size(lista_final),conteo_pais
    
        

    


def req_2(data_structs, offer_number, company_name, city):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    offers = lt.newList("ARRAY_LIST")
    final = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(mp.keySet(data_structs)):
        if company_name in i and city in i:
            filterr = mp.get(data_structs, i)
            adds = me.getValue(filterr)
            for offer in lt.iterator(adds):
                    
                    lt.addLast(offers, offer)
    
            
    #if lt.size(offers) >= 10:
    if lt.size(offers) >= 10:
        sb1 = lt.subList(offers, 1, 5)
        for zc in lt.iterator(sb1):
            lt.addLast(final, zc)
           
        
        sb2 = lt.subList(offers, (lt.size(offers)-5), 5)
        for zt in lt.iterator(sb2):
            lt.addLast(final, zt )    
                
       # primeros_cinco = lt.addLast(final, lt.subList(offers, 1, 5))
       # ultimos_cinco = lt.addLast(final, lt.subList(offers, lt.size(offers)-5, lt.size(offers)))
     
        

    elif lt.size(offers) < 10 and lt.size(offers)>0 : 
        if lt.size(offers)>= int(offer_number):
            final = lt.subList(offers, 1, int(offer_number)) 
        else:
            final = offers
    else:
        final = None
    return final, lt.size(offers)


def req_3(data_structs,empresa,fecha1,fecha2):
    """
    Función que soluciona el requerimiento 3
    """
    catalogo= mp.keySet(data_structs["specific_jobs"])
    lista= lt.newList("ARRAY_LIST")
    fecha_1= datetime.strptime(fecha1,"%Y-%m-%d")
    fecha_2= datetime.strptime(fecha2,"%Y-%m-%d")
    contador_mid=0
    contador_senior=0
    contador_junior=0
    mid=str("mid")
    junior= str("junior")
    senior= str("senior")

    for key in lt.iterator(catalogo):
        keysplit= key.split(";")
        fecha_of=datetime.strptime(keysplit[4],"%Y-%m-%d")
        if empresa == keysplit[2]:
            if fecha_of >= fecha_1 and fecha_of <= fecha_2 and keysplit[3]== mid:
                pareja=mp.get(data_structs["specific_jobs"],key)
                valor=me.getValue(pareja)
                for element in lt.iterator(valor):
                    lt.addLast(lista, element)
                    contador_mid += 1
            elif fecha_of >= fecha_1 and fecha_of <= fecha_2 and keysplit[3]== junior:
                pareja=mp.get(data_structs["specific_jobs"],key)
                valor=me.getValue(pareja)
                for element in lt.iterator(valor):
                    lt.addLast(lista, element)
                    contador_junior += 1
            elif fecha_of >= fecha_1 and fecha_of <= fecha_2 and keysplit[3]== senior:
                pareja=mp.get(data_structs["specific_jobs"],key)
                valor=me.getValue(pareja)
                for element in lt.iterator(valor):
                    lt.addLast(lista, element)   
                    contador_senior += 1
                    
                
    lista_final=merg.sort(lista,sort_crit_req3)
    return contador_junior,contador_mid,contador_senior,lt.size(lista_final),lista_final



def req_4(data_structs, pais, fecha_inicial,fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    
    #-------------------------------------------
    conteo_empresas = 0
    #-------------------------------------------
    
    
    filtered_keys = lt.newList("ARRAY_LIST")
    
    for key in lt.iterator(mp.keySet(data_structs)):
        
        fechaOf = datetime.strptime(key[-10:] ,"%Y-%m-%d")
        #if key[-10:] == "2023-06-28":
        #    print("stop")
        if pais in key:
            if fechaOf.year >= fecha_inicial[0] and fechaOf.year <= fecha_final[0]:
                if fechaOf.month >= fecha_inicial[1] and fechaOf.month <= fecha_final[1]:
                    if (fechaOf.month*30 + fechaOf.day) >= (fecha_inicial[1]*30 + fecha_inicial[2]) and (fechaOf.month*30 + fechaOf.day) <= (fecha_final[1]*30 + fecha_final[2]):
                        lt.addLast(filtered_keys, key)
                
    if lt.size(filtered_keys) == 0:
        return False, False, False, False, False, False, False, False
    filtered_offers= lt.newList("ARRAY_LIST")
    
    empresas = mp.newMap(numelements= 1000, maptype="PROBING", loadfactor=0.5)
    ciudades = mp.newMap(numelements= 700, maptype= "PROBING", loadfactor=0.5)
    
    for key in lt.iterator(filtered_keys):
        key_splited = key.split(";")
        if len(key_splited) > 5:
            print("habemus un problema")
        
        mp.put(empresas, key_splited[2], 0)
        
        existscity = mp.contains(ciudades, key_splited[1])
        if not existscity:
            mp.put(ciudades, key_splited[1],lt.newList("ARRAY_LIST"))
        
        
            
        entry = mp.get(data_structs, key)
        entry_ciudad = mp.get(ciudades, key_splited[1])
         
        lst = me.getValue(entry)
        lst_ciudad = me.getValue(entry_ciudad)
        
        for offer in lt.iterator(lst):
            lt.addLast(filtered_offers, offer)
            lt.addLast(lst_ciudad, offer)
        
    max_city = None
    min_city = None
    maxc = 0
    minc = None
    cant_ciudades = 0
    
    for city in lt.iterator(mp.keySet(ciudades)):
        entry = mp.get(ciudades, city)
        #print(city)
        if entry != None:
            cant_ciudades +=1
            cityOf = me.getValue(entry)
            
            if minc == None:
                minc = lt.size(cityOf)
                min_city = city
        
            size = lt.size(cityOf)
        
            if size > maxc:
                maxc = size
                max_city = city
            if size <= minc:
                minc = size
                min_city = city
    
    sort_crit = get_sort_crit("req4")
    
    sort(filtered_offers, sort_crit)
    #for offer in lt.iterator(filtered_offers):
    #    print(offer["published_at"][:10], offer["company_name"])
        
           
    cant_empresas = lt.size(mp.keySet(empresas))
    
    cant_ofertas = lt.size(filtered_offers)
    
    
    return cant_empresas, cant_ciudades, cant_ofertas, max_city,lt.size(me.getValue(mp.get(ciudades,max_city))), min_city, lt.size(me.getValue(mp.get(ciudades,min_city))), filtered_offers
    
def manipular_ofertas_filtradas(filtered_offers):
    
    

    cinco = False
    if lt.size(filtered_offers) > 10:
        firstf = lt.subList(filtered_offers,1,5)
        lastf = lt.subList(filtered_offers, lt.size(filtered_offers)-5, 5)
        cinco = True
        return firstf, lastf, cinco
    
    return None, None, cinco
        
    


def req_5(data_structs, city, first_date, last_date):

    
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    offers = lt.newList("ARRAY_LIST")
    final = lt.newList("ARRAY_LIST")
    
    primer_limite = first_date
    primer_limite0= datetime.strptime(primer_limite, "%Y-%m-%d")

    ultimo_limite = last_date
    ultimo_limite0 = datetime.strptime(ultimo_limite, "%Y-%m-%d")
    
    for i in lt.iterator(mp.keySet(data_structs)):
        if city in i:
            slide = i.split(";")
            slide = slide[-1]
            fecha_dt = datetime.strptime( slide, "%Y-%m-%d")
            if primer_limite0<= fecha_dt and fecha_dt<= ultimo_limite0:
                filterr = mp.get(data_structs, i)
                adds = me.getValue(filterr)
                for offer in lt.iterator(adds):
                    
                    lt.addLast(offers, offer)
    
    
    if lt.size(offers) !=0:
        sort_crit = get_sort_crit("req4")
    
        sort(offers, sort_crit)
    
    
    if lt.size(offers) >= 10:
        sb1 = lt.subList(offers, 1, 5)
        for zc in lt.iterator(sb1):
            lt.addLast(final, zc)
           
        
        sb2 = lt.subList(offers, (lt.size(offers)-5), 5)
        for zt in lt.iterator(sb2):
            lt.addLast(final, zt )
        
        
        
    elif lt.size(offers)<10 and lt.size(offers)>0:
        final = offers
    elif lt.size(offers)==0:
        final = None
    
    size = lt.size(offers)
    
    return final, size
    


def req_6(data_structs,n,año,experticia):

    """
    Función que soluciona el requerimiento 6
    """
    catalogo= mp.keySet(data_structs["specific_jobs"])
    lista= lt.newList("ARRAY_LIST")
    empresas = mp.newMap(numelements= 1000, maptype="PROBING", loadfactor=0.5)
    ciudades = mp.newMap(numelements= 700, maptype= "PROBING", loadfactor=0.5)
    
    for key in lt.iterator(catalogo):
        keysplit= key.split(";")
        fecha=keysplit[4]
        añoF,mesF,diaF= fecha.split("-")
        añoF= int(añoF)
        if experticia != str("indiferente"):
            if año == añoF and experticia == keysplit[3]:
                parejaE=mp.get(data_structs["specific_jobs"],key)
                valorE=me.getValue(parejaE)
                for e in lt.iterator(valorE):
                    lt.addLast(lista, e)
        else:
            if año == añoF:
                parejaE=mp.get(data_structs["specific_jobs"],key)
                valorE=me.getValue(parejaE)
                for e in lt.iterator(valorE):
                    lt.addLast(lista, e)

    lista_salario=encontrar_salario(lista,data_structs)
    add_mapas(lista_salario,ciudades,empresas)
    mayor_menor_ciudad= max_min(ciudades)
    mayor_menor_empresa= max_min(empresas)
    lista_P=lista_ciudades(ciudades)
    sorted_list=merg.sort(lista_P,sort_crit_req6)
    
    if lt.size(sorted_list) >= n:
        sublista= lt.subList(sorted_list,1,n)
    else:
        sublista=sorted_list


    return sublista,mayor_menor_ciudad,mayor_menor_empresa,lt.size(lista_P)

def lista_ciudades(ciudades):
    
    lista_ciudades=mp.keySet(ciudades)
    lista_nueva= lt.newList("ARRAY_LIST")
    mapa_empresa_ciudad= mp.newMap(numelements= 1000, maptype="PROBING", loadfactor=0.5)
    for ciudad in lt.iterator(lista_ciudades):
        maximo=0
        minimo=float("inf")
        mejor= None
        peor=None
        pareja=mp.get(ciudades,ciudad)
        valor= me.getValue(pareja)
        llave=me.getKey(pareja)
        salario=0
        for e in lt.iterator(valor):
            dict={}
            size=lt.size(valor)
            empresa= e["company_name"]
            salario += e["salario"]
            pais= e["country_code"]
            if e["salary_to"]:
                salary_to= float(e["salary_to"])
                if salary_to>maximo:
                    maximo= salary_to
                    mejor=e["title"]
            if e["salary_from"]:
                salary_from= float(e["salary_from"])
                if salary_from < minimo:
                    minimo= salary_from
                    peor= e["title"]
            if mp.contains(mapa_empresa_ciudad,empresa) == False:
                valorT=lt.newList("ARRAY_LIST")
                lt.addLast(valorT,e)
                mp.put(mapa_empresa_ciudad,empresa,valorT)
            else:
                parejaE=mp.get(mapa_empresa_ciudad,empresa)
                valorE=me.getValue(parejaE)
                lt.addLast(valorE,e)

       
        mejor_empresa,peor_empresa,conteo_mejor,conteo_menor,num_empresas= max_min(mapa_empresa_ciudad)

        promedio= salario/lt.size(valor)
        dict["salario"]=promedio
        dict["total_ofertas"]=size
        dict["ciudad"]=llave
        dict["pais"]=pais
        dict["mejor_oferta"]=mejor
        dict["peor_oferta"]=peor
        dict["Empresa_con_mas_ofertas"]=mejor_empresa
        dict["conteos"]=conteo_mejor
        dict["total_empresas"]=num_empresas
        lt.addLast(lista_nueva,dict)

    return lista_nueva


def add_mapas(lista,ciudades,empresas):
    for element in lt.iterator(lista):
        ciudad=element["city"]
        if mp.contains(ciudades,ciudad) == False:
            valorL=lt.newList("ARRAY_LIST")
            lt.addLast(valorL,element)
            mp.put(ciudades,ciudad,valorL)
        else:
            pareja=mp.get(ciudades,ciudad)
            valorC=me.getValue(pareja)
            lt.addLast(valorC,element)
                
        empresa=element["company_name"]
        if mp.contains(empresas,empresa) == False:
            valorT=lt.newList("ARRAY_LIST")
            lt.addLast(valorT,element)
            mp.put(empresas,empresa,valorT)
        else:
            parejaE=mp.get(empresas,empresa)
            valorE=me.getValue(parejaE)
            lt.addLast(valorE,element)

def max_min(mapa):
    maximo=0
    VariableMX= None
    VariableMN=None
    minimo=float("inf")
    llaves=mp.keySet(mapa)
    sizeTotal=lt.size(llaves)
    for llave in lt.iterator(llaves):
        pareja= mp.get(mapa,llave)
        valorP=me.getValue(pareja)
        size=lt.size(valorP)
        if size > maximo:
            maximo=size
            VariableMX=str(llave)

        if size < minimo:
            minimo=size
            VariableMN=str(llave)

    return VariableMX,VariableMN,maximo,minimo,sizeTotal

def encontrar_salario(lista,data_structs):
    for element in lt.iterator(lista):
        Global=0
        id= element["id"]
        mapa= data_structs["employments_types"]
        pareja=mp.get(mapa,id)
        info= me.getValue(pareja)
        for j in lt.iterator(info):
            salario_from= j["salary_from"]
            salario_to=j["salary_to"]
            if j["salary_from"] and j["salary_to"]:
                Global += (float(j["salary_from"]) + float(j["salary_to"]))/2

            elif j["salary_from"]:
                Global += float(j["salary_from"])
            elif j["salary_to"]:
                Global += float(j["salary_to"])
            else:
                Global += 0.0

        promedio = Global/lt.size(info)
        element["salario"] = promedio
        element["salary_from"]=salario_from
        element["salary_to"]=salario_to

    return lista

def req_7(data_structs, country_number, month, year):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
#######################################################################################################################
#######################################################################################################################
################### Incializar lo que vamos a utilizar ################################################################
#######################################################################################################################
#######################################################################################################################
    offers = lt.newList("ARRAY_LIST")
    dicc_country = {}
    conteo_countries= {}
    dicc_final = {}
    lista_final = lt.newList("ARRAY_LIST")
    dicc_experience = {}
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#################################### Filtrar las ofertas por mes y año ################################################
#######################################################################################################################
#######################################################################################################################
    for skills_it in lt.iterator(mp.keySet(data_structs["specific_jobs"])):
        slide = skills_it.split(";")
        slide = slide[-1]
        fecha_dt = datetime.strptime( slide, "%Y-%m-%d")
        mes = fecha_dt.month
        anio = fecha_dt.year
        if int(mes)== int(month) and int(year) == int(anio):
            filterr = mp.get(data_structs["specific_jobs"], skills_it)

            adds = me.getValue(filterr)
            for offer in lt.iterator(adds):
                    
                lt.addLast(offers, offer)
    #Ya quedo esta parte, NO TOCAR
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
################################# Contar cuantos paises aparecen y cuantas veces ######################################
#######################################################################################################################
#######################################################################################################################
    #for a in offers["elements"]:
        #for i in a["elements"]:
    for i in lt.iterator(offers):
            if i["country_code"] not in dicc_country:
                lista = []
                lista.append(i)
                dicc_country[i["country_code"]] = lista       
            else:
                dicc_country[i["country_code"]].append(i)       
            if i["country_code"]not in conteo_countries:
                conteo_countries[i["country_code"]]=1
            else:      
                conteo_countries[i["country_code"]]+=1
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
############################# Sacar solo el numero de paises que nos piden ############################################
#######################################################################################################################
#######################################################################################################################
    if len(conteo_countries)>0:
        for i in range(int(country_number)):
            if len(conteo_countries)>0:
                maximo = max(conteo_countries.values())
                for i in conteo_countries.items():
                    if i[1]==maximo:
                        nombre_maximo = i[0]
                dicc_final[nombre_maximo]=maximo
                conteo_countries.pop(nombre_maximo)
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
    for i in dicc_country.items():
        if i[0] in dicc_final:
            for j in i[1]:
                lt.addLast(lista_final, j)
    # si esta guardando en lista final
#######################################################################################################################         
#######################################################################################################################
#######################################################################################################################
####################################################################################################################### 

    for i in lt.iterator(lista_final):
        #for j in lt.iterator(mp.keySet(data_structs["skills"])):
#######################################################################################################################         
#######################################################################################################################
#######################################################################################################################
####################################################################################################################### 
            if "junior" == i["experience_level"]:
                if i["experience_level"] not in dicc_experience:
                    dicc_sec = {}
                    dicc_experience["junior"] = dicc_sec
                else:
                    dicc_sec = dicc_experience["junior"]
                """
                if i["id"] in j:
                    filterr_sk = mp.get(data_structs["skills"], j)
                    adds_sk = me.getValue(filterr_sk)
                    for b in adds_sk["elements"]:
                            #for b in a["name"]:
                """
                skill = me.getValue(mp.get(data_structs["skills"], i["id"] ))          
                for sk_j in lt.iterator(skill):
                    #print(sk_j)
                    if sk_j["name"] not in dicc_sec:
                        dicc_sec[sk_j["name"]  ] = 1
                    else:
                        dicc_sec[sk_j["name"]  ] += 1
                dicc_experience["junior"] = dicc_sec
                
                
    #######################################################################################################################         
    #######################################################################################################################
    #######################################################################################################################
    ####################################################################################################################### 
            if "mid" == i["experience_level"]:
                if i["experience_level"] not in dicc_experience:
                    dicc_sec1 = {}
                    dicc_experience["mid"] = dicc_sec1
                else:
                    dicc_sec1 = dicc_experience["mid"]
                """
                if i["id"] in j:
                    filterr_sk1 = mp.get(data_structs["skills"], j)
                    adds_sk1 = me.getValue(filterr_sk1)
                    for b in adds_sk1["elements"]:
                            #for b in a["name"]:
                """
                skill = me.getValue(mp.get(data_structs["skills"], i["id"] ))  
                for sk_jr in lt.iterator(skill):
                    #print(sk_jr)
                    if sk_jr["name"] not in dicc_sec1:
                        dicc_sec1[sk_jr["name"]  ] = 1
                    else:
                        dicc_sec1[sk_jr["name"] ] += 1
                dicc_experience["mid"] = dicc_sec1
    #######################################################################################################################         
    #######################################################################################################################
    #######################################################################################################################
    ####################################################################################################################### 
            if "senior" == i["experience_level"]:
                if i["experience_level"] not in dicc_experience:
                    dicc_sec2 = {}
                    dicc_experience["senior"] = dicc_sec2
                else:
                    dicc_sec2 = dicc_experience["senior"]

                """
                if i["id"] in j:
                    filterr_sk2 = mp.get(data_structs["skills"], j)
                    adds_sk2 = me.getValue(filterr_sk2)
                    for b in adds_sk2["elements"]:
                            #for b in a["name"]:
                """           
                skill = me.getValue(mp.get(data_structs["skills"], i["id"] ))  
                for sk_jh in lt.iterator(skill):
                    #print(sk_jh)
                    if sk_jh["name"] not in dicc_sec2:
                        dicc_sec2[sk_jh["name"]  ] = 1
                    else:
                        dicc_sec2[sk_jh["name"]  ] += 1
                dicc_experience["mid"] = dicc_sec2
    
#######################################################################################################################         
#######################################################################################################################
#######################################################################################################################
####################################################################################################################### 
    
    return lista_final, dicc_final, dicc_experience
    


def req_8(catalog,  lvl_exp, divisa, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    filtered_keys_ET = lt.newList("ARRAY_LIST")
    
    
    #for key_ET in lt.iterator(mp.keySet(catalog["employments_types"])):
    #    if divisa in key_ET:
    #        if lvl_exp != "indiferente":
    #            if lvl_exp in key_ET:
    #                lt.addLast(filtered_keys_ET, key_ET)
    #        else:
    #            lt.addLast(filtered_keys_ET, key_ET)
            
    filtered_keys_JB = lt.newList("ARRAY_LIST")
    
    for key_JB in lt.iterator(mp.keySet(catalog["specific_jobs"])):
        key_splited = key_JB.split(";")
        fechaOf = datetime.strptime(key_JB[-10:] ,"%Y-%m-%d")
        
        if fechaOf.year>= fecha_inicial[0] and fechaOf.year <= fecha_final[0]:
            if fechaOf.month >= fecha_inicial[1] and fechaOf.month <= fecha_final[1]:
                if (fechaOf.month*30 + fechaOf.day) >= (fecha_inicial[1]*30 + fecha_inicial[2]) and (fechaOf.month*30 + fechaOf.day) <= (fecha_final[1]*30 + fecha_final[2]):
                    if lvl_exp == key_splited[3]:
                        lt.addLast(filtered_keys_JB, key_JB)
                    elif lvl_exp == "indiferente":
                        lt.addLast(filtered_keys_JB, key_JB)
        
    
    filtered_offers = lt.newList("ARRAY_LIST")
    
    c= CurrencyConverter()
    if lt.size(filtered_keys_JB) == 0:
        
        return False, False, False ,False, False, False, False, False, False
        
        
    paises = mp.newMap(numelements=200, maptype= "PROBING", loadfactor=0.5)
    empresas = mp.newMap(numelements=1000, maptype="PROBING", loadfactor=0.5)
    ciudades = mp.newMap(numelements= 2000, maptype="PROBING", loadfactor=0.5)
    ofertas_con_salario = lt.newList("ARRAY_LIST")
    ofertas_sin_salario = lt.newList("ARRAY_LIST")
    
    
    
       
    #for key_Jb in lt.iterator(filtered_keys_JB):
    for key_Jb in lt.iterator(filtered_keys_JB):
        key_splited = key_Jb.split(";")
        
        existscountry = mp.contains(paises,key_splited[0])
        
        if not existscountry:
            mp.put(paises, key_splited[0], mp.newMap(numelements=1000, maptype="PROBING", loadfactor=0.5))
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "promedio_salarial", 0)
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "suma_salarios", 0)
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "cantidad_salarios", 0)
            
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "promedio_habilidades", 0)
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "suma_habilidades", 0)
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "cantidad_habilidades", 0)
            
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "empresas_presentes", mp.newMap(numelements=1000, maptype="PROBING", loadfactor= 0.5))
            
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "mayor_oferta", (None,None))
            mp.put(me.getValue(mp.get(paises, key_splited[0])), "menor_oferta", (None,None))
            
        existscity = mp.contains(me.getValue(mp.get(paises, key_splited[0])), key_splited[1])
        if not existscity:
            mp.put(me.getValue(mp.get(paises, key_splited[0])), key_splited[1], mp.newMap(numelements=1000, maptype="PROBING", loadfactor=0.5))
            mp.put(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])), "con_salario", lt.newList("ARRAY_LIST"))
            mp.put(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])), "sin_salario", lt.newList("ARRAY_LIST"))
            mp.put(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])), "con_salario_fijo", lt.newList("ARRAY_LIST"))
        
        
        for offer in lt.iterator(me.getValue(mp.get(catalog["specific_jobs"], key_Jb))):
            employment_type = me.getValue(mp.get(catalog["employments_types"], offer["id"]))
            skill = me.getValue(mp.get(catalog["skills"], offer["id"]))
            
            
            #if lt.size(skill) > 1:
            #    print("HABEMUS UN PROBLEMA")
            #    print(lt.size(skill))
            
            for i in range(1, lt.size(skill)+1):
                #OJOOOO esta leyendo todas las habilidades aquí
                #if lt.getElement(employment_type, i)["currency_salary"] == divisa or lt.getElement(employment_type, i)["currency_salary"] == "":
                skill_level = lt.getElement(skill, i)
                mp.put(me.getValue(mp.get(paises, key_splited[0])),"suma_habilidades", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"suma_habilidades")) + int(skill_level["level"]))
                mp.put(me.getValue(mp.get(paises, key_splited[0])),"cantidad_habilidades", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"cantidad_habilidades")) + 1)
            
            salario_promedio_oferta = 0
            conteo_salario = 0
            
            for i in range(1, lt.size(employment_type)+1):
                #salario_usd = 
                """
                mp.put(empresas, key_splited[2], 0)
                mp.put(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"empresas_presentes")),key_splited[2], 0)
                mp.put(ciudades, key_splited[1], 0)
                print(mp.keySet(ciudades))
                    #print(offer)
                    
                if lt.getElement(employment_type,i)["fijo"] == False :
                    salario_usd = convertir_divisas(lt.getElement(employment_type,i)["promedio_salarial"], lt.getElement(employment_type,i)["currency_salary"],c)
                    salario_promedio_oferta += salario_usd #Salario promedio por oferta
                    conteo_salario += 1
                    lt.getElement(employment_type,i)["promedio_salarial"] = salario_usd
                    lt.getElement(employment_type,i)["currency_salary"] = "usd"
                    mp.put(me.getValue(mp.get(paises, key_splited[0])),"suma_salarios", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"suma_salarios")) + salario_usd)
                    mp.put(me.getValue(mp.get(paises, key_splited[0])),"cantidad_salarios", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"cantidad_salarios")) + 1)
                    if i == 1:
                        lt.addLast(me.getValue(mp.get(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])),"con_salario")), offer)
        
                elif lt.getElement(employment_type,i)["fijo"] == True :
                    salario_usd = convertir_divisas(lt.getElement(employment_type,i)["promedio_salarial"], lt.getElement(employment_type,i)["currency_salary"],c)
                    salario_promedio_oferta += salario_usd  #Salario promedio por oferta
                    conteo_salario += 1
                    lt.getElement(employment_type,i)["promedio_salarial"] = salario_usd
                    lt.getElement(employment_type,i)["currency_salary"] = "usd"
                    mp.put(me.getValue(mp.get(paises, key_splited[0])),"suma_salarios", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"suma_salarios")) + salario_usd)
                    mp.put(me.getValue(mp.get(paises, key_splited[0])),"cantidad_salarios", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"cantidad_salarios")) + 1)
                    if i == 1:
                        lt.addLast(me.getValue(mp.get(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])),"con_salario_fijo")), offer)
                
           
          
        #    lt.addLast(me.getValue(mp.get((me.getValue(mp.get(paises, key_splited[0]))), key_splited[1])),offer)

                else:
                    if i == 1:
                        lt.addLast(me.getValue(mp.get(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])),"sin_salario")), offer)
                """
                if lt.getElement(employment_type, i)["currency_salary"] == divisa or lt.getElement(employment_type, i)["currency_salary"] == "":
                    
                    mp.put(empresas, key_splited[2], 0)
                    mp.put(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"empresas_presentes")),key_splited[2], 0)
                    mp.put(ciudades, key_splited[1], 0)
                    #print(mp.keySet(ciudades))
                    #print(offer)
                    
                    if lt.getElement(employment_type,i)["fijo"] == False :
                        salario_usd = convertir_divisas(lt.getElement(employment_type,i)["promedio_salarial"], lt.getElement(employment_type,i)["currency_salary"],c)
                        salario_promedio_oferta += salario_usd #Salario promedio por oferta
                        conteo_salario += 1
                        #lt.getElement(employment_type,i)["promedio_salarial"] = salario_usd
                        #lt.getElement(employment_type,i)["currency_salary"] = "usd"
                        mp.put(me.getValue(mp.get(paises, key_splited[0])),"suma_salarios", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"suma_salarios")) + salario_usd)
                        mp.put(me.getValue(mp.get(paises, key_splited[0])),"cantidad_salarios", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"cantidad_salarios")) + 1)
                        if i == 1:
                            lt.addLast(me.getValue(mp.get(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])),"con_salario")), offer)
            
                    elif lt.getElement(employment_type,i)["fijo"] == True :
                        salario_usd = convertir_divisas(lt.getElement(employment_type,i)["promedio_salarial"], lt.getElement(employment_type,i)["currency_salary"],c)
                        salario_promedio_oferta += salario_usd  #Salario promedio por oferta
                        conteo_salario += 1
                        #lt.getElement(employment_type,i)["promedio_salarial"] = salario_usd
                        #lt.getElement(employment_type,i)["currency_salary"] = "usd"
                        mp.put(me.getValue(mp.get(paises, key_splited[0])),"suma_salarios", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"suma_salarios")) + salario_usd)
                        mp.put(me.getValue(mp.get(paises, key_splited[0])),"cantidad_salarios", me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"cantidad_salarios")) + 1)
                        if i == 1:
                            lt.addLast(me.getValue(mp.get(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])),"con_salario_fijo")), offer)
                
           
          
        #    lt.addLast(me.getValue(mp.get((me.getValue(mp.get(paises, key_splited[0]))), key_splited[1])),offer)

                    else:
                        if i == 1:
                            lt.addLast(me.getValue(mp.get(me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),key_splited[1])),"sin_salario")), offer)
                
            if conteo_salario != 0: 
                salario_promedio_oferta = salario_promedio_oferta/conteo_salario          
            if  me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"mayor_oferta"))[0] == None:
                mp.put(me.getValue(mp.get(paises, key_splited[0])),"mayor_oferta", (salario_promedio_oferta, offer))
            if  me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"menor_oferta"))[0] == None:
                if salario_promedio_oferta !=0:
                    mp.put(me.getValue(mp.get(paises, key_splited[0])),"menor_oferta", (salario_promedio_oferta, offer))
        
            if salario_promedio_oferta > me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"mayor_oferta"))[0]:
                mp.put(me.getValue(mp.get(paises, key_splited[0])),"mayor_oferta", (salario_promedio_oferta, offer))
            if me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"menor_oferta"))[0] != None:
                if salario_promedio_oferta < me.getValue(mp.get(me.getValue(mp.get(paises, key_splited[0])),"menor_oferta"))[0] and salario_promedio_oferta !=0:
                    mp.put(me.getValue(mp.get(paises, key_splited[0])),"menor_oferta", (salario_promedio_oferta, offer))
            
        
        
    #                       A PARTIR DE AQUÍ SE COMIENZA LA MANIPULACIÓN DE LOS RESULTADOS DE LA CONSULTA
    
    cant_of_con_salario = 0
    cant_of_con_salario_fijo = 0
    cant_of_sin_salario = 0
    
    paises_orden = lt.newList("ARRAY_LIST")
    
    for key_country in lt.iterator(mp.keySet(paises)):
        if key_country == None:
            print("ABBIAMO UN PROBLEMA")
            
        country = me.getValue(mp.get(paises, key_country))
        if me.getValue(mp.get( country, "suma_salarios")) != 0 and me.getValue(mp.get( country, "cantidad_salarios")) != 0:
            mp.put(country, "promedio_salarial", (me.getValue(mp.get( country, "suma_salarios"))/me.getValue(mp.get( country, "cantidad_salarios"))))
        
        if me.getValue(mp.get( country, "suma_habilidades")) != 0 and me.getValue(mp.get( country, "cantidad_habilidades")) != 0:
            mp.put(country, "promedio_habilidades", (me.getValue(mp.get( country, "suma_habilidades"))/me.getValue(mp.get( country, "cantidad_habilidades"))))
        
        #print(f"{me.getValue(mp.get( country, 'empresas_presentes'))} --------------- Esta es")
        mp.put(country, "empresas_presentes" , lt.size(mp.keySet(me.getValue(mp.get( country, "empresas_presentes")))))
        
        if mp.isEmpty(country):
            mp.remove(paises, key_country)
            
        
        lt.addLast(paises_orden , (key_country, me.getValue(mp.get( country, "promedio_salarial")))) 
        borrar = ""
        for key_city in lt.iterator(mp.keySet(country)):
            no =["suma_salarios","cantidad_salarios","promedio_salarial","cantidad_habilidades","suma_habilidades","promedio_habilidades", "mayor_oferta", "menor_oferta", "empresas_presentes"]
            if key_city not in no:
                cant_of_con_salario += lt.size(me.getValue(mp.get(me.getValue(mp.get(country, key_city)), "con_salario")))
                cant_of_con_salario_fijo += lt.size(me.getValue(mp.get(me.getValue(mp.get(country, key_city)), "con_salario_fijo")))
                cant_of_sin_salario +=  lt.size(me.getValue(mp.get(me.getValue(mp.get(country, key_city)), "sin_salario")))
                if lt.size(me.getValue(mp.get(me.getValue(mp.get(country, key_city)), "con_salario"))) == 0 and lt.size(me.getValue(mp.get(me.getValue(mp.get(country, key_city)), "con_salario_fijo"))) == 0 and lt.size(me.getValue(mp.get(me.getValue(mp.get(country, key_city)), "sin_salario"))) == 0: 
                    borrar += "True"
                else:
                    borrar += "False"
        
        if "False" not in borrar:
            mp.remove(paises, key_country)
            lt.removeLast(paises_orden)
                    
                  
         
        
    total_ofertas = cant_of_sin_salario + cant_of_con_salario + cant_of_con_salario_fijo 
    
    paises_orden = sort(paises_orden, sort_crit_req8)
    #for pais in lt.iterator(paises_orden):
    #    print(pais)
    return lt.size(mp.keySet(empresas)), total_ofertas, mp.size(paises) , lt.size(mp.keySet(ciudades)), cant_of_con_salario, cant_of_con_salario_fijo, cant_of_sin_salario, paises_orden, paises

def convertir_divisas(salario_a_convertir, divisa, c):
   
    if divisa == "usd":
        return salario_a_convertir
    else:
        
        divisa = str.upper(divisa)
        #c= CurrencyConverter()
        #print(c.currencies)
        salario_convertido = c.convert(salario_a_convertir, divisa,  'USD')
        #print(salario_a_convertir)
        return salario_convertido
           
    
"""
def convertir_divisas(salario_a_convertir, divisa):
    #print(divisa)
    
    if divisa == "usd":
        return salario_a_convertir
    else:
        
        divisa = str.upper(divisa)
        c= CurrencyConverter()
        #print(c.currencies)
        salario_convertido = c.convert(salario_a_convertir, divisa,  'USD')
        #print(salario_a_convertir)
        return salario_convertido
"""   
            
        
        


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


def sort(data_structs, sort_crit):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    sorted_list = merg.sort(data_structs, sort_crit)
    return sorted_list