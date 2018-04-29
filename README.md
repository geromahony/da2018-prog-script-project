## Data Analytics 2018 - Programming and Scripting Module 
## Project 2018 - Fisher's Iris Data Set Analysis

Data:- [Iris Data Set](IrisData/iris.data.txt) [[1]](#references)

---
### Table of Contents
 * **[Introduction](#introduction)**<br>
 * **[Iris Data Set Analysis](#iris-data-set-analysis)**<br>
 	* **[Data Import](#data-import)**<br>
    * **[Data Description](#data-description)**<br>
    * **[Data Visualisation](#data-visualisation)**<br>
    	* **[Box Plot](#box-plot)**<br>
    	* **[Histogram Plot](#histogram-plot)**<br>
    	* **[Scatter Plot](#scatter-plot)**<br>
 * **[Conclusions](#conclusions)**<br>
 * **[References](#references)**<br>

### Introduction

The Iris Data Set was first examined by British statistician Ronald Aylmer Fisher in his paper 'The use of multiple measurements in taxonomic problems' published in 1936 [[2]](#references). In the paper he credits Dr E. Anderson for the data measurement and it is sometimes also referred to as Anderson's Iris Dats Set [[3]](#references) in the literature because of this.

The data is comprised of 150 measurements in centimetres. The measurements are of the flowers of fifty plants of three species of Iris; Iris-setosa, Iris-versicolor & Iris-virginica referred to as classes. Four flower measurements are given for each class; Sepal length, Sepal width, Petal length & Petal width [[2]](#references). One class is linearly separable from the other 2; the latter are not linearly separable from each other [[1]](#references).

A search of the literature reveals that the data set has become widely used as testing data, essentially becoming the 'Hello World!' of Data Science. Bezdek et al. [[4]](#references) have observed that there are at least two distinct published replications of the original data citing two different errors in the University of California at Irvine (UCI) machine learning data set. Two vectors in the UCI Iris-setosa class differ from those published in Fisher's paper:
 
| Vector No.| UCI Data        | Fisher Data     |
|:---------:|:---------------:|:---------------:|
|35         | 4.9,3.1,1.5,0.1 | 4.9,3.1,1.5,0.2 |
|38         | 4.9,3.1,1.5,0.1 | 4.9,3.6,1.4,0.1 |
 
For the purposes of this project the data in this repository is as taken from the UCI Machine Learning Repository [[1]](#references).

---
### Iris Data Set Analysis
#### Data Import

The Iris data set is easily imported for data analysis using the open source [_Pandas_](http://pandas.pydata.org/) library which provides easy-to-use data structures and data analysis tools for the [_Python_](https://www.python.org/) programming language. The [_Pandas_](http://pandas.pydata.org/) _read_csv_ method can be used to read the Iris data comma seperated values from file as follows:

```python
import pandas as pd

iris_data = pd.read_csv('./IrisData/iris.data.csv',
                        names=['sepal_length', 'sepal_width',
                               'petal_length', 'petal_width', 'iris_class'])
```
The data was imported with named columns for the sepal lengths/widths, petal lengths/widths and Iris species class.
<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

#### Data Description
The first thing to do with the data is a basic analysis where descriptive statistics are generated that summarize the central tendency, dispersion and shape of a dataset’s distribution. This is easily facilitated with the _Pandas_ module as folows:
```python
print(iris_data.describe())
```
This results in the following output:

|     |sepal_length | sepal_width | petal_length | petal_width |
|:---:|:-----------:|:-----------:|:------------:|:-----------:|
|count| 150.000000  | 150.000000  |  150.000000  | 150.000000  |
|mean |   5.843333  |   3.054000  |    3.758667  |   1.198667  |
|std  |   0.828066  |   0.433594  |    1.764420  |   0.763161  |
|min  |   4.300000  |   2.000000  |    1.000000  |   0.100000  |
|25%  |   5.100000  |   2.800000  |    1.600000  |   0.300000  |
|50%  |   5.800000  |   3.000000  |    4.350000  |   1.300000  |
|75%  |   6.400000  |   3.300000  |    5.100000  |   1.800000  |
|max  |   7.900000  |   4.400000  |    6.900000  |   2.500000  |

As can be seen from the table above, the data is described in terms of mean, standard deviation, min, 1st Quartile (25th percentile), median (50th percentile), 3rd Quartile (75th percentile) & max for each column of data across all three Iris species classes, which have 50 observations in each giving a total count of 150 observations.

It is also possible to isolate each class data to be described separately if required as follows:
```python
setosa = iris_data["iris_class"] == "Iris-setosa"

print(iris_data[setosa].describe())
```
The variable setosa is _True_ for all Iris-setosa class and is used subsequently to describe only that class resulting in the following output:
<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

**Iris-setosa**

|     |sepal_length | sepal_width | petal_length | petal_width |
|:---:|:-----------:|:-----------:|:------------:|:-----------:|
|count|   50.00000  |  50.000000  |   50.000000  |   50.00000  |
|mean |    5.00600  |   3.418000  |    1.464000  |    0.24400  |
|std  |    0.35249  |   0.381024  |    0.173511  |    0.10721  |
|min  |    4.30000  |   2.300000  |    1.000000  |    0.10000  |
|25%  |    4.80000  |   3.125000  |    1.400000  |    0.20000  |
|50%  |    5.00000  |   3.400000  |    1.500000  |    0.20000  |
|75%  |    5.20000  |   3.675000  |    1.575000  |    0.30000  |
|max  |    5.80000  |   4.400000  |    1.900000  |    0.60000  |

The same method can be used to describe the other two species classes:

**Iris-versicolor**

|     |sepal_length | sepal_width | petal_length | petal_width |
|:---:|:-----------:|:-----------:|:------------:|:-----------:|
|count|  50.000000  |  50.000000  |   50.000000  |  50.000000  |
|mean |   5.936000  |   2.770000  |    4.260000  |   1.326000  |
|std  |   0.516171  |   0.313798  |    0.469911  |   0.197753  |
|min  |   4.900000  |   2.000000  |    3.000000  |   1.000000  |
|25%  |   5.600000  |   2.525000  |    4.000000  |   1.200000  |
|50%  |   5.900000  |   2.800000  |    4.350000  |   1.300000  |
|75%  |   6.300000  |   3.000000  |    4.600000  |   1.500000  |
|max  |   7.000000  |   3.400000  |    5.100000  |   1.800000  |

**Iris-virginica**

|     |sepal_length | sepal_width | petal_length | petal_width |
|:---:|:-----------:|:-----------:|:------------:|:-----------:|
|count|   50.00000  |  50.000000  |   50.000000  |   50.00000  |
|mean |    6.58800  |   2.974000  |    5.552000  |    2.02600  |
|std  |    0.63588  |   0.322497  |    0.551895  |    0.27465  |
|min  |    4.90000  |   2.200000  |    4.500000  |    1.40000  |
|25%  |    6.22500  |   2.800000  |    5.100000  |    1.80000  |
|50%  |    6.50000  |   3.000000  |    5.550000  |    2.00000  |
|75%  |    6.90000  |   3.175000  |    5.875000  |    2.30000  |
|max  |    7.90000  |   3.800000  |    6.900000  |    2.50000  |

While numerical statistical descriptions are useful in getting an initial summarisation of the data, it may be easier to make an assesment of the data by displaying it visually in plot format. 

#### Data Visualisation
##### Box Plot
The box plot is a visual representation of five numbers which we outputted in the data description above namely; minimum, first quartile, median, third quartile, and maximum as shown in the image below[[5]](#references). The central rectangle spans from the first quartile to the third quartile. This region is known as the interquartile range (IQR). The median is shown in the IQR and the plot "whiskers" show the maximum and minimum locations[[5]](#references).

<p align="center">
  <img src="../master/images/box_plot_description.png" >
</p>

The box plot of the Iris data set is shown below and is easily generated with the following code:
```python
# Box plot of the data set - saved to the images folder in the
# project repo for inclusion in the readme via an image link

bp = iris_data.boxplot(column=['sepal_length', 'sepal_width',
                               'petal_length', 'petal_width'], figsize=(10, 8))
plt.title('Box Plot of Sepal Length, Sepal Width, Petal Length & Petal Width of Iris Data Set')
plt.ylabel('Centimetres')
plt.savefig('./images/box_plot.png', bbox_inches='tight')
```

The plot Title and Y Axis label are easily added using the _matplotlib.pyplot_ methods _title_ and _ylabel_. 

<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

The box plot, when compared to the numbers in the table above for the description, is as expected as the numbers correspond to the diagram:  

![alt text](../master/images/box_plot.png "Iris Data Set - Box Plot")

This visual representation doesn't give us much more information apart from the outliers shown in the Sepal Width box plot as unfilled circles above and below the max and min whiskers. Given their proximity to the whiskers these can be described as suspected outliers and may deserve further consideration. With this in mind our next visual analysis should be a closer look at the Iris species. The box plot can be grouped by the species class as follows:

```python
# Box plot of the different species by grouping by Iris class
bps = iris_data.boxplot(by='iris_class', figsize=(10, 8))
plt.savefig('./images/box_plot_by_class.png', bbox_inches='tight')
```

![alt text](../master/images/box_plot_by_class.png "Iris Data Set - Box Plot by Iris Class")

This plot shows us that there are more suspected outliers in the Iris-setosa class in both petal length and width, with one suspected outlier in the Iris-versicolor class for petal length. The Iris-virginica class is also showing a couple of outliers for both sepal length and width. The shapes of the box plots are also interesting in that they are similar and closer together between the Iris Versicolor and Virginica classes suggesting more simiiilarities between these two species of Iris. Further information about the data can be found from histogram plots. 

##### Histogram Plot

A histogram is a type of bar chart that displays the frequencies of a data set. It plots the frequency on the vertical axis with the variable being measured on the horixontal axis. Again, the plot is easily generated using Python:

```python
# Histogram plot of the data set - saved to the images folder in the
# project repo for inclusion in the readme via an image link

hist = iris_data.hist(column=['sepal_length', 'sepal_width',
                               'petal_length', 'petal_width'], figsize=(10, 8))
# plt.title('Histogram Plot of Sepal Length, Sepal Width, Petal Length & Petal Width of Iris Data Set')
plt.suptitle('Histogram Plot of Sepal Length, Sepal Width, Petal Length & Petal Width of Iris Data Set')
plt.text(-0.7, -8, 'Centimetres')
plt.text(2.8, -8, 'Centimetres')
plt.text(-2, 75, 'Frequency', rotation='vertical')
plt.text(-2, 25, 'Frequency', rotation='vertical')
plt.savefig('./images/histogram_plot.png', bbox_inches='tight')
```

This time the plot and axis titles are defined using the _suptitle_ & _text_ methods.

![alt text](../master/images/histogram_plot.png "Iris Data Set - Histogram Plot")

<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

An examination of the histogram plots show that the data has multiple peaks which indicates that there are outliers in the data and also seperate groupings within this data so it is worth looking at additional plots such as scatters.

##### Scatter Plot

The _Pandas_ Scatter plot allows each of the columns in the data frame to be plotted against each other. The code to generate this plot is as follows:

```python
from pandas.plotting import scatter_matrix

scatter_matrix(iris_data, figsize=(10, 8))
plt.suptitle('Scatter Plot of Sepal Length, Sepal Width, Petal Length & Petal Width of Iris Data Set')
plt.savefig('./images/scatter_plot.png', bbox_inches='tight')
```

![alt text](../master/images/scatter_plot.png "Iris Data Set - Scatter Plot")

It is not very clear from the similar colour of the two columns plotted against each other in the above plot so the [_Seaborn_](https://seaborn.pydata.org/) statistical visualisation library provides an easier method to generate a more descernable plot:

<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

```python
import seaborn as sbn

pp = sbn.pairplot(iris_data, kind='scatter', hue='iris_class')
plt.suptitle('Scatter Plot of Sepal Length, Sepal Width, Petal Length & Petal Width of Iris Data Set')
plt.savefig('./images/hue_scatter_plot.png')
```

![alt text](../master/images/hue_scatter_plot.png "Iris Data Set - Scatter Plot")

Each Iris class is clearly defined by colour and as before there is strong similarities shown between the two species Iris-versicolor and Iris-virgiinica as evidenced by the close grouping of both across a combination of petal length/width vs sepal length/width variables while the Iris-setosa species is clearly distinct and grouped on its own across all feature pairings. 

---
### Conclusions
<p align="right">
  <a href="https://github.com/geromahony/da2018-prog-script-project#table-of-contents">[Go to Top]</a>
</p>

The analysis caried out on the Iris data set in this project generated descriptive statistical properties of mean, standard deviation, min, 1st Quartile (25th percentile), median (50th percentile), 3rd Quartile (75th percentile) & max for the data set and the species subsets also. A more indept analysis using various statistical visualisations such as box plots, histograms and scatter plots has shown various aspects of the data such as outliers and correlerations between the two Iris species Versicolor and Virgiinica. It has also shown a distiinction between the third Iris species Setosa and the previous two.

It is clear that data analysis is easily facilitated in the [_Python_](https://www.python.org/) programming language with the availability of data processing and visualisation libraries such as [_Numpy_](http://www.numpy.org/), [_Pandas_](http://pandas.pydata.org/), [_Matplotlib_](https://matplotlib.org/) & [_Seaborn_](https://seaborn.pydata.org/) which were used in this analysis. There are numerious other open source libraries such as[[6]](#references):

 * [_Bokeh_](https://bokeh.pydata.org/en/latest/) <br>Which is used for creating interactive plots, dashboards and data applications on modern web-browsers.
 * [_Blaze_](http://blaze.pydata.org/) <br>Which is used for extending the capability of Numpy and Pandas to distributed and streaming datasets. 
 * [_Requests_](http://docs.python-requests.org/en/master/) <br>Which is a web access library.
 * [_SciPy_](https://www.scipy.org/) <br>Which stands for scientific Python and is a useful library for variety of high level science and engineering modules like discrete Fourier transform, Linear Algebra, Optimization and Sparse matrices.
 * [_Scikit Learn_](http://scikit-learn.org/stable/) <br>Which is a maachine learning library.
 * [_Statsmodels_](https://www.statsmodels.org/stable/index.html) <br>Which is used for statistical modeling.
 * [_Scrapy_](https://scrapy.org/) <br>Which is a web crawling framework. 
 * [_SymPy_](http://www.sympy.org/en/index.html) <br>Which is used for symbolic mathematical computations.

 The availablity of these languages make Python the language of choice for data analysis today.

 
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

[5] Kirkman, T.W. (1996) Statistics to Use.
	http://www.physics.csbsju.edu/stats/ Retrieved April 29th 2018

[6] Analytics Vidhya.
	https://www.analyticsvidhya.com/ Retrieved April 29th 2018

---