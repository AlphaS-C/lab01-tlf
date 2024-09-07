import io
import sys
from matplotlib_venn import venn3
from matplotlib import pyplot as plt 

def union(set1, set2, set3):
    """
    Calcula la unión de tres conjuntos. La unión incluye todos los elementos que están en al menos uno de los conjuntos.

    :param set1: Primer conjunto.
    :param set2: Segundo conjunto.
    :param set3: Tercer conjunto.
    :return: Una lista que contiene la unión de los tres conjuntos.
    """
    set4 = []

    # Abstracción: Unir 3 conjuntos
    # Descomposición: 
        # Crear un conjunto vacio
        # agregarle los datos del conjunto 1
        # agregar los datos del conjunto 2 y 3 sin repetir
    for dato in set1:
        set4.append(dato)

    for dato in set2:
        if dato not in set4:
            set4.append(dato)

    for dato in set3:
        if dato not in set4:
            set4.append(dato)

    return set4

def interseccion(set1, set2, set3):
    """
    Calcula la intersección de tres conjuntos usando el método basado en listas. La intersección incluye los elementos comunes a los tres conjuntos.

    :param set1: Primer conjunto.
    :param set2: Segundo conjunto.
    :param set3: Tercer conjunto.
    :return: Una lista que contiene la intersección de los tres conjuntos.
    """
    set4 = []

    # Abstracción: Identificación de elementos comunes entre tres conjuntos
    # Descomposición: Elegir la lista más larga para optimizar la búsqueda
    tamaño_lista1 = len(set1)
    tamaño_lista2 = len(set2)
    tamaño_lista3 = len(set3)

    if tamaño_lista1 >= tamaño_lista2 and tamaño_lista1 >= tamaño_lista3:
        lista_mayor = set1
    elif tamaño_lista2 >= tamaño_lista1 and tamaño_lista2 >= tamaño_lista3:
        lista_mayor = set2
    else:
        lista_mayor = set3
    
    # Recorrer la lista mayor y agregar los datos que se repiten en las 3 listas

    for dato in lista_mayor:
        if dato in set1 and dato in set2 and dato in set3:
            set4.append(dato)

    return set4

def interseccion2(set1, set2):
    """
    Calcula la intersección de dos conjuntos usando el método basado en listas. La intersección incluye los elementos comunes a ambos conjuntos.

    :param set1: Primer conjunto.
    :param set2: Segundo conjunto.
    :return: Una lista que contiene la intersección de los dos conjuntos.
    """
    set3 = []

    # Abstracción: Identificación de elementos comunes entre dos conjuntos
    # Descomposición: Elegir la lista más larga para optimizar la búsqueda
    tamaño_lista1 = len(set1)
    tamaño_lista2 = len(set2)
    lista_mayor = set1 if tamaño_lista1 >= tamaño_lista2 else set2

    # Recorrer la lista mayor y agregar los datos que se repiten en las 2 listas

    for dato in lista_mayor:
        if dato in set1 and dato in set2:
            set3.append(dato)
    
    return set3

def diferencia(set1, set2, set3):
    """
    Calcula la diferencia entre tres conjuntos. La diferencia incluye los elementos que están en set1 pero no en set2 ni en set3.

    :param set1: Primer conjunto.
    :param set2: Segundo conjunto.
    :param set3: Tercer conjunto.
    :return: Una lista que contiene la diferencia entre los tres conjuntos.
    """
    set4 = list(set1)  # Convertimos set1 a lista para modificarlo

    # Abstracción: Eliminar elementos de set4 que están en set2 y set3
    # Descomposición: Procesar cada conjunto para eliminar sus elementos repetidos
    #   Primero se compara con el set 2 
    for dato in set2:
        if dato in set4:
            set4.remove(dato)
    # Y ese resultado se compara con el set3
    for dato in set3:
        if dato in set4:
            set4.remove(dato)

    return set4

def diferenciaSimetrica(set1, set2):
    """
    Calcula la diferencia simétrica entre dos conjuntos. La diferencia simétrica incluye los elementos que están en uno u otro conjunto, pero no en ambos.

    :param set1: Primer conjunto.
    :param set2: Segundo conjunto.
    :return: Una lista que contiene la diferencia simétrica entre los dos conjuntos.
    """
    set4 = union(set1, set2, [])  # Usamos una lista vacía como el tercer conjunto

    # Abstracción: Eliminar elementos comunes de set4
    # Descomposición: Primero calcular la unión y luego eliminar los elementos comunes
    # Reutilizamos la funcion de interseccion - Removemos la interseccion de la union
    for dato in interseccion2(set1, set2):
        set4.remove(dato)
    
    return set4

def is_subconjunto(set1, set2):
    """
    Determina si set1 es un subconjunto de set2. Un subconjunto es un conjunto cuyos elementos están todos en otro conjunto.

    :param set1: Primer conjunto.
    :param set2: Segundo conjunto.
    :return: True si set1 es un subconjunto de set2, False en caso contrario.
    """
    # Abstracción: Verificar si todos los elementos de set1 están en set2
    for dato in set1:
        if dato not in set2:
            print(set1, " no es un subconjunto de ", set2 )
            return False
    print(set1, " si es un subconjunto de ", set2 )
    return True


def is_superconjunto(set1, set2):
    """
    Determina si set1 es un superconjunto de set2. Un superconjunto es un conjunto que contiene todos los elementos de otro conjunto.

    :param set1: Primer conjunto.
    :param set2: Segundo conjunto.
    :return: True si set1 es un superconjunto de set2, False en caso contrario.
    """

    original_stdout = sys.stdout

    # Redirigir sys.stdout a un objeto de archivo temporal
    sys.stdout = io.StringIO()

    try:
        # Llamar a la función que queremos ejecutar sin mostrar sus prints
        # Reutilizamos la funcion is_subconjunto
        respuesta = is_subconjunto(set1, set2)
    finally:
        # Restaurar sys.stdout a su valor original
        # Abstracción: Determinar si set1 contiene todos los elementos de set2
        sys.stdout = original_stdout
        if respuesta:
            print(set1, " es un superconjunto de", set2)
        else:
            print(set1, " no es un superconjunto de ", set2)


def main():
    # Definimos tres conjuntos de ejemplo
    A = {1, 2, 3, 7}
    B = {3, 5, 6, 7}
    C = {2, 3, 8, 9, 7}

    # Calculamos y mostramos la unión, intersección, diferencia y diferencia simétrica
    union_R = union(A.copy(), B.copy(), C.copy())
    print("Union a pedal: ", union_R)
    print("Union python: ", A.copy() | B.copy() | C.copy())

    interseccion_R = interseccion(A.copy(), B.copy(), C.copy())
    print("Interseccion a pedal: ", interseccion_R)
    print("Interseccion python: ", A.copy() & B.copy() & C.copy())

    diferencia_R = diferencia(B.copy(), C.copy(), A.copy())
    print("Diferencia a pedal: ", diferencia_R)
    print("Diferencia python: ", (B.copy() - C.copy()) - A.copy())

    diferencia_simetrica_R = diferenciaSimetrica(diferenciaSimetrica(A.copy(), B.copy()), C.copy())
    print("Diferencia simetrica a pedal: ", diferencia_simetrica_R)
    print("Diferencia simetrica python: ", A.copy() ^ B.copy() ^ C.copy())

    D = {3,6,7}

    is_subconjunto(D.copy(), B.copy())

    is_superconjunto(A.copy(), D.copy())


    # DIAGRAMA DE VENN

    venn = venn3((A, B, C), ('A', 'B', 'C'))
    # Obtener los subconjuntos y sus elementos
    subset_ids = {
    '100': diferencia(A.copy(), B.copy(), C.copy()),
    '010': diferencia(B.copy(), A.copy(), C.copy()),
    '001': diferencia(C.copy(), A.copy(), B.copy()),
    '110': interseccion(A.copy(), B.copy(), diferencia(B.copy(), A.copy(), C.copy())),
    '101': interseccion(A.copy(), C.copy(), diferencia(A.copy(), B.copy(), C.copy())),
    '011': interseccion(B.copy(), C.copy(), diferencia(A.copy(), B.copy(), C.copy())),
    '111': interseccion(A.copy(), B.copy(), C.copy())
    }

    # Añadir el conteo de elementos y los elementos a las etiquetas del diagrama de Venn
    for subset_id, elements in subset_ids.items():
        venn.get_label_by_id(subset_id).set_text(f'{len(elements)}\n{elements}')
    plt.show()

if __name__ == "__main__":
    main()
