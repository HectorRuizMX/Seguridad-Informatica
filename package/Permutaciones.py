def exchange(palabra):
    lista = []
    if len(palabra) == 1:
        lista.append(palabra)
    else:
        for i in range(len(palabra)):
            for j in exchange(palabra[:i] + palabra[i+1:]):
                lista.append(palabra[i] + j)
  

    return lista

def getExchangedWord(palabra):
    lista = exchange(palabra)
    lista.sort()
    
    obj = {
      "palabras": lista,
      "cantidad": len(lista)
    }
    
    return obj
