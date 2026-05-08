from os import strerror
import os

try:
    # Inicialitzem un comptador per contar els caràcters
    counter = 0
    
    # Obrim l'arxiu 'text.txt' en mode lectura de text
    # Usem la ruta absoluta basada en la ubicació d'aquest script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'text.txt')
    stream = open(file_path, "rt", encoding="UTF-8")
    
    # Llegim el primer caràcter de l'arxiu
    char = stream.read(1)
    
    # Iterem mentre hi hagi caràcters per llegir
    while char != '':
        print(char, end='')  # Imprimeix cada caràcter sense salt de línia
        counter += 1  # Incrementem el comptador
        char = stream.read(1)  # Llegim el següent caràcter
    
    # Tanquem l'arxiu
    stream.close()
    
    # Imprimeix el total de caràcters llegits
    print("\n\nCaràcters en l'arxiu:", counter)  # Ex: Caràcters en l'arxiu: 150
    
except IOError as e:
    # Si hi ha un error d'entrada/sortida, mostrem el missatge d'error
    print("S'ha produït un error d'E/S: ", strerror(e.errno))  # Ex: S'ha produït un error d'E/S: No such file or directory