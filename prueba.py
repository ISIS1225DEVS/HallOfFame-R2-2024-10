#PRUEBAS
import Merge_sort_G01 as merge
import Lists_G01 as lists
from datetime import datetime

A=lists.new_list()
a,b,c,d={'num':5, 'let': 'A'},{'num':9, 'let': 'B'},{'num':1, 'let': 'C'},{'num':1, 'let': 'C'}
lists.add_last(A,a)
lists.add_last(A,b)
lists.add_last(A,c)
lists.add_last(A,d)

#orden=merge.merge_sort(A,'num')
#print(orden)

contada=lists.conteo(A,'let')
print(contada)
