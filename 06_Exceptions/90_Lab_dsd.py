# Exercise 55: Validation of values within a range

"""
STATEMENT:
---------
Write a function capable of reading integer values and checking whether they are within 
a specified range.

The function must:
------------------
1. Accept three arguments: 
   - prompt: message to show to the user
   - min: acceptable lower limit
   - max: acceptable upper limit

2. If the user enters a string that is not an integer value:
   - Display the message: "Error: incorrect input"
   - Ask the user to enter the value again

3. If the user enters a number outside the range:
   - Display the message: "Error: the value is not within the allowed range (min..max)"
   - Ask the user to enter the value again

4. If the value is valid, return it as the result

USAGE EXAMPLE:
--------------
value = read_int("Enter a number between -10 and 10: ", -10, 10)
print(f"The number is: {value}")

EXPECTED OUTPUT:
----------------
Enter a number between -10 and 10: 100
Error: the value is not within the allowed range (-10..10)
Enter a number between -10 and 10: asd
Error: incorrect input
Enter a number between -10 and 10: 1
The number is: 1
"""

# Write your code here:
def read_int(prompt, min, max):
    while True:
        try:
            # check type number
            number = int(input("give me a number"))

            # check range
            assert not (number < min or number > max)

            # return number if ok
            return number

        except ValueError as e:
            print("Error: incorrect input")
        except AssertionError as e:
            print("Error: the value is not within the allowed range (min..max)")
        

value = read_int("Enter a number between -10 and 10: ", -10, 10)
print(f"The number is: {value}")