import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()
sns.set_style('whitegrid')
sns.set_palette('gray')

myFile = open("data.txt")

line = myFile.readline()
x = []
y = []
point = []

while line:
    data = line.strip().split(",")
    print(data)
    print(data[0])
    print(data[1])
    x.append(int(data[0]))
    y.append(int(data[1]))
    point.append(data[2])

    line = myFile.readline()


myFile.close()
print(x)
print(y)
outputx = np.array(x)
outputy = np.array(y)
plt.xlabel("date")
plt.ylabel("articles")

plt.plot(outputx, outputy)
plt.show()