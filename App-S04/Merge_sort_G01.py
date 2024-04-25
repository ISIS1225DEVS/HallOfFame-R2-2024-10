import Lists_G01 as lists

#IMPLEMENTACION MERGESORT

def sort_crite(A,B,C,D):
    if A != B:
        return A > B
    else:
        return C < D

def merge_sort(lst, sort_crit, sort_crit2):
    '''
    Codigo basado en ISIS1225-Examples/DISClib/Algorithms/Sorting/mergesort.py
    '''
    size = lists.size(lst)
    if size > 1:
        mid = (size // 2)
        #se divide la lista original, en dos partes, izquierda y derecha,desde el punto mid
        leftlist = lists.sublist(lst, 0, mid)
        rightlist = lists.sublist(lst, mid, size - mid)

        #se hace el llamado recursivo con la lista izquierda y derecha
        merge_sort(leftlist,sort_crit, sort_crit2)
        merge_sort(rightlist,sort_crit, sort_crit2)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 0

        leftelements = lists.size(leftlist)
        rightelements = lists.size(rightlist)

        while (i < leftelements) and (j < rightelements):
            elemi = lists.get_element(leftlist, i)
            elemj = lists.get_element(rightlist, j)
            """compara y ordena los elementos"""
            if sort_crite(elemj[sort_crit], elemi[sort_crit], elemj[sort_crit2], elemi[sort_crit2] ):   # caso estricto elemj < elemi
                lists.change_info(lst, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                lists.change_info(lst, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i < leftelements:
            lists.change_info(lst, k, lists.get_element(leftlist, i))
            i += 1
            k += 1

        while j < rightelements:
            lists.change_info(lst, k, lists.get_element(rightlist, j))
            j += 1
            k += 1
    return lst
