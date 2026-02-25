# dictionary with {key, value }
# book
book = {"title": "one", "pages" : 145}
# add element
book["genre"] = "belic"
# print each element
book["pages"] = 100
# print all keys
print(book.keys())
# print all values
print(book.values())
# print keys and values
for key, value in book.items():
    print(key, value)