from sys import path
#path.append('C:\\Users\\formacio\\Documents\\py2126\\exercici16\\package\\') 
path.append('C:\\Users\\Jose\\OneDrive - Stucom, S.A\\Escritorio\\Cursos\\python_curso\\myFirstPython\\08_Modules_Packages_PIP\\custom_package\\package')
path.insert(0,r'../package')

import extra.iota
print(extra.iota.FunI())
