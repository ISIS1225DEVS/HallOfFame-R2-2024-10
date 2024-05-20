from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylist as arr

def EnsureADTLi(InLi : any):
    if type(InLi) == list:
        Type = "PyList"
    elif type(InLi) == dict:
        Type = InLi.get("type", None)

    if (Type != 'ARRAY_LIST') and (Type != None) and (Type != "PyList") and (Type != "SINGLE_LINKED"):
        raise Exception("Lista NO Válida, sólo se recibe ARRAY-LIST, SINGLE_LINKED o ListaPython")
    
    elif Type == "PyList":
        Lit = Rpckg(InLi)
        print("\033[7m \033[5m \033[94m La lista enviada NO es ARRAY-LIST, se empaquetará y regresará cómo ARRAY-LIST \033[0m")
    elif (Type == "ARRAY_LIST") or (Type == "SINGLE_LINKED"):
        Lit = InLi
        
    return Lit

def Rpckg(InLi: list) -> dict:
    OutLi = lt.newList("ARRAY_LIST")
    for item in InLi:
        lt.addLast(OutLi, item)
    return OutLi

def LiPeel(arrLi) -> list:
    '''"Pela" una lista de tipo ARRAY_LIST para acceder a sus elementos. La única razón 
    por la que se hace acá es para que se vea menos feo en otra parte del código.'''
    lili = arrLi['elements']
    return lili