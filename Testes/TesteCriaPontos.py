Frequencia = 2
Nb_points = Frequencia*4

LargPX = 1 #DEPENDE DO TAMANHO DA FOLHA E QUANTOS PIXELS TEM NA IMAGEM
NumeroPixel = 2 #CONTADOR

# y constante no momento

for i in range(1, Nb_points, 2): #PEGA SÓ IMPARES
    PosX = (i/(Nb_points))#*LargPX + LargPX*NumeroPixel
    print(PosX)