file = open("text.txt", "r")

line1 = file.readline()


print(line1)


if line1 == "1":
    print("True")
else:
    print("False")
file.close()