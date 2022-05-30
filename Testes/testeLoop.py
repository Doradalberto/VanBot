
estado = 0
while True:
    if estado == 0:
        print('estado',estado)
        valor = int(input('valor: '))
        print('')

    if valor == 1:
        print('estado 1')
        print('')
        estado = 0

    if valor == 2:
        print('estado 2')
        print('')
        estado = 0
        
    if valor == 3:
        exit()