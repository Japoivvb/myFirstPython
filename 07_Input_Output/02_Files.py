# read files
# inputFile = open("input_file.txt", mode(r))
# inputFile.read()
# inputFile.close()

# write files
# outputFile = open("output_file.txt", mode(w))
# outputFile.write()
# outputFile.close()

# exercise read products
inputFile = open("./07_Input_Output/input_file.txt", "r")
content = inputFile.read()
print(content)
inputFile.close()

# exercise write phones
outputFile = open("./07_Input_Output/output_file.txt", "w")
outputFile.write("555-1234\n555-5678\n555-9012\n")
outputFile.close()