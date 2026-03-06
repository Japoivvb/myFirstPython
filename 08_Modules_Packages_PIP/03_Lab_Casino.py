#EXERCICI: EL DAU DEL CASINO (AMB WHILE)
# Crear un programa que simuli el llançament d'un dau en un casino i permeti jugar múltiples vegades.

"""Requisits
- s'ha d'importar un modul...?¿?¿
El programa ha de:
- Utilitzar un bucle per jugar repetidament
- Preguntar a l'usuari per un número entre 1 i 6
- Generar un número aleatori entre 1 i 6 (simulant el dau)
- Comparar els dos números
- Dir si ha encertat o no
- Preguntar si vol jugar una altra vegada"""

# PAS 1: IMPORTAR EL MÒDUL
import random

# PAS 2: MOSTRAR CAPÇALERA
print("welcome to casino")

# PAS 3: INICIALITZAR VARIABLE DEL BUCLE
exit = False

# PAS 4: BUCLE PRINCIPAL 
do = True
while not exit:
    # Demanar número a l'usuari
    number =  int(input("Give me a number between 1 to 6"))  
    
    # Generar número aleatori
    random_number =  random.randint(1,6)  
    
    # Mostrar resultats
    print(f"number selected {number}")
    print(f"number random {random_number}")
     
    # Comprovar si ha encertat
    if number == random_number:
        print(f"you guessed the number")
    else:
        print(f"you failed")

    # Preguntar si vol continuar
    answer =  input("Try again? yes or no")  
    if answer == "no":
        exit = True
    
print("bye")

    