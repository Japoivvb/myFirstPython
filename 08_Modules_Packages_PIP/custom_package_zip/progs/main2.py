from sys import path
path.append('C:\\Users\\Jose\\OneDrive - Stucom, S.A\\Escritorio\\Cursos\\python_curso\\myFirstPython\\08_Modules_Packages_PIP\\custom_package\\package\\extrapack.zip')
# path.append('..\\package\\extrapack.zip')
 
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB
 
print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())