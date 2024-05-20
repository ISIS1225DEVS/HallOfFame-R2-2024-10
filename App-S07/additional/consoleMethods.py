#Para retornar sólo las llaves que nos interesan de una lista de diccionarios (pues usar Del Putea TODO)
from DISClib.ADT import list as lt
from additional import ilegalHandling as ile


def DicKeepOnly(keep: list, arrLi: any, N= None, head = True):
    '''Dada una ARRAY-LIST que sea una lista de diccionarios (e.g [{'title': 'Java ', 'street': ' 12', 'city': ''}, 
    {'title': '', 'street': ' 13', ...]) y una lista de llaves a MANTENER regresa una lista modificada con sólo las llaves a 
    mantener. #?Opcional: Se puede dar un argumento para mantener N-elementos (recortados desde la cabeza hacia la cola)'''
    arl = ile.EnsureADTLi(arrLi)
    arl = arl['elements']
    if N == None:
        arl = arl
    else:
        try:
            if (N < 10):
                arl = arl[0:N]
            else:
                if N >= 10:
                    first = arl[0:5]
                    last = arl[(len(arl))-6:(len(arl))]
                    ret = []
                    for ele in first: ret.append(ele)
                    for ele in last: ret.append(ele)  
                    arl = ret
                else:
                    arl = arl
        except:
            raise Exception("N puede ser Type 'None' o 'int' NO "+ str(type(N)))
    kept = lt.newList("ARRAY_LIST")
    for element in arl:
        dic = {}
        for key in keep:
            dic[key] =  element[key]
        lt.addLast(kept, dic)
    return kept