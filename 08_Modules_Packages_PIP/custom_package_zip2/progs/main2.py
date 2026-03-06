# Importem la llista 'path' del mòdul sys per poder modificar les rutes de cerca de mòduls
from sys import path
 
# Afegim la ruta del fitxer ZIP que conté els paquets Python al final de sys.path
path.append('..\\package\\extrapack.zip')
 
# Importem el mòdul sigma del paquet extra.good.best i li assignem l'àlies 'sig'
import extra.good.best.sigma as sig  # type: ignore
# Importem el mòdul alpha del paquet extra.good i li assignem l'àlies 'alp'
import extra.good.alpha as alp  # type: ignore
# Importem la funció FunI del mòdul iota que està dins del paquet extra
from extra.iota import FunI  # type: ignore
# Importem la funció FunB del mòdul beta que està dins del paquet extra.good
from extra.good.beta import FunB  # type: ignore
 
# Executem la funció FunS del mòdul sigma i imprimim el seu resultat
print(sig.FunS())
# Executem la funció FunA del mòdul alpha i imprimim el seu resultat
print(alp.FunA())
# Executem la funció FunI i imprimim el seu resultat
print(FunI())
# Executem la funció FunB i imprimim el seu resultat
print(FunB())