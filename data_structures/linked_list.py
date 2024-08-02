
class Nodo:
    
    

	def __init__(self, data):
		# datos del nodo
		self.datos = data

		# puntero siguiente
		self.next = None





class LinkedList:
    
    def __init__(self):
		# inicializar la cabeza con None
        self.head = None
        self.len = 0
  
    
    def insert(self, nuevo_nodo):
        
        if self.head != None:
            
            puntero = self.head
            while puntero.next != None:
                puntero = puntero.next
            
            puntero.next = nuevo_nodo
                    
        else:
            self.head = nuevo_nodo
        self.len += 1
    
    def mostrar (self):
        
         if self.head != None:
            puntero = self.head
            contador = 0
        
            while contador < self.len:
                print(puntero.datos)
                puntero = puntero.next
                contador +=1
        
        
        
    def eliminar (self, pos):
        pass 

    
valores = 'abcdefg'
lista = LinkedList()

for letra in valores:
    
    lista.insert(Nodo(letra))
    
lista.mostrar()
