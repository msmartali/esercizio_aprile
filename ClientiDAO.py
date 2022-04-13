from MySqlConnection import MySqlConnection
class ClientiDAO(object):
    __db = None

    def __init__(self):
        self.__db = MySqlConnection()

    def getclientiperagente(self):
        risultato=self.__db.query("SELECT count(*)as numero,agente FROM clienti group by agente").fetchall()
        for x in risultato:
            print(f'Agente: {x[1]},Numero clienti: {x[0]}') 

    def getclientibyagente(self):
        agente=input('Di quale agente vuoi conoscere i clienti?\n')
        risultato=self.__db.query(f"SELECT nome  FROM clienti where agente='{agente}'").fetchall()
        print(f'-----Lista clienti agente {agente}-----')
        for cliente in risultato:
            print(cliente[0])