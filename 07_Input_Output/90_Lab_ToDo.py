"""Exercici: La meva llista de tasques
Fitxer proporcionat: tasks.txt
Fer els deures
Comprar el pa
Trucar l'avi
Rentar els plats

Tasques
1. Llegir i mostrar totes les tasques de tasques.txt
2. Afegir una nova tasca al fitxer
3. Mostrar el contingut actualitzat amb la nova tasca

Pistes

Usa open('tasques.txt', 'r') per llegir
Usa open('tasques.txt', 'a') per afegir sense esborrar el que hi ha
Usa with per tancar el fitxer automàticament
Usa read() per llegir tot el contingut"""

import os

# Obtenir el directori de l'script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'tasks.txt')

print("=== TASQUES ORIGINALS ===")
# Tasca 1: Llegir i mostrar totes les tasques
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

print("\n=== AFEGIR UNA NOVA TASCA ===")
# Tasca 2: Afegir una nova tasca
new_task = "Estudiar Python\n"
with open(file_path, 'a') as file:
    file.write(new_task)
print(f"Tasca afegida: {new_task.strip()}")

print("\n=== CONTINGUT ACTUALITZAT ===")
# Tasca 3: Mostrar el contingut actualitzat
with open(file_path, 'r') as file:
    updated_content = file.read()
    print(updated_content)