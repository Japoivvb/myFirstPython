from os import strerror

# Iniciem un bloc try per capturar possibles errors d'entrada/sortida
try:
    # Obrim (o creem) el fitxer 'newtext.txt' en mode escriptura de text ('wt')
    file = open('newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
    # Bucle que itera 10 vegades (de 0 a 9)
    for i in range(10):
        # Creem una cadena de text amb el número de línia i un salt de línia
        s = "línea #" + str(i+1) + "\n"
        # Iterem caràcter per caràcter de la cadena
        for char in s:
            # Escrivim cada caràcter al fitxer
            file.write(char)
    # Tanquem el fitxer per alliberar recursos
    file.close()
# Capturem qualsevol excepció d'entrada/sortida
except IOError as e:
    # Mostrem un missatge d'error amb la descripció del codi d'error
    print("Se produjo un error de E/S: ", strerror(e.errno))