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
import traceback
import threading


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
    
    control = controller.new_controller()
    return control 

    #TODO:) Llamar la función del controlador donde se crean las estructuras de datos
    pass


def print_menu():
    print("Bienvenido a Just Join IT, seleccione una opción:")
    print("1- Cargar información")
    print("2- Listar las últimas N ofertas según experticia y país (Req 1)")
    print("3- Listar las últimas N ofertas según empresa y ciudad (Req 2)")
    print("4- Consultar ofertas publicadas en una empresa específica durante un periodo de tiempo (Req 3)")
    print("5- Consultar ofertas publicadas en un país específico durante un periodo de tiempo (Req 4)")
    print("6- Consultar las ofertas que se publicaron en una ciudad durante un periodo de tiempo (Req 5)")
    print("7- Clasificar N ciudades con mayor número de ofertas por experticia en un rango de tiempo (Req 6)")
    print("8- Clasificar N países con mayor número de ofertas de trabajo según nivel de experticia (Req 7)")
    print("9- Escoger ordenamiento")
    print("0- Salir") 


def load_data(control, muestra):
    """
    Carga los datos
    """
    
    jobsID = controller.load_data(control, muestra)
    return jobsID

    #TODO:) Realizar la carga de datos
    pass


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, pais, exp, n,mem):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    a = controller.req_1(control, pais, exp, n, mem)

    ans = a[0]
    tomaMemoriaTiempo = a[1]
    if isinstance(tomaMemoriaTiempo, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo[0]:.3f}", "||",
              "Memoria [kB]: ", f"{tomaMemoriaTiempo[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo:.3f}")

    print ("Hay", ans[0], "ofertas de ese país.")
    print ("Hay", ans[1], "ofertas de ese nivel de experiencia.")

    ofertas = ans[2]
    sizeof=lt.size(ofertas)

    final = [0]*sizeof

    i = 0
    while i < sizeof:
        temp = {}
        for key in ofertas["elements"][i]:
            if key == "country_code"  or key == "published_at" or key == "city" or key == "company_name" or key == "title" or key == "experience_level" or key == "remote_interview" or key == "workplace_type":
                temp[key] = ofertas["elements"][i][key]

        final[i] = temp
        i+=1

    table = tabulate(final, headers = "keys", tablefmt = "fancy_outline")
    print("Las ofertas de ese país y nivel de experiencia son: ")
    print (table)  
    print("")     



def print_req_2(control, city, emp, n, mem):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    ans = controller.req_2(control, city, emp, n, mem)
    
    a = ans[0]
    
    size_general = a[0]
    ofertas = a[1]
    sizeof = lt.size(ofertas)
    print ("Hay", size_general, "ofertas de esa ciudad y esa empresa.")

    tomaMemoriaTiempo = ans[1]
    if isinstance(tomaMemoriaTiempo, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo[0]:.3f}", "||",
              "Memoria [kB]: ", f"{tomaMemoriaTiempo[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo:.3f}")
    final = [0]*sizeof
    
    i = 0
    while i < sizeof:
        temp = {}
        for key in ofertas["elements"][i]:
            if key == "country_code"  or key == "published_at" or key == "city" or key == "company_name" or key == "title" or key == "experience_level" or key == "remote_interview" or key == "workplace_type":
                temp[key] = ofertas["elements"][i][key]

        final[i] = temp
        i+=1

    table = tabulate(final, headers = "keys", tablefmt = "fancy_outline")
    print (table)  
    print("") 
    
    #print(a)



def print_req_3(control, company_name,start_date, end_date,mem):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    respuesta = controller.req_3(control, company_name,start_date, end_date ,mem)
    tomaMemoriaTiempo=respuesta[1]
    
    if isinstance(tomaMemoriaTiempo, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo[0]:.3f}", "||",
              "Memoria [kB]: ", f"{tomaMemoriaTiempo[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo:.3f}")

    r=respuesta[0]


    total_ofertas=r[0]
    ofertas_junior=r[1]
    ofertas_mid=r[2]
    ofertas_senior=r[3]
    offer_details_company=r[4]

    print ("Hay",total_ofertas, "ofertas en total")
    print ("Hay ", ofertas_junior , " ofertas para el nivel de experiencia junior")
    print ("Hay ",  ofertas_mid, " ofertas para el nivel de experiencia mid")
    print ("Hay ",  ofertas_senior, " ofertas para el nivel de experiencia senior")
    print ("A continuacion, la lista de ofertas de la empresa ordenadas cronologicamente por fecha y pais:   " )

    # Verificar que hay suficientes ofertas para mostrar los primeros y últimos cinco
    
    num_ofertas = len(offer_details_company['elements'])

    # Preparar la lista para los primeros elementos para mostrar, que serán los mismos para los últimos si hay menos de 5
    final_primeros5 = []
    for i in range(min(num_ofertas, 5)):
        final_primeros5.append({key: offer_details_company['elements'][i][key]
                                for key in offer_details_company['elements'][i]
                                if key in ["title", "published_at", "experience_level", "company_name", "city", "workplace_type", "open_to_hire_ukrainians"]})

    # Preparar la lista para los últimos cinco solo si hay más de 5 ofertas
    final_ultimos5 = final_primeros5.copy() if num_ofertas <= 5 else []
    if num_ofertas > 5:
        for i in range(1, 6):
            final_ultimos5.append({key: offer_details_company['elements'][-i][key]
                                for key in offer_details_company['elements'][-i]
                                if key in ["title", "published_at", "experience_level", "company_name", "city", "workplace_type", "open_to_hire_ukrainians"]})

    # Imprimir los resultados con tabulate
    print("Los primeros cinco son:" if num_ofertas >= 5 else "Las ofertas son:")
    print("")
    table_primeros5 = tabulate(final_primeros5, headers='keys', tablefmt="fancy_outline")
    print(table_primeros5)
    print("")

    # Si hay más de 5 ofertas, imprimir también los últimos cinco
    if num_ofertas > 5:
        print("Los últimos cinco son:")
        print("")
        table_ultimos5 = tabulate(final_ultimos5, headers='keys', tablefmt="fancy_outline")
        print(table_ultimos5)
        print("")



def print_req_4(control, pais, datei, datef, mem):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    ans = controller.req_4(control, pais, datei, datef, mem)
    #a = [ofertas_rango, size_emp, size_city, city_may, mayor, city_men, menor]
    
    a = ans[0]
    ofertas = a[0]
    empresas = a[1]
    city_may = a[3]
    mayor = a[4]
    city_men = a[5]
    menor = a[6]
    
    tomaMemoriaTiempo = ans[1]
    if isinstance(tomaMemoriaTiempo, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo[0]:.3f}", "||",
              "Memoria [kB]: ", f"{tomaMemoriaTiempo[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo:.3f}")

    sizeof = lt.size(ofertas)

    print ("Hay",sizeof, "ofertas")
    print ("Hay ofertas de", empresas, "empresas diferentes")
    if mayor == 0:
        print ("No hay ciudad con mayor número de ofertas")
    else: 
        print ("La ciudad con más ofertas es", city_may, "con,", mayor, "ofertas.")
    if menor == 0:
        print ("No hay ciudad con menor número de ofertas")
    else: 
        print ("La ciudad con menos ofertas es", city_men, "con,", menor, "ofertas.")


    if sizeof != 0: 
        final_primeros5=[0,0,0,0,0]
        i=0
        while i<5:
            temp={}
            for key in ofertas["elements"][i]:
                if key == "title" or key == "published_at" or key == "experience_level" or key == "company_name" or key == "city" or key == "workplace_type" or key == "open_to_hire_ukrainians":
                  temp[key] = ofertas["elements"][i][key]

            final_primeros5[i]=temp
            i+=1
    
        final_ultimos5=[0,0,0,0,0]
        i=0
        while i<5:
            temp={}
            numjobs=sizeof
            for key in ofertas['elements'][numjobs-i-1]:
                if key == "title" or key == "published_at" or key == "experience_level" or key == "company_name" or key == "city" or key == "workplace_type" or key == "open_to_hire_ukrainians":
                    temp[key]=ofertas['elements'][numjobs-i-1][key]

            final_ultimos5[i]=temp
            i+=1
                
        #Printing de las sublistas depuradas
        print("Los primeros cinco son:")
        print("")
        table_primeros5 = tabulate(final_primeros5,headers='keys',tablefmt="fancy_outline")
        print(table_primeros5)
        print("")
    
        print("Los ultimos cinco son:")
        print("")
        table_ultimos5 = tabulate(final_ultimos5,headers='keys',tablefmt="fancy_outline")
        print(table_ultimos5)
        print("")  
        
    #print(a)


def print_req_5(control,  ciudad, fechaInicial, fechaFinal, mem):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    answer=controller.req_5(control,  ciudad, fechaInicial, fechaFinal, mem)
    ans=answer[0]
    tomaMemoriaTiempo=answer[1]
    
    if isinstance(tomaMemoriaTiempo, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo[0]:.3f}", "||",
              "Memoria [kB]: ", f"{tomaMemoriaTiempo[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo:.3f}")
        
    if lt.size(ans[0])<10:
        tabla=[]
        for job in lt.iterator(ans[0]):
            temp={}
            for key in job:
                if key=="title" or key=="company_name" or key=="company_size" or key=="workplace_type" or key=="published_at":
                    temp[key]=job[key]
            tabla.append(temp.copy())
            
        tabla_imp = tabulate(tabla,headers='keys',tablefmt="fancy_outline")
        print("")
        print(tabla_imp)
        print("")

    else:
        final_primeros5=[0,0,0,0,0]
        i=0
        while i<5:
            temp={}
            for key in ans[0]['elements'][i]:
                if key=="title" or key=="company_name" or key=="company_size" or key=="workplace_type" or key=="published_at":
                    temp[key]=ans[0]['elements'][i][key]

            final_primeros5[i]=temp
            i+=1

        final_ultimos5=[0,0,0,0,0]
        i=0
        while i<5:
            temp={}
            numjobs = ans[6] 
            for key in ans[0]['elements'][numjobs-i-1]:
                if key=="title" or key=="company_name" or key=="company_size" or key=="workplace_type" or key=="published_at":
                    temp[key]=ans[0]['elements'][numjobs-i-1][key]

            final_ultimos5[i]=temp
            i+=1    
        

        print("Los primeros cinco son:")
        print("")
        table_primeros5 = tabulate(final_primeros5,headers='keys',tablefmt="fancy_outline")
        print(table_primeros5)
        print("")
        
        print("Los ultimos cinco son:")
        print("")
        table_ultimos5 = tabulate(final_ultimos5,headers='keys',tablefmt="fancy_outline")
        print(table_ultimos5)
        print("") 


    print("Hay un total de",ans[6],"ofertas de trabajo en la ciudad entre", fechaInicial,"y",fechaFinal,".")
    
    print("Hay un total de",ans[5],"empresas ofreciendo trabajo en ",ciudad)
    
    print("La empresa con mayor ofertas fue",ans[1],"con",ans[2],"ofertas.")
    print("La empresa con menor ofertas fue",ans[3],"con",ans[4],"ofertas.")
    print("")
    
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control,numCiudades,year,exp_level,mem):
    """
        imprime:
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
                    'total_empresas'
    

    """
        
    # TODO: Imprimir el resultado del requerimiento 6
    respuesta=controller.req_6(control, numCiudades, year, exp_level,mem)

    tomaMemoriaTiempo=respuesta[1]
    
    if isinstance(tomaMemoriaTiempo, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo[0]:.3f}", "||",
              "Memoria [kB]: ", f"{tomaMemoriaTiempo[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo:.3f}")

    resp=respuesta[0]
    
    if resp is not None:
            
              
        # Preparamos los datos para tabulate
        headers = [
            'Nombre de la ciudad',
            'País de la ciudad',
            'Total de ofertas',
            'Numero de empresas',
            'Empresa con mayor número de ofertas',
            'Promedio de salario ofertado',
            'Mejor oferta por salario',
            'Peor oferta por salario'
        ]

        # Convertimos la lista de ciudades a una lista de listas para tabulate
        table_data = []
        for ciudad in lt.iterator(resp["listado_ciudades"]):
            city_info = []
            for key in headers:
                city_info.append(ciudad[key])
            table_data.append(city_info)

        # Creamos la tabla usando tabulate
        table = tabulate(table_data, headers=headers, tablefmt="fancy_outline")
        print(table)

       #print("A continuacion se ve el listado de las ciudades ordenadas por el número de ofertas publicadas y nombre de la ciudad:" + str(resp["listado_ciudades"]))
        
        print("Hay", lt.size(resp["listado_ciudades"]), "ciudades que cumplen con las condiciones de consultas.")
        print("Hay", resp["total_ofertas"],"ofertas en total.")
        print("La ciudad con mas ofertas es:", resp["ciudad_con_mas_ofertas"])
        print("La ciudad con menos ofertas es:", resp["ciudad_con_menos_ofertas"])
        print("Hay", resp["total_empresas"],"en total.")
        
    pass


def print_req_7(control, numPaises, year, mes, mem):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    answer=controller.req_7(control, numPaises, year, mes, mem)
    ans=answer[0]
    tomaMemoriaTiempo=answer[1]
    
    if isinstance(tomaMemoriaTiempo, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo[0]:.3f}", "||",
              "Memoria [kB]: ", f"{tomaMemoriaTiempo[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo:.3f}")
    
    """
    ans=[lista para imprimir, 
        numero de ofertas totales, 
        numero de ciudades totales,
        [nombre de la ciudad con más puestos,  numero ofertas], 
        [nombre del pais con más puestos,  numero ofertas]
    """
    if ans != None:
        print("Hay", ans[1], "ofertas en total.")
        print("Hay", ans[2], "ciudades.")
        print("El país con más ofertas es", ans[4][0], "con", ans[4][1], "ofertas.")
        print("La ciudad con más ofertas es", ans[3][0], "con", ans[3][1], "ofertas.")
        print("")
        print("//////")

        for pais in lt.iterator(ans[0]):
            code = (lt.getElement(pais, 0))["País"]
            print("El listado de", code, ":")

            size_pais=lt.size(pais)
        
            final=[0]*size_pais
        
            i=0
            while i<size_pais:
                temp={}
                for key in pais['elements'][i]:
                    if key=="Nivel de experiencia" or key=="Numero_habilidades_solicitadas" or key=="Habilidad_mas_solicitada" or key=="Habilidad_menos_solicitada" or key=="Promedio_nivel_mínimo_de_hablidades" or key=="Numero_empresas_totales" or key=="Empresa_mayor_ofertas" or key=="Empresa_menor_ofertas" or key=="Numero_empresas_multisedes" :
                        temp[key]=pais['elements'][i][key]

                final[i]=temp
                i+=1
        
        
            table = tabulate(final,headers='keys',tablefmt="fancy_outline")
            print("")
            print(table)
            print("")

    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False


def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    tomaMemoriaTiempo=answer[0]
    if isinstance(tomaMemoriaTiempo, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo[0]:.3f}", "||",
              "Memoria [kB]: ", f"{tomaMemoriaTiempo[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{tomaMemoriaTiempo:.3f}")

    primeros3=answer[1]
    ultimos3=answer[2]
    
    #Depuración de la información de las sublistas de los primeros y ultimos 3
    final_primeros3=[0,0,0,0,0]
    i=0
    while i<3:
        temp={}
        for dicc in lt.iterator(primeros3):
            for key in dicc:
                if key=="title" or key=="company_name" or key=="city" or key=="country_code" or key=="published_at" or key=="experience_level":
                    temp[key]=dicc[key]

            final_primeros3[i]=temp.copy()
            i+=1
    
    final_ultimos3=[0,0,0,0,0]
    i=4
    while i>0:
        temp={}
        for dicc in lt.iterator(ultimos3):
            for key in dicc:
                if key=="title" or key=="company_name" or key=="city" or key=="country_code" or key=="published_at" or key=="experience_level":
                    temp[key]=dicc[key]
                    
            final_ultimos3[i]=temp.copy()
            i-=1
    
    #Printing de las sublistas depuradas
    print("Los primeros cinco son:")
    print("")
    table_primeros3 = tabulate(final_primeros3,headers='keys',tablefmt="fancy_outline")
    print(table_primeros3)
    print("")
    
    print("Los ultimos cinco son:")
    print("")
    table_ultimos3 = tabulate(final_ultimos3,headers='keys',tablefmt="fancy_outline")
    print(table_ultimos3)
    print("")
            


# Se crea el controlador asociado a la vista
control = new_controller()

opciones_yes = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")


# main del reto
def menu_cycle():
    """
    Menu principal
    """
    working = True
    
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        
        
        if int(inputs) == 1:
            muestra=input("Digite el tamaño de la muestra que desea probar:")            
            
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
                        
            print("Cargando información de los archivos ....\n")
            answer = controller.load_data(control,muestra, memflag=mem)
            printLoadDataAnswer(answer[1])

            ("Se cargo",answer[0],"ofertas de trabajo publicadas")
            print("")
            
             
            
        elif int(inputs) == 2:
            
            pais = str(input("Ingrese el codigo del pais: "))
            exp = str(input("Ingrese el nivel de experiencia (junior, mid, o senior): "))
            n = int(input("Ingresa la cantidad de trabajos a consultar: "))
            
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)

            print_req_1(control, pais, exp, n, mem)

        elif int(inputs) == 3:
            
            city = input("Ciudad: ")
            emp = input("Empresa: ")
            n = int(input("Número N de datos más recientes que desea conocer: "))


            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)

            print_req_2(control, city, emp, n, mem)

        elif int(inputs) == 4:

            company_name=input("Ingrese nombre de la empresa que desea consultar: ")
            start_date = input("Ingrese la fecha mínima (forma a-m-d): ")
            end_date = input("Ingrese la fecha máxima (forma a-m-d): ")

            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)

            print_req_3(control,company_name,start_date, end_date,mem)

        elif int(inputs) == 5:
            
            datei = input("Ingrese la fecha mínima (forma a-m-d): ")
            datef = input("Ingrese la fecha máxima (forma a-m-d): ")
            codPais= input("Ingrese el código de  un país: ")
            
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            
            print_req_4(control, codPais, datei, datef, mem)

        elif int(inputs) == 6:
            ciudad=(input("Digite la ciudad que desea consultar: "))
            fechaInicial=input("Digite la fecha inicial: ")
            fechaFinal=input("Digite la fecha final: ")
            
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            
            print_req_5(control, ciudad, fechaInicial, fechaFinal, mem)

        elif int(inputs) == 7:
            numCiudades=int(input("Digite el número de ciudades que desea consultar: "))
            year=input("Digite el anio de consulta: ")
            exp_level=input("Digite el nivel de experiencia de consulta: ")

            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            
            print_req_6(control, numCiudades, year, exp_level,mem)

        elif int(inputs) == 8:
            numPaises=int(input("Digite el número de países que desea consultar: "))
            year=input("Digite el anio de consulta: ")
            mes=input("Digite el mes de consulta: ")
            
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            
            print_req_7(control, numPaises, year, mes, mem)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)


if __name__ == "__main__":
    default_limit=1000
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target= menu_cycle)
    thread.start()
