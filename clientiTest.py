from ClientiDAO import ClientiDAO

class ClientitestDao:
    def __init__(self):
        __clientidao = ClientiDAO()
        inp=int(input('Cosa vuoi fare? \n 1-Voglio sapere il numero di clienti per agente, 2-Voglio sapere chi sono i clienti di uno specifico agente'))
        if (inp!=1) and (inp!=2):
            print('Numero errato')
        elif inp==1:
            __clientidao.getclientiperagente()
        else:
            __clientidao.getclientibyagente()

print (ClientitestDao)  