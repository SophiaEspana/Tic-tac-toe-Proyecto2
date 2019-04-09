import random
print("Proyecto # 2 Sophia España")


print ('Como desea jugar?')
print ('Juego de dos jugadores: 1')
print ('Juego de un jugador: 2')
print ('Gana quien no hace totito: 3')

opcion = input('que opcion desea?: ') 
type(opcion)

if opcion == '1':
    jugador1 = input('ingrese nombre: ')
    type(jugador1)
    jugador2 = input('ingrese nombre: ')
    type(jugador2)

    matriz = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
    jugador = random.randint(1,2)  
    Gano = 1    
    Empate = -1    
    CorrerCd = 0    
    Juego = CorrerCd    

    #cuadros    
    def Matriz():

        matrizejemplo = [' ','A','B','C','D','E','F','G','H','I']

        print("Matriz ejemplo", " ", "Matriz de juego")
        print("                                         ")
        print( matrizejemplo[1] ,'|', matrizejemplo[2] ,'|', matrizejemplo[3], '      ', matriz[1] ,'|', matriz[2] ,'|', matriz[3])    
        print("__|___|__", '      ', "__|___|__")    
        print( matrizejemplo[4] ,'|', matrizejemplo[5] ,'|', matrizejemplo[6], '      ', matriz[4] ,'|', matriz[5] ,'|', matriz[6])   
        print("__|___|__", '      ', "__|___|__")    
        print( matrizejemplo[7] ,'|', matrizejemplo[8] ,'|', matrizejemplo[9], '      ', matriz[7] ,'|', matriz[8] ,'|', matriz[9])    
        print("  |   |  ", '      ', "  |   |  ") 


    
    #ver si la posicion esta limpia     
    def Posicion(x):    
        if(matriz[x] == ' '):    
            return True    
        else:    
            return False    
    
    #para ver si gano o no     
    def SiGano():    
        global Juego    
        #ganar de forma horizontal   
        if(matriz[1] == matriz[2] and matriz[2] == matriz[3] and matriz[1] != ' '):    
            Juego = Gano    
        elif(matriz[4] == matriz[5] and matriz[5] == matriz[6] and matriz[4] != ' '):    
            Juego = Gano    
        elif(matriz[7] == matriz[8] and matriz[8] == matriz[9] and matriz[7] != ' '):    
            Juego = Gano    
        #ganar de forma vertical    
        elif(matriz[1] == matriz[4] and matriz[4] == matriz[7] and matriz[1] != ' '):    
            Juego = Gano    
        elif(matriz[2] == matriz[5] and matriz[5] == matriz[8] and matriz[2] != ' '):    
            Juego = Gano    
        elif(matriz[3] == matriz[6] and matriz[6] == matriz[9] and matriz[3] != ' '):    
            Juego= Gano    
        #ganar de forma diagonal    
        elif(matriz[1] == matriz[5] and matriz[5] == matriz[9] and matriz[5] != ' '):    
            Juego = Gano    
        elif(matriz[3] == matriz[5] and matriz[5] == matriz[7] and matriz[5] != ' '):    
            Juego= Gano    
        #nadie gana (empate)/ que siga el juego     
        elif(matriz[1]!=' ' and matriz[2]!=' ' and matriz[3]!=' ' and matriz[3]!=' ' and matriz[5]!=' ' and matriz[6]!=' ' and matriz[7]!=' ' and matriz[8]!=' ' and matriz[9]!=' '):    
            Juego=Empate   
        else:            
            Juego=CorrerCd    
        
    
    print("Jugardor 1 [X] --- Jugador 2 [O]")      

    #turno de los jugadores  
    while(Juego == CorrerCd):        
        Matriz()    
        if(jugador == 1):    
            print("Turno Jugador 1: ", jugador1)    
            Trazo = 'X'
            jugador+=1   
        else:    
            print("Turno Jugador 2: ", jugador2)    
            Trazo = 'O'
            jugador-= 1    
         

        letra = input('Ingrese una letra mayuscula en la posicion donde quiere marcar: ')
        type(letra)

        if letra == 'A':
            numletra = 1
        elif letra == 'B':
            numletra = 2
        elif letra == 'C':
            numletra = 3
        elif letra == 'D':
            numletra = 4
        elif letra == 'E':
            numletra = 5
        elif letra == 'F':
            numletra = 6
        elif letra == 'G':
            numletra = 7
        elif letra == 'H':
            numletra = 8
        elif letra == 'I':
            numletra = 9

        if(Posicion(numletra)): 

            matriz[numletra] = Trazo    
            SiGano()    
        
    
    Matriz()    
    if(Juego==Empate):    
        print("Empate!!")    
    elif(Juego== Gano):    
        jugador-=1    
        if(jugador == 1):    
            print("Jugador 1 Gano")    
        else:    
            print("Jugador 2 Gano") 


    

if opcion == '2':


    jugador = input('ingrese nombre: ')
    type(jugador)

    def cuadrante(matriz):
        print('   |   |')
        print(' ' + matriz[1] + ' | ' + matriz[2] + ' | ' + matriz[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + matriz[4] + ' | ' + matriz[5] + ' | ' + matriz[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + matriz[7] + ' | ' + matriz[8] + ' | ' + matriz[9])
        print('   |   |')


        matrizejemplo = [' ','Q','W','E','A','S','D','Z','X','C']

        print("Matriz ejemplo", " ", "Matriz de juego")
        print("                                         ")
        print( matrizejemplo[1] ,'|', matrizejemplo[2] ,'|', matrizejemplo[3], '      ', matriz[1] ,'|', matriz[2] ,'|', matriz[3])    
        print("__|___|__", '      ', "__|___|__")    
        print( matrizejemplo[4] ,'|', matrizejemplo[5] ,'|', matrizejemplo[6], '      ', matriz[4] ,'|', matriz[5] ,'|', matriz[6])   
        print("__|___|__", '      ', "__|___|__")    
        print( matrizejemplo[7] ,'|', matrizejemplo[8] ,'|', matrizejemplo[9], '      ', matriz[7] ,'|', matriz[8] ,'|', matriz[9])    
        print("  |   |  ", '      ', "  |   |  ") 

    def LetraIngresada():
        marca = ''
        while not (marca == 'X' or marca == 'O'):
            print('Quiere jugar con X o O?')
            marca = input().upper()
        if marca == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def turno():
        if random.randint(0, 1) == 0:
            return 'compu'
        else:
            return 'jugador'

    def jugada(matriz, marca, mov):
        matriz[mov] = marca

    def SiGano(posicion, lugar):
        return ((posicion[1] == lugar and posicion[2] == lugar and posicion[3] == lugar) or 
        (posicion[4] == lugar and posicion[5] == lugar and posicion[6] == lugar) or
        (posicion[7] == lugar and posicion[8] == lugar and posicion[9] == lugar) or 
        (posicion[1] == lugar and posicion[4] == lugar and posicion[7] == lugar) or
        (posicion[2] == lugar and posicion[5] == lugar and posicion[8] == lugar) or 
        (posicion[3] == lugar and posicion[6] == lugar and posicion[9] == lugar) or 
        (posicion[3] == lugar and posicion[5] == lugar and posicion[7] == lugar) or 
        (posicion[1] == lugar and posicion[5] == lugar and posicion[9] == lugar)) 

    def copiaMatriz(matriz):
        duplicaMatriz = []

        for i in matriz:
            duplicaMatriz.append(i)

        return duplicaMatriz

    def espacioLimpio(matriz, movimiento):
        return matriz[movimiento] == ' '

    def jugadormov(matriz):
        movimiento = ' '
        while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not espacioLimpio(matriz, int(movimiento)):
            print('Ingrese las letras de la matriz en mayuscula')
            movimiento = input()
            if movimiento=='Q':
                movimiento='1'
            elif movimiento=='W':
                movimiento='2'
            elif movimiento=='E':
                movimiento='3'
            elif movimiento=='A':
                movimiento='4'
            elif movimiento=='S':
                movimiento='5'
            elif movimiento=='D':
                movimiento='6'
            elif movimiento=='Z':
                movimiento='7'
            elif movimiento=='X':
                movimiento='8'
            elif movimiento=='C':
                movimiento='9'
            else:
                 break
        return int (movimiento) 
    

    def randommovimientolista(matriz, movesList):
        posiblesjugadas = []
        for i in movesList:
            if espacioLimpio(matriz, i):
                posiblesjugadas.append(i)

        if len(posiblesjugadas) != 0:
            return random.choice(posiblesjugadas)
        else:
            return None

    def juegoCompu(matriz, opcioncompu):
        if opcioncompu == 'X':
            marcaJugador = 'O'
        else:
            marcaJugador = 'X'

        for i in range(1, 10):
            copy = copiaMatriz(matriz)
            if espacioLimpio(copy, i):
                jugada(copy, opcioncompu, i)
                if SiGano(copy, opcioncompu):
                    return i
    # ver si las orillas estan libres
        movimiento = randommovimientolista(matriz, [1, 3, 7, 9])
        if movimiento != None:
            return movimiento

    # ver si el centro esta libre
        if espacioLimpio(matriz, 5):
            return 5

    # moverse en lados 
        return randommovimientolista(matriz, [2, 4, 6, 8])

    def matrizllena(matriz):
        for i in range(1, 10):
            if espacioLimpio(matriz, i):
                return False
        return True

    while True:
    # Reset the matriz
        lamatriz = [' '] * 10
        marcaJugador, opcioncompu = LetraIngresada()
        turn = turno()
        print('The ' + turn + ' will go first.')
        correrJuego = True

        while correrJuego:
            if turn == 'jugador':
            # jugador's turn.
                cuadrante(lamatriz)
                movimiento = jugadormov(lamatriz)
                jugada(lamatriz, marcaJugador, movimiento)

                if SiGano(lamatriz, marcaJugador):
                    cuadrante(lamatriz)
                    print('Yei! ganaste el juego')
                    correrJuego = False
                else:
                    if matrizllena(lamatriz):
                        cuadrante(lamatriz)
                        print('Empate')
                        break
                    else:
                        turn = 'compu'

            else:
            # turno de computadora
                movimiento = juegoCompu(lamatriz, opcioncompu)
                jugada(lamatriz, opcioncompu, movimiento)

                if SiGano(lamatriz, opcioncompu):
                    cuadrante(lamatriz)
                    print('Gano la computadora, perdiste :(')
                    correrJuego = False
                else:
                    if matrizllena(lamatriz):
                        cuadrante(lamatriz)
                        print('Empate!')
                        break
                    else:
                        turn = 'jugador'

        break



if opcion == '3':
    jugador1 = input('ingrese nombre: ')
    type(jugador1)
    jugador2 = input('ingrese nombre: ')
    type(jugador2)

    matriz = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
    jugador = random.randint(1,2)  
    perdio = 1    
    Empate = -1    
    CorrerCd = 0    
    Juego = CorrerCd    

    #cuadros    
    def Matriz():

        matrizejemplo = [' ','A','B','C','D','E','F','G','H','I']

        print("Matriz ejemplo", " ", "Matriz de juego")
        print("                                         ")
        print( matrizejemplo[1] ,'|', matrizejemplo[2] ,'|', matrizejemplo[3], '      ', matriz[1] ,'|', matriz[2] ,'|', matriz[3])    
        print("__|___|__", '      ', "__|___|__")    
        print( matrizejemplo[4] ,'|', matrizejemplo[5] ,'|', matrizejemplo[6], '      ', matriz[4] ,'|', matriz[5] ,'|', matriz[6])   
        print("__|___|__", '      ', "__|___|__")    
        print( matrizejemplo[7] ,'|', matrizejemplo[8] ,'|', matrizejemplo[9], '      ', matriz[7] ,'|', matriz[8] ,'|', matriz[9])    
        print("  |   |  ", '      ', "  |   |  ") 


    
    #ver si la posicion esta limpia     
    def Posicion(x):    
        if(matriz[x] == ' '):    
            return True    
        else:    
            return False    
    
    #para ver si gano o no     
    def SiPerdio():    
        global Juego    
        #ganar de forma horizontal   
        if(matriz[1] == matriz[2] and matriz[2] == matriz[3] and matriz[1] != ' '):    
            Juego = perdio    
        elif(matriz[4] == matriz[5] and matriz[5] == matriz[6] and matriz[4] != ' '):    
            Juego = perdio    
        elif(matriz[7] == matriz[8] and matriz[8] == matriz[9] and matriz[7] != ' '):    
            Juego = perdio    
        #ganar de forma vertical    
        elif(matriz[1] == matriz[4] and matriz[4] == matriz[7] and matriz[1] != ' '):    
            Juego = perdio   
        elif(matriz[2] == matriz[5] and matriz[5] == matriz[8] and matriz[2] != ' '):    
            Juego = perdio    
        elif(matriz[3] == matriz[6] and matriz[6] == matriz[9] and matriz[3] != ' '):    
            Juego= perdio    
        #ganar de forma diagonal    
        elif(matriz[1] == matriz[5] and matriz[5] == matriz[9] and matriz[5] != ' '):    
            Juego = perdio    
        elif(matriz[3] == matriz[5] and matriz[5] == matriz[7] and matriz[5] != ' '):    
            Juego= perdio    
        #nadie gana (empate)/ que siga el juego     
        elif(matriz[1]!=' ' and matriz[2]!=' ' and matriz[3]!=' ' and matriz[3]!=' ' and matriz[5]!=' ' and matriz[6]!=' ' and matriz[7]!=' ' and matriz[8]!=' ' and matriz[9]!=' '):    
            Juego=Empate   
        else:            
            Juego=CorrerCd    
        
    
    print("Jugardor 1 [X] --- Jugador 2 [O]")      

    #turno de los jugadores  
    while(Juego == CorrerCd):        
        Matriz()    
        if(jugador == 1):    
            print("Turno Jugador 1: ", jugador1)    
            Trazo = 'X'
            jugador+=1   
        else:    
            print("Turno Jugador 2: ", jugador2)    
            Trazo = 'O'
            jugador-= 1    
         

        letra = input('Ingrese una letra mayuscula en la posicion donde quiere marcar: ')
        type(letra)

        if letra == 'A':
            numletra = 1
        elif letra == 'B':
            numletra = 2
        elif letra == 'C':
            numletra = 3
        elif letra == 'D':
            numletra = 4
        elif letra == 'E':
            numletra = 5
        elif letra == 'F':
            numletra = 6
        elif letra == 'G':
            numletra = 7
        elif letra == 'H':
            numletra = 8
        elif letra == 'I':
            numletra = 9

        if(Posicion(numletra)): 

            matriz[numletra] = Trazo    
            SiPerdio()    
        
    
    Matriz()    
    if(Juego==Empate):    
        print("Empate!!")    
    elif(Juego== perdio):    
        jugador-=1    
        if(jugador == 1):    
            print("Jugador 1 Perdio")    
        else:    
            print("Jugador 2 Perdio") 