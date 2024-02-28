from contextlib import nullcontext
from operator import truediv


class Nodo:
    def __init__(self, valor):
        self.data = valor
        self.siguiente = None

class ListaSE:
    def __init__(self):
        self.cabeza = None


    def agregarInicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    #Función para buscar elemento por valor

    def buscarElemento(self, elemento):

        elementoActual = self.cabeza

        while elementoActual != None:
            if elementoActual.data is elemento: return True
            else: elementoActual = elementoActual.siguiente
        
        return False


    #Función para contar cuántos elementos tiene la lista

    def contarElementos(self):

        longitud = 0

        elementoActual = self.cabeza

        while elementoActual != None:
            elementoActual = elementoActual.siguiente
            longitud += 1
        
        return longitud


    #Función para indicar si la lista está vacía


    def estaVacia(self):

        if self.cabeza is None: 
            return True
        else: return False

#Fin de la lista


#Prueba de funciones y comandos
ListaSimple = ListaSE()
print(ListaSimple.estaVacia())
ListaSimple.agregarInicio(5)
ListaSimple.agregarInicio(10)
ListaSimple.agregarInicio(30)
print(ListaSimple.cabeza.data)
print(ListaSimple.buscarElemento(40))
print(ListaSimple.contarElementos())
ListaSimple.agregarInicio(40)
print(ListaSimple.contarElementos())
print(ListaSimple.buscarElemento(40))
