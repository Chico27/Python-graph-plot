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

while line:
    data = line.strip().split(",")
    print(data)
    print(data[0])
    print(data[1])
    x.append(int(data[0]))
    y.append(int(data[1]))
    line = myFile.readline()


myFile.close()
print(x)
print(y)
outputx = np.array(x)
outputy = np.array(y)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(outputx, outputy)
ax.set_xlabel('cold treatment [hour]')
ax.set_ylabel('gene activity')
ax.set_ylim(0, 2)
plt.show()
