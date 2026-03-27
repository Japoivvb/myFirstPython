"""
TUPLES IN PYTHON - Complete Tutorial
=====================================
A tuple is an immutable sequence collection.
Unlike lists, tuples cannot be modified after creation.
"""

print("=" * 60)
print("TUPLES - Basic Concepts")
print("=" * 60)

# ============================================================================
# 1. Creating Tuples
# ============================================================================
print("\n1. Creating Tuples:")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with parentheses
coordinates = (14, 50, 60)
print(f"Coordinates: {coordinates}")

# Tuple without parentheses (implicit)
colors = "blue", "red", "yellow"
print(f"Colors: {colors}")

# Single element tuple (note the comma!)
single = (42,)
print(f"Single element: {single}")

# Using tuple() constructor
from_list = tuple([1, 2, 3])
print(f"From list: {from_list}")


# ============================================================================
# 2. Accessing Elements
# ============================================================================
print("\n2. Accessing Elements:")

map_coords = (14, 50, 60)
print(f"First element: {map_coords[0]}")
print(f"Second element: {map_coords[1]}")
print(f"Third element: {map_coords[2]}")
print(f"Last element: {map_coords[-1]}")
print(f"Length: {len(map_coords)}")


# ============================================================================
# 3. Slicing Tuples
# ============================================================================
print("\n3. Slicing Tuples:")

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Original: {numbers}")
print(f"First 3: {numbers[0:3]}")
print(f"Middle 5: {numbers[3:8]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Every 2nd: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")


# ============================================================================
# 4. Immutability - Tuples Cannot Be Modified
# ============================================================================
print("\n4. Immutability (Tuples are Read-Only):")

my_tuple = (1, 2, 3, 4, 5)
print(f"Original tuple: {my_tuple}")

# Attempting to modify will raise an error:
try:
    my_tuple[2] = 99  # This will fail
except TypeError as e:
    print(f"❌ Error when trying to modify: {e}")

# Cannot add elements
try:
    my_tuple.append(6)
except AttributeError as e:
    print(f"❌ Error when trying to append: {e}")


# ============================================================================
# 5. Tuple Unpacking
# ============================================================================
print("\n5. Tuple Unpacking:")

# Unpacking values
point = (10, 20, 30)
x, y, z = point
print(f"Unpacked: x={x}, y={y}, z={z}")

# Unpacking with *
a, *middle, b = (1, 2, 3, 4, 5)
print(f"First: {a}, Middle: {middle}, Last: {b}")

# Swapping values
x, y = 5, 10
x, y = y, x
print(f"After swap: x={x}, y={y}")


# ============================================================================
# 6. Useful Tuple Methods
# ============================================================================
print("\n6. Tuple Methods:")

my_tuple = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {my_tuple}")
print(f"Count of 2: {my_tuple.count(2)}")
print(f"Index of 3: {my_tuple.index(3)}")


# ============================================================================
# 7. Membership Testing
# ============================================================================
print("\n7. Membership Testing (in/not in):")

colors = ("red", "green", "blue", "yellow")
print(f"Colors: {colors}")
print(f"'red' in colors: {'red' in colors}")
print(f"'purple' in colors: {'purple' in colors}")
print(f"'orange' not in colors: {'orange' not in colors}")


# ============================================================================
# 8. Tuple Concatenation and Repetition
# ============================================================================
print("\n8. Concatenation and Repetition:")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"{tuple1} + {tuple2} = {combined}")

repeated = tuple1 * 3
print(f"{tuple1} * 3 = {repeated}")


# ============================================================================
# 9. Nested Tuples
# ============================================================================
print("\n9. Nested Tuples:")

student = ("John", 25, ("Math", "Physics", "Chemistry"))
name, age, subjects = student
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Subjects: {subjects}")
print(f"First subject: {student[2][0]}")

# Matrix-like structure
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"\nMatrix:\n{matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")


# ============================================================================
# 10. Dictionary of Tuples
# ============================================================================
print("\n10. Using Tuples as Dictionary Keys (since they're immutable):")

# Tuples can be dictionary keys
locations = {
    (40.7128, 74.0060): "New York",
    (51.5074, 0.1278): "London",
    (48.8566, 2.3522): "Paris"
}

print(f"Locations: {locations}")
print(f"Paris coordinates: {(48.8566, 2.3522)}")

# Lists cannot be keys (mutable), but tuples can
# bad = {[1,2]: "value"}  # This would fail
good = {(1, 2): "value"}  # This works
print(f"Valid key: {good}")


# ============================================================================
# 11. Practical Example: Storing Data
# ============================================================================
print("\n11. Practical Example - Student Records as Tuples:")

students = [
    ("EST-1001", "Maria Garcia", "maria@example.com"),
    ("EST-1002", "Pere Martinez", "pere@example.com"),
    ("EST-1003", "Anna Sanchez", "anna@example.com")
]

print("Student Records:")
for student in students:
    code, name, email = student
    print(f"  Code: {code}, Name: {name}, Email: {email}")


# ============================================================================
# 12. Converting Between Collections
# ============================================================================
print("\n12. Converting Between Collections:")

# List to Tuple
my_list = [1, 2, 3, 4, 5]
as_tuple = tuple(my_list)
print(f"List {my_list} → Tuple {as_tuple}")

# Tuple to List
as_list = list(as_tuple)
print(f"Tuple {as_tuple} → List {as_list}")

# String to Tuple
word = "hello"
letters = tuple(word)
print(f"Word '{word}' → Tuple {letters}")


# ============================================================================
# 13. When to Use Tuples
# ============================================================================
print("\n13. When to Use Tuples:")
print("""
✓ Use TUPLES when:
  - Data should not be modified (immutable)
  - Using as dictionary keys
  - Returning multiple values from functions
  - Protecting data from accidental changes
  
✓ Use LISTS when:
  - Data needs to be modified frequently
  - Adding/removing elements dynamically
""")


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 60)
print("TUPLES SUMMARY")
print("=" * 60)
print("""
Key Points:
1. Tuples are immutable (cannot be changed after creation)
2. Created with () or just commas
3. Access elements by index: tuple[0], tuple[-1]
4. Slice tuples: tuple[start:end:step]
5. Unpack with: a, b, c = tuple
6. Can be used as dictionary keys
7. Support: len(), count(), index(), in operator
8. Cannot be modified (no append, remove, etc.)
9. More memory efficient than lists
10. Better performance for iteration
""")