import math

# Custom entity (Namespace Local)
pi = 3.0 

# Custom function
def cos(angle):
    if angle == 0:
        return 1.0 
    else:
        return 0.0

# 1. Using local namespace
print(f"La nostra constant 'pi' local és: {pi}") 
print(f"El resultat de la nostra funció 'cos(0)' és: {cos(0)}") 

# 2. Using module math
print(f"La constant 'pi' del mòdul math és: {math.pi}")
print(f"El resultat de la funció 'math.cos(0)' és: {math.cos(0)}")

# 3. Using specific function
from math import sin
#from math import sin, pi
print(sin(pi/2))

# 4. Using alies with "as"
from math import pi as PI, sin as sen  
print(sen(PI/2))

# 5. Using PIP
# pip install scipy, to get location  python -m site
# Different modules with similar funcionts
import statistics as stats1
import scipy.stats as stats2

data = [1, 2, 3, 4, 5] # list type
avg_stats = stats1.mean(data)  # from statistics
avg_scipy = stats2.tmean(data)  # from scipy.stats

print("Average (statistics):",  avg_stats)
print("Average (scipy):", avg_scipy)

# 6. Using platform module
from platform import python_implementation, python_version_tuple

print(python_implementation()) # type of python implementation
for atr in python_version_tuple(): # show version M.m.f
    print(atr)

# 7. Using pygame
# pip install pygame
# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#   for event in pygame.event.get():
#    if event.type == pygame.QUIT\
#    or event.type == pygame.MOUSEBUTTONUP\
#    or event.type == pygame.KEYUP:
#     run = False