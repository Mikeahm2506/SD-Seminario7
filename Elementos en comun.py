"""
Previo seminario 7
Hernandez Martinez Miguel Angel
Funcion que recibe dos listas y arroja la lista de elementos en comun
"""

l1 =[0,1,2,3,4,5,6,7,8,9]
l2=[0,2,4,6,8]

def lista_comun(a,b):
    lf=[]
    for i in a:
        if (i not in lf) and (i in b):
                lf.append(i)
    print(lf)

lista_comun(l1,l2)

