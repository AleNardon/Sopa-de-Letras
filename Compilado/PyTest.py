from ProgramaEnPy import *

def testRemoveN():
    assert removeN(['maria 1\n', 'cohete 2\n', 'tela 0']) ==  ['maria 1','cohete 2','tela 0']
    assert removeN(['pablo 3\n', 'raul 5\n', 'sergio\n 2']) ==  ['pablo 3','raul 5','sergio 2']
    assert removeN(['casa 8\n', 'arbol 5\n', 'planta 4\n']) ==  ['casa 8','arbol 5','planta 4']

def testMakeL():
    assert makeL(['maria 1', 'cohete 2', 'tela 0']) ==  [['maria',1], ['cohete',2],['tela',0]]
    assert makeL(['pablo 3', 'raul 5', 'sergio 2']) ==  [['pablo',3], ['raul',5], ['sergio',2]]
    assert makeL(['casa 8', 'arbol 5', 'planta 4']) ==  [['casa' ,8 ],['arbol',5 ], ['planta',4]]

def testcreaTablero():
    assert (creaTablero(4)) == [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
    assert (creaTablero(0)) == []
    assert (creaTablero(1)) == [["-"]]

def testCheckPrimero():
    assert (checkPrimero([['maria', 4], ['cohete', 2], ['templen', 5]] ,6)) == False 
    assert (checkPrimero([['c', 4], ['b', 2], ['a', 5]] ,1)) == True 
    assert (checkPrimero([['maria', 4], ['monitor', 0], ['a', 0]] ,2)) == False 

def testgeneraLista ():
    assert (generaLista([['maria', 4], ['monitor', 0], ['a', 0]])) == (['monitor', 'a'], [], ['maria'])
    assert (generaLista([])) == ([], [], [])
    assert (generaLista([['maria', 0], ['monitor', 0], ['a', 0]])) == (['maria','monitor', 'a'], [], [])

def testlistaLetras():
    assert(listaLetras(['maria','monitor', 'a'])) == ['m', 'a', 'r', 'i', 'a', 'm', 'o', 'n', 'i', 't', 'o', 'r', 'a']
    assert(listaLetras(["a","b","cde"])) == ['a', 'b', 'c', 'd', 'e']
    assert(listaLetras([])) == []

def testvariablesLetras():
    assert(variablesLetras([['monitor', 0],['a', 0],["a",2],['moni', 4]])) == 8
    assert(variablesLetras([['m', 0],['m', 0],["m",2],['m', 4]])) == 2
    assert(variablesLetras([['hoy', 0],["ola",2],['alo', 4]])) == 5

def testcheckHorizontal():
    assert (checkHorizontal([["-","-","-"],["-","-","-"],["-","-","-"]],"hola",0,0,True)) == False
    assert (checkHorizontal([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,1,False)) == False
    assert (checkHorizontal([["l","-"],["-","a"]],"a",1,1,False)) == True

def testaggHorizontal():
    assert(aggHorizontal([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,1,True)) ==[["-","s","o","l"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]]
    assert(aggHorizontal([["l","-"],["-","a"]],"a",1,1,False)) == [["l","-"],["-","a"]]
    assert(aggHorizontal([["-","-","-"],["-","-","-"],["-","-","-"]],"ola",2,2,False)) == [["-","-","-"],["-","-","-"],["a","l","o"]] 

def testcheckVertical():
    assert (checkVertical([["-","-","-"],["-","-","-"],["-","-","-"]],"hola",0,0,True)) == False
    assert (checkVertical([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,1,False)) == False
    assert (checkVertical([["l","-"],["-","a"]],"a",1,1,False)) == True

def testaggVertical():
    assert(aggVertical([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,1,True)) ==[["-","s","-","-"],["-","o","-","-"],["-","l","-","-"],["-","r","-","-"]]
    assert(aggVertical([["l","-"],["-","a"]],"a",1,1,False)) == [["l","-"],["-","a"]]
    assert(aggVertical([["-","-","-"],["-","-","-"],["-","-","-"]],"ola",2,2,False)) == [["-","-","a"],["-","-","l"],["-","-","o"]] 

def testcheckDiagonal():
    assert (checkDiagonal([["-","-","-"],["-","-","-"],["-","-","-"]],"hola",0,0,True)) == False
    assert (checkDiagonal([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,1,False)) == False
    assert (checkDiagonal([["l","-"],["-","a"]],"a",1,1,False)) == True

def testaggDiagonal():
    assert(aggDiagonal([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,1,True)) ==[["-","s","-","-"],["-","m","o","-"],["-","a","-","l"],["-","r","-","-"]]
    assert(aggDiagonal([["l","-"],["-","a"]],"a",1,1,False)) == [["l","-"],["-","a"]]
    assert(aggDiagonal([["-","-","-"],["-","-","-"],["-","-","-"]],"ola",2,2,False)) == [["a","-","-"],["-","l","-"],["-","-","o"]] 

def testcheckRepetidosh1():
    assert (checkRepetidosh1([["-","-","-"],["-","-","-"],["-","-","-"]],"hola",0,0,True)) == False
    assert (checkRepetidosh1([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,3,False)) == False
    assert (checkRepetidosh1([["l","-"],["-","a"]],"a",1,1,False)) == True

def testcheckRepetidosH():
    assert(checkRepetidosH([["l","-"],["-","a"]],"a")) ==([[0, 0, False], [0, 1, False], [1, 0, False], [1, 1, True]], [[0, 0, False], [0, 1, False], [1, 0, False], [1, 1, True]])
    assert(checkRepetidosH([["l"],["z"]],"a")) == ([[0, 0, False], [1, 0, False]], [[0, 0, False], [1, 0, False]])

def testcheckRepetidosv1():
    assert (checkRepetidosv1([["-","-","-"],["-","-","-"],["-","-","-"]],"hola",0,0,True)) == False
    assert (checkRepetidosv1([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,1,False)) == False
    assert (checkRepetidosv1([["l","-"],["-","a"]],"a",1,1,False)) == True

def testcheckRepetidosV():
    assert(checkRepetidosV([["l","-"],["-","a"]],"a")) ==([[0, 0, False], [0, 1, False], [1, 0, False], [1, 1, True]], [[0, 0, False], [0, 1, False], [1, 0, False], [1, 1, True]])
    assert(checkRepetidosV([["l"],["z"]],"a")) == ([[0, 0, False], [1, 0, False]], [[0, 0, False], [1, 0, False]])

def testcheckRepetidosd1():
    assert (checkRepetidosd1([["-","-","-"],["-","-","-"],["-","-","-"]],"hola",0,0,True)) == False
    assert (checkRepetidosd1([["-","-","-","-"],["-","m","-","-"],["-","a","-","-"],["-","r","-","-"]],"sol",0,1,False)) == False
    assert (checkRepetidosd1([["l","-"],["-","a"]],"a",1,1,False)) == True

def testcheckRepetidosD():
    assert(checkRepetidosD([["l","-"],["-","a"]],"al")) ==([[0, 0, False], [0, 1, False], [1, 0, False], [1, 1, False]], [[0, 0, False], [0, 1, False], [1, 0, False], [1, 1, True]])
    assert(checkRepetidosD([["l"],["z"]],"a")) == ([[0, 0, False], [1, 0, False]], [[0, 0, False], [1, 0, False]])

def testPalabras():
    assert(palabras([["hola",2],["ola",1],["sol",3]])) == ["hola","ola","sol"]
    assert(palabras([["papa",2],["ale",1],["rata",3]])) == ["papa","ale","rata"]
    assert(palabras([["mama",2],["ole",1],["perro",3]])) == ["mama","ole","perro"]

def pytest():
    testRemoveN()
    testMakeL()
    testcreaTablero()
    testcreaTablero()
    testCheckPrimero()
    testgeneraLista ()
    testlistaLetras()
    testvariablesLetras()
    testcheckHorizontal()
    testaggHorizontal()
    testcheckVertical()
    testaggVertical()
    testcheckDiagonal()
    testaggDiagonal()
    testcheckRepetidosh1()
    testcheckRepetidosH()  
    testcheckRepetidosv1()
    testcheckRepetidosV()
    testcheckRepetidosd1()
    testcheckRepetidosD()
    testPalabras()
pytest()
