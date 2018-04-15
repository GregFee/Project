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

#Calculate max value of Sepal Length
maxsepallength = np.max(iris[:,0])
print("The Max of Sepal Length is", maxsepallength)
#Calculate max value of Sepal Width
maxsepalwidth = np.max(iris[:,1])
print("The Max of Sepal Width is", maxsepalwidth)
#Calculate max value of Petal Length
maxpetallength = np.max(iris[:,2])
print("The Max of Petal Length is", maxpetallength)
#Calculate max value of Petal Width
maxpetalwidth = np.max(iris[:,3])
print("The Max of Petal Width is", maxpetalwidth)



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

#Histogram of Petal Length
plt.hist(petallength)
plt.title("Petal Length")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#Histogram of Petal Width
plt.hist(petalwidth)
plt.title("Petal Width")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#scatter plot of Sepal Width and Length
#Edited from https://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot-on-matplotlib

plt.scatter(sepallength, sepalwidth, color=['red', 'blue'])
plt.title("Scatter Diagram of Sepal Length(Red) and Width(Blue)")
plt.show()

#scatter plot of Petal Length and Width
plt.scatter(petallength, petalwidth, color=['green', 'yellow'])
plt.title("Scatter Diagram of Petal Length(Green) and Width(Yellow)")
plt.show()

#scatter plot of Petal Length and Sepal Length
plt.scatter(petallength, sepallength, color=['green', 'blue'])
plt.title("Scatter Diagram of Petal Length(Green) and Sepal Length(Blue)")
plt.show()

#scatter plot of Petal Width and Sepal Width
plt.scatter(petalwidth, sepalwidth, color=['yellow', 'blue'])
plt.title("Scatter Diagram of Petal Width(Yellow) and Sepal Width(Blue)")
plt.show()








