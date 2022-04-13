import pickle

def carica_dati():
    try:
        
        nome_file = input('Inserisci il nome del file: ')
        apri_file = open(nome_file,'r')
        dati = apri_file.readlines()
        apri_file.close()
    except Exception as err:
        dati = list()
        print("File errato")
    return dati
 
def carica_nominativi(dati):
    nominativi = list()
    medie = list()
    for i in range(0,len(dati),3):
        nominativi.append(dati[i].rstrip('\n'))
        medie.append([(float(dati[i + 1].rstrip('\n')) + float(dati[i + 2].rstrip('\n')))//2])
    return nominativi, medie
 
def carica_dizionario(n, m):
    d = dict()
    for i in range(0,len(n)):
        d[n[i]] = m[i]
    return d

def salva_dizionario(d):
    file = open('voti.dat','wb')
    pickle.dump(d, file)
    file.close()
 

   
 
def visualizza_info1(nominativo_media):
    for key in nominativo_media:
        print("Nominativo studente: "+key+"\t"+ " Media voti: "+str(nominativo_media[key]),end='')
        if nominativo_media[key][0] < 18:
            print("\t Esame non superato")
        else:
            print("\t Esame superato")
 
def visualizza_info2(nominativo_media):
    print("Esame superato da:")
    for key in nominativo_media:
        if nominativo_media[key][0] >= 18:
            print(key)
 
def main():
    dati = carica_dati()
    if (len(dati)>0):
        try:
            nominativi, medie = carica_nominativi(dati)
            nominativo_media = carica_dizionario(nominativi, medie)
            
            visualizza_info1(nominativo_media)
            visualizza_info2(nominativo_media)
        except Exception as err:
            print(err)
 
main()