# Higher Diploma in Data Analytics 2018
# Programming & Scripting Module
# Project 2018
#
# Developer: Gerard O'Mahony
#
# Problem Statement:
# The following project concerns the well-known Fisher’s Iris data set [3]. The project
# entails you researching the data set, and then writing documentation and code in the
# Python programming language [1] based on that research.
# An online search for information on the data set will convince you that many people
# have investigated and written about it previously, and many of those are not experienced
# programmers. You are expected to be able to break this project into several smaller tasks
# that are easier to solve, and to plug these together after they have been completed. You
# might do that for this project as follows:
#  1. Research background information about the data set and write a summary about it.
#  2. Keep a list of references you used in completing the project.
#  3. Download the data set and write some Python code to investigate it.
#  4. Summarise the data set by, for example, calculating the maximum, minimum and
#  mean of each column of the data set. A Python script will quickly do this for you.
#  5. Write a summary of your investigations.
#  6. Include supporting tables and graphics as you deem necessary.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f = open('outfile.dat', 'w')

# Read in the Iris data set using Pandas to a data frame
iris_data = pd.read_csv('./IrisData/iris.data.csv',
                        names=['sepal_length', 'sepal_width',
                               'petal_length', 'petal_width', 'iris_class'])

# First step is to get a basic description of the data, including max, min, median & standard deviation
print('Descriptive Statistics - Iris Data Set')
print('======================================')
print(iris_data.describe(percentiles=[0.5]))

# Isolate each Iris species class and get a basic data description
print('\nDescriptive Statistics - Iris-setosa')
print('======================================')
setosa = iris_data["iris_class"] == "Iris-setosa"
print(iris_data[setosa].describe(percentiles=[.5]))

print('\nDescriptive Statistics - Iris-versicolor')
print('======================================')
versicolor = iris_data["iris_class"] == "Iris-versicolor"
print(iris_data[versicolor].describe(percentiles=[.5]))

print('\nDescriptive Statistics - Iris-virginica')
print('======================================')
virginica = iris_data["iris_class"] == "Iris-virginica"
print(iris_data[virginica].describe(percentiles=[.5]))



# data_string = str(iris_data.describe(percentiles=[0.5]))
# f.write(data_string)

# data_string = str(iris_data.groupby('iris_class').describe())
# f.write(data_string)
f.close()


# setosa_data = iris_data[setosa]
# print(setosa_data)












