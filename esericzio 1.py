class Persona:
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
 
    def __str__(self):
        return f"Ciao {self.__nome}{self.__cognome} hai" + str(self.__eta)
 
 
class Studente(Persona):
    def __init__(self, nome, cognome, eta, corso):
        Persona.__init__(self, nome, cognome, eta)
        self.__corso = corso
 
    def __str__(self):
        return Persona.__str__(self)+ f", e frequenti {self.__corso}"
 
 
class Lavoratore(Persona):
    def __init__(self, nome, cognome, eta, professione):
        Persona.__init__(self, nome, cognome, eta)
        self.__professione = professione
 
    def __str__(self):
        return Persona.__str__(self)+ f", e sei {self.__professione}"

def __main__ ():
    persone= Persona("Marta", "Lilla", 31)
    studenti= Studente("Luca", "Ravenna", 34, "giurisprudenza")
    lavoratori= Lavoratore("Edoardo", "Ferrario", 35, "comico")
    print(persone, studenti, lavoratori)

print (__main__())