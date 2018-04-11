#Iris Data Project "Greg Feeley" 11-04-2018
#https://en.wikipedia.org/wiki/Iris_flower_data_set

#import libraries
import numpy 
import pandas as pd 
import matplotlib.pyplot as plt

#import data from address
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
iris = pd.read_csv(url, names=names)

#print data for checking
print(iris)



