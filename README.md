## Data Analytics 2018 - Programming and Scripting Module 
## Project 2018 - Fisher's Iris Data Set Analysis

Data:- [Iris Data Set](IrisData/iris.data.txt) [[1]](#references)

---
### Table of Contents
 * **[Introduction](#introduction)**<br>
 * **[Iris Data Set Analysis](#iris-data-set-analysis)**<br>
 * **[Conclusions](#conclusions)**<br>
 * **[References](#references)**<br>

### Introduction

The Iris Data Set was first examined by British statistician Ronald Aylmer Fisher in his paper 'The use of multiple measurements in taxonomic problems' published in 1936 [[2]](#references). In the paper he credits Dr E. Anderson for the data measurement and it is sometimes also referred to as Anderson's Iris Dats Set [[3]](#references) in the literature because of this.

The data is comprised of 150 measurements in centimetres. The measurements are of the flowers of fifty plants of three species of Iris; Iris-setosa, Iris-versicolor & Iris-virginica referred to as classes. Four flower measurements are given for each class; Sepal length, Sepal width, Petal length & Petal width [[2]](#references). One class is linearly separable from the other 2; the latter are not linearly separable from each other [[1]](#references).

A search of the literature reveals that the data set has become widely used as testing data essentially becoming the 'Hello World!' of Data Science. Bezdek et al. [[4]](#references) have observed that they are at least two distinct published replications of the original data citing two different errors in the University of California at Irvine (UCI) machine learning data set. Two vectors in the UCI Iris-setosa class differ from those published in Fisher's paper:
 
| Vector No.| UCI Data        | Fisher Data     |
|:---------:|:---------------:|:---------------:|
|35         | 4.9,3.1,1.5,0.1 | 4.9,3.1,1.5,0.2 |
|38         | 4.9,3.1,1.5,0.1 | 4.9,3.6,1.4,0.1 |
 
For the purposes of this project the data in this repository is as taken from the UCI Machine Learning Repository [[1]](#references).

---
### Iris Data Set Analysis


The Iris data set is easily imported for data analysis using the open source [_Pandas_](http://pandas.pydata.org/) library which provides easy-to-use data structures and data analysis tools for the [_Python_](https://www.python.org/) programming language. The [_Pandas_](http://pandas.pydata.org/) _read_csv_ method can be used to read the Iris data comma seperated values from file as follows:

```python
import pandas as pd

iris_data = pd.read_csv('./IrisData/iris.data.csv',
                        names=['sepal_length', 'sepal_width',
                               'petal_length', 'petal_width', 'iris_class'])
```
The data was imported with named columns for the sepal lengths/widths, petal lengths/widths and Iris species class.

The first thing to do with the data is a basic analysis where descriptive statistics are generated that summarize the central tendency, dispersion and shape of a dataset’s distribution. This is easily facillitated with the _Pandas_ module as folows:
```python
print(iris_data.describe(percentiles=[0.5]))
```
This results in the following output:

|     |sepal_length | sepal_width | petal_length | petal_width |
|:---:|:-----------:|:-----------:|:------------:|:-----------:|
|count| 150.000000  | 150.000000  |  150.000000  | 150.000000  |
|mean |   5.843333  |   3.054000  |    3.758667  |   1.198667  |
|std  |   0.828066  |   0.433594  |    1.764420  |   0.763161  |
|min  |   4.300000  |   2.000000  |    1.000000  |   0.100000  |
|50%  |   5.800000  |   3.000000  |    4.350000  |   1.300000  |
|max  |   7.900000  |   4.400000  |    6.900000  |   2.500000  |

As can be seen from the table above the data is described in terms of mean, standard deviation, min, median, max for each column of data across all three Iris species classes, which have 50 observations in each giving a total count of 150 observations.

It is also possible to isolate each class data to be described separately if required as follows:
```python
setosa = iris_data["iris_class"] == "Iris-setosa"

print(iris_data[setosa].describe(percentiles=[.5]))
```
The variable setosa is _True_ for all Iris-setosa class and is used subsequently to describe only that class resulting in the following output:
<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

#### Iris-setosa

|     |sepal_length | sepal_width | petal_length | petal_width |
|:---:|:-----------:|:-----------:|:------------:|:-----------:|
|count|   50.00000  |  50.000000  |   50.000000  |   50.00000  |
|mean |    5.00600  |   3.418000  |    1.464000  |    0.24400  |
|std  |    0.35249  |   0.381024  |    0.173511  |    0.10721  |
|min  |    4.30000  |   2.300000  |    1.000000  |    0.10000  |
|50%  |    5.00000  |   3.400000  |    1.500000  |    0.20000  |
|max  |    5.80000  |   4.400000  |    1.900000  |    0.60000  |

The same method can be used to describe the other two species classes:

#### Iris-versicolor

|     |sepal_length | sepal_width | petal_length | petal_width |
|:---:|:-----------:|:-----------:|:------------:|:-----------:|
|count|  50.000000  |  50.000000  |   50.000000  |  50.000000  |
|mean |   5.936000  |   2.770000  |    4.260000  |   1.326000  |
|std  |   0.516171  |   0.313798  |    0.469911  |   0.197753  |
|min  |   4.900000  |   2.000000  |    3.000000  |   1.000000  |
|50%  |   5.900000  |   2.800000  |    4.350000  |   1.300000  |
|max  |   7.000000  |   3.400000  |    5.100000  |   1.800000  |

#### Iris-virginica

|     |sepal_length | sepal_width | petal_length | petal_width |
|:---:|:-----------:|:-----------:|:------------:|:-----------:|
|count|   50.00000  |  50.000000  |   50.000000  |   50.00000  |
|mean |    6.58800  |   2.974000  |    5.552000  |    2.02600  |
|std  |    0.63588  |   0.322497  |    0.551895  |    0.27465  |
|min  |    4.90000  |   2.200000  |    4.500000  |    1.40000  |
|50%  |    6.50000  |   3.000000  |    5.550000  |    2.00000  |
|max  |    7.90000  |   3.800000  |    6.900000  |    2.50000  |

While numerical statistical descriptions are useful in getting an initial summarisation of the data it may be easier to make an assesment of the data by displaying it visually in plot format.

![alt text](../master/images/box_plot.png "Iris Data Set - Box Plot")

---
### Conclusions
<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

---
### References 
<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

[1] Iris data set. UCI Machine Learning Repository. 
	University of California, Irvine, School of Information and Computer Sciences
	https://archive.ics.uci.edu/ml/datasets/iris Retrieved April 4th 2018.

[2] Fisher, R. A., "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936)

[3] Anderson, E., “The Irises of the Gaspe peninsula,” Bull. Amer. Iris Soc., vol.  59,  pp.  2–5,  1935.

[4] Bezdek, J. C., Keller, J. M., Krishnapuram, R., Kuncheva, L. I., & Pal, N. R., "Will the real iris data please stand up?," in IEEE Transactions on Fuzzy Systems, vol. 7, no. 3, pp. 368-369, Jun 1999.

---
