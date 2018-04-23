#Iris Data Project "Greg Feeley" 11-04-2018
#https://en.wikipedia.org/wiki/Iris_flower_data_set 

#check python version
import sys
print (sys.version)

#import libraries
import numpy as np
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

#Calculate minimum value of Sepal Length
minsepallength = np.min(iris[:,0])
print("The Minimum of Sepal Length is", minsepallength)
#Calculate minimum value of Sepal Width
minsepalwidth = np.min(iris[:,1])
print("The Minimum of Sepal Width is", minsepalwidth)
#Calculate minimum value of Petal Length
minpetallength = np.min(iris[:,2])
print("The Minimum of Petal Length is", minpetallength)
#Calculate minimum value of Petal Width
minpetalwidth = np.min(iris[:,3])
print("The Minimum of Petal Width is", minpetalwidth)


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

#calculate median
mediansepallength = np.median(iris[:,0])
print('The Median Sepal Length is:', mediansepallength)

#calculate median
mediansepalwidth = np.median(iris[:,1])
print('The Median Sepal Width is:', mediansepalwidth)

#calculate median
medianpetallength = np.median(iris[:,2])
print('The Median Petal Length is:', medianpetallength)

#calculate median
medianpetalwidth = np.median(iris[:,3])
print('The Median Petal Width is:', mediansepalwidth)

#Histogram of Sepal Length
plt.hist(sepallength, edgecolor='black')
plt.title("Sepal Length")
plt.xlabel("Value in CM")
plt.ylabel("Frequency")
plt.show()

#Historgram of Sepal Width
plt.hist(sepalwidth, edgecolor='black')
plt.title("Sepal Width")
plt.xlabel("Value in CM")
plt.ylabel("Frequency")
plt.show()

#Histogram of Petal Length
plt.hist(petallength, edgecolor='black')
plt.title("Petal Length")
plt.xlabel("Value in CM")
plt.ylabel("Frequency")
plt.show()

#Histogram of Petal Width
plt.hist(petalwidth, edgecolor='black')
plt.title("Petal Width")
plt.xlabel("Value in CM")
plt.ylabel("Frequency")
plt.show()

#plot of petal length
plt.plot(petallength)
plt.title("Plot of Petal Length")
plt.ylabel("Value in CM")
plt.xlabel("Occurence")
plt.show()



#plot of petal width
plt.plot(petalwidth)
plt.title("Plot of Petal Width")
plt.ylabel("Value in CM")
plt.xlabel("Occurence")
plt.show()

#plot of sepal length
plt.plot(sepallength)
plt.title("Plot of Sepal Length")
plt.ylabel("Value in CM")
plt.xlabel("Occurence")
plt.show()

#plot of sepal width
plt.plot(sepalwidth)
plt.title("Plot of Sepal Width")
plt.ylabel("Value in CM")
plt.xlabel("Occurence")
plt.show()

#Plot data concurrently edited from https://pythonspot.com/matplotlib-legend/
#Plot Sepal and Petal Length
fig = plt.figure()
ax = plt.subplot()
ax.plot(sepallength, label='Sepal Length')
ax.plot(petallength, label= 'Petal Length')
plt.ylabel("Measurement in CM")
ax.legend()
plt.show()

#Plot Petal and Sepal Width
fig = plt.figure()
ax = plt.subplot()
ax.plot(petalwidth, label= 'Petal Width')
ax.plot(sepalwidth, label='Sepal Width')
plt.ylabel("Measurement in CM")
ax.legend()
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


#Boxplot of Sepal Length
plt.boxplot(sepallength)
plt.title("Boxplot of Sepal Length")
plt.ylabel("Measurement in CM")
plt.show()

#Boxplot of Sepal Width
plt.boxplot(sepalwidth)
plt.title("Boxplot of Sepal Width")
plt.ylabel("Measurement in CM")
plt.show()

#Boxplot of Petal Length
plt.boxplot(petallength)
plt.title("Boxplot of Petal Length")
plt.ylabel("Measurement in CM")
plt.show()

#Boxplot of Petal Width
plt.boxplot(petalwidth)
plt.title("Boxplot of Petal Width")
plt.ylabel("Measurement in CM")
plt.show()



#boxplot of categories combined showing distribution edited from
#https://matplotlib.org/examples/pylab_examples/boxplot_demo.html

data = np.concatenate((petallength, sepallength), 0)
plt.boxplot(data)
plt.title("Boxplot of Petal and Sepal Length")
plt.show()

#boxplot showing distribution for petal width and sepal width
data = np.concatenate((petalwidth, sepalwidth), 0)
plt.boxplot(data)
plt.title("Boxplot of Petal and Sepal Width")
plt.show()










