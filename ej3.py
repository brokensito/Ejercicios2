
valor = [5,2,5,6,8,1,4,5,9]

def modificar(valor):
    
    lista = list(set(valor))
    lista.sort()

    for i, c in enumerate(lista):
        if (lista[i]%2)!=0:
            lista.remove(c)

    lista.insert(0, sum(lista))
    return lista

n_lista = modificar(valor)

print(n_lista[0]==sum(n_lista[1:]))