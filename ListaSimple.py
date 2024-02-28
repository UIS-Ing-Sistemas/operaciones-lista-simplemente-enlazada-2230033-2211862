from contextlib import nullcontext
from operator import truediv


class Nodo:
    def __init__(self, valor):
        self.data = valor
        self.siguiente = None

class ListaSE:
    def __init__(self):
        self.cabeza = None
#Funcion para Imprimir la lista
    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.data, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")
#Funcion para agregar al inicio
    def agregarInicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            
#Funcion para Agregar al final
    def agregarFinal(self, valor):
        nuevo_nodo = Nodo(valor)
        nodo_Actual = self.cabeza

        if nodo_Actual is None:
            self.cabeza = nuevo_nodo
            return self.cabeza

        while nodo_Actual.siguiente is not None:
            nodo_Actual = nodo_Actual.siguiente

        nodo_Actual.siguiente = nuevo_nodo
        return self.cabeza
    
# Funcion eliminar el primero

    def eliminarPrimero(self):
        if self.cabeza is None:
            print("La lista esta vacia")
            return
        
        self.cabeza = self.cabeza.siguiente
        
#Funcion Elimiar el ultimo
    def eliminarFinal(self):
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        
        nodo_actual = self.cabeza
        while nodo_actual.siguiente.siguiente is not None:
            nodo_actual = nodo_actual.siguiente
            
        nodo_actual.siguiente = None

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
ListaSimple.agregarFinal(16)
ListaSimple.imprimir_lista()
ListaSimple.eliminarFinal()
ListaSimple.imprimir_lista()
ListaSimple.eliminarPrimero()
ListaSimple.imprimir_lista()