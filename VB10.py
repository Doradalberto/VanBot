import teste11 as t
import matplotlib.pyplot as plt
import numpy as np
import socket
import math

def Comunicacao(estilo, Arquivo, Freq_max, res, tamanho, Request):

    (Y, X, Z) = t.Estilo(estilo, Arquivo, Freq_max, res, tamanho)

    FrameX = [min(Y), min(Y), max(Y), max(Y),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    FrameY = [min(X), max(X), max(X), min(X),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    FrameZ = np.ones(len(FrameX))/200


    numberOfLists = math.ceil(len(X)/30) # + 1
    print('Numero de pontos totais:', len(X))
    print('Numero de Listas:', numberOfLists)


    Listas = np.arange(numberOfLists)

    objX = [[] for i in range(numberOfLists)]
    objY = [[] for i in range(numberOfLists)]
    objZ = [[] for i in range(numberOfLists)]


    for i in Listas:
        objX[i].append(X[30*i:30*i + 30])
        objY[i].append(Y[30*i:30*i + 30])
        objZ[i].append(Z[30*i:30*i + 30])
        
        if len(objX[i][0]) < 29:
            Nzeros = 30 - len(objX[i][0])
            ZerosX = np.zeros(Nzeros)
            ZerosY = np.zeros(Nzeros) - 0.07
            ZerosZ = np.ones(Nzeros)/10

            objX[i][0] = [*objX[i][0],*ZerosX]
            objY[i][0] = [*objY[i][0],*ZerosY]
            objZ[i][0] = [*objZ[i][0],*ZerosZ]


    if Request == 0: #RODAR

        for f in Listas:
        
            Size = len(objX[f][0])
            # print('')
            # print('Tamanho da lista {0}: {1}'.format(f, Size))

            Tamanho = str([len(objX[f][0])])     

            # # create an INET, STREAMing socket
            # serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # # bind the socket to a public host, and a well-known port
            # serversocket.bind(('0.0.0.0', 30002))
            # # become a server socket
            # serversocket.listen(5)
            # # accept connections from outside
            # (conn, address) = serversocket.accept()
            

            # conn.send(Tamanho.encode())  # send data to the client
            # conn.send(str(tuple(objX[f][0])).encode())  # send data to the client
            # conn.send(str(tuple(objY[f][0])).encode())  # send data to the client
            # conn.send(str(tuple(objZ[f][0])).encode())  # send data to the client

            # conn.close()

            
    elif Request == 1: #FRAME
        
        Xround = [round (k,3) for k in FrameX]
        Yround = [round (k,3) for k in FrameY]
        Zround = [FrameZ]

        print('')
        print('X:', Xround)
        print('Y:', Yround)
        print('Z:', FrameZ)

        Tamanho = str([len(Xround)])

        # # create an INET, STREAMing socket
        # serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # # bind the socket to a public host, and a well-known port
        # serversocket.bind(('0.0.0.0', 30002))
        # # become a server socket
        # serversocket.listen(5)
        # # accept connections from outside
        # (conn, address) = serversocket.accept()

        # conn.send(Tamanho.encode())  # send data to the client
        # conn.send(str(tuple(Yround)).encode())  # send data to the client
        # conn.send(str(tuple(Xround)).encode())  # send data to the client
        # conn.send(str(tuple(FrameZ)).encode())  # send data to the client

        # conn.close()

        # exit()

    else:
        exit()

    print('Enviado')
