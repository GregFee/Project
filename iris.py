#Iris Data Project "Greg Feeley" 11-04-2018
#https://en.wikipedia.org/wiki/Iris_flower_data_set

#import libraries
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt

#read data file in numpy array edited from https://stackoverflow.com/questions/25614749/how-to-import-csv-file-as-numpy-array-in-python
iris = np.genfromtxt ('data/iris.csv', delimiter=",")

#access first column of data sepal length
sepallength = iris[:,0]
#access second column of data sepal width
sepalwidth = iris[:,1]
#access third column of data petal length
petallength = iris[:,2]
#access fourth column of data petal width
petalwidth = iris[:,3]

#check for data instance sample size 
print(sepallength.shape)
print(sepalwidth.shape)
print(petallength.shape)
print(petalwidth.shape)

#calculate mean sepal length
meansepallength = np.mean(iris[:,0])
#calculate mean sepal width
meansepalwidth = np.mean(iris[:,1])
#calculate mean petal length
meanpetallength = np.mean(iris[:,2])
#calculate mean petal width
meanpetalwidth = np.mean(iris[:,3])
#print result
print("Mean Sepal Length is:", meansepallength)
#print result
print("Mean Sepal Width is:", meansepalwidth)
#print result
print("Mean Petal Length is:", meanpetallength)
#print result
print("Mean Petal Width is:", meanpetalwidth)

#Histogram of Sepal Length
plt.hist(sepallength)
plt.title("Sepal Length")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#Historgram of Sepal Width
plt.hist(sepalwidth)
plt.title("Sepal Width")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()






