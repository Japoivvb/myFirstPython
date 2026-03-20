from sys import path

# list of folders where modules are searched
for p in path:
    print(p)

# add folder to path
#path.append('C:\\Users\\formacio\\Documents\\py2126\\exercici16\\package\\') 
# path.append('C:\\Users\\Jose\\OneDrive - Stucom, S.A\\Escritorio\\Cursos\\python_curso\\myFirstPython\\08_Modules_Packages_PIP\\custom_package\\package')

# add as first folder to search
path.insert(0,r'C:\\Users\\Jose\\OneDrive - Stucom, S.A\\Escritorio\\Cursos\\python_curso\\myFirstPython\\08_Modules_Packages_PIP\\custom_package\\package') # add as first folder

import extra.iota
print(extra.iota.FunI())
import extra.good.alpha
print(extra.good.alpha.FunA())
