# define a class
class Stack:
    def __init__(self): # constructor
        self.__stack_list = []  # initialize a empty list

    def push(self, val): # method to add a value
        self.__stack_list.append(val) 

    def pop(self): # method to remove a value
        val = self.__stack_list[-1]  
        del self.__stack_list[-1]  
        return val 

# define a subclass from Stack
class AddingStack(Stack):  
    def __init__(self):
        Stack.__init__(self)  # call superclass constructor
        self.__sum = 0  # initialize child attribute

    def get_sum(self):
        return self.__sum  # get value sum

    def push(self, val):
        self.__sum += val  
        Stack.push(self, val)  

    def pop(self):
        val = Stack.pop(self)  
        self.__sum -= val  
        return val  


stack_object = AddingStack()  # create an object AddingStack

for i in range(5):  
    stack_object.push(i)  
print(stack_object.get_sum())  

for i in range(5):  
    print(stack_object.pop())  

# Sample class
class ExampleClass:
    a = 1  # class variable 
    def __init__(self):
        self.b = 2  # instance variable


# create an object
sample_object = ExampleClass()

# Check if the object has attribute 'b' (instance variable)
print(hasattr(sample_object, 'b'))  # True - 'b' exists in the instance
# Check if the object has access to attribute 'a' (class variable)
print(hasattr(sample_object, 'a'))  # True - 'a' is accessible from the instance
# Check if the class has attribute 'b' (instance variable)
print(hasattr(ExampleClass, 'b'))  # False - 'b' does not exist at class level
# Check if the class has attribute 'a' (class variable)
print(hasattr(ExampleClass, 'a'))  # True - 'a' exists in the class