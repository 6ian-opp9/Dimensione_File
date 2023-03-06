"""
=========================================================================================
Programma:                Backup file Cartella 

Descrizione:              Faccio il backup di una cartella tramite metodi e importazioni

Autore:                   Gianluca Oppedisano
Data Di Pubblicazione:    26/02/2023
Relase:                   v1.0
=========================================================================================
"""

import os

def dimensione_file():

    print("Digitare 1 se si desidera utilizzare la directory corrente, dove risiede il file.")          # Chiedo all'utente che cosa vuole fare
    print("Digitare 2 se si vuole immettere manualmente la directory.")

    print()

    sel = int(input("Inserimento: "))

    print()

    if (sel == 1):                                                                                      # Verifico che cosa l'utente desidera fare 

        temp_dir = os.getcwd()                                                                          # Prendo la directory nella quale il file viene eseguito

        print ("Ora, la directory selezionata è: ", temp_dir)                                           # Comunico la directory in cui ci si trova

        print()


        src_dir = os.getcwd() + '\\' + input("Inserire il nome della cartella da backuppare: ")         # Chiedo all'utente la directory sorgente 
        print()

        if not os.path.isdir(src_dir):                                                                  # Verifico che la directory inserita esista
            
            return print("La directory sorgente non esiste.")
    
    else:

        src_dir = input("Inserire la directory sorgente da backuppare: ")                               # Chiedo all'utente la directory sorgente 
        print()

        if not os.path.isdir(src_dir):                                                                  # Verifico che la directory inserita esista
            
           return print("La directory sorgente non esiste.")
 

    tipo_file = input("Inserisci la tipologia di file (es. .txt): ")                                    # Chiedo all'utente di inserire l'estensione del file desiderata

    print()

    lista_file = [file for file in os.listdir(src_dir) if file.endswith(tipo_file)]                     # Cerca i file nella directory con il tipo specificato

    
    if not lista_file:                                                                                  # Gestisci l'assenza di file
        print("Non ci sono file di questo tipo nella directory.")
        return

   
    totale_dimensione = 0                                                                               # Variabile di supporto

    for file in lista_file:                                                                             # Calcola la somma delle dimensioni dei file

        percorso_file = os.path.join(src_dir, file)
        dimensione_file = os.path.getsize(percorso_file)
        totale_dimensione += dimensione_file                                                            # Sommo dimensione file

    
    with open("dimensione.txt", "w") as f:                                                              # Creo e scrivo su un file il peso di tutti i file all'interno della cartella

        f.write(f"La dimensione totale dei file {tipo_file} nella directory {src_dir} è di {totale_dimensione / (1024*1024):.2f} MB.")  # Comunico output

    print(f"La dimensione totale dei file {tipo_file} nella directory {src_dir} è stata scritta nel file dimensione.txt.") 


"""
=======================================================================================================================================================================
"""



print("Questo programma permettere fare un backup di alcuni file all'interno di una cartella. ")

print()

while True:
    
    dimensione_file()                                                                                   #Invoco metodo
    
    print()                                                                      

    end = input("Se si vuole terminare il programma digitare si altrimenti, no: ")                      #Chiedo se si vogliono fare altre istanze

    print()

    if (end == "si"):                                                                                   #Verifico condizione e nel caso termino il programma 
        break
    
