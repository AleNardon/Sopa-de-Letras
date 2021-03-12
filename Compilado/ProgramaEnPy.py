from random import randint

#removeN:list -> list
#Dada una lista, si esta tiene en sus str un salto de página es decir "\n"
#lo quita y nos devuelve otra lista de str sin \n.

def removeN(lista):
    newlist = []
    for x in lista:
        w = x.replace("\n","")
        newlist.append(w)
    return newlist

#----------------------
#makeL:list->list
#Dada una lista, crea una nueva lista con la palabra y como segunda componente el dígito.

def makeL(lista):
    newlist = []
    for x in lista:
        s = len(x)
        newlist.append([x.replace(" " + x[s-1],"") , int (x[s-1])])
    return newlist

#-------------------
#extraerTexto: str -> list
#Dado un archivo del tipo de salida de la sopa de letras, realizará una lista de listas que contendrá
#la palabra seguida de la posición que esta tendrá.

def extraerJug(ruta):
    archivo = open(ruta,"r")                #Abrimos el archivo de las jugadas.

    listarchivo = archivo.readlines()       #Extraemos todas las lineas y van a una lista.
    listarchivo = removeN(listarchivo)      #Removemos los \n de los elementos de la lista.
    tam = int(listarchivo[1])               #Extraemos el tamaño de la sopa.
    
    listarchivo.pop(0)                      
    listarchivo.pop(0)                      #Eliminamos las tres primeras componentes de la lista para que queden sólo las palabras con el número.
    listarchivo.pop(0)
    
    archivo.close()                         #Cerramos el archivo.
    
    listarchivo = makeL(listarchivo)        #Organizamos a través de una sub-lista las palabras con su orientación [str,int].

    return listarchivo, tam                 #Devolvemos una lista del tipo [[str, int],[str, int]...] y el tamaño de la sopa.

#-------------------
#ExtraeLem: str or None -> list
#Dada una ruta o la predefinida (lemario.txt) nos devuelve el contenido del txt en una lista.

def extraeLem(ruta = "lemario.txt"):
    lem = open(ruta,"r")
    listalem = lem.readlines()
    listalem = removeN(listalem)
    lem.close()
    return listalem

#-------------------
#palabraNew: str int str - > str
#Dada la ruta del lemario, el tamaño de la sopa y la palabra, si es que la palabra no se encuentra en el lemario, la sustituye por una palabra del 
# lemario con una cantidad de caracteres menor o igual al tamaño de la sopa. Si no mantenemos la palabra inicial.

def palabraNew(lemario,tam,palabra):
    pal = palabra                                         

    if not pal in lemario:                                  #Si la palabra no está en el lemario o es mayor al tamaño.
        
        pal = lemario[randint(0,len(lemario))]              #Eligue otra palabra al azar del lemario.
        
        while not len(pal) <= tam :                         #Si su tamaño no sigue siendo el adecuado.
            pal = lemario[randint(0,len(lemario))]          #Eligue otra palabra al azar del lemario.
    
    return pal                                              #Devuelve la palabra.

#-------------------
#checkL: str str -> list 
#Dada la ruta del lemario y la ruta de la jugada nos devuelve una lista con las palabras chequeadas, es decir 
#si alguna de las palabras inicialmente no se encuentra en el lemario se remplazará.

def checkL (rutalem,rutajug):
    jugadas = extraerJug(rutajug)[0]            #Extrae la lista de palabras jugadas.
    
    tam = extraerJug(rutajug)[1]                #Extrae el tamaño de la sopa de letras. 
    lemario = extraeLem(rutalem)                #Extrae una lista con las palabras del lemario.

    l = []
    for x in jugadas:
        pal = x[0]                              #Toma la primer componente de la sub-lista [str,int].
        o = x[1]                                #Toma la segunda componente de la sub-lista [str,int].
        newpal = palabraNew(lemario,tam,pal)    #Escoge una palabra nueva de ser necesario.
        l.append([newpal,o])                    #Agrega la jugada a una nueva lista.
    
    return l,tam         

#-------------------
#Nuestro programa generará una lista de listas las cuales hacen referencia a cada fila de la sopa de letras, es decir 
#el primer elemento de nuestra lista será la primer fila, el segundo la segunda y asi sucesivamente.
#-------------------

#CreaTablero: int -> list
# Dado un número n nos devuelve una lista de listas donde tendrá n-veces "-" como elemento y n sub-listas. 

def creaTablero(numero):
    t = []
    for _ in range(numero):
        t.append(["-"]*numero)        
    return t

#-------------------
#checkPrimero: list int -> bool
#Es el primer chequeo que haremos sobre si se puede crear o no la sopa.
#Dada una lista de listas(lista de la sopa) y un número (tamaño) nos devuelve False si alguna palabra excede 
#en caracteres el tamaño de la sopa.

def checkPrimero(lista ,tam):
    e = True
    for x in lista:
        if len(x[0])>tam:
            e = False
            break
    return e

#-------------------
#genereaLista: list -> tuple 
#Dada una lista del tipo sopa, nos devuelve una tupla de tres elementos, el primero serán la palabras en horizontal 
#el segundo serán las palabras que están en vertical y la última componente serán de las palabras en diagonal.

def generaLista(lista):
    h = []                  #Horizonltales con el número 0 y 1.
    v = []                  #Verticales con el número 2 y 3.
    d = []                  #Diagonales con el número 4 y 5.

    for x in lista:
        if x[1] == 0 or x[1] == 1:
            h.append(x[0])
        elif x[1] == 2 or x[1] == 3:
            v.append(x[0])
        else :
            d.append(x[0])
    
    return h,v,d

#-------------------
# listaLetras: list -> list
# Dada una lista de palabras nos devolverá una nueva lista donde cada elemento serán las letras de las palabras. 
def listaLetras(lista):
    li = []
    for x in lista:
        for l in x:
            li.append(l)
    
    return li

#-------------------
#variablesLetras: lista -> int 
# Dada una lista del tipo sopa, nos devolverá un número el cual será una suma de la cantidad de caracteres que hay por orientación, es decir [0,1][2,3][4,5], de los cuales no se sumarán 
# caracteres que esten en otro grupo. Por ejemplo tenemos la palabra "hoy" en un grupo y en el otro "ola", el caracter "o" no se sumara dos veces sino una. 
# Lo usaremos más tarde para ver si la suma total de caracteres será mayor o menor a la dimensión de la sopa     [["hoy",0],["ola",3],[]] == 5 .

def  variablesLetras(lista):
    h = generaLista (lista)[0]
    v = generaLista (lista)[1]
    d = generaLista (lista)[2]

    hl = listaLetras(h)
    vl = listaLetras(v)
    dl = listaLetras(d)

    for x in hl:
        if x in vl:
            vl.remove(x)
    
    for x in hl:
        if x in dl:
            dl.remove(x)
    
    for x in vl:
        if x in dl:
            dl.remove(x)

    contador = len(hl) + len(vl) + len(dl)

    return contador

#-------------------
# elcPos :list int -> tuple 
#Dada una lista con las jugadas anteriormente usadas y el tamaño, nos devuelve una posición aleatoria de la sopa 
#que no se haya jugado anteriormente.

def elcPos(lista,tam):
    posv = randint(0,tam-1) 
    posh = randint(0,tam-1)
        
    while [posv,posh] in lista: 
        posv = randint(0,tam-1) 
        posh = randint(0,tam-1)

    return posv, posh 

#-------------------
#NOTA: A continuación tendremos 9 funciones las cuales actuan de manera similar, el único cambio es su forma de realizar los movimientos respecto a cada 
#orientación de las palabras. Dentro de cada función tendremos la orientación que se indicara con un bool, si este es True, la palabra
#tendrá una orientación normal es decir de izq a der, arriba hacia abajo y arriba izq hacia abajo derecha. Con False daremos las orientraciones inversas, 
# es decir de der a izq, de abajo hacia arriba y de abajo izq hacia arriba der.
#-------------------

#CheckHorizontal: list str int int bool -> bool
#Dada la lista del tablero, una palabra, una posición vertical en el tablero, 
# una posición horizontal en el tablero y la orientación de la palabra representada con True o False,
#nos devolverá True si es que la palabra entra desde esa posición y también si hay "-" 
# o letras que coincidan con los caracteres de la palabra, en caso contrario nos devuelve false.

def checkHorizontal(tablero,palabra,posv,posh,orientacion):
    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                          #El try se ejecuta y si da error es por que se va del index de la lista.
            if tablero[v][h] == letra or tablero[v][h] == "-":        #Si la letra que estaba en el tablero coincide con la de la palabra o hay una casilla vacía es decir "-".
                
                if v>=0 and h>=0:                                     #Esta condicion se debe a que al restar puede pasar en negativo y que no de error pero no sea posible la palabra en horizontal.
                    if orientacion:         	                      #Se mueve en horizontal sumando 1 en horizontal si la orientación es True.
                        h += 1
                    else:
                        h-=1                                          #Se mueve en horizontal restando 1 en horizontal si la orientación es False.
                
                else:                                                 #Caso que la posición sea negativa es porque se salió del rango, por lo tanto no entra.
                    e = False               
                    break    

            else:
                e = False                                             #No es válida la palabra en esa posición.
                break

        except IndexError:                                            #Si hay un error donde el index de la lista del tablero a excedido su tam, entonces la palabra no es válida.
            e = False
            break

    return e                                                          #Devuelve el estado.

#------
#aggHorizontal: list str int int bool -> list 
# Dada la lista del tablero, una palabra, dos posiciones en el tablero y la orientación, agrega la palabra de forma horizontal según la orientación colocada.

#No se tienen en cuenta errores como si esta por fuera del index debido a que en la función madre de horizontal tendrá en cuenta 
# estas excepciones.

def aggHorizontal(tablero,palabra,posv,posh,orientacion):
    v = posv
    h = posh

    for letra in palabra:
        tablero[v][h] = letra
        if orientacion:
            h +=1
        else:
            h -=1

    return tablero

#------
#horizontal: list str int bool -> list or bool
#Dada una lista del tablero, una palabra, el tamaño del tablero y la orientación, agregaremos la palabra en una posición inicial random y nos devolverá un nuevo tablero con la palabra agregada
#en un lugar que sea válido. En caso de no encontrar un lugar nos devolverá un bool-> False indicando que esa palabra no se puede colocar.

def horizontal(tablero,palabra,tam,orientacion):
    jugadas = []                                                       #Creamos una lista con las posiciones jugadas en esta función.
                            
    pos = elcPos(jugadas,tam)                                          #Generamos una posición inicial aleatoria la cual no se a jugado anteriormente en esta función.
    posv = pos[0]                                                      #Posición vertical de la letra inicial.
    posh = pos[1]                                                      #Posición horizontal de la letra inicial.           
    jugadas.append([posv,posh])                                        #Agregamos la jugada a las posiciones jugadas en la función.
                        
    intentos = tam*tam                                                 #La cantidad de posibilidades de una posición inicial no será mayor a la cantidad de casillas.
    
    while  not checkHorizontal(tablero,palabra,posv,posh,orientacion): #Si la palabra no es válida a partir de la posición inicial.
        intentos-=1
        
        if intentos  == 0:                                             #Si ya no hay más casillas por probar.
            break 
       
        else:
            pos = elcPos(jugadas,tam)                                  #Repite los pasos anteriormente hechos.
            posv = pos[0]
            posh = pos[1]
            jugadas.append([posv,posh])

    if intentos == 0:                                                  #Si ya no hay más casillas por probar.
        return False

    else:
        table = aggHorizontal(tablero,palabra,posv,posh,orientacion)   #Creamos el nuevo tablero.
        return table

#-------------------
#CheckVertical:list str int int bool -> bool
#Dada la lista del tablero, una palabra , una posición vertical en el tablero, 
# una posición horizontal en el tablero y la orientación de la palabra representada con True o False,
#nos devolverá True si es que la palabra entra desde esa posición y también si hay "-" 
# o letras que coincidan con los caracteres de la palabra, en caso contrario nos devuelve false.

def checkVertical(tablero,palabra,posv,posh,orientacion):

    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                       #El try se ejecuta y si da error es por que se va del index de la lista.
            if tablero[v][h] == letra or tablero[v][h] == "-":     #Si la letra que estaba en el tablero coincide con la de la palabra o hay una casilla vacia es decir "-".
                
                if v>=0 and h>=0:                                  #Esta condicion se debe a que al restar puede pasar en negativo y que no de error pero no sea posible la palabra en vertical.
                    if orientacion:                                #Se mueve en vertical sumando 1 si la orientación es True.
                        v += 1
                    else:
                        v -=1                                      #Se mueve en vertical restando 1 si la orientación es False.
                
                else:                                              #Caso que la posición sea negativa es por que se salió del rango, por lo tanto no entra.
                    e = False           
                    break    

            else:
                e = False                                          #No es válida la palabra en esa posición.
                break

        except IndexError:                                          #Si hay un error donde el index de la lista del tablero a excedido su tam, entonces la palabra no es válida.
            e = False
            break

    return e                                                       #Devuelve el estado.

#------
#aggVertical: list str int int bool -> list 
# Dada la lista del tablero, una palabra, dos posiciones en el tablero y la orientación, agrega la palabra de forma vertical según la orientación colocada.

#No se tienen en cuenta errores como si esta por fuera del index debido a que en la función madre de vertical tendrá en cuenta 
# estas excepciones.

def aggVertical(tablero,palabra,posv,posh,orientacion):

    v = posv
    h = posh

    for letra in palabra:
        tablero[v][h] = letra
        if orientacion:
            v +=1
        else:
            v -=1

    return tablero

#------
#vertical: list str int bool -> list or bool
#Dada una lista del tablero, una palabra, el tamaño del tablero y la orientación, agregaremos la palabra en una posición inicial random y nos devolverá un nuevo tablero con la palabra agregada
#en un lugar que sea válido. En caso de no encontrar un lugar nos devolverá un bool-> False indicando que esa palabra no se puede colocar.

def vertical(tablero,palabra,tam,orientacion):
    jugadas = []                                                       #Creamos una lista con las posiciones jugadas en esta función.
                            
    pos = elcPos(jugadas,tam)                                          #Generamos una posición inicial aleatoria la cual no se a jugado anteriormente en esta función.
    posv = pos[0]                                                      #Posición vertical de la letra inicial.
    posh = pos[1]                                                      #Posición horizontal de la letra inicial.
    jugadas.append([posv,posh])                                        #Agregamos la jugada a las posiciones jugadas en la función.
                        
    intentos = tam*tam                                                 #la cantidad de posibilidades de una posición inicial no sera mayor a la cantidad de casillas.
    
    while  not checkVertical(tablero,palabra,posv,posh,orientacion):   #Si la palabra no es válida a partir de la posición inicial.
        intentos-=1
        
        if intentos  == 0:                                             #Si ya no hay más casillas por probar.
            break 
        else:
            pos = elcPos(jugadas,tam)                                  #Repite los pasos anteriormente hechos.
            posv = pos[0]
            posh = pos[1]
            jugadas.append([posv,posh])

    if intentos == 0:                                                 #Si ya no hay más casillas por probar.
        return False

    else:
        table = aggVertical(tablero,palabra,posv,posh,orientacion)    #Creamos el nuevo tablero.
        return table

#-------------------
#checkDiagonal : list str int int bool -> bool
#Dada la lista del tablero, una palabra, una posición vertical en el tablero, 
# una posición horizontal en el tablero y la orientación de la palabra representada con True o False,
#nos devolverá True si es que la palabra entra desde esa posición y también si hay "-" 
# o letras que coincidan con los caracteres de la palabra, en caso contrario nos devuelve false.

def checkDiagonal(tablero,palabra,posv,posh,orientacion):
    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                    #El try se ejecuta y si da error es por que se va del index de la lista.
            if tablero[v][h] == letra or tablero[v][h] == "-":  #Si la letra que estaba en el tablero coincide con la de la palabra o hay una casilla vacía es decir "-".

                if v>=0 and h>=0:                               #Esta condicion se debe a que al restar puede pasar en negativo y que no de error pero no sea posible la palabra en diagonal.
                    if orientacion:                             #Se mueve en diagonal sumando 1 en vertical y horizontal si la orientación es True.
                        v +=1                                           
                        h +=1
                    else:                                       #Se mueve en diagonal restando 1 en vertical y horizontal si la orientación es False.
                        v -=1              
                        h +=1
                
                else:                                           #Caso que la posición sea negativa es por que se salió del rango, por lo tanto no entra.
                    e = False
                    break    
   
            else:
                e = False                                       #No es válida la palabra en esa posición.
                break

        except IndexError:                                      #Si hay un error donde el index de la lista del tablero a excedido su tam, entonces la palabra no es válida.
            e = False
            break

    return e                                                    #Devuelve el estado.

#------
#aggDiagonal: list str int int bool -> list 
# Dada la lista del tablero, una palabra, dos posiciones en el tablero y la orientación, agrega la palabra de forma diagonal según la orientación colocada.

#No se tienen en cuenta errores como si esta por fuera del index debido a que en la función madre de diagonal tendrá en cuenta 
# estas excepciones.

def aggDiagonal(tablero,palabra,posv,posh,orientacion):

    v = posv
    h = posh

    for letra in palabra:
        tablero[v][h] = letra
        if orientacion:                                   #Se mueve en diagonal sumando 1 en vertical y horizontal si la orientación es True.
            v +=1                                           
            h +=1
        else:                                             #Se mueve en diagonal restando 1 en vertical y sumando 1 horizontal si la orientación es False.
            v -=1              
            h +=1
  
    return tablero

#------
#diagonal: list str int bool -> list or bool
#Dada una lista del tablero, una palabra, el tamaño del tablero y la orientación, agregaremos la palabra en una posición inicial random y nos devolverá un nuevo tablero con la palabra agregada
#en un lugar que sea válido. En caso de no encontrar un lugar nos devolverá un bool-> False indicando que esa palabra no se puede colocar.

def diagonal(tablero,palabra,tam,orientacion):
    jugadas = []                                    #Creamos una lista con las posiciones jugadas en esta función.
    
    pos = elcPos(jugadas,tam)                       #Generamos una posición inicial aleatoria la cual no se a jugado anteriormente en esta función.
    posv = pos[0]                                   #Posición vertical de la letra inicial.
    posh = pos[1]                                   #Posición horizontal de la letra inicial.
    jugadas.append([posv,posh])                     #Agregamos la jugada a las posiciones jugadas en la función.

    intentos = tam*tam                              #la cantidad de posibilidades de una posición inicial no sera mayor a la cantidad de casillas.
    
    while not checkDiagonal(tablero,palabra,posv,posh,orientacion): #Si la palabra no es válida a partir de la posición inicial.
        intentos-=1

        if intentos == 0:                           #Si ya no hay más casillas por probar.
            break 
        
        else:
            pos = elcPos(jugadas,tam)               #Repite los pasos anteriormente hechos.                                                 
            posv = pos[0]
            posh = pos[1]
            jugadas.append([posv,posh])

    if intentos == 0:                               #Si ya no hay más casillas por probar. 
        return False

    else:
        table = aggDiagonal(tablero,palabra,posv,posh,orientacion) #Creamos el nuevo tablero.
        return table

#-------------------
#aggPalabras: list str int  -> list or bool
#Dado una lista del tablero, una palabra y la orientación del 0-5 nos devuelve una lista con la palabra agregada 
# o un bool indicando que esa palabra no fue posible agregarla.

def aggPalabras(tablero,palabra,orientacion):
    if   orientacion == 0:                                          #Horizontal de izquierda a derecha.
        return horizontal(tablero,palabra,len(tablero),True)
    elif orientacion == 1:                                          #Horizontal de derecha a izquierda. 
        return horizontal(tablero,palabra,len(tablero),False)
    
    elif orientacion == 2:                                          #Vertical de arriba hacia abajo.
        return vertical(tablero,palabra,len(tablero),True)
    elif orientacion == 3:                                          #Vertical de abajo hacia arriba.
        return vertical(tablero,palabra,len(tablero),False)

    elif orientacion == 4:                                          #Diagonal de arriba izq hacia abajo der.
        return diagonal(tablero,palabra,len(tablero),True)
    elif orientacion == 5:                                          #Diagonal de abajo izq hacia arriba der.
        return diagonal(tablero,palabra,len(tablero),False)


#-------------------
#escribeTablero: list int  -> list or bool
#Dada una lista de palabras con su orientación y el tamaño del tablero, nos devuelve una lista del tablero con las palabras en el tablero 
#o nos devuelve un bool indicando que no es posible realizar la sopa.

def escribeTablero(lista,tam):
    tablero = creaTablero(tam)                                      #Creamos un tablero.
    
    
    if checkPrimero(lista,tam):                                     #Realizamos el primer chequeo si es que alguna palabra es mayor al tamaño ya no se puede hacer.
        
        if variablesLetras(lista)>=tam:                             #Realizamos el segundo chequeo anteriormente explicado. ········
            
            for x in lista:                         
                tablero = aggPalabras(tablero,x[0],x[1])            #Agregamos cada palabra al tablero.
                if tablero == False:                                #Si dio false no se puede hacer.
                    return False

            return tablero                              
        else:
            return False

    else:
        return False 

#-------------------
# abc: None -> str 
#Nos devuelve una letra al azar del abecedario.
def abc():
    abce = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    n = randint(0,len(abce)-1)

    return abce[n]

#-------------------
#rellenaTablero: List -> list
#Dada una lista con las palabras dentro del tablero rellenaremos los espacios en blanco "-" por una letra al azar del abecedario
#y devuelve una nueva lista con los espacios en blanco completos.

def rellenaTablero(tablero):
    contv = 0
    conth = 0
    l = tablero

    for listas in l:
        
        for e in listas:
            if e == "-":
                l[contv][conth] = abc()
            conth +=1
        conth=0
        contv+=1

    return l

#-------------------
# NOTA: Las siguientes funciones serán muy similares a las anteriores con la diferencia que no detecta si hay "-", 
# sólo detecta si coinciden los caracteres de la palabra.
#-------------------

#checkRepetidosh1: list str int int bool -> bool
#Dada la lista del tablero, una palabra, una posición vertical en el tablero, 
# una posición horizontal en el tablero y la orientación de la palabra representada con True o False,
#nos devolverá True si letras que coinciden con los caracteres de la palabra, en caso contrario nos devuelve false.

def checkRepetidosh1(tablero,palabra,posv,posh,orientacion):
    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                          #El try se ejecuta y si da error es por que se va del index de la lista.
            if tablero[v][h] == letra :                               #Si la letra que estaba en el tablero coincide con la de la palabra.
                
                if v>=0 and h>=0:                                     #Esta condicion se debe a que al restar puede pasar en negativo y que no de error pero no sea posible la palabra en horizontal.
                    if orientacion:         	                      #Se mueve en horizontal sumando 1 en horizontal si la orientación es True.
                        h += 1
                    else:
                        h-=1                                          #Se mueve en horizontal restando 1 en horizontal si la orientación es False.
                
                else:                                                 #Caso que la posición sea negativa es por que se salió del rango, por lo tanto no entra. 
                    e = False               
                    break    

            else:
                e = False                                             #No es válida la palabra en esa posición.
                break

        except IndexError:                                            #Si hay un error donde el index de la lista del tablero a excedido su tam, entonces la palabra no es válida.
            e = False
            break

    return e                                                          #Devuelve el estado.     

#-------------------
#checkRepetidosH: list str -> tuple
#Dado un tablero y una palabra nos devuelve una tupla donde la primer componente son 
# sub-listas donde se contiene una posición y un bool que hace referencia a si la 
#palabra se encuentra en horizontal de izq a der, True si se encuentra y False si no.
#La segunda componente de la tupla es lo mismo nada más que tenemos en cuenta la palabra de der a izq.

def checkRepetidosH(tablero,pal):
    v = 0
    h = 0
    t = []
    f = []

    for lista in tablero:
        for _ in lista:                                                     #No itera con los elementos de la lista pero si los recorre.
            t.append([v,h,checkRepetidosh1(tablero,pal,v,h,True)])          #Agrega a una lista si en esa posición esta la palabra en horizontal de izq a der.
            f.append([v,h,checkRepetidosh1(tablero,pal,v,h,False)])         #Agrega a una lista si en esa posición esta la palabra en horizontal de der a izq. 
            h+=1
        h=0
        v+=1
    
    return t,f

#-------------------
#checkRepetidosv1: list str int int bool -> bool
#Dada la lista del tablero, una palabra, una posición vertical en el tablero, 
# una posición horizontal en el tablero y la orientación de la palabra representada con True o False,
#nos devolverá True si letras que coinciden con los caracteres de la palabra, en caso contrario nos devuelve false.

def checkRepetidosv1(tablero,palabra,posv,posh,orientacion):

    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                       #El try se ejecuta y si da error es por que se va del index de la lista.
            if tablero[v][h] == letra:                             #Si la letra que estaba en el tablero coincide con la de la palabra. 
                
                if v>=0 and h>=0:                                  #Esta condicion se debe a que al restar puede pasar en negativo y que no de error pero no sea posible la palabra en horizontal.
                    if orientacion:                                #Se mueve en horizontal sumando 1 en horizontal si la orientación es True.
                        v += 1
                    else:
                        v -=1                                      #Se mueve en horizontal restando 1 en horizontal si la orientación es False.
                
                else:                                              #Caso que la posición sea negativa es por que se salió del rango, por lo tanto no entra. 
                    e = False           
                    break    

            else:
                e = False                                          #No es válida la palabra en esa posición.
                break

        except IndexError:                                         #Si hay un error donde el index de la lista del tablero a excedido su tam, entonces la palabra no es válida.
            e = False
            break

    return e                                                       #Devuelve el estado. 

#-------------------
#checkRepetidosV: list str -> tuple
#Dado un tablero y una palabra nos devuelve una tupla donde la primer componente son 
# sub-listas donde se contiene una posición y un bool que hace referencia a si la 
#palabra se encuentra en vertical de arriba hacia abajo, True si se encuentra y False si no.
#La segunda componente de la tupla es lo mismo nada más que tenemos en cuenta la palabra de abajo hacia arriba.

def checkRepetidosV(tablero,pal):
    v = 0
    h = 0
    t = []
    f = []

    for lista in tablero:
        for _ in lista:
            t.append([v,h,checkRepetidosv1(tablero,pal,v,h,True)])
            f.append([v,h,checkRepetidosv1(tablero,pal,v,h,False)])
            h+=1
        h=0
        v+=1
    
    return t,f

#-------------------
#checkRepetidosd1: list str int int bool -> bool
#Dada la lista del tablero, una palabra, una posición vertical en el tablero, 
# una posición horizontal en el tablero y la orientación de la palabra representada con True o False,
#nos devolverá True si letras que coinciden con los caracteres de la palabra, en caso contrario nos devuelve false.

def checkRepetidosd1(tablero,palabra,posv,posh,orientacion):
    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                    #El try se ejecuta y si da error es por que se va del index de la lista.
            if tablero[v][h] == letra:                          #Si la letra que estaba en el tablero coincide con la de la palabra. 

                if v>=0 and h>=0:                               #Esta condicion se debe a que al restar puede pasar en negativo y que no de error pero no sea posible la palabra en diagonal.
                    if orientacion:                             #Se mueve en diagonal sumando 1 en vertical y horizontal si la orientación es True.
                        v +=1                                           
                        h +=1
                    else:                                       #Se mueve en diagonal restando 1 en vertical y horizontal si la orientación es False.
                        v -=1              
                        h +=1
                
                else:                                           #Caso que la posición sea negativa es por que se salió del rango, por lo tanto no entra. 
                    e = False           
                    break    
                   
            else:
                e = False                                       #No es válida la palabra en esa posición.
                break

        except IndexError:                                      #Si hay un error donde el index de la lista del tablero a excedido su tam, entonces la palabra no es válida.
            e = False
            break

    return e                                                    #Devuelve el estado. 

#-------------------
#checkRepetidosD: list str -> tuple
#Dado un tablero y una palabra nos devuelve una tupla donde la primer componente son 
# sub-listas donde se contiene una posición y un bool que hace referencia a si la 
#palabra se encuentra en diagonal de arriba izq hacia abajo der, True si se encuentra y False si no.
#La segunda componente de la tupla es lo mismo nada más que tenemos en cuenta la palabra de abajo der hacia arriba izq.

def checkRepetidosD(tablero,pal):
    v = 0
    h = 0

    t = []
    f = []

    for lista in tablero:

        for _ in lista:
            t.append([v,h,checkRepetidosd1(tablero,pal,v,h,True)])
            f.append([v,h,checkRepetidosd1(tablero,pal,v,h,False)])
            h+=1
        h=0
        v+=1
    
    return t,f

def limpiaL(lista):
    l = []
    for x in lista:
        if x[2]:
            l.append(x)
    
    return l

#-------------------
#repitido: list str -> bool
#Dado un tablero y una palabra nos devuelve Fasle si es que esta palabra se repite más de una vez en el tablero, o True si sólo aparece 1 vez.

def repetido(tablero,pal):
    
    if len(pal)>1:                                              #Si la palabra es mayor a una sola letra.
        h1 = limpiaL(checkRepetidosV(tablero,pal)[0])
        h2 = limpiaL(checkRepetidosV(tablero,pal)[1])
        v1 = limpiaL(checkRepetidosH(tablero,pal)[0])
        v2 = limpiaL(checkRepetidosH(tablero,pal)[1])
        d1 = limpiaL(checkRepetidosD(tablero,pal)[0])
        d2 = limpiaL(checkRepetidosD(tablero,pal)[1])

        if len(h1)+len(h2)+len(v1)+len(v2)+len(d1)+len(d2) <= 1: #Si entre todas las listas sólo hay un true. 
            return True
        else:
            return False
    else:                                                       #Si la palabra es mayor a una letra, inmediatamente devuelve true porque seguro que va a haber más de 1.
        return True

#-------------------
#palabras: list -> list
#Dada una lista de sub-listas del tipo [str,int] nos devuelve una lista con la primer componente de cada sub-lista.

def palabras(lista):
    l=[]
    for x in lista:
        l.append(x[0])
    return l

#-------------------
#checkRepe: list list -> bool
#Dado el tablero y la lista de jugadas, analiza si alguna de todas las palabras aparece más de 1 vez. Si sucediera esto devuelve False,
# caso contario True.

def checkRepetidos(tablero,lista):
    pals = palabras(lista)

    for x in pals:
        if not repetido(tablero,x):
            return False
    
    return True

#-------------------
#ImprimeTablero: list -> None
#Dado un tablero nos los imprime.
def imprimeTablero(lista):

    for x in lista:
        p = ""
        for e in x:
            p = p + " "
            p = p + e
        print(p)

#-------------------
#Jugar: None -> None 
#Es la función madre del juego concatena todas las funciones anteriores.

def jugar():
    lemario = str(input("Ingrese la direccion del lemario o 0 si quiere que la misma sea la predefinida: "))
    if lemario == "0":
        lemario = "lemario.txt"

    jugada = "jugada.txt"

    palabras = checkL(lemario,jugada)[0]                                #Lista de listas de palabras con su orientación.
    tam = checkL(lemario,jugada)[1]                                     #Tamaño de la sopa de letras.

    tablero = escribeTablero(palabras,int(tam))                         #Colocamos las palabras en el tablero.
    c = tam*tam
    
    while tablero == False and c != 0:                                  #Realizamos varios intentos para colocar las palabras en el tablero.
        tablero = escribeTablero(palabras,tam)
        c-=1
    
    if tablero == False:        
        print("No es posible generar esta sopa de letras.")             #La sopa de letras no se puede hacer.

    else:
        tableroC = rellenaTablero(tablero)                              #Rellenamos los lugares vacios del tablero.

        while not checkRepetidos(tableroC,palabras):                    #Revismaos que al llenarlo no se genere por azar una palabra ya existente. 
            tableroC = rellenaTablero(tablero)
        
        imprimeTablero(tableroC)                                        #Imprimimos el tablero.

jugar()