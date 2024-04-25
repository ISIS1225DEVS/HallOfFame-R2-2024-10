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
assert cf
import Maps_G01 as mp
import Lists_G01 as s
import Merge_sort_G01 as merge
from datetime import datetime

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
    data_struct={'jobs':None,
                 'multilocations':None,
                 'employments':None,
                 'skills':None}
    data_struct['jobs'] = mp.new_map(50000)
    data_struct['multilocations'] = mp.new_map(100000)
    data_struct['employments'] = mp.new_map(100000)
    data_struct['skills']=mp.new_map(100000)
    
    return data_struct


# Funciones para agregar informacion al modelo

def add_jobs(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    mp.put(data_structs['jobs'], data['id'], data)

def add_multilocations(data_structs, data):
    mp.put(data_structs['multilocations'], data['id'], data)

def add_employments(data_structs, data):
    mp.put(data_structs['employments'], data['id'], data) 
      
def add_skills(data_structs, data):
    mp.put(data_structs['skills'], data['id'], data)

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    return {'id': id, 'info': info}


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    return mp.get_value(data_structs,id)

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return mp.mapa_size(data_structs)

def data_size_jobs(data_structs):
    return mp.mapa_size(data_structs['jobs'])

def data_size_multilocations(data_structs):
    return mp.mapa_size(data_structs['multilocations'])

def data_size_employments(data_structs):
    return mp.mapa_size(data_structs['employments'])

def data_size_skills(data_structs):
    return mp.mapa_size(data_structs['skills'])

def tres_info(lista_entrada):
    '''
    Retorna los primeros tres primeros y ultimos elementos de la lista
    '''
    jobs = lista_entrada['jobs']
    elementos = s.new_list()
    info_t=[['Fecha de publicación','Título de la oferta',
           'Nombre de la empresa que publica',
           'Nivel de experticia de la oferta',
           'País de la oferta','Ciudad de la oferta']]
    for i in range(len(mp.keys(jobs))):
        key_l=mp.keys(jobs)[i]
        for j in range(len(key_l)):
            key=key_l[j]
            elemento=mp.get(jobs,key)
            info=elemento['value']
            tiempo=s.fecha_analisis(info['published_at'])
            info['published_at']=tiempo
            s.add_last(elementos,info)
    elementos_ord=merge.merge_sort(elementos,'published_at', 'title')
    for i in range(3):
        dato=s.get_element(elementos_ord,i)
        datos_lista=[dato['published_at'], dato['title'], dato['company_name'],
                     dato['experience_level'], dato['country_code'], dato['city']]
        info_t.append(datos_lista)
    for j in range(s.size(elementos_ord)-3, len(elementos_ord['content'])):
        dato=s.get_element(elementos_ord,j)
        datos_lista=[dato['published_at'], dato['title'], dato['company_name'],
                     dato['experience_level'], dato['country_code'], dato['city']]
        info_t.append(datos_lista)
    return info_t

def req_1(control,num_ofertas,codigo_pais,nivel_experticia):
    """
    Función que soluciona el requerimiento 1
    """
    cumplen=s.new_list()
    ofertas_pais=0
    for i in range(len(mp.keys(control))):
        key_l=mp.keys(control)[i]
        for j in range(len(key_l)):
            key=key_l[j]
            elemento=mp.get(control,key)
            info=elemento['value']
            pais=info['country_code']
            n_exp=info['experience_level']
            if pais == codigo_pais:
                ofertas_pais +=1
                if n_exp == nivel_experticia:
                    s.add_last(cumplen,info)
    ord_cumplen=merge.merge_sort(cumplen,'published_at', 'title')
    total_ofertas=s.size(ord_cumplen)
    ofertas_r1=[['Fecha publicación','Título oferta',
                 'Nombre empresa',
                 'Nivel experticia',
                 'País','Ciudad',
                 'Tamaño empresa',
                 'Tipo de ubicación',
                 'Contratar ucranianos']]
    for i in range(num_ofertas):
        dato=s.get_element(ord_cumplen,i)
        datos_lista=[dato['published_at'], dato['title'], dato['company_name'],
                        dato['experience_level'], dato['country_code'], dato['city'],
                        dato['company_size'], dato['workplace_type'],
                        dato['open_to_hire_ukrainians']]
        ofertas_r1.append(datos_lista)
        
    if len(ofertas_r1) > 11:
        primeros=ofertas_r1[0:6]
        ultimos=ofertas_r1[-5:]
        ofertas_r1=primeros+ultimos
        
    return [total_ofertas,ofertas_r1,ofertas_pais]

def req_2(control,num_ofertas,nom_empresa,ciudad_oferta):
    """
    Función que soluciona el requerimiento 2
    """
    cumplen=s.new_list()
    for i in range(len(mp.keys(control))):
        key_l=mp.keys(control)[i]
        for j in range(len(key_l)):
            key=key_l[j]
            elemento=mp.get(control,key)
            info=elemento['value']
            company_name=info['company_name']
            city=info['city']
            if company_name == nom_empresa and city == ciudad_oferta:
                s.add_last(cumplen,info)
    ord_cumplen=merge.merge_sort(cumplen,'published_at', 'title')
    total_ofertas=s.size(ord_cumplen)
    ofertas_r2=[['Fecha publicación','País',
                 'Ciudad',
                 'Nombre de la empresa',
                 'Título oferta','Nivel experticia',
                 'Tipo de trabajo']]
    for i in range(num_ofertas):
        dato=s.get_element(ord_cumplen,i)
        datos_lista=[dato['published_at'], dato['country_code'], dato['city'],
                     dato['company_name'], dato['title'], dato['experience_level'],
                     dato['workplace_type']]
        ofertas_r2.append(datos_lista)
    if len(ofertas_r2)>11:
        primeros=ofertas_r2[0:6]
        ultimos=ofertas_r2[-5:]
        ofertas_r2=primeros+ultimos
    return [total_ofertas, ofertas_r2]

def req_3(control,nom_empresa,fecha_inicial,fecha_final):
    """
    Función que soluciona el requerimiento 3
    """
    fecha_inicial=s.fecha_analisis(fecha_inicial)
    fecha_final=s.fecha_analisis(fecha_final)
    control=control['jobs']
    cumplen=s.new_list()
    total_junior=0
    total_mid=0
    total_senior=0
    for i in range(len(mp.keys(control))):
        key_l=mp.keys(control)[i]
        for j in range(len(key_l)):
            key=key_l[j]
            elemento=mp.get(control,key)
            info=elemento['value']
            company_name=info['company_name']
            fecha=info['published_at']
            experticia=info['experience_level']
            if company_name == nom_empresa and fecha >= fecha_inicial and fecha <= fecha_final:
                s.add_last(cumplen,info)
                if experticia=='junior':
                    total_junior+=1
                elif experticia=='mid':
                    total_mid+=1
                elif experticia=='senior':
                    total_senior+=1
    cumplen_ord=merge.merge_sort(cumplen, 'published_at', 'country_code')
    total_ofertas=s.size(cumplen_ord)
    ofertas_r3=[['Fecha publicación','Título oferta',
                 'Nivel experticia',
                 'Nombre empresa',
                 'Ciudad',
                 'País',
                 'Tamaño de empresa',
                 'Tipo de ubicación',
                 'Contratar ucranianos']]
    for i in range(total_ofertas):
        dato=s.get_element(cumplen_ord,i)
        datos_lista=[dato['published_at'], dato['title'],
                        dato['experience_level'], dato['company_name'], dato['city'],
                        dato['country_code'],dato['company_size'], dato['workplace_type'],
                        dato['open_to_hire_ukrainians']]
        ofertas_r3.append(datos_lista) 
    if len(ofertas_r3) > 11:
        primeros=ofertas_r3[0:6]
        ultimos=ofertas_r3[-5:]
        ofertas_r3=primeros+ultimos

    return [total_ofertas, total_junior,total_mid, total_senior, ofertas_r3]

def req_4(control,codigo_pais,fecha_inicial,fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    fecha_inicial=s.fecha_analisis(fecha_inicial)
    fecha_final=s.fecha_analisis(fecha_final)
    jobs=control['jobs']
    cumplen=s.new_list()
    pais=s.new_list()
    for i in range(len(mp.keys(jobs))):
        key_l=mp.keys(jobs)[i]
        for j in range(len(key_l)):
            key=key_l[j]
            elemento=mp.get(jobs,key)
            info=elemento['value']
            paiss=info['country_code']
            fecha=info['published_at']
            if paiss == codigo_pais:
                s.add_last(pais,info)
                if fecha >= fecha_inicial and fecha <= fecha_final:
                    s.add_last(cumplen,info)
    
    cumplen_ord=merge.merge_sort(cumplen,'published_at', 'company_name')
    total_ofertas=s.size(cumplen_ord)
    empresas=s.conteo(pais,'company_name')
    total_empresas=s.size(empresas)
    ciudades=s.conteo(pais,'city')
    total_ciudades=s.size(ciudades)
    ciudad_mas=s.first_element(ciudades)
    ciudad_menos=s.last_element(ciudades)
    
    ofertas_r1=[['Fecha publicación','Título oferta',
                 'Nivel experticia',
                 'Nombre empresa',
                 'Ciudad',
                 'Tipo de ubicación',
                 'Tipo Trabajo',
                 'Contratar ucranianos']]
    for i in range(total_ofertas):
        dato=s.get_element(cumplen_ord,i)
        datos_lista=[dato['published_at'], dato['title'],
                        dato['experience_level'], dato['company_name'], dato['city'],
                        dato['workplace_type'], dato['remote_interview'],
                        dato['open_to_hire_ukrainians']]
        ofertas_r1.append(datos_lista)
        
    if len(ofertas_r1) > 11:
        primeros=ofertas_r1[0:6]
        ultimos=ofertas_r1[-5:]
        ofertas_r1=primeros+ultimos
    return [total_ofertas,total_empresas,total_ciudades,ciudad_mas,ciudad_menos,ofertas_r1]

def req_5(control,ciudad_oferta,fecha_inicial,fecha_final):
    """
    Función que soluciona el requerimiento 5
    """
    fecha_inicial=s.fecha_analisis(fecha_inicial)
    fecha_final=s.fecha_analisis(fecha_final)
    jobs=control['jobs']
    cumplen=s.new_list()
    ciudad=s.new_list()
    for i in range(len(mp.keys(jobs))):
        key_l=mp.keys(jobs)[i]
        for j in range(len(key_l)):
            key=key_l[j]
            elemento=mp.get(jobs,key)
            info=elemento['value']
            ciudad_o=info['city']
            fecha=info['published_at']
            if ciudad_o == ciudad_oferta:
                s.add_last(ciudad,info)
                if fecha >= fecha_inicial and fecha <= fecha_final:
                    s.add_last(cumplen,info)

    cumplen_ord=merge.merge_sort(cumplen,'published_at', 'company_name')
    total_ofertas=s.size(cumplen_ord)
    empresas=s.conteo(ciudad,'company_name')
    total_empresas=s.size(empresas)
    empresa_mas=s.first_element(empresas)
    empresa_menos=s.last_element(empresas)

    ofertas_ciudad=[['Fecha publicación','Título oferta',
                 'Nombre empresa',
                 'Tipo de ubicación',
                 'Tamaño de la empresa',
                 'Tipo de trabajo']]
    
    for i in range(total_ofertas):
        dato=s.get_element(cumplen_ord,i)
        datos_lista=[dato['published_at'], dato['title'],
                        dato['company_name'],dato['workplace_type'],dato['company_size'],
                        dato['remote_interview']]
        ofertas_ciudad.append(datos_lista)

    if len(ofertas_ciudad) > 11:
        primeros=ofertas_ciudad[0:6]
        ultimos=ofertas_ciudad[-5:]
        ofertas_ciudad=primeros+ultimos
    return [total_ofertas,total_empresas,empresa_mas,empresa_menos,ofertas_ciudad]


def req_6(control,num_ciudades,nivel_experticia,ano_consulta):
    """
    Función que soluciona el requerimiento 6
    """
    inicio=datetime(ano_consulta,1,1)
    fin=datetime(ano_consulta,12,31,23,59,59)
    jobs=control['jobs']
    emply=control['employments']
    cumplen=s.new_list()
    for i in range(len(mp.keys(jobs))):
        key_l=mp.keys(jobs)[i]
        for j in range(len(key_l)):
            key=key_l[j]
            elemento=mp.get(jobs,key)
            info=elemento['value']
            nivel=info['experience_level']
            fecha=info['published_at']
            if fecha >= inicio and fecha <= fin:
                if nivel_experticia == 'indiferente':
                    s.add_last(cumplen,info)
                else:
                    if nivel == nivel_experticia: 
                        s.add_last(cumplen,info)
    ciudades=s.conteo_info(cumplen,'city')
    total_ciudades=s.size(ciudades)
    if total_ciudades < num_ciudades:
        resultado_total_ciudades=total_ciudades
    else:
        resultado_total_ciudades=num_ciudades
    empresas=s.conteo(cumplen,'company_name')
    resultado_total_empresas=s.size(empresas)
    resultado_total_ofertas=s.size(cumplen)
    ciudad_mas=s.first_element(ciudades)
    ciudad_menos=s.last_element(ciudades)
    
    ofertas_r1=[['Ciudad', 'País', 'Ofertas hechas',
                 'Promedio salario', 'Número empresas',
                 'Empresa más ofertas', 'ID Mejor oferta',
                 'ID Peor oferta']]
    
    for i in range(total_ciudades):
        dato = s.get_element(ciudades,i)
        ciudad=dato[0]
        empresas_ciudad=s.new_list()
        salario = 0
        sal_max = 0
        sal_min = 9999999999
        sal_max_info = None
        sal_min_info = None
        for j in range(s.size(cumplen)):
            elem = s.get_element(cumplen,j)
            city = elem['city']
            if city == ciudad:
                s.add_last(empresas_ciudad,elem)
                aidi = elem['id']
                info_sal = mp.get(emply,aidi)['value']
                if info_sal['salary_from'] != '':
                    sal_info = (int(info_sal['salary_to'])+int(info_sal['salary_from']))/2
                    sal_info2=int(info_sal['salary_to'])
                    salario += sal_info
                    if sal_info2 > sal_max:
                        sal_max_info = elem['id']
                        sal_max=sal_info2
                    if sal_info2 < sal_min:
                        sal_min_info = elem['id']
                        sal_min=sal_info2
        empresas_conteo = s.conteo(empresas_ciudad,'company_name')
        salario=salario/s.size(empresas_ciudad)
            
        datos_lista=[ciudad, dato[1]['country_code'], dato[2],
                     round(salario,2), s.size(empresas_conteo),
                     s.first_element(empresas_conteo), sal_max_info, sal_min_info]
        ofertas_r1.append(datos_lista)
        
    ofertas_r1=ofertas_r1[0:num_ciudades+1]
    if len(ofertas_r1) > 11:
        primeros=ofertas_r1[0:6]
        ultimos=ofertas_r1[-5:]
        ofertas_r1=primeros+ultimos
        
    return [resultado_total_ciudades, resultado_total_empresas,
            resultado_total_ofertas, ciudad_mas, ciudad_menos, ofertas_r1]


def req_7(control,num_paises,ano_consulta,mes_consulta):
    """
    Función que soluciona el requerimiento 7
    """
    inicio=datetime(ano_consulta,mes_consulta,1)
    fin=datetime(ano_consulta,mes_consulta,31,23,59,59)
    jobs=control['jobs']
    skills=control['skills']
    cumplen=s.new_list()
    for i in range(len(mp.keys(jobs))):
        key_l1=mp.keys(jobs)[i]
        for j in range(len(key_l1)):
            key1=key_l1[j]
            elemento1=mp.get(jobs,key1)
            info1=elemento1['value']
            fecha1=info1['published_at']
            if fecha1 >= inicio and fecha1 <= fin:
                s.add_last(cumplen,info1)
                id1=info1['id']
                experiencia=info1['experience_level']

    resultado2=s.conteo_info_req7(cumplen,'country_code')
    ordenado=merge.merge_sort(resultado2, 1, 0 )
    #N países
    total_content=len(ordenado['content'])
    if num_paises<=total_content:
        ordenado=ordenado['content'][:num_paises]
    else:
        ordenado=ordenado['content'][:total_content]
    total_ofertas_paises=0
    for sublista in ordenado:
        total_ofertas_paises+=sublista[1]
    #mayor país
    pais_mayor_oferta=ordenado[0][0]
    conteo_pais_mayor_oferta=ordenado[0][1]
    pais_mayor=[pais_mayor_oferta,conteo_pais_mayor_oferta]
    #mayor ciudad
    ciudad_max_numero = None
    max_numero = 0
    #Mapa para cada nivel de experticia donde está el id como llave y la empresa como valor
    mapa_junior=mp.new_map(50000)
    mapa_mid=mp.new_map(50000)
    mapa_senior=mp.new_map(50000)
    for pais, numero, ciudades, experticia in ordenado:
        for ciudad, num in ciudades:
            if num > max_numero:
                max_numero = num
                ciudad_max_numero = ciudad
        for nivel, diccionario_id in experticia.items():
            if nivel == 'junior':
                for llave, valor in diccionario_id.items():
                    mp.put(mapa_junior, llave, valor)
            elif nivel == 'mid':
                for llave, valor in diccionario_id.items():
                    mp.put(mapa_mid, llave, valor)
            elif nivel == 'senior':
                for llave, valor in diccionario_id.items():
                    mp.put(mapa_senior, llave, valor)
    mayor_ciudad=[ciudad_max_numero, max_numero]
    #Total ciudades
    total_ciudades = 0
    for elemento in ordenado:
        total_ciudades += len(elemento[2])

    #Habilidades
    #lista de id en cada mapa
    id_junior=mp.keys(mapa_junior)
    id_junior=[sublista for sublista in id_junior if len(sublista) > 0]
    id_junior = [dato for sublista in id_junior for dato in sublista]
    id_mid=mp.keys(mapa_mid)
    id_mid=[sublista for sublista in id_mid if len(sublista) > 0]
    id_mid = [dato for sublista in id_mid for dato in sublista]
    id_senior=mp.keys(mapa_senior)
    id_senior=[sublista for sublista in id_senior if len(sublista) > 0]
    id_senior = [dato for sublista in id_senior for dato in sublista]
    #Recorrido archivo skills y comparar id
    habilidades_junior=s.new_list()
    habilidades_mid=s.new_list()
    habilidades_senior=s.new_list()
    suma_nivel_junior=0
    suma_nivel_mid=0
    suma_nivel_senior=0
    total_suma_nivel_junior=0
    total_suma_nivel_mid=0
    total_suma_nivel_senior=0
    for i in range(len(mp.keys(skills))):
        key_l1=mp.keys(skills)[i]
        for j in range(len(key_l1)):
            key1=key_l1[j]
            elemento1=mp.get(skills,key1)
            info1=elemento1['value']
            id=info1['id']
            nombre_skill=info1['name']
            nivel_skill=int(info1['level'])
            if id in id_junior:
                s.add_last(habilidades_junior,info1)
                suma_nivel_junior+=nivel_skill
                total_suma_nivel_junior += 1
            elif id in id_mid:
                s.add_last(habilidades_mid,info1)
                suma_nivel_mid+=nivel_skill
                total_suma_nivel_mid += 1
            elif id in id_senior:
                s.add_last(habilidades_senior,info1)
                suma_nivel_senior+=nivel_skill
                total_suma_nivel_senior += 1

        
    habilidades_junior_conteo=s.conteo(habilidades_junior,'name')
    ordenado_habilidades_junior_conteo=merge.merge_sort(habilidades_junior_conteo, 1, 0 )
    habilidades_mid_conteo=s.conteo(habilidades_mid,'name')
    ordenado_habilidades_mid_conteo=merge.merge_sort(habilidades_mid_conteo, 1, 0 )  
    habilidades_senior_conteo=s.conteo(habilidades_senior,'name')    
    ordenado_habilidades_senior_conteo=merge.merge_sort(habilidades_senior_conteo, 1, 0 )


    #empresas
    #Valores empresas junior
    empresas_junior=s.new_list()
    for i in range(len(mp.keys(mapa_junior))):
        key_l1=mp.keys(mapa_junior)[i]
        for j in range(len(key_l1)):
            key1=key_l1[j]
            elemento1=mp.get(mapa_junior,key1)
            if elemento1 is not None and elemento1['value'] is not None:
                info1=elemento1['value']
                s.add_last(empresas_junior,[info1])
    empresas_junior_conteo=s.conteo(empresas_junior,0)
    ordenado_empresas_junior_conteo=merge.merge_sort(empresas_junior_conteo, 1, 0 )
    #Valores empresas mid
    empresas_mid=s.new_list()
    for i in range(len(mp.keys(mapa_mid))):
        key_l1=mp.keys(mapa_mid)[i]
        for j in range(len(key_l1)):
            key1=key_l1[j]
            elemento1=mp.get(mapa_mid,key1)
            if elemento1 is not None and elemento1['value'] is not None:
                info1=elemento1['value']
                s.add_last(empresas_mid,[info1])
    empresas_mid_conteo=s.conteo(empresas_mid,0)
    ordenado_empresas_mid_conteo=merge.merge_sort(empresas_mid_conteo, 1, 0 )
    #Valores empresas senior
    empresas_senior=s.new_list()
    for i in range(len(mp.keys(mapa_senior))):
        key_l1=mp.keys(mapa_senior)[i]
        for j in range(len(key_l1)):
            key1=key_l1[j]
            elemento1=mp.get(mapa_senior,key1)
            if elemento1 is not None and elemento1['value'] is not None:
                info1=elemento1['value']
                s.add_last(empresas_senior,[info1])
    empresas_senior_conteo=s.conteo(empresas_senior,0)
    ordenado_empresas_senior_conteo=merge.merge_sort(empresas_senior_conteo, 1, 0 )


        
    #Junior resultados habilidades y empresas
    total_habilidades_junior=len(ordenado_habilidades_junior_conteo['content'])
    habilidad_mas_junior=s.first_element(ordenado_habilidades_junior_conteo)
    habilidad_menos_junior=s.last_element(ordenado_habilidades_junior_conteo)
    promedio_nivel_minimo_junior=suma_nivel_junior/total_suma_nivel_junior
    redondeo_promedio_junior=round(promedio_nivel_minimo_junior,2)
    total_empresas_junior=len(ordenado_empresas_junior_conteo['content'])
    empresa_mas_junior=s.first_element(ordenado_empresas_junior_conteo)
    empresa_menos_junior=s.last_element(ordenado_empresas_junior_conteo)
    resultado_junior=[total_habilidades_junior, habilidad_mas_junior, habilidad_menos_junior, redondeo_promedio_junior, total_empresas_junior,empresa_mas_junior,empresa_menos_junior]
    #Mid resultados habilidades
    total_habilidades_mid=len(ordenado_habilidades_mid_conteo['content'])
    habilidad_mas_mid=s.first_element(ordenado_habilidades_mid_conteo)
    habilidad_menos_mid=s.last_element(ordenado_habilidades_mid_conteo)
    promedio_nivel_minimo_mid=suma_nivel_mid/total_suma_nivel_mid
    redondeo_promedio_mid=round(promedio_nivel_minimo_mid,2)
    total_empresas_mid=len(ordenado_empresas_mid_conteo['content'])
    empresa_mas_mid=s.first_element(ordenado_empresas_mid_conteo)
    empresa_menos_mid=s.last_element(ordenado_empresas_mid_conteo)
    resultado_mid=[total_habilidades_mid, habilidad_mas_mid, habilidad_menos_mid, redondeo_promedio_mid,total_empresas_mid,empresa_mas_mid, empresa_menos_mid ]
    #Senior resultados habilidades
    total_habilidades_senior=len(ordenado_habilidades_senior_conteo['content'])
    habilidad_mas_senior=s.first_element(ordenado_habilidades_senior_conteo)
    habilidad_menos_senior=s.last_element(ordenado_habilidades_senior_conteo)
    promedio_nivel_minimo_senior=suma_nivel_senior/total_suma_nivel_senior
    redondeo_promedio_senior=round(promedio_nivel_minimo_senior,2)
    total_empresas_senior=len(ordenado_empresas_senior_conteo['content'])
    empresa_mas_senior=s.first_element(ordenado_empresas_senior_conteo)
    empresa_menos_senior=s.last_element(ordenado_empresas_senior_conteo)
    resultado_senior=[total_habilidades_senior, habilidad_mas_senior, habilidad_menos_senior, redondeo_promedio_senior, total_empresas_senior, empresa_mas_senior, empresa_menos_senior]

    return [total_ofertas_paises,total_ciudades, pais_mayor, mayor_ciudad, resultado_junior, resultado_mid, resultado_senior]
    


def req_8(control,nivel_experticia,divisa,fecha_inicial,fecha_final):
    """
    Función que soluciona el requerimiento 8
    """
    fecha_inicial=s.fecha_analisis(fecha_inicial)
    fecha_final=s.fecha_analisis(fecha_final)
    jobs=control['jobs']
    employments=control['employments']
    cumplen=s.new_list()
    cumplen2=s.new_list()
    cumplen3=s.new_list()
    cumplen4=s.new_list()
    for i in range(len(mp.keys(jobs))):
        key_l=mp.keys(jobs)[i]
        for j in range(len(key_l)):
            key=key_l[j]
            elemento=mp.get(jobs,key)
            info=elemento['value']
            fecha=info['published_at']
            experticia=info['experience_level']
            if experticia == nivel_experticia and fecha >= fecha_inicial and fecha <= fecha_final:
                for k in range(len(mp.keys(employments))):
                     key_l2=mp.keys(employments)[k]
                     for l in range(len(key_l2)):
                         key2=key_l2[l]
                         elemento2=mp.get(employments,key2)
                         info2=elemento2['value']
                         divis=info2['currency_salary']
                         salario_inicial=info2['salary_from']
                         salario_final=info2['salary_to']
                         if divis==divisa:
                             s.add_last(cumplen,info)
                             if salario_inicial!=None and salario_final!=None:
                                 s.add_last(cumplen2,info2)
                             elif salario_inicial!=None and salario_final==None:
                                 s.add_last(cumplen3,info2)
                             elif salario_inicial==None and salario_final!=None:
                                 s.add_last(cumplen3,info2)
                             else:
                                 s.add_last(cumplen4,info2)

    cumplen_ord=merge.merge_sort(cumplen,'published_at', 'company_name')
    total_ofertas=s.size(cumplen_ord)
    empresas=s.conteo(cumplen_ord,'company_name')
    total_empresas=s.size(empresas)
    ciudades=s.conteo(cumplen_ord,'city')   
    total_ciudades=s.size(ciudades)                     
    paises=s.conteo(cumplen_ord,'country_code')  
    total_paises=s.size(paises)  
    total_rangos=s.size(cumplen2)
    total_fijas=s.size(cumplen3)
    total_sin=s.size(cumplen4)          


    paises_r1=[[ 'País','Promedio_salario', 'Número_empresas',
                 'Ofertas_hechas','Ofertas_rango']]    
    
    for i in range(total_paises):
        dato = s.get_element(paises,i)
        pais_info=dato[0]
        salario = 0
        for j in range(s.size(cumplen)):
            elem = s.get_element(cumplen,j)
            country= elem['country_code']
            if country == pais_info:
                id_info = elem['id']
                info_sal = mp.get(employments,id_info)['value']
                if info_sal['salary_from'] != '':
                    sal_info = (int(info_sal['salary_to'])+int(info_sal['salary_from']))/2
                    salario += sal_info
                    
            
        datos_lista=[pais_info,round(salario,2),total_empresas,total_ofertas]
        paises_r1.append(datos_lista)
        paises_r1_ord=merge.merge_sort(paises_r1,'País', 'Promedio_salario')
        pais_mayor=s.first_element(paises_r1_ord)
        pais_menor=s.last_element(paises_r1_ord)       



    return [total_empresas,total_ofertas,total_paises,total_ciudades,total_rangos,total_fijas,total_sin,paises_r1,pais_mayor,pais_menor]          
    
               
                


    


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


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass