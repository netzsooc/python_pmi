__author__ = 'netzsooc'

#               P(x, y)
# PMI(x, y) = ----------- =
#             P(x) * P(y)
#
#             P(x|y)
#             ------ =
#              P(x)
#
#             P(y|x)
#             ------
#              P(y)



''' 
La probabilidad condicional de dos palabras puede entenderse como las veces en
las que ocurre una palabra 'x' en la vecindad de 'y' sobre el total de veces
que ocurre 'y'.
'''


def prob_cond(x, y, concurrencias, absolutos):
    """TODO: 'x' y 'y' deben ser un par ordenado lexicográficamente en orden
    ascendente.

    :x: elemento condicionado
    :y: condición
    :concurrencias: TODO
    :absolutos: TODO
    :returns: float

    """
    return concurrencias(x, y) / absolutos[y]


def pmi(x, y, concurrencias, absolutos, probabilidad):
    """TODO: Docstring for pmi.

    :x: TODO
    :y: TODO
    :concurrencias: TODO
    :absolutos: TODO
    :probabilidad: TODO
    :returns: TODO

    """
    return prob_cond(x, y, concurrencias, absolutos) / probabilidad[x]
