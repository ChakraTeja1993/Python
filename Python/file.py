file = open("C:\\Users\\Chakra Teja\\Desktop\\Python\\file.txt","r")
print(file.read())
file.close()

file =  open("C:\\Users\\Chakra Teja\\Desktop\\Python\\file.txt","w")
file.write("Added more content")
file.close()

file = open("C:\\Users\\Chakra Teja\\Desktop\\Python\\file.txt","r")
print(file.read())
file.close()

