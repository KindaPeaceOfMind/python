# Чтение файла по символам
file1 = open("3/file1.txt", "r")
st = file1.read(1)
st += file1.read()
print("File1: ", st)
file1.close()

# Построчное чтение
file2 = open("3/file2.txt", "r")
print("File2: ")
i = 0
for line in file2:
    print("Line {}: {}".format(i, line.replace("\n", "")))
    i += 1
file2.close()

# Запись в файл
file3 = open("3/file3.txt", "w")
for s in "Strings can be easily written to file":
    file3.write(s)
    if s == " ":
        file3.write("\n")
print("File 3 was written successfully")
file3.close()