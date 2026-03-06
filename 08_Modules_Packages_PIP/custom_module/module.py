#print("I like this module")
#print(__name__)
counter = 0

if __name__ == "__main__": # if executed by itself
   print("I prefer to be a module.")
else:
   print("it is a " + __name__)
   print("I like to be a module.")