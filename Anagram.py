from itertools import permutations

data = []
result = []

# Lee el archivo para pasar cada palabra a una lista
def readFile():
    file = open('wl.txt', 'r')
    row = file.readline()
    while row != "":
        data.append(row.strip())
        row = file.readline()
    file.close()

# Procesa la palabra ingresada con ciclos para recorrer cada posicion
'''
Procesa la palabra ingresada para obtener las conbinaciones
posibles de la palabra
'''
def processWordOne(w, i):
    if i == len(w) - 1:
        result.append(tuple(list(w)))
    else:
        for j in range(i, len(w)):
            t = w
            w = w[j] + w[:j] + w[(j + 1):]
            processWordOne(w, i + 1)
            w = t

# Procesa la palabra ingresada con el metodo "permutations"
def processWordTwo(word):
    for i in permutations(word):
        result.append(i)
    printResult(word)

# Imprime el resultado del anagrama
def printResult(word):
    for item in result:
        c = ''
        for p in item:
            c += p

        if c in data and len(c) == len(word):
            print(c)


'''
Se hace un llamado a la funcion "readFile" para leer
los datos del archivo y se guarda cada palabra en una lista
'''
readFile()

# Se ingresa la palabara a trabajar
word = str(input('Ingresar palabra: '))

'''
1RA OPCION DE RESULTADO
Metodo para trabajar la palabra y crear el anagrama
'''
processWordOne(word, 0)
printResult(word)

'''
2DA OPCION DE RESULTADO
Metodo para trabajar la palabra y crear el anagrama
'''
#processWordTwo(word)





