import threading
from datetime import datetime as dt
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
from additional import ilegalHandling as ile
import time 
from datetime import datetime as dt
import pytz

default_limit = 1000
sys.setrecursionlimit(default_limit*100)

def getIdentical(ARRLiA, ARRLiB):
    # Sacemos los tamaños otra vez
    ARRLiA = ile.EnsureADTLi(ARRLiA)
    ARRLiB = ile.EnsureADTLi(ARRLiB)    
    sizeA = lt.size(ARRLiA) ## Sacar el tamaño de las ARRAY_LISTS 
    sizeB = lt.size(ARRLiB)
    if sizeA > sizeB:
        larger = ARRLiA
        smaller = ARRLiB
    elif sizeB > sizeA:
        larger = ARRLiB
        smaller = ARRLiA
    # Ahora metamos todas las llaves del más grande en un mapa
    largerSize = int(lt.size(larger))
    IdMap = mp.newMap(numelements= (largerSize*(1 + 0.1)),
                        maptype='PROBING',
                        loadfactor=0.5,
                        )
    for element in lt.iterator(larger):
        # Dado que son Ids no nos importa casos de repetición (pues no los hay)
        mp.put(IdMap, element, element)
        # Suena estúpido pero nos va a ayudar un CHINGO
    
    common = lt.newList('ARRAY_LIST')
    for element in lt.iterator(smaller):
        if mp.contains(IdMap, element):
            lt.addLast(common, element)

    return common
    '''
    # Plan Z1 - Una puta mierda
    ARRLiA = ile.EnsureADTLi(ARRLiA)
    ARRLiB = ile.EnsureADTLi(ARRLiB)    
    sizeA = lt.size(ARRLiA) ## Sacar el tamaño de las ARRAY_LISTS 
    sizeB = lt.size(ARRLiB)
    if sizeA > sizeB:
        larger = ARRLiA
        smaller = ARRLiB
    elif sizeB > sizeA:
        larger = ARRLiB
        smaller = ARRLiA
    common = lt.newList("ARRAY_LIST")
    for element in lt.iterator(smaller):
        pos = lt.isPresent(larger, element)
        if pos != 0:
            largerEle = lt.getElement(larger, pos)
            lt.addLast(common, largerEle)
    
    return common
    '''
    '''
    # Plan Z: 
    ARRLiA = ile.EnsureADTLi(ARRLiA)
    ARRLiB = ile.EnsureADTLi(ARRLiB)
    ARRLiA = ARRLiA['elements']
    ARRLiB = ARRLiB['elements']
    common = list(set(ARRLiA) & set(ARRLiB)) # https://stackoverflow.com/questions/62721107/fastest-way-to-find-the-common-item-between-two-lists-in-python
    commonF = ile.Rpckg(common)
    return commonF
    '''
    '''
    # Plan A (No funcó)
    ARRLiA = ile.EnsureADTLi(ARRLiA)
    ARRLiB = ile.EnsureADTLi(ARRLiB)
    # Dado que acá queremos hacer la menor cantidad de O(K)s hacermos:
    sizeA = lt.size(ARRLiA) ## Sacar el tamaño de las ARRAY_LISTS 
    sizeB = lt.size(ARRLiB)
    if sizeA > sizeB:
        larger = ARRLiA
        smaller = ARRLiB
    elif sizeB > sizeA:
        larger = ARRLiB
        smaller = ARRLiA
    # Vamos a organizar la más larga (por ID/STRING)
    largeSorted = merg.sort(larger, ASCII_CRIT)
    print(largeSorted)
    # Ahora vamos a buscar la que tenga menos llaves en la que tenga más
    common  = []
    for singleId in lt.iterator(smaller):
        # Vamos a usar binary search para esto
        largerEle = largeSorted['elements']
        index = ASCIIBinSearch(largerEle, singleId)
        if index != -1:
            common.append(largerEle[index])
            #? lt.addLast(common, lt.getElement(largeSorted, index+1)) se hizo el todo intento, no funcionó\
                
    common = ile.Rpckg(common)
    return common
    '''

    
def getDoubleCriteria(fullJobsMap, IdList, keytoGrab, coincidence):
    None
    pass
        
def getFullInfos(map, IDList):
    '''
    Saca la información completa badado en una lista de IDs y la retorna cómo una lista
    '''
    IDList = ile.EnsureADTLi(IDList)
    fullInfos = lt.newList("ARRAY_LIST")
    for idi in lt.iterator(IDList):
        fullDic = mp.get(map, idi) ## Sacamos cada llave del mapa
        fullInfo =  fullDic['value'] ## Accedemos toda la info
        lt.addLast(fullInfos, fullInfo)
        
    return fullInfos

def getKeysByFullDate(dateMap, FullDate: str):
    '''Recibe MAPA, y una fecha "YYY-MM-DD" cómo STRING y lo busca dentro del mapa de fechas. 
    -> Regresa: 'ARRAY_LIST' con todas las llaves que cumplen con año'''
    dateTrup = parseStrDate(FullDate)
    keySet = mp.keySet(dateMap) ##! KeySet devuelve un Single_Linked
    year, month, day = dateTrup[0], dateTrup[1], dateTrup[2]
    meetsCriteria = lt.newList("ARRAY_LIST")
    for key in lt.iterator(keySet):
        DateKey = dt.fromisoformat(key)
        DateKeyYear = DateKey.year
        DateKeyMonth = DateKey.month
        DateKeyDay = DateKey.day
        if (DateKeyYear == year) and (DateKeyMonth == month) and (DateKeyDay == day):
            lt.addLast(meetsCriteria, key)
    
    return meetsCriteria
   
def getKeyRangeByFullDates(dateMap, StartFullDate: str, EndFullDate: str):
    '''Recibe MAPA, y una fecha "YYY-MM-DD" cómo STRING y lo busca dentro del mapa de fechas. 
    -> Regresa: 'ARRAY_LIST' con todas las llaves que cumplen con año'''
    startDate = dt.strptime(StartFullDate, '%Y-%m-%d')
    endDate = dt.strptime(EndFullDate, '%Y-%m-%d')
    keySet = mp.keySet(dateMap) ##! KeySet devuelve un Single_Linked
    meetsCriteria = lt.newList("ARRAY_LIST")
    for key in lt.iterator(keySet):
        dateKey = dt.fromisoformat(key)  
        dateKey = dateKey.replace(tzinfo=None)
        if startDate <= dateKey <= endDate:
            lt.addLast(meetsCriteria, key)
    
    return meetsCriteria

def getKeyRangeByFullDates_p(dateMap, startDate, endDate):
    '''Recibe MAPA, y una fecha "YYY-MM-DD" cómo STRING y lo busca dentro del mapa de fechas. 
    -> Regresa: 'ARRAY_LIST' con todas las llaves que cumplen con año'''
    keySet = mp.keySet(dateMap) ##! KeySet devuelve un Single_Linked
    meetsCriteria = lt.newList("ARRAY_LIST")
    for key in lt.iterator(keySet):
        dateKey = dt.fromisoformat(key)  
        dateKey = dateKey.replace(tzinfo=None)
        if startDate <= dateKey <= endDate:
            lt.addLast(meetsCriteria, key)
    
    return meetsCriteria
   
def getKeysByYearMonth(dateMap, year, month):
    '''Recibe MAPA, un año y un mes cómo str o int y lo busca dentro del mapa de fechas. 
    -> Regresa: 'ARRAY_LIST' con todas las llaves que cumplen con año'''
    year = int(year)
    month = int(month)
    keySet = mp.keySet(dateMap) ##! KeySet devuelve un Single_Linked
    ymKeys = lt.newList("ARRAY_LIST")
    for key in lt.iterator(keySet):
        DateKey = dt.fromisoformat(key)
        DateKeyYear = DateKey.year
        DateKeyMonth = DateKey.month
        if (DateKeyYear == year) and (DateKeyMonth == month):
            lt.addLast(ymKeys, key)            
    return ymKeys

def getKeysByYear(dateMap, year):
    '''Recibe MAPA, un año cómo str o int y lo busca dentro del mapa de fechas. 
    -> Regresa: 'ARRAY_LIST' con todas las llaves que cumplen con año'''
    year = int(year)
    keySet = mp.keySet(dateMap) ##! KeySet devuelve un Single_Linked
    yearKeys = lt.newList("ARRAY_LIST")
    for key in lt.iterator(keySet):
        DateKey = dt.fromisoformat(key)
        DateKeyYear = DateKey.year
        if DateKeyYear == year:
            lt.addLast(yearKeys, key)            
    return yearKeys

def parseStrDate(date_str):
    """
    Recibe un String del tipo YYY-MM-DD y lo parsea a una Trupla (YYYY , MM, DD) de integers.
    """
    year, month, day = date_str.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    return year, month, day


def deboneIds(Infos:dict)->dict:
    '''Deshuesa (quita) las llaves de un diccionario -> ArrayList de sólo los valores'''
    Infos = Infos['elements']
    values = lt.newList('ARRAY_LIST')
    for element in Infos:
        keys = list(element.keys())  
        key = keys[0]  
        lt.addLast(values, element[key])
    return values

def ContadorMapasNOList(ArrayList,llave:str):
    '''IN: Una lista simple (JobsDeboned) que contenga todas las llaves Y una llave por la cúal contar
    OUT: Un mapa con las cuentas'''
    # Una idea / código desarrollado absolutamente genial de Jacome
    Ne = (lt.size(ArrayList) * 0.05) # Una aproximación
    Mapcontador = mp.newMap(numelements= Ne,maptype="PROBING",loadfactor=0.5)
    for element in lt.iterator(ArrayList):
        subelement = element[llave]
        existdato = mp.contains(Mapcontador,subelement)
        if existdato:
            entry = mp.get(Mapcontador, subelement)
            dato = me.getValue(entry)
        else:
            dato = 0
        dato = dato + 1
        mp.put(Mapcontador,subelement,dato)
    return Mapcontador

def ContadorMapasList(ArrayList,llave:str):
    Ne = (lt.size(ArrayList) * 0.05) # Una aproximación
    '''IN: Una lista simple (JobsDeboned) que contenga todas las llaves, LISTAS DENTRO DE LLAVE
    Y una llave por la cúal contar | OUT: Un mapa con las cuentas'''
    # Una idea / código desarrollado absolutamente genial de Jacome
    Mapcontador = mp.newMap(numelements=Ne, maptype="PROBING",loadfactor=0.5)
    for item in lt.iterator(ArrayList):
        sublist = item[llave]
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

def getMapStats(map, stat='max'):
    '''Basado en un mapa de conteo regresa la pareja llave valor con valor más alto o bajo
    IN: mapa, stat ('min'o 'max') OUT: pareja llave valor <k,v> correspondiente a stat'''
    keySet = mp.keySet(map)
    mini = float('inf')
    minikv = None
    maxi = float('-inf')
    maxikv = None
    for key in lt.iterator(keySet):
        kvpair = mp.get(map, key)
        try:
            val = int(kvpair['value'])
        except ValueError:
            raise Exception("getMapStats - Solo compara valores numericos!")
        if stat == 'min':
            if val < mini:
                mini = val
                minikv = kvpair
        elif stat == 'max':
            if val > maxi:
                maxi = val
                maxikv = kvpair
        else:
            raise ValueError("getMapStats - stat debe ser 'min' o 'max'")
    if stat == 'min':
        return minikv
    elif stat == 'max':
        return maxikv

def sortC_MapValues(map, crop= None):
    ''' Sortear según su valor descendientemente los valores de un mapa
    IN: Mapa, Crop[OPTNL]: Factor de recorte (De mayor a menor) | 
    Out: ARRAY_LIST Ordenado de mayor a menor [OPTNL] Recortado hasta crop
    '''
    kvlist = lt.newList('ARRAY_LIST')
    keys = mp.keySet(map)
    for key in lt.iterator(keys):
        value = mp.get(map, key)
        value = value['value']
        lt.addLast(kvlist, {key: value})
    def Sort_crit(pair1, pair2):
        val1 = list(pair1.values())
        val2 = list(pair2.values())
        val1, val2 = val1[0], val2[0]
        if val1 > val2:
            return True
        else:
            return False

    sortedC_List = merg.sort(kvlist, Sort_crit)
    if crop != None:
        try:
            sortedCrop_List = lt.subList(sortedC_List, 1, crop)
            return sortedCrop_List

        except:
            raise Exception("CROP Está fuera del índice")
    return sortedC_List

def ASCIIBinSearch(sorted_list, elem):
    """
    Búsqueda binaria en una lista ordenada de cadenas, buscando un elemento específico.
    Parámetros:
    - sorted_list (List[str]): La lista ordenada de cadenas donde se realiza la búsqueda.
    - elem (str): El elemento que se busca en la lista.
    Retorna:
    - int: El índice lista python del elemento en la lista si se encuentra, -1 si el elemento no está presente.
    """
    
    left = 0 
    right = len(sorted_list) - 1
    elem = elem.upper() 

    while left <= right:
        mid = (left + right) // 2
        mid_val = sorted_list[mid].upper() 

        if mid_val < elem:
            left = mid + 1
        elif mid_val > elem:
            right = mid - 1
        else:
            return mid 
    return -1 


def ASCII_CRIT(ID1: str, ID2: str): 
    """
    Compara dos identificadores (ID1 e ID2) y determina si el primero es mayor al segundo basado en el valor ASCII.
    Parámetros:
    - ID1 (str): Primer identificador a comparar.
    - ID2 (str): Segundo identificador a comparar.
    Retorna:
    - bool: Verdadero si ID1 es mayor que ID2; falso si ID1 es menor o igual a ID2.
    """
    ID1 = ID1.upper()
    ID2 = ID2.upper()
    return ID1> ID2
    