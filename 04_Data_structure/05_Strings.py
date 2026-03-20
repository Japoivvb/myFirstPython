# Strings
# to know length string
word = 'by'
print(len(word)) 

# to set multiline with 3 ' or 3 "
multiline = '''Linea #1
Linea #2'''
print(len(multiline))

# concat and repeat n times with *
str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# char as number with ord(), number as char with chr()
char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))
print(chr(97))
print(chr(32))

# read each character
the_string = 'pedra pomez'
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
print()

# slicing
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:]) # until the end
print(alpha[:3]) # from beg
print(alpha[1::2]) # 2 by 2

# find 
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("f" not in alphabet)


# immutable
alphabet = "bcdefghijklmnopqrstuvwxy"
# "a" + alphabet
alphabet = "a" + alphabet
print(alphabet)

# find smallest min() and greatest max()
print(min("aAbByYzZ"))
print(max("aAbByYzZ"))

# get position found
print("aAbByYzZaA".index("b"))
print(alphabet.find('c')) # returns lowest index
print(alphabet.rfind('a')) # returns highest index


# create a list from string, explode
print(list("abcabc"))

# count occurrences
print("abcabc".count("b"))

# to upper case only first char
print('aBcD'.capitalize())

# to center a word between spaces
print('[' + 'Beta'.center(8) + ']')

# to check how to ends
t = "zeta"
print(t.endswith("a"))

# to check if it is alphanumeric
text = "123"
print(text.isalnum()) #True

# to check if it is numeric
number =123
print(number.isdigit()) #True

# to check if there are spaces
sentence = "once upon a time"
print(sentence.isspace()) #True

# join strings
day = "21"
month = "gener"
year = "2026"
print(" of ".join([day,month,year]))

# remove specific values with lstrip()
text1 = "123456Hello world"
result = text1.lstrip("0123456789")
print(result)

# replace values with replace()
text1 = "Hello world"
print(text1.replace("o", "i"))

# to explode a string with 
text1 = "Python és un llenguatge de programació potent"
words1 = text1.split() # by default with spaces
print(f"Result: {words1}")

# to remove spaces from beg and end
text1 = "   Hello world   "
result1 = text1.strip()
print(f"Original: '{result1}'")

# to format as title, capital letter in each word 
text1 = "python as programming language"
result1 = text1.title()
print(f"Resultat: {result1}")

# to order with sort() and sorted()
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print(f"order asc: {numbers}")
print(f"order desc: {sorted(numbers, reverse="True")}")
