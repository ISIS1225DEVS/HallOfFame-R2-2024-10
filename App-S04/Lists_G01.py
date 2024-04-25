#LISTAS
#Crea una nueva Linked-List
from datetime import datetime
import Merge_sort_G01 as merge

def new_list():
    lista = {'head':None, 'last':None, 'size':0, 'content':[]}
    return lista

#Verificar si una lista esta vacia.
def is_empty(lista):
    if lista==None:
        return True
    elif lista['size']==0:
        return True
    else:
        return False
    
#Agrega un elemento al final de la lista
def add_last(lista, data):
    node={'value':data, 'next':None, 'prev':last_element(lista)}
    if is_empty(lista):
        lista['head'] = node
    else:
        lista['last']['next'] = node
    lista['last']=node
    lista['content'].append(data)
    lista['size']=len(lista['content'])
    return lista

#Agrega un elemento al inicio de la lista
def add_first(lista,data):
    node={'value':data, 'next':first_element(lista), 'prev':None}
    if not is_empty(lista):
        lista['head']['prev']=node
    lista['head'] = node
    lista['content'].insert(0,data)
    lista['size'] = len(lista['content'])
    return lista

#Retorna el tamaño de la lista.
def size(lista):
    return lista['size']

#Retornar el primer elemento de la lista
def first_element(lista):
    if is_empty(lista):
        return None
    if size(lista) ==1:
        return lista['head']['value']
    else:
        return lista['head']

#Retorna el ultimo elemento de la lista.
def last_element(lista):
    if is_empty(lista):
        return None
    if size(lista) ==1:
        return lista['last']['value']
    else:
        return lista['last']
       
#Retorna el elemnto de la posicion dada.
def get_element(lista,pos):
    if pos < size(lista):
        return lista['content'][pos]
    else:
        return None
    
#Se retorna una lista que contiene los elementos a partir de la posición pos, con una longitud de numelem elementos. Se crea una copia de dichos elementos y se retorna una lista nueva.
def sublist(lista,pos,numelem):
    if pos<0 or pos>=size(lista) or numelem<1:
        return None
    else:
        nueva_lista=new_list()
        i=0
        while i < numelem:
            elemento=get_element(lista, pos+i)
            add_last(nueva_lista, elemento)
            i+=1
    return nueva_lista

#AAAAA
def change_info(lista, pos, element):
    if pos<0 or pos>=size(lista):
        return None
    else:
        lista['content'][pos]=element
        lista['head']=lista['content'][0]
        lista['last']=lista['content'][-1]
        '''
        nodo_actual=lista['head']
        pos_actual=0
        while nodo_actual is not None and pos_actual<pos:
            nodo_actual=nodo_actual['next']
            pos_actual+=1
        if nodo_actual is not None:
            nodo_actual['value']=element
            if nodo_actual['next'] is not None:
                nodo_actual['next']['prev'] = nodo_actual['value']
        '''

#Analisis de fechas
def fecha_analisis(fecha_csv):
    return datetime.strptime(fecha_csv, "%Y-%m-%dT%H:%M:%S.%fZ")

def conteo(lista,parametro):
    '''Permite contar la cantidad de elementos repetidos de una lista'''
    conteo_lista=new_list()
    for i in range(size(lista)):
        valor = get_element(lista,i)[parametro]
        find=False
        for sublist in conteo_lista['content']:
            if sublist[0] == valor:
                find = True
                sublist[1] += 1
        if not find:
            add_last(conteo_lista,[valor,1])
    conteo_lista_ord=merge.merge_sort(conteo_lista,1,0)
    return conteo_lista_ord

def conteo_info(lista,parametro):
    '''Permite contar la cantidad de elementos repetidos de una lista 
    con la información importante'''
    conteo_lista=new_list()
    for i in range(size(lista)):
        valor = get_element(lista,i)[parametro]
        datos=get_element(lista,i)
        find=False
        for sublist in conteo_lista['content']:
            if sublist[0] == valor:
                find = True
                sublist[2] += 1
        if not find:
            add_last(conteo_lista,[valor,datos,1])
    conteo_lista_ord=merge.merge_sort(conteo_lista,2,0)
    return conteo_lista_ord

def conteo_info_req7(lista,parametro):
    '''Permite contar la cantidad de elementos repetidos de una lista 
    con la información importante'''
    conteo_lista=new_list()
    for i in range(size(lista)):
        valor = get_element(lista,i)[parametro]
        ciudad=get_element(lista,i)['city']
        id=get_element(lista,i)['id']
        experticia=get_element(lista,i)['experience_level']
        empresa=get_element(lista,i)['company_name']
        find=False
        find2=False
        for sublist in conteo_lista['content']:
            if sublist[0] == valor:
                if experticia == 'junior':
                    diccionario_mayor=sublist[3]
                    diccionario_mayor['junior'][id]=empresa
                elif experticia == 'mid':
                    diccionario_mayor=sublist[3]
                    diccionario_mayor['mid'][id]=empresa
                else:
                    diccionario_mayor=sublist[3]
                    diccionario_mayor['senior'][id]=empresa
                find = True
                sublist[1] += 1
                for sublist_city in sublist[2]:
                    if sublist_city[0] == ciudad:
                        find2=True
                        sublist_city[1] += 1
                if not find2:
                    sublist[2].append([ciudad,1])
        if not find:
            if experticia == 'junior':
                add_last(conteo_lista,[valor,1, [[ciudad,1]], {'junior':{id:empresa}, 'mid':{}, 'senior':{}}])
            elif experticia == 'mid':
                add_last(conteo_lista,[valor,1, [[ciudad,1]], {'junior':{}, 'mid':{id:empresa}, 'senior':{}} ])
            else:
                add_last(conteo_lista,[valor,1, [[ciudad,1]], {'junior':{}, 'mid':{}, 'senior':{id:empresa}}])
    return conteo_lista