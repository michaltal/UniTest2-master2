open_file = open('D:/MyDocs/data.txt', 'w')
open_file.write('My Data File!\n')
open_file.write('My second line.\n')
open_file.close()
rfile = open('data.txt', 'r')
# print(rfile.read(4))
# print(rfile.read(16))
print(rfile.readlines())
rfile.close()
# print(rfile.closed)

# using with statement
with open('data.txt', 'a+') as file:
    file.write('hello My world !\n')

with open('data.txt', 'r') as file:
    print(file.read())

print(file.closed)





