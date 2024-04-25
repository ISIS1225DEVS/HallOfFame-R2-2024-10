import Lists_G01 as lists
#Funciones para la estructura de Mapas
#Implementacion
def new_map(capacity):
    '''
    Crea un mapa vacio; dos listas vacias, una de llaves "keys" y otra 
    de valores "values".
    '''
    return hash_table(capacity)

def is_empty(mapa):
    '''
    Retorna True si el mapa está vacío y retorna False si tiene algú contenido.
    '''
    if lists.is_empty(mapa['keys']):
        return True
    else:
        return False
    
def keys(mapa):
    '''
    Retorna la lista con las llaves del mapa.
    '''
    return mapa['keys']

def get(ht, key):
    ''' 
    Retorna la pareja llave, valor, cuya llave sea igual a key.
    '''
    pos = hashfun(ht, key)
    for i in range(len(ht['keys'][pos])):
        if ht['keys'][pos][i] == key:
            return {'key': key, 'value': ht['values'][pos][i]}
    return None
 
def contains(mapa,key):
    '''
    Retorna True si la llave key se encuentra en el map
    o False en caso contrario.
    '''
    for llave in mapa['keys']:
        if llave == key:
            return True
    return False

def mapa_size(mapa):
    """
    Retorna el tamaño del mapa, es decir, la cantidad de elementos almacenados en él.
    """
    size = 0
    for lista in mapa['keys']:
        size += len(lista)
    return size
#SEPARATE CHAINING        

def put (ht, key, value):
    '''
    Se da una llave y un valor, y se añade la inormación en el mapa.
    '''
    if size_p(ht):
        ht = resize(ht)
    pos = hashfun(ht, key)
#    while ht['keys'][pos]:
#        pos = (pos + 1) % ht['capacity']
    ht['keys'][pos].append(key)
    ht['values'][pos].append(value)
    ht['load'] = max(len(ht["values"][pos]), ht["load"])
    return ht
#0n
def size_p(ht):
    if(ht["load"]) > 400:
        return True
    return False

def get_value(ht, key):
    '''
    Retorna el valor asociado a la llave dada de un mapa
    '''
    pos = hashfun(ht,key)
    dato=ht['values'][pos]
    return dato
    '''
    for i in range(len(dato)):
        if dato[i] == key:
            return ht['values'][i]
    while ht['keys'][pos] != None:
        k = ht['keys'][pos]
        if k==key:
            return k
        pos = (pos + 1) % ht['capacity']
    return None
    '''

def remove (ht, key):
    pos = hashfun(ht, key)
    for i in range(len(ht['keys'][pos])):
        if ht['keys'][pos][i] == key:
            ht['values'][pos].pop(i)
            ht['keys'][pos].pop(i)
            ht['load'] -= 1
            return ht
def rehash (ht):
    new = hash_table(2*ht['capacity']+1)
    for elem in ht['keys']:
        if elem !=None:
            put (new, elem[0], elem[1])
    return new

def get_info(pareja):
    return pareja[1]


def resize(ht):
    '''
    Amplia la tabla de Hash con una nueva capacidad
    '''
    new = hash_table(2*ht['capacity']+1)
    for i in range(len(ht['keys'])):
        for j in range(len(ht['keys'][i])):
            put(new, ht['keys'][i][j], ht['values'][i][j])
    return new

def hashfun(ht, key):
    return hash(key) % ht['capacity']

def hash_table(capacity):
    keys=[[] for _ in range(capacity)]
    values=[[] for _ in range(capacity)]
    return {'capacity':capacity, 'keys':keys, 'values':values, 'load': 0}

def remove(ht, key):
    '''
    Saca un elemento del mapa, dado su llave.
    '''
    pos = hashfun(key)
    for i in range(len(ht['keys'][pos])):
        if ht['keys'][pos][i] == key:
            ht['values'][pos].pop(i)
            ht['keys'][pos].pop(i)


    
    
    

    
