"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
from datetime import datetime 
import traceback
import csv
import re
csv.field_size_limit(2147483647)
default_limit = 10000
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control
    


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- ¿Desea probar almacenamiento o rapidez?")
    print("11- Cambiar tamaño de archivos cargados")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    control, prueba, nombre_prueba, sorted_list = controller.load_data(control)
    return control, prueba, nombre_prueba, sorted_list
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control,n,pais,experticia):
    trabajos= controller.req_1(control,n,pais,experticia)[0]
    Res_prueba= controller.req_1(control,n,pais,experticia)[1]
    prueba= controller.req_1(control,n,pais,experticia)[2]
    if trabajos[0] == None:
        print("-"*220)
        print("NO se encontraron ofertas para los datos otorgados")
        print("-"*200)
        return None
    
    size= trabajos[1]
    lista=trabajos[0]
    conteo_p= trabajos[2]
    
    print("fueron cargadas un total de ", size, "ofertas que cumplen las condiciones especificadas")
    print("El total de ofertas publicadas por ",pais,"son: ",conteo_p)

    imprimir=[]
    headers= ["Fecha de publicación", "Título", "Empresa",
               "Nvl experticia", "País", "Ciudad",
               "Tamaño_empresa", "Ubicación", "¿Contrata ucranianos?"]
    llaves=["published_at","title", "company_name", "experience_level", "country_code", "city","company_size","workplace_type","open_to_hire_ukrainians"]
    for i in lt.iterator(lista):
        provisional=[]
        for k in llaves:
            provisional.append(i[k])
        imprimir.append(provisional)
    print(tabulate(imprimir,headers=headers,tablefmt="grid"),"\n")
    if prueba == "Rapidez":
        print(f"Se ha demorado un total de {Res_prueba}[ms]")
    else:
        print(f"Ha consumido un total de {Res_prueba}[kB]")




def print_req_2(control, offer_number, company_name, city):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    function = controller.req_2(control, offer_number, company_name, city)
    return function
    

def print_req_3(control,empresa,fecha1,fecha2):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    trabajos=controller.req_3(control,empresa,fecha1,fecha2)[0]
    Res_prueba=controller.req_3(control,empresa,fecha1,fecha2)[1]
    prueba=controller.req_3(control,empresa,fecha1,fecha2)[2]
    contajor_junior=trabajos[0]
    contajor_mid=trabajos[1]
    contajor_senior=trabajos[2]
    total_of= trabajos[3]
    listaF= trabajos[4]
    print("Fueron cargadas un total de",total_of," ofertas publicadas por ",empresa, "desde ", fecha1, "hasta ", fecha2,"\n")
    print(contajor_junior,"ofertas de trabajo con nivel de experticia junior")
    print(contajor_mid,"ofertas de trabajo con nivel de experticia mid")
    print(contajor_senior,"ofertas de trabajo con nivel de experticia senior","\n")
    if lt.size(listaF) <= 10:
        imprimir=[]
        headers= ["Fecha de publicación", "Título", "Empresa",
               "Nvl experticia", "País", "Ciudad",
               "Tamaño_empresa", "Ubicación", "¿Contrata ucranianos?"]
    
        llaves=["published_at","title", "company_name", "experience_level", "country_code", "city","company_size","workplace_type","open_to_hire_ukrainians"]
        for i in lt.iterator(listaF):
            provisional=[]
            for k in llaves:
                provisional.append(i[k])
            imprimir.append(provisional)
        print(tabulate(imprimir,headers=headers))
    else:
        print("los primeros 5 elementos son: ","\n")
        listaP=lt.subList(listaF,1,5)
        imprimir=[]
        headers= ["Fecha de publicación", "Título", "Empresa",
               "Nvl experticia", "País", "Ciudad",
               "Tamaño_empresa", "Ubicación", "¿Contrata ucranianos?"]
    
        llaves=["published_at","title", "company_name", "experience_level", "country_code", "city","company_size","workplace_type","open_to_hire_ukrainians"]
        for i in lt.iterator(listaP):
            provisional=[]
            for k in llaves:
                provisional.append(i[k])
            imprimir.append(provisional)
        print(tabulate(imprimir,headers=headers))

        print("los ultimos 5 elementos son: ","\n")
        listaU=lt.subList(listaF,-4,5)
        imprimir=[]
        headers= ["Fecha de publicación", "Título", "Empresa",
               "Nvl experticia", "País", "Ciudad",
               "Tamaño_empresa", "Ubicación", "¿Contrata ucranianos?"]
    
        llaves=["published_at","title", "company_name", "experience_level", "country_code", "city","company_size","workplace_type","open_to_hire_ukrainians"]
        for i in lt.iterator(listaU):
            provisional=[]
            for k in llaves:
                provisional.append(i[k])
            imprimir.append(provisional)
        print(tabulate(imprimir,headers=headers),"\n")
    if prueba == "Rapidez":
        print(f"Se ha demorado un total de {Res_prueba}[ms]")
    else:
        print(f"Ha consumido un total de {Res_prueba}[kB]")
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print("\n POR FAVOR DIGITE LOS SIGUIENTES DATOS PARA HACER EFECTIVA SU CONSULTA\n")
    print("\nConsultar las ofertas que se publicaron en un país durante un periodo de tiempo\n")
    pais = input("Digite el código del país por favor... ")
    fecha0 = input("Digite el límite inferior del rango de fechas (Y-M-D): ")
    fecha1 = input("Digite el límite superior del rango de fechas (Y-M-D): ")
    
    correct0 = re.search(pattern=r"^[0-9]{4}-[0]{1}[0-9]{1}-[0-9]{2}$|^[0-9]{4}-[1]{1}[0-2]{1}-[0-9]{2}$", string= fecha0)
    correct1 = re.search(pattern=r"^[0-9]{4}-[0]{1}[0-9]{1}-[0-9]{2}$|^[0-9]{4}-[1]{1}[0-2]{1}-[0-9]{2}$", string= fecha1)
    
    if not correct0 or not correct1:
        print("-"*220)
        print("¡Digito mal el formato de fecha, por favor intentelo nuevamente!".center(220))
        print("-"*220)
        print_req_4(control)
        return None
    
    año0, mes0, dia0 = map(int,(fecha0).split("-"))
    año1, mes1, dia1 = map(int, (fecha1).split("-"))
    
    
    cant_empresas, cant_ciudades, cant_ofertas,max_city ,ofertas_max, min_city,ofertas_min, filtered_offers, res_prueba, prueba= controller.req_4(control, pais, (año0,mes0,dia0), (año1, mes1, dia1))
    if cant_empresas == False and cant_ciudades == False and cant_ofertas ==False and max_city == False and ofertas_max == False and min_city == False and ofertas_min == False and filtered_offers == False:
        print("\n")
        print("-"*220)
        print("NO se encontraron ofertas para los datos que dio".center(220))
        print("intente nuevamente :) ".center(220))
        print("-"*220)
        return None
    if prueba == "Rapidez":
        print(f"Se ha demorado un total de {res_prueba}[ms]")
    else:
        print(f"Ha consumido un total de {res_prueba}[kB]")
    
        
    print("-"*220)
    print(("RESULTADOS DE LA CONSULTA").center(220))
    print("Se encontraron los siguientes resultados:\n".center(220))
    print(f"Cantidad empresas presentes: {cant_empresas}".center(220))
    print(f"Cantidad ciudades presentes: {cant_ciudades}".center(220))
    print(f"Cantidad de ofertas publicadas: {cant_ofertas}".center(220))
    print(f"La ciudad con mayor cantidad de ofertas publicadas fue {max_city} con {ofertas_max} ofertas".center(220))
    print(f"La ciudad con menor cantidad de ofertas publicadas fue {min_city} con {ofertas_min} ofertas".center(220))
    print("-"*220)
    
    firstf, lastf, cinco = controller.manipular_ofertas_filtradas(filtered_offers)
    
    if cinco:
        
        print("\nPRIMERAS CINCO OFERTAS\n")
        
        llaves=["published_at","title", "company_name", "experience_level", "country_code", "city","marker_icon", "workplace_type", "open_to_hire_ukrainians"]
        valores_a_imprimir1 = []
        
        for offer in lt.iterator(firstf):
            lst_provisional = []
            for llave in llaves:
                lst_provisional.append(offer[llave])
            valores_a_imprimir1.append(lst_provisional)
            
        print((tabulate(valores_a_imprimir1, headers=llaves)).center(220))
        
        print("\nULTIMAS CINCO OFERTAS\n")
        
        valores_a_imprimir1 = []
        
        for offer in lt.iterator(lastf):
            lst_provisional = []
            for llave in llaves:
                lst_provisional.append(offer[llave])
            valores_a_imprimir1.append(lst_provisional)
            
        print((tabulate(valores_a_imprimir1, headers=llaves)).center(220))
            
    else:
        
        llaves=["published_at","title", "company_name", "experience_level", "country_code", "city","marker_icon", "workplace_type", "open_to_hire_ukrainians"]
        valores_a_imprimir1 = []
        
        for offer in lt.iterator(filtered_offers):
            lst_provisional = []
            for llave in llaves:
                lst_provisional.append(offer[llave])
            valores_a_imprimir1.append(lst_provisional)
            
        print((tabulate(valores_a_imprimir1, headers=llaves)).center(220))
        
        

def print_req_5(control,city, first_date, last_date):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    function = controller.req_5(control,city, first_date, last_date)
    return function


def print_req_6(control,n,año,experticia):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    trabajos= controller.req_6(control,n,año,experticia)[0]
    Res_prueba=controller.req_6(control,n,año,experticia)[1]
    prueba=controller.req_6(control,n,año,experticia)[2]
    lista= trabajos[0]
    nombre_ciudadMx=trabajos[1][0]
    size_ciudadMX=trabajos[1][2]
    nombre_ciudadMN=trabajos[1][1]
    size_ciudadMN=trabajos[1][3]
    total_ciudades=trabajos[1][4]
    nombre_empresaMx=trabajos[2][0]
    size_empresaMX=trabajos[2][2]
    nombre_empresaMN=trabajos[2][1]
    size_empresaMN=trabajos[2][3]
    total_empresas=trabajos[2][4]
    total_ofertas=trabajos[3]

    print("fueron publicadas un total de ",total_ofertas," de acuerdo a las condiciones especificadas ","\n")
    print(total_ciudades,"ciudades publicaron ofertas en ", año, "con nivel de experticia ",experticia,"\n")
    print(total_empresas,"empresas publicaron ofertas en ", año, "con nivel de experticia ",experticia,"\n")
    if nombre_ciudadMx==nombre_ciudadMN:
        print("Solo ",nombre_ciudadMx,"publicó ofertas en ",año, "con nivel de esperticia ",experticia)
        print("publicó un total de ",size_ciudadMX," ofertas")
    else:
        print("la ciudad con mas ofertas publicadas en el ",año,"con nivel de experticia ",experticia, " es ",nombre_ciudadMx)
        print("Publicó un total de ",size_ciudadMX, " ofertas","\n")
        print("la ciudad con menos ofertas publicadas en el ",año,"con nivel de experticia ",experticia, " es ",nombre_ciudadMN)
        print("Publicó un total de ",size_ciudadMN, " ofertas","\n")

    if nombre_empresaMN==nombre_empresaMx:
        print("Solo ",nombre_empresaMx,"publicó ofertas en ",año, "con nivel de esperticia ",experticia)
        print("publicó un total de ",size_empresaMX," ofertas")
    else:
        print("la empresa con mas ofertas publicadas en el ",año,"con nivel de experticia ",experticia, " es ",nombre_empresaMx)
        print("Publicó un total de ",size_empresaMX, " ofertas","\n")
        print("la empresa con menos ofertas publicadas en el ",año,"con nivel de experticia ",experticia, " es ",nombre_empresaMN)
        print("Publicó un total de ",size_empresaMN, " ofertas","\n")
    
    imprimir=[]
    headers= ["Salario", "Total ofs", "Ciudad",
                "País", "Mejor of","Peor of",
               "Empresa mas ofs","Conteo", "Total"]
    
    
    llaves=["salario","total_ofertas", "ciudad", "pais", "mejor_oferta","peor_oferta", "Empresa_con_mas_ofertas","conteos","total_empresas"]
    for i in lt.iterator(lista):
        provisional=[]
        for k in llaves:
            provisional.append(i[k])
        
        imprimir.append(provisional)
    print(tabulate(imprimir,headers=headers),"\n")
    if prueba == "Rapidez":
        print(f"Se ha demorado un total de {Res_prueba}[ms]")
    else:
        print(f"Ha consumido un total de {Res_prueba}[kB]")



def print_req_7(control, country_number, month, year):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    function = controller.req_7(control, country_number, month, year)
    return function
    


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print("Identificación de los países con mayor y menor ofertas de trabajo en un rango de fechas".center(220))
    print("\n Por favor digite los siguientes datos: \n")
    lvl_exp = input("Nivel de experiencia a consultar (junior, mid, senior, indiferente): ")
    divisa = input("Divisa bajo la cual desea hacer la consulta: ")
    fecha0 = input("Digite el límite inferior del rango de fechas (Y-M-D): ")
    fecha1 = input("Digite el límite superior del rango de fechas (Y-M-D): ")
    
    correct0 = re.search(pattern=r"^[0-9]{4}-[0]{1}[0-9]{1}-[0-9]{2}$|^[0-9]{4}-[1]{1}[0-2]{1}-[0-9]{2}$", string= fecha0)
    correct1 = re.search(pattern=r"^[0-9]{4}-[0]{1}[0-9]{1}-[0-9]{2}$|^[0-9]{4}-[1]{1}[0-2]{1}-[0-9]{2}$", string= fecha1)
    
    if not correct0 or not correct1:
        print("-"*220)
        print("¡Digito mal el formato de fecha, por favor intentelo nuevamente!".center(220))
        print("-"*220)
        print_req_8(control)
        return None
    
    año0, mes0, dia0 = map(int,(fecha0).split("-"))
    año1, mes1, dia1 = map(int, (fecha1).split("-"))
    
    cant_empresas, total_ofertas, cant_paises , cant_ciudades, cant_of_con_salario, cant_of_con_salario_fijo, cant_of_sin_salario, paises_orden, paises, res_prueba, prueba = controller.req_8(control, lvl_exp, divisa, (año0, mes0, dia0), (año1, mes1, dia1) )
    if paises == False:
        
        print("\n")
        print("-"*220)
        print("NO se encontraron ofertas dentro del rango de fechas dado".center(220))
        print("-"*220)
        print("\n")
        return None
    if prueba == "Rapidez":
        print(f"Se ha demorado un total de {res_prueba}[ms]")
    else:
        print(f"Consumio un total de {res_prueba}[kB]")
    print()
    print("-"*220)
    print(("RESULTADOS DE LA CONSULTA").center(220))
    print("Se encontraron los siguientes resultados:\n".center(220))
    print(f"Cantidad empresas presentes: {cant_empresas}".center(220))
    print(f"Cantidad paises presentes: {cant_paises}".center(220))
    print(f"Cantidad ciudades presentes: {cant_ciudades}".center(220))
    print(f"Cantidad de ofertas publicadas: {total_ofertas}".center(220))
    print(f"En el periodo de consulta se publicaron un total de {cant_of_con_salario} ofertas con rango salarial".center(220))
    print(f"En el periodo de consulta se publicaron un total de {cant_of_con_salario_fijo} ofertas con salario fijo".center(220))
    print(f"En el periodo de consulta se publicaron un total de {cant_of_sin_salario} ofertas sin salario".center(220))
    print("-"*220)
    conteo = 0
    llaves=["published_at","id", "company_name", "experience_level", "country_code", "city"]
    valores_a_imprimir1 = []
    
    llaves_pais=["país", "ofertas_con_rango_salarial", "total_ofertas", "mayor_oferta", "menor_oferta","promedio_salarial","promedio_habilidades", "empresas_presentes"]
    valores_a_imprimir1_pais = []
    conteo_pais = 0
    
    for pais in lt.iterator(paises_orden):
        firstf = me.getValue(mp.get(paises, pais[0]))
        
        
        ofertas_con_rango_salarial = 0
        total_ofertas_pais = 0
        
        for key_city in lt.iterator(mp.keySet(firstf)):
            #print(key_city)
            no =["suma_salarios","cantidad_salarios","promedio_salarial","cantidad_habilidades","suma_habilidades","promedio_habilidades", "mayor_oferta", "menor_oferta", "empresas_presentes"]
            if key_city not in no:
                for key in lt.iterator(mp.keySet(me.getValue(mp.get(firstf, key_city)))):
                    if key == "con_salario":
                        
                        ofertas_con_rango_salarial += lt.size(me.getValue(mp.get(me.getValue(mp.get(firstf, key_city)),key)))
                    total_ofertas_pais += lt.size(me.getValue(mp.get(me.getValue(mp.get(firstf, key_city)),key)))
                    
                    for offer in lt.iterator(me.getValue(mp.get(me.getValue(mp.get(firstf, key_city)),key))):
                        if conteo < 5 or conteo > total_ofertas-6:
                            lst_provisional = []
                            for llave in llaves:
                                lst_provisional.append(offer[llave])
                            valores_a_imprimir1.append(lst_provisional)
                        conteo +=1
            
        if conteo_pais < 5 or conteo_pais > lt.size(paises_orden) - 6:
            lst_provisional = [pais[0], ofertas_con_rango_salarial, total_ofertas_pais]
            for llave in llaves_pais:
                if llave != "país" and llave != "ofertas_con_rango_salarial" and llave != "total_ofertas":
                    if llave == "mayor_oferta" or llave == "menor_oferta":
                        lst_provisional.append(me.getValue(mp.get(firstf ,llave))[0])
                    else:
                        lst_provisional.append(me.getValue(mp.get(firstf ,llave)))
            valores_a_imprimir1_pais.append(lst_provisional)
        conteo_pais += 1          
                
    #print(paises_orden)
    print("MUESTRA DE 10 OFERTAS".center(150))
    print((tabulate(valores_a_imprimir1, headers=llaves)).center(220))
    if lt.size(paises_orden) > 10:
        print("\n")
        print("PRIMEROS CINCO Y ULTIMOS CINCO PAÍSES".center(150))
        print((tabulate(valores_a_imprimir1_pais, headers=llaves_pais)).center(220))
        
    else:
        print("\n")
        print("PAÍSES".center(150))
        print((tabulate(valores_a_imprimir1_pais, headers=llaves_pais)).center(220))
        
    #IMPRIME SEGUNDA PARTE
    if len(valores_a_imprimir1_pais) >= 1:
        mayor_pais = [valores_a_imprimir1_pais[0]]
        menor_pais = [valores_a_imprimir1_pais[len(valores_a_imprimir1_pais)-1]]
        print("\n")
        print("MAYOR PAÍS".center(150))
        print((tabulate(mayor_pais, headers=llaves_pais)).center(220))
        print("\n")
        print("MENOR PAÍS".center(150))
        print((tabulate(menor_pais, headers=llaves_pais)).center(220))
    
    return None
    """
    Código del país.
• Total de ofertas de empleo.
• Promedio de salario ofertado.
• Número de ciudades donde se ofertaron.
• Número de empresas que publicaron ofertas en el país.
• Valor del mayor salario ofertado.
• Valor del menor salario ofertado.
• Número de habilidades promedio solicitadas por oferta en el país.
    """
    
    
    
    
    
def cambiar_pruebas(respuesta):
    prueba= controller.cambiar_pruebas(respuesta)
    return prueba


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            control = new_controller()
            print("Cargando información de los archivos ....\n")
            data, prueba, nombre_prueba, sorted_list = load_data(control)
            
            firstJobs, lastJobs , size= controller.three_first_last(sorted_list)
            
            print("\nFirst three elements\n")
            #print(firstJobs)
            llaves=["published_at","title", "company_name", "experience_level", "country_code", "city"]
            valores_a_imprimir1 = []
            conteo=1
            for offer in lt.iterator(firstJobs):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(lt.getElement(offer,1)[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            
            print("\nLast three elements\n")
            valores_a_imprimir1 = []
            conteo=size-2
            for offer in lt.iterator(lastJobs):
                lst_provisional = [conteo]
                for llave in llaves:
                    lst_provisional.append(lt.getElement(offer,1)[llave])
                valores_a_imprimir1.append(lst_provisional)
                conteo += 1
            print(tabulate(valores_a_imprimir1, headers=llaves))
            
            print("_"*150)
            #print("paso")
            #for i in lt.iterator(sorted_list):
            #    print(lt.getElement(i, 1)["published_at"])
                
            if nombre_prueba == "Rapidez":
                print(f"Se ha demorado un total de {prueba}[ms]")
            else:
                print(f"Se han consumido un total de {prueba}[kB]")
            
        elif int(inputs) == 2:
            n=int(input("Por favor ingrese el numero de ofertas a listar "))
            pais=str(input("Ingrese el codigo del pais "))
            experticia= str(input("Ingrese el nivel de experiencia "))
            print_req_1(control,n,pais,experticia)

            

        elif int(inputs) == 3:
            offer_number = input("Por favor digite el numero de ofertas a imprimir: ")
            city = input( "Por favor digite la ciudad a consultar: ")
            company_name = input("Por favor digite el nombre de la compañia a consultar: ")
            function = print_req_2(control, offer_number, company_name, city)
            print()
            print("................................")
            print()
            print("Total de ofertas ofrecida por la empresa y ciudad:", function[0] )
            if function[0]!=0:
                #for a in range( lt.size(function[1])):
                for i in lt.iterator(function[1]):
                    #for a in function[1]["elements"]:
                        #for i in a["elements"]:
                        
                            print()
                            print()
                            print("................................")
                            print()
                            fecha = i["published_at"]
                            fecha0= datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%fZ")
                            fecha1 = fecha0.strftime("%d %B, %Y")
                            print("Fecha de publicacion:", fecha1)
                            print("Pais de la oferta: ", i["country_code"])
                            print("Ciudad de la oferta: ", i["city"])
                            print("Nombre de la empresa de la oferta: ", i["company_name"])
                            print("Titulo de la oferta: ", i["title"])
                            print("Nivel de experticia de la oferta: ", i["experience_level"])
                            if i["remote_interview"]== False:
                                print("Formato de aplicación de la oferta: presencial")
                            else:
                                print("Formato de aplicación de la oferta: remota")
                            print("Tipo de trabajo: ", i["workplace_type"])
                            print()
            else:
                print("No se encontraron ofertas")
            print()
            print("................................")
            print()
            print(f"Ha demorado {function[2]} [ms]")
            print()

        elif int(inputs) == 4:
            empresa=str(input(" Por favor ingrese la empresa para la que desea hacer la búsqueda: "))
            fecha1=input("Ingrese la fecha inicial en formato %Y-%m-%\d ")
            fecha2=input("Ingrese la fecha final en formato %Y-%m-%\d ")
            print_req_3(control,empresa,fecha1,fecha2)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            limite_inicial = input("Por favor digite la fecha inicial del periodo a consultar: ")
            limite_final = input("Por favor digite la fecha final del periodo a consultar: ")
            city = input("Por favor digite el nombre de la ciudad: ")
            function = print_req_5(control, city, limite_inicial, limite_final)
            print()
            print("Total de ofertas publicadas en la ciudad en el periodo de consulta: ", function[0] )
            print("Total de empresas que publicaron por lo menos una oferta en la ciudad de consulta: ", function[2])
            if function[0] == 0 or function[1]==None:
                print("Empresa con mayor número de ofertas: Ninguna","......Numero de ofertas: Ninguna" )
                print("Empresa con menor número de ofertas: Ninguna",".......Numero de ofertas: Ninguna"  )
                print()
                print("................................")
                print()
                print("No encontramos ofertas en esta ciudad en estas fechas, porfavor intenta de nuevo ")
                print()
                print("................................")
                print()   
            else:
                print("Empresa con mayor número de ofertas: ", function[5],"......Numero de ofertas: ", function[3] )
                print("Empresa con menor número de ofertas: ",function[6],".......Numero de ofertas: ", function[4]  )
    
            #for a in function[1]["elements"]:
                        #for i in a["elements"]:
            if function[1]!= None:
                for i in lt.iterator(function[1]):
                                print()
                                fecha = i["published_at"]
                                fecha0 = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%fZ")
                                fecha1 = fecha0.strftime("%d %B, %Y")
                                print("Fecha de publicacion:", fecha1)
                                print("Titulo de la oferta: ", i["title"])
                                print("Nombre de la empresa de la oferta: ", i["company_name"])
                                print("Tipo de lugar de trabajo de la oferta: ", i["workplace_type"])
                                print("Tamaño de la empresa de la oferta: ",  i["company_size"])
            print(f"Ha demorado {function[7]} [ms]")
            print()

        elif int(inputs) == 7:
            n=int(input("Por favor ingrese el numero de ofertas a listar "))
            año=int(input("Por favor ingrese el año "))
            experticia=str(input("Ingrese el nivel de experiencia "))
            print_req_6(control,n,año,experticia)

        elif int(inputs) == 8:
            year = input("Por favor digite el año a consultar: ")
            month = input("Por favor digite el mes a consultar (solo el numero sin ceros): ")
            country_number = input("Por favor digite el numero de paises que desea consultar:  ")
            function = print_req_7(control, country_number, month, year)
            print()
            print("Total de ofertas de empleo: ", function[0] )
            print("Total de ciudades donde se ofertó en los países resultantes de la consulta: ", function[2])
            print("País con mayor cantidad de ofertas: ", function[4], ".......Numero de ofertas: ", function[3]  )
            print("Ciudad con mayor cantidad de ofertas: ", function[6], ".......Numero de ofertas: ", function[5]  )
            
            
            for i in function[1][2].items():
                
                print()
                print("................................")
                print()
                print("Nivel de epxerticia: ", i[0])
                print()
                print("................................")
                print()
                llave = i[0]
                print("Numero de habilidades: ", len(function[1][2][llave]))
                
                
                if llave in function[7]:
                    
                    
                    may = max(function[7][llave].values())
                    for i in function[7][llave.lower()].items():
                        if i[1]==may:
                            may0 = i[0]

                    print("Habilidad más solicitada: ",may0,".......Numero de ofertas: ", may )
                    
                
            
                if llave in function[8]:
                    
                    men = min(function[8][llave].values())
                    for i in function[8][llave.lower()].items():
                        if i[1]==men:
                            men0 = i[0]

                    print("Habilidad menos solicitada: ",men0,".......Numero de ofertas: ", men )
                
          
    
                
    
                
                mayores = max(function[9][llave].values())
                menores = min(function[9][llave].values())
                cont = 0
                for i in function[9][llave].items():
                    if i[1]==mayores:
                        mayores0 = i[0]
                    if i[1]==menores:
                        menores0 = i[0]
                        
                    cont +=1
                    
                    print("Conteo de empresas que publicaron una oferta: ", cont)
                    print("Empresa con mayor número de ofertas: ", mayores0,"......Numero de ofertas: ", mayores)
                    print("Empresa con menor número de ofertas: ", menores0,".......Numero de ofertas: ", menores )
                    print()
                    print("................................")
                    print()
            print(f"Ha demorado {function[10]} [ms]")
            print()
                
            
            
            
            
            
            
            
            
            
            


        elif int(inputs) == 7:
            n=int(input("Por favor ingrese el numero de ofertas a listar "))
            año=int(input("Por favor ingrese el año "))
            experticia=str(input("Ingrese el nivel de experiencia "))
            print_req_6(control,n,año,experticia)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)
        
        elif int(inputs) == 10:
            print("[1] Rapidez")
            print("[2] Almacenamiento\n")
            respuesta = input("¿Qué opción desea escoger? ")
            while respuesta != "1" and respuesta != "2":
                
                
                print("Opción no disponible\n")
                respuesta = input("¿Qué opción desea escoger? ")
            if respuesta == "1":
                cambiar_pruebas("Rapidez")
            elif respuesta == "2":
                cambiar_pruebas("Almacenamiento")
        elif int(inputs) == 11:
            print("\nPOR FAVOR DIGITE A CONTINUACIÓN EL SUFIJO DEL ARCHIVO PARA EL QUE DESEA MANIPULAR LA MUESTRA\n")
            sufijo = input("sufijo : ")
            
            if sufijo in ["10-por", "20-por", "30-por","40-por","50-por", "60-por", "70-por", "80-por","90-por","small","medium", "large"]:
                controller.cambiarTamañoMuestra(sufijo)
            else:
                print("\n no existen archivos con ese sufijo, intente nuevamente\n")

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
