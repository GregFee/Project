# Project

**Project - Programming and Scripting Iris Data Set**

Introduction: This project will explore Fisher's Iris Data Set (1936)[1]. This is an example of discriminate analysis and the data set conists of fifty samples from each of three Iris flowers including the setosa, virginica and versicolor type[2]. There are 150 observations in the set. Performance on the data set is a standard bearer for new proposed machine learning[3]. This project will analyse the data from 150 observations in relation to petal length/width and sepal length/width.


Installing: *Download and install Anaconda to run this code. https://www.anaconda.com/

Version used 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)]

Download and save dataset from  http://archive.ics.uci.edu/ml/datasets/Iris. File to be saved as iris.csv into same folder as code is executed from


Procedure:

The project can be run from the iris.py file

1. The maximun and minimum of each column of data was calculated.
2. The mean and median for each column of data is calculated.
3. A historgram is presented for each measurement category.
4. A simple plot was made for each data category.
5. Plots were constructed to show data catergories running concurrently
6. Scatter plots are presented for the data catergories. 
7. Box Plots were created to show distribution.

**Iris Data Summary**

The shape of the data showed that the 150 observations were saved over from the file for manipulation.  The 150 observations measured the categories of sepal length and width and petal length and width. The 3 species of iris flower included the setosa, virginica and versicolor type. There were 50 occurrences of each type of species.

The maximum and minimum of value for each category was calculated.  Although maximum and minimum are not very useful it can give you a quick representation of data in each category to see any noticeable relationship. The mean value for all categories was calculated. Mean value is an indication for central tendency in the data. This value is an example of a typical data point put keep in mind the mean value is sensitive to extreme data value [4]. Therefore, the median was also calculated. Considering the mean and median for both the values of Sepal Length and Width the values showed up similar. There is however a variance in the values when considering the Petal Length and Petal Width categories with mean Petal Length measurin 3.75 and the median measuring 4.35. This may show how an extreme data value may skew an attempt to calculate a typical data point.

There is a histogram produced for each category. A histogram gives and excellent visual representation of variability.  In the histograms labelled (1.3) and (1.4) measuring petal length and width there are gaps in distribution and this could be valuable if you can find a relationship with the species. This is an example of multimodal data where the distribution does not follow a bell curve pattern, and this may be because you are dealing with three different species of flower[5]. These gaps in data are indicative of different species in the data set.

Line plots were produced for each category and also combined to exhibit any possible relationship. These plots can give a quick visual reference of variance in the data. In the plot labelled 2.1 you can see how the variance increase markedly when occurrences reach 50 and 100 as the different species of iris enter the data set. This difference between the species can also be seen in the other line plots to varying amounts. When the categories are plotted concurrently in plots labelled 2.5, 2.6 and 2.7 this relationship in the variance between occurrences 50 and 100 where the species of iris change in the data set is most obvious. This is further illustrated visually in a polygon filled plot labelled 2.8 where you can see the variance and relationship bleed together where setosa, virginica and versicolor iris types enter the data set after each 50 instances. You can make a prediction from visualising this data that if iris flower in question has small measurements in both sepal length, width and petal length and width it is from the setosa iris species as these occur over the first 50 instances. Likewise, a higher measurement on these categories for the last 50 instances shows you may predict it is from the virginica species.

Various scatter plots were also created to show the relationship between the data visually. In the plot labelled 2.10 of petal length and width a relationship can be visualised clearly. The elongated overall shape of the points shows a strong correlation with the variables and the two distinct groupings is evidence of a separability of the categories [6].  It is also a similar case in the plots labelled 2.11 and 2.12 where a correlation between the variables can be seen.

Finally, boxplots were constructed for each category. This describes the data through their quartiles. A boxplot can give an immediate indication of the skewness of distribution [7]. A boxplot can show some iris measurements that may not be typical for that category.  This is evident in plot 3.2 sepal width where we you can see outliers outside of the norm and the interquartile range with the lowest measurement outlier caused by a measurement of 2cm. This measurement may be an extreme and the boxplots for the other categories have no evidence of such extremes.  However, if you construct a boxplot of the data combined for petal and sepal length as in plot 3.5 there is numerous outliers. Comparing this with a boxplot of petal and sepal width as in plot 3.6. there are none noticeable outliers.  This is interesting to note. In summary there were clear differnces bewteen in the measurements of the three differnet species of iris and this was able to be represnted visually. From Looking at the measurements the species of iris could be predicted.






**References**

[1] UC Irvine Machine Learning Repository. Iris data set. http://archive.ics.uci.edu/ml/datasets/Iris.

[2] Innovations in Compter Science and Engineering(2017) Saini, Sayal and Rawat(pg. 268)

[3] Advances in Data Mining(2015)Petra Perner(pg.119)

[4] Fire Data Analysis Handbook by Tom McEwen pg. 42 www.googlebooks.com

[5] Predictive Analytics and Data Mining: Concepts and Practice with Rapid Miner by Vijay Kotu and Bala Desphande. Pg. 48

[6] Python for Data Science by John Paul Mueller, Luca Massaron (2015) pg. 248

[7] Statistics: An Interactive Text for the Health and Life Sciences by Goteti Bala, Patricia Schmitt, David J. Ostroff (1995) Pg.190




Author: Greg Feeley.
