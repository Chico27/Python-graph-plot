import matplotlib.pyplot as plt

myFile = open("data.txt")

line = myFile.readline()

while line:
    print(line)
    line = myFile.readline()
    data = line.strip().split(",")
    print(data)

myFile.close()

