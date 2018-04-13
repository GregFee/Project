#Iris Data Project "Greg Feeley" 11-04-2018
#https://en.wikipedia.org/wiki/Iris_flower_data_set

#import libraries
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt

#read data file in numpy array
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






