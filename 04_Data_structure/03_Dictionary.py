# ============================================================================
# DICTIONARY BASICS - Dictionary with {key: value}
# ============================================================================
# Create a dictionary
book = {"title": "Harry Potter", "pages": 145, "genre": "Fantasy"}
print("Original book:", book)

# Access elements by key
print("Title:", book["title"])
print("Pages:", book["pages"])

# Add new element
book["author"] = "J.K. Rowling"
print("After adding author:", book)

# Modify element
book["pages"] = 309
print("After updating pages:", book)

# Delete element
del book["genre"]
print("After deleting genre:", book)

# ============================================================================
# DICTIONARY METHODS
# ============================================================================

# Print all keys
print("\nKeys:", book.keys())

# Print all values
print("Values:", book.values())

# Print keys and values
print("\nKeys and Values:")
for key, value in book.items():
    print(f"  {key}: {value}")

# ============================================================================
# DICTIONARY WITH DIFFERENT DATA TYPES
# ============================================================================

student = {
    "code": "EST-1001",
    "name": "Maria",
    "surname": "García López",
    "email": "maria@example.com",
    "grades": [8.5, 9.0, 7.5],
    "active": True
}

print("\n\nStudent Dictionary:")
print(student)

# Access nested data
print("Student name:", student["name"])
print("First grade:", student["grades"][0])
print("Is active:", student["active"])

# ============================================================================
# COMMON DICTIONARY OPERATIONS
# ============================================================================

# Check if key exists
if "name" in student:
    print("\nStudent has a name:", student["name"])

# Get with default value
phone = student.get("phone", "Not provided")
print("Phone:", phone)

# Get all students
students = [
    {"code": "EST-1001", "name": "Maria", "surname": "García"},
    {"code": "EST-1002", "name": "Pere", "surname": "Martínez"},
    {"code": "EST-1003", "name": "Anna", "surname": "Sánchez"}
]

print("\n\nAll Students:")
for student in students:
    print(f"  {student['code']}: {student['name']} {student['surname']}")