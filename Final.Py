from random import randint

#removeN:list -> list
#Dada una lista si esta tiene en sus str un salto de paguina es decir "\n"
#lo quita y nos devuelve otra lista de str sin \n

def removeN(lista):
    newlist = []
    for x in lista:
        w = x.replace("\n","")
        newlist.append(w)
    return newlist

#----------------------
#makeL:list->list
#Dada una lista crea una nueva lista con la palabra y como segunda componente el digito  

def makeL(lista):
    newlist = []
    for x in lista:
        s = len(x)
        newlist.append([x.replace(" " + x[s-1],"") , int (x[s-1])])
    return newlist

#-------------------
#extraerTexto: str -> list
#Dado un archivo del tipo de salida de la sopa de letras nos realizara una lista de listas donde contendra
#la palabra seguida de la posicion que tendra

def extraerJug(ruta):
    archivo = open(ruta,"r")                #Abrimos el archivo de las jugadas

    listarchivo = archivo.readlines()       #Extraemos todas las lineas y van a una lista
    listarchivo = removeN(listarchivo)      #Removemos los \n de los elementos de la lista 
    tam = int(listarchivo[1])               #extraemos el tamaño de la sopa
    
    listarchivo.pop(0)                      
    listarchivo.pop(0)                      #eliminamos las tres primeras componentes de la lista para que queden solo laas palabras con el numero
    listarchivo.pop(0)
    
    archivo.close()                         #Cerramos el archivo
    
    listarchivo = makeL(listarchivo)        #Organizamos a travez de una sublista las palabras con su orientacion [str,int]

    return listarchivo, tam                 #devolvemos una lista del tipo [[str, int],[str, int]...] y el tamaño de la sopa

#-------------------
#ExtraeLem: str or None -> list
#Dada una ruta o la predefinida lemario.txt nos devuelve el contenido del txt en una lista

def extraeLem(ruta = "lemario.txt"):
    lem = open(ruta,"r")
    listalem = lem.readlines()
    listalem = removeN(listalem)
    lem.close()
    return listalem

#-------------------
#palabraNew: str int str - > str
#Dada la ruta del lemario el tamaño de la sopa y la palabra, si es que la cantidad de caracteres de esa 
# palabra es mayor al tamaño de la sopa, y/o si la palabra no se encuentra en el lemario, la sustituye por una palabra del 
# lemario con una cantidad de caracteres menor o igual que el tamaño de la sopa. Sino mantenemos la palabra inicial

def palabraNew(lemario,tam,palabra):
    pal = palabra                                         

    if not pal in lemario or len(pal) > tam :               #Si la palabra no esta en el lemario o es mayor al tamaño
        
        pal = lemario[randint(0,len(lemario))]              #Eligue otra palabra al azar del lemario
        
        while not len(pal) <= tam :                         #Si su tamaño no sigue siendo el adecuado
            pal = lemario[randint(0,len(lemario))]          #Eligue otra palabra al azar del lemario
    
    return pal                                              #Devuelve la palabra 

#-------------------
#checkL: str str -> list 
#Dada la ruta del lemario y la ruta de la jugada nos devuelve una lista con las palabras checkeadas, es decir 
#si alguna de las palabras inicialmente son mayores al tamaño de la sopa de letras o no se encuentra en el lemario se remplazara

def checkL (rutalem,rutajug):
    jugadas = extraerJug(rutajug)[0]            #Extrae la lista de palabras jugadas
    tam = extraerJug(rutajug)[1]                #Extrae el tamaño de la sopa de letras 
    lemario = extraeLem(rutalem)                #Extrae una lista con las palabras del lemario

    l = []
    for x in jugadas:
        pal = x[0]                              #Toma la primer componente de la sublista [str,int]
        o = x[1]                                #Toma la segunda componente de la sublista [str,int]
        newpal = palabraNew(lemario,tam,pal)    #Escoge una palabra nueva de ser necesario
        l.append([newpal,o])                    #Agrega la jugada a una nueva lista
    
    return l,tam         

#-------------------
#Nuestro programa generara una lista de listas las cuales hacen referencia a cada fila de la sopa de letras es decir 
#el primer elemento de nuestra lista sera la primer fila el segundo la segunda y asi sucesivamente
#-------------------

#CreaTablero: int -> list
# Dado un numero n nos devuelve una lista de listas donde tendra n-veces "-" como elemento y n sublistas 

def creaTablero(numero):
    t = []
    for _ in range(numero):
        t.append(["-"]*numero)        
    return t

#-------------------
#checkPrimero: list int -> bool
#Es el primer chequeo que haremos sobre si se puede crear o no la sopa
#Dada una lista de listas(lista de la sopa) y un numero (tamaño) nos devuelve False si alguna palabra excede 
#en caracteres el tamaño de la sopa

def checkPrimero(lista ,tam):
    e = True
    for x in lista:
        if len(x[0])>tam:
            e = False
            break 
    return e

#-------------------
#genereaLista: list -> tuple 
#Dada una lista de sopa nos devuelve una tupla de tre elementos el primero seran las palabras en horizontal 
#la segunda componente estaran las palabras que estan en vertical y la ultima componente sera de las palabras en diagonal

def generaLista(lista):
    h = []                  #horizonltales con el numero 0 y 1
    v = []                  #verticales con el numero 2 y 3
    d = []                  #diagonales con el numero 4 y 5

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
# Dada una lista de palabras nos devolvera una nueva lista donde cada elemento seran las letras de las palabras 
def listaLetras(lista):
    li = []
    for x in lista:
        for l in x:
            li.append(l)
    
    return li

#-------------------
#variablesLetras: lista -> int 
# Dada una lista de sopa nos devolvera un numero el cual sera una suma de la cantidad de caracteres que hay por horientacion es decir [0,1][2,3][4,5], de los cuales no se sumaran 
# caracteres que esten en otro grupo, por ejemplo tenemos la palabra "hoy"en un grupo y en el otro "ola" el caracter "o" no se sumara dos veces sino una. 
# Lo usaremos mas tarde para ver si la suma total de caracteres sera mayor ao menor a la dimencion de la sopa[["hoy",0],["ola",3],[]] == 5 

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
#Dada una lista con las jugadas anteriormente jugadas y el tamaño, nos devuelve una posicion aleatoria de la sopa 
#que no se haya jugado anteriormente

def elcPos(lista,tam):
    posv = randint(0,tam-1) 
    posh = randint(0,tam-1)
        
    while [posv,posh] in lista: 
        posv = randint(0,tam-1) 
        posh = randint(0,tam-1)

    return posv, posh 

#-------------------
#NOTA: a continuacion tendremos 9 funciones las cuales actuan de manera similar lo unico que cambia es su forma de realizar las cosas debido a cada 
#orientacion de las palabras, dentro de cada funcion tendremos la orientacio la cual se indicara con un bool, si este es True la palabra
#tendra una orientacion normal es decir de der a izq y arriba hacia abajo y con False daremos las orientraciones inversas es decir de izq a der de abajo hacia arriba
#-------------------

#CheckHorizontal:list str int int bool -> bool
#Dada la lista del tablero, una palabra , una posicion vertical del tablero, 
# una posicion horizontal del tablero y la orientacion de la palabra representada con True o False.
#Nos devolvera True si es que la palabra entra desde esa posicion y tambien si hay "-" o letras que coincidan con la palabra en caso contrario nos devuelve false.

def checkHorizontal(tablero,palabra,posv,posh,orientacion):
    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                          #Intenta hacer esto si da error es por que se va del index de la lista
            if tablero[v][h] == letra or tablero[v][h] == "-":           #Si la letra que estaba en el tablero coincide con la de la palabra o hay una casilla vacia es decir "-"
                
                if v>=0 and h>=0:                                     #Se hace esto ya que al restar puede pasar en negativo y que no de error pero no sea posible la diagonal
                    if orientacion:         	                      #Se mueve en horizontal sumando 1 en horizontal si la orientacion es True
                        h += 1
                    else:
                        h-=1                                          #Se mueve en horizontal restando 1 en horizontal si la orientacion es False
                
                else:                                                 #Caso que la posicion sea negativa es por que se salio del rango por lo tanto no entra 
                    e = False               
                    break    

            else:
                e = False                                            #No es valida la palabra en esa posicion
                break

        except IndexError:                                           #Si hay un error de que se fue el index de la lista del tablero entonces la palabra no es valida
            e = False
            break

    return e                                                         #Devuelve el estado 

#------
#aggHorizontal: list str int int bool -> list 
# Dada la lista del tablero, una palabra, dos posiciones en el tablero y la orientacion, agrega la palabra de forma horizontal segun la orientacion colocada 

#No se tienen en cuenta errores como si esta por fuera del index debido a que en la funcion madre de horizontal lo tendra en cuenta 
# esta funcion solo agrega la palabra al tablero

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
#Dada una lista del tablero, una palabra, el tamaño del tablero y la orientacion, agregaremos la palabra en una posicion inicial random y nos devolvera un nuevo tablero con la palabra agregada
#en un lugar que sea valido. En caso de no encontrar un lugar nos devolvera u bool-> False indicando que esa palabra no se puede poner en ningun lugar

def horizontal(tablero,palabra,tam,orientacion):
    jugadas = []                                                       #Creamos una lista con las posiciones jugadas en esta funcion por el momento ninguna
                            
    pos = elcPos(jugadas,tam)                                          #Generamos una posicion inicial aleatoria la cual no se a jugado en la funcion
    posv = pos[0]                                                      #Posicion vertical de la letra inicial 
    posh = pos[1]                                                      #Posicion horizontal de la letra inicial           
    jugadas.append([posv,posh])                                        #Agregamos la jugada a las posiciones jugadas en la funcion 
                        
    intentos = tam*tam                                                 #la cantidad de posibilidades de una posicion inicial no sera mayor a la cantidad de casillas
    
    while  not checkHorizontal(tablero,palabra,posv,posh,orientacion): #Si la palabra no es valida a partir de la pos inicial
        intentos-=1
        
        if intentos  == 0:                                             #Si ya no hay mas casillas por probar
            break 
       
        else:
            pos = elcPos(jugadas,tam)                                  #Repite los paso anteriormente echo                                             
            posv = pos[0]
            posh = pos[1]
            jugadas.append([posv,posh])

    if intentos == 0:                                                  #Si ya no hay mas casillas por probar
        return False

    else:
        table = aggHorizontal(tablero,palabra,posv,posh,orientacion) #Creamos el nuevo tablero
        return table

#-------------------
#CheckVertical:list str int int bool -> bool
#Dada la lista del tablero, una palabra , una posicion vertical del tablero, 
# una posicion horizontal del tablero y la orientacion de la palabra representada con True o False.
#Nos devolvera True si es que la palabra entra desde esa posicion y tambien si hay "-" o letras que coincidan con la palabra en caso contrario nos devuelve false.

def checkVertical(tablero,palabra,posv,posh,orientacion):

    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                       #Intenta hacer esto si da error es por que se va del index de la lista
            if tablero[v][h] == letra or tablero[v][h] == "-":     #Si la letra que estaba en el tablero coincide con la de la palabra o hay una casilla vacia es decir "-"
                
                if v>=0 and h>=0:                                  #Se hace esto ya que al restar puede pasar en negativo y que no de error pero no sea posible la diagonal
                    if orientacion:                                #Se mueve en vertical sumando 1 si la orientacion es True
                        v += 1
                    else:
                        v -=1                                      #Se mueve en vertical restando 1 si la orientacion es False
                
                else:                                              #Caso que la posicion sea negativa es por que se salio del rango por lo tanto no entra 
                    e = False           
                    break    

            else:
                e = False                                          #No es valida la palabra en esa posicion
                break

        except IndexError:                                         #Si hay un error de que se fue el index de la lista del tablero entonces la palabra no es valida
            e = False
            break

    return e                                                       #Devuelve el estado 

#------
#aggVertical: list str int int bool -> list 
# Dada la lista del tablero, una palabra, dos posiciones en el tablero y la orientacion, agrega la palabra de forma vertical segun la orientacion colocada 

#No se tienen en cuenta errores como si esta por fuera del index debido a que en la funcion madre de vertical lo tendra en cuenta 
# esta funcion solo agrega la palabra al tablero

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
#Dada una lista del tablero, una palabra, el tamaño del tablero y la orientacion, agregaremos la palabra en una posicion inicial random y nos devolvera un nuevo tablero con la palabra agregada
#en un lugar que sea valido. En caso de no encontrar un lugar nos devolvera u bool-> False indicando que esa palabra no se puede poner en ningun lugar

def vertical(tablero,palabra,tam,orientacion):
    jugadas = []                                                       #Creamos una lista con las posiciones jugadas en esta funcion por el momento ninguna
                            
    pos = elcPos(jugadas,tam)                                          #Generamos una posicion inicial aleatoria la cual no se a jugado en la funcion
    posv = pos[0]                                                      #Posicion vertical de la letra inicial 
    posh = pos[1]                                                      #Posicion horizontal de la letra inicial           
                        
    jugadas.append([posv,posh])                                        #Agregamos la jugada a las posiciones jugadas en la funcion 
                        
    intentos = tam*tam                                                 #la cantidad de posibilidades de una posicion inicial no sera mayor a la cantidad de casillas
    
    while  not checkVertical(tablero,palabra,posv,posh,orientacion):   #Si la palabra no es valida a partir de la pos inicial
        intentos-=1
        
        if intentos  == 0:                                             #Si ya no hay mas casillas por probar
            break 
        else:
            pos = elcPos(jugadas,tam)                                  #Repite los paso anteriormente echo                                                           
            posv = pos[0]
            posh = pos[1]
            jugadas.append([posv,posh])

    if intentos == 0:                                                 #Si ya no hay mas casillas por probar
        return False

    else:
        table = aggVertical(tablero,palabra,posv,posh,orientacion)    #Creamos el nuevo tablero
        return table

#-------------------
#checkDiagonal : list str int int bool -> bool
#Dada la lista del tablero, una palabra , una posicion vertical del tablero , una posicion horizontal del tablero y la orientacion de la palabra 
#representada con True(de arrriba hacia abajo) o False (de abajo hacia arriba)
#Nos devolvera True si es que la palabra entra desde esa posicion y tambien si hay "-" o letras que coincidan con la palabra
# en caso contrario nos devuelve false

def checkDiagonal(tablero,palabra,posv,posh,orientacion):
    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                    #Intenta hacer esto si da error es por que se va del index de la lista
            if tablero[v][h] == letra or tablero[v][h] == "-":     #Si la letra que estaba en el tablero coincide con la de la palabra o hay una casilla vacia es decir "-"

                if v>=0 and h>=0:                               #Se hace esto ya que al restar puede pasar en negativo y que no de error pero no sea posible la diagonal
                    if orientacion:                             #Se mueve en diagonal sumando 1 en vertical y horizontal si la orientacion es True
                        v +=1                                           
                        h +=1
                    else:                                       #Se mueve en diagonal restando 1 en vertical y horizontal si la orientacion es False
                        v -=1              
                        h +=1
                
                else:                                           #Caso que la posicion sea negativa es por que se salio del rango por lo tanto no entra 
                    e = False           
                    break    
   
            else:
                e = False                                       #No es valida la palabra en esa posicion
                break

        except IndexError:                                      #Si hay un error de que se fue el index de la lista del tablero entonces la palabra no es valida
            e = False
            break

    return e                                                    #Devuelve el estado 

#------
#aggDiagonal: list str int int bool -> list 
# Dada la lista del tablero, una palabra, dos posiciones en el tablero y la orientacion, agrega la palabra de forma diagonal segun la orientacion colocada 

#No se tienen en cuenta errores como si esta por fuera del index debido a que en la funcion madre de diagonal  lo tendra en cuenta 
# esta funcion solo agrega la palabra al tablero

def aggDiagonal(tablero,palabra,posv,posh,orientacion):

    v = posv
    h = posh

    for letra in palabra:
        tablero[v][h] = letra
        if orientacion:                                   #Se mueve en diagonal sumando 1 en vertical y horizontal si la orientacion es True
            v +=1                                           
            h +=1
        else:                                             #Se mueve en diagonal restando 1 en vertical y horizontal si la orientacion es False
            v -=1              
            h +=1
  
    return tablero

#------
#diagonal: list str int bool -> list or bool
#Dada una lista del tablero, una palabra, el tamaño del tablero y la orientacion, agregaremos la palabra en una posicion inicial random y nos devolvera un nuevo tablero con la palabra agregada
#en un lugar que sea valido. En caso de no encontrar un lugar nos devolvera u bool-> False indicando que esa palabra no se puede poner en ningun lugar

def diagonal(tablero,palabra,tam,orientacion):
    jugadas = []                                    #Creamos una lista con las posiciones jugadas en esta funcion por el momento ninguna
    
    pos = elcPos(jugadas,tam)                       #Generamos una posicion inicial aleatoria la cual no se a jugado en la funcion
    posv = pos[0]                                   #Posicion vertical de la letra inicial 
    posh = pos[1]                                   #Posicion horizontal de la letra inicial

    jugadas.append([posv,posh])                     #Agregamos la jugada a las posiciones jugadas en la funcion 

    intentos = tam*tam                              #la cantidad de posibilidades de una posicion inicial no sera mayor a la cantidad de casillas
    
    while not checkDiagonal(tablero,palabra,posv,posh,orientacion): #Si la palabra no es valida a partir de la pos inicial
        intentos-=1

        if intentos == 0:                           #Si ya no hay mas casillas por probar
            break 
        
        else:
            pos = elcPos(jugadas,tam)               #Repite los paso anteriormente echo                                              
            posv = pos[0]
            posh = pos[1]
            jugadas.append([posv,posh])

    if intentos == 0:                               #Si la cantidad de intentos se agoto es por que la sopa de letras no es posible generar 
        return False

    else:
        table = aggDiagonal(tablero,palabra,posv,posh,orientacion) #Creamos el nuevo tablero
        return table

#-------------------
#aggPalabras: list str int  -> list or bool
#Dado una lista del tablero, una palabra y la orientacion del 0-5 nos devuelve una lista con la palabra agregada 
# o un bool indicando que esa palabra no fue posible agregarla

def aggPalabras(tablero,palabra,orientacion):
    if   orientacion == 0:                                          #Horizontal de izquierda a derecha
        return horizontal(tablero,palabra,len(tablero),True)
    elif orientacion == 1:                                          #Horizontal de derecha a izquierda  
        return horizontal(tablero,palabra,len(tablero),False)
    
    elif orientacion == 2:                                          #Vertical de arriba hacia abajo
        return vertical(tablero,palabra,len(tablero),True)
    elif orientacion == 3:                                          #Vertical de abajo hacia arriba
        return vertical(tablero,palabra,len(tablero),False)

    elif orientacion == 4:                                          #Diagonal de arriba hacia abajo
        return diagonal(tablero,palabra,len(tablero),True)
    elif orientacion == 5:                                          #Diagonal de abajo hacia arriba
        return diagonal(tablero,palabra,len(tablero),False)


#-------------------
#escribeTablero: list int  -> list or bool
#Dada una lista de palabras con su orientacion y el tamaño del tablero, nos devuelve una lista del tablero con las palabras en el tablero 
#o nos devuelve Un bool indicando que no es posible realizar la sopa

def escribeTablero(lista,tam):
    tablero = creaTablero(tam)                                      #Creamos un tablero
    
    
    if checkPrimero(lista,tam):                                     #Realizamos el primer checkeo si es que alguna palabra es mayor al tamaño ya no se puede hacer
        
        if variablesLetras(lista)>=tam:                             #Realizamos el segundo chequeo anteriormente explicado
            
            for x in lista:                         
                tablero = aggPalabras(tablero,x[0],x[1])            #Agregamos cada palabra al tablero
                if tablero == False:                                #Si dio false nose puede hacer
                    return False

            return tablero                              
        else:
            return False

    else:
        return False 

#-------------------
# abc: None -> str 
#Nos devuelve una letra al azar del abecedario
def abc():
    abce = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    n = randint(0,len(abce)-1)

    return abce[n]

#-------------------
#rellenaTablero: List -> list
#Dada una lista con las palabras dentro del tablero rellenaremos los espacios en blanco "-" por una letra al azar del abecedario
#y devuelve una nueva lista con los espacios en blanco completos

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
# NOTA: Las siguientes funciones seran muy similares a las anteriores con la diferencia que no detecta si hay "-" solo si esta la palabra
#-------------------

#checkRepetidosh1: list str int int bool -> bool
#Dada la lista del tablero, una palabra , una posicion vertical del tablero, 
# una posicion horizontal del tablero y la orientacion de la palabra representada con True o False.
#Nos devolvera True si las letras del tablero coinciden con las letras de la palabra con una orientacion horizontal en caso contrario nos devuelve false.

def checkRepetidosh1(tablero,palabra,posv,posh,orientacion):
    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                          #Intenta hacer esto si da error es por que se va del index de la lista
            if tablero[v][h] == letra :                               #Si la letra que estaba en el tablero coincide con la de la palabra 
                
                if v>=0 and h>=0:                                     #Se hace esto ya que al restar puede pasar en negativo y que no de error pero no sea posible la diagonal
                    if orientacion:         	                      #Se mueve en horizontal sumando 1 en horizontal si la orientacion es True
                        h += 1
                    else:
                        h-=1                                          #Se mueve en horizontal restando 1 en horizontal si la orientacion es False
                
                else:                                                 #Caso que la posicion sea negativa es por que se salio del rango por lo tanto no entra 
                    e = False               
                    break    

            else:
                e = False                                            #No es valida la palabra en esa posicion
                break

        except IndexError:                                           #Si hay un error de que se fue el index de la lista del tablero entonces la palabra no es valida
            e = False
            break

    return e                                                         #Devuelve el estado     

#-------------------
#checkRepetidosH: list str -> tuple
#Dado un tablero y una palabra nos devuelve una tupla donde lka primer componente son sublistas donde se contiene una posicicon y un bool que hace referencia a si la 
#palabra se encuentra en horizontal de izq a der, True si se encuentra y False si no. La segunda componente de la tupla es los mismo nada mas que tenemos en cuenta la palabra de der a izq

def checkRepetidosH(tablero,pal):
    v = 0
    h = 0
    t = []
    f = []

    for lista in tablero:
        for _ in lista:                                                     #No intera con los elementos de la lista pero s los recorre
            t.append([v,h,checkRepetidosh1(tablero,pal,v,h,True)])          #Agrega a una lista si en esa posicion esta la palabra en horizontal de izq a der
            f.append([v,h,checkRepetidosh1(tablero,pal,v,h,False)])         #Agrega a una lista si en esa posicion esta la palabra en horizontal de der a izq 
            h+=1
        h=0
        v+=1
    
    return t,f

#-------------------
#checkRepetidosv1: list str int int bool -> bool
#Dada la lista del tablero, una palabra , una posicion vertical del tablero, 
# una posicion horizontal del tablero y la orientacion de la palabra representada con True o False.
#Nos devolvera True si las letras del tablero coinciden con las letras de la palabra con una orientacion vertical en caso contrario nos devuelve false.

def checkRepetidosv1(tablero,palabra,posv,posh,orientacion):

    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                       #Intenta hacer esto si da error es por que se va del index de la lista
            if tablero[v][h] == letra:                             #Si la letra que estaba en el tablero coincide con la de la palabra 
                
                if v>=0 and h>=0:                                  #Se hace esto ya que al restar puede pasar en negativo y que no de error pero no sea posible la diagonal
                    if orientacion:                                #Se mueve en vertical sumando 1 si la orientacion es True
                        v += 1
                    else:
                        v -=1                                      #Se mueve en vertical restando 1 si la orientacion es False
                
                else:                                              #Caso que la posicion sea negativa es por que se salio del rango por lo tanto no entra 
                    e = False           
                    break    

            else:
                e = False                                          #No es valida la palabra en esa posicion
                break

        except IndexError:                                         #Si hay un error de que se fue el index de la lista del tablero entonces la palabra no es valida
            e = False
            break

    return e                                                       #Devuelve el estado 

#-------------------
#checkRepetidosV: list str -> tuple
#Dado un tablero y una palabra nos devuelve una tupla donde la primer componente son sublistas donde se contiene una posicicon y un bool que hace referencia a si la 
#palabra se encuentra en vertical de arriba hacia abajo, True si se encuentra y False si no. La segunda componente de la tupla es los mismo nada mas que tenemos en cuenta la palabra de abajo hacia arriba

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
#Dada la lista del tablero, una palabra , una posicion vertical del tablero, 
# una posicion horizontal del tablero y la orientacion de la palabra representada con True o False.
#Nos devolvera True si las letras del tablero coinciden con las letras de la palabra con una orientacion diagonal en caso contrario nos devuelve false.

def checkRepetidosd1(tablero,palabra,posv,posh,orientacion):
    e = True
    v = posv
    h = posh
    
    for letra in palabra:
        try:                                                    #Intenta hacer esto si da error es por que se va del index de la lista
            if tablero[v][h] == letra:                          #Si la letra que estaba en el tablero coincide con la de la palabra

                if v>=0 and h>=0:                               #Se hace esto ya que al restar puede pasar en negativo y que no de error pero no sea posible la diagonal
                    if orientacion:                             #Se mueve en diagonal sumando 1 en vertical y horizontal si la orientacion es True
                        v +=1                                           
                        h +=1
                    else:                                       #Se mueve en diagonal restando 1 en vertical y horizontal si la orientacion es False
                        v -=1              
                        h +=1
                
                else:                                           #Caso que la posicion sea negativa es por que se salio del rango por lo tanto no entra 
                    e = False           
                    break    
                   
            else:
                e = False                                       #No es valida la palabra en esa posicion
                break

        except IndexError:                                      #Si hay un error de que se fue el index de la lista del tablero entonces la palabra no es valida
            e = False
            break

    return e                                                    #Devuelve el estado 

#-------------------
#checkRepetidosD: list str -> tuple
#Dado un tablero y una palabra nos devuelve una tupla donde la primer componente son sublistas donde se contiene una posicicon y un bool que hace referencia a si la 
#palabra se encuentra en vertical de arriba hacia abajo, True si se encuentra y False si no. La segunda componente de la tupla es los mismo nada mas que tenemos en cuenta la palabra de abajo hacia arriba

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
#Dado un tablero y una palabra nos devuelve Fasle si es que esta palabra se repite mas de una vez en el tablero, o True si solo aparece 1 vez

def repetido(tablero,pal):
    
    if len(pal)>1:                                              #si la palabra es mayor a una sola letra
        h1 = limpiaL(checkRepetidosV(tablero,pal)[0])
        h2 = limpiaL(checkRepetidosV(tablero,pal)[1])
        v1 = limpiaL(checkRepetidosH(tablero,pal)[0])
        v2 = limpiaL(checkRepetidosH(tablero,pal)[1])
        d1 = limpiaL(checkRepetidosD(tablero,pal)[0])
        d2 = limpiaL(checkRepetidosD(tablero,pal)[1])

        if len(h1)+len(h2)+len(v1)+len(v2)+len(d1)+len(d2) <= 1: #si entre todas las listas solo hay un true 
            return True
        else:
            return False
    else:                                                       #si la palabra es mayor a una letra inmediato devuelve true por que seguro que va a haber mas de 1
        return True

#-------------------
#palabras: list -> list
#Dada una lista de sub listas del tipo [str,int] nos devuelve una lista con la primer componente de cada sublista

def palabras(lista):
    l=[]
    for x in lista:
        l.append(x[0])
    return l

#-------------------
#checkRepe: list list -> bool
#Dado el tablero y la lista de jugadas, analiza si alguna de todas de todas las palabras aparece mas de 1 vez, si sucedira esto devuelve False
# caso contario True 

def checkRepetidos(tablero,lista):
    pals = palabras(lista)

    for x in pals:
        if not repetido(tablero,x):
            return False
    
    return True

#-------------------
#ImprimeTablero: list -> None
#Dado un tablero nos los imprime 
def imprimeTablero(lista):

    for x in lista:
        p = ""
        for e in x:
            p = p + " "
            p = p + e
        print(p)

#-------------------
#Jugar: None -> None 
#Es la funcion madre del juego concatena todas las funciones anteriores

def jugar():
    lemario = str(input("Ingrese la direccion del lemario o 0 si quiere que la misma sea la predefinida: "))
    if lemario == "0":
        lemario = "lemario.txt"

    jugada = "type.txt"

    palabras = checkL(lemario,jugada)[0]                                #Lista de listas de palabras con su orientacion
    tam = checkL(lemario,jugada)[1]                                     #tamaño de la sopa de letras

    tablero = escribeTablero(palabras,int(tam))                         #Colocamos las palabras en el tablero
    c = tam*tam
    
    while tablero == False and c != 0:                                  #ealizamos varios intentos para colocar las palabras en el tablero
        tablero = escribeTablero(palabras,tam)
        c-=1
    
    if tablero == False:        
        print("No es posible generar esta sopa de letras.")             #La sopa de letras no se puede hacer

    else:
        tableroC = rellenaTablero(tablero)                              #rellenamos los lugares vacios del tablero 

        while not checkRepetidos(tableroC,palabras):                    #Revismaos que al llebnarlo no se genere por azar una palabra ya existente 
            tableroC = rellenaTablero(tablero)
        
        imprimeTablero(tableroC)                                        #Imprimimos el tablero

jugar()