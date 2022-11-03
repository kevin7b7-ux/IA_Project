from Nodo import Nodo, np
entorno = np.loadtxt('entorno.txt', dtype=int)
nodo = Nodo(entorno)
meta = [1, 2]

#Búsqueda por amplitud, evitando devolverse
def bfs(nodo, goal):
    stack = []
    arbol = []
    stack.append(nodo)
    arbol.append(nodo)
    ruta = []
    while len(stack) > 0:
        nodo_expandido = stack.pop(0)
        ruta.append(nodo_expandido.entorno)
        if (nodo_expandido.posm() == goal):
            print("Se encontró a la princesa")
            return ruta
        else:
            #Izquierda
            if (nodo_expandido.posm()[1]-1 >= 0):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]-1] != 1):
                    hijo=Nodo(nodo_expandido.mover(1), nodo_expandido)
                    #evitar devolverse
                    if np.array_equal(nodo_expandido.padre,hijo.entorno):
                        pass    
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)
            #Derecha  
            if (nodo_expandido.posm()[1]+1 <= len(nodo_expandido.entorno[0])-1):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]+1] != 1):
                    hijo=Nodo(nodo_expandido.mover(2), nodo_expandido)
                    #evitar devolverse
                    if np.array_equal(nodo_expandido.padre,hijo.entorno):
                        pass    
                    else:
                        stack.append(hijo)
                        arbol.append(hijo) 
            #Arriba  
            if(nodo_expandido.posm()[0]-1 >= 0):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]-1][nodo_expandido.posm()[1]] != 1):
                    hijo=Nodo(nodo_expandido.mover(3), nodo_expandido)
                    #evitar devolverse
                    if np.array_equal(nodo_expandido.padre,hijo.entorno):
                        pass    
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)  
            #Abajo  
            if (nodo_expandido.posm()[0]+1 <= len(nodo_expandido.entorno)-1):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]+1][nodo_expandido.posm()[1]] != 1):
                    hijo=Nodo(nodo_expandido.mover(4), nodo_expandido)
                    #evitar devolverse
                    if np.array_equal(nodo_expandido.padre,hijo.entorno):
                        pass    
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)            


res = bfs(nodo, meta)

#Imprmir los nodos expandidos contenidos en la ruta
for i in res:
    print(i)

