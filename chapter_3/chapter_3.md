# Chapter 3 - Interactive Machine Learning

In this chapter, we will explore how PyScript allows to easily create interactive
Machine Learning (`ML`) applications in the browser.

Similarly to what we have been doing in the previous two chapters, we will be starting from a basic PyScript
[template](/chapter_3/template.html) that we will incrementally modify as long as we will work on our exercises.
The template is indeed very simple as it only includes [`scikit-learn`](https://scikit-learn.org/stable/) in the
list of packages specified in the `<py-config>` directive.

## Before we start

Before moving on to our exercises, it is important to clarify what are the prerequisites (i.e. _things that 
you need to know_) for this chapter. There is _None_, really! 😄

We will be using `scikit-learn` for our machine learning code, along with
[`numpy`](https://numpy.org/) and [`pandas`](https://pandas.pydata.org/) to load and process the data.

Threfore, if you are already familiar with `scikit-learn`, and you have a general understanding of how machine
learning works, that is certainly a **big plus**. However each exercise will include enough explanations to get a
general understanding of what we are working on. Moreover, references to external resources will be also reported
(_whenever necessary_, ed.) to expand more on specific subjects.

In addition, we will also be focusing on combining the interactivity of Javascript with Python machine learning
code running in the browser. _It is indeed one of the super powers that `PyScript` provides_ 🦸.
Therefore I will assume that you are already familiar with HTML, Javascript, and the
[DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).
The exercises in [Chapter 2](/chapter2) could be a fantastic refresher, or something to get started with.


## Preamble: Every ML journey starts with the data 🍷

> Every journey in machine learning starts with the data!

Indeed data in machine learning have a very crucial role: they represent the foundation of our learning strategy!
We are planning to program our algorithms (i.e. ML models) to learn from this data, so data normally requires a lot
processing and [_preparation_](https://developers.google.com/machine-learning/data-prep) before any ML model could
be effectively used.

For the exercises included in this chapter we will be playing with the
[**Wine data set**](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data)
as included in `scikit-learn`:
[`sklearn.datasets.load_wine`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html).

In more details: ([Source](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-dataset))

> The [Wine] data(set) is the results of a chemical analysis of wines grown in the same region in Italy
> by three different cultivators.
> There are thirteen different measurements taken for different constituents found in the three types of wine.
>
> Original Owners:
> Forina, M. et al, PARVUS - An Extendible Package for Data Exploration, Classification and Correlation. Institute of Pharmaceutical and Food Analysis and Technologies, Via Brigata Salerno, 16147 Genoa, Italy.

From a machine learning perspective, we are aiming at building a system that can automatically classify
(in a [_supervised learning_](https://en.wikipedia.org/wiki/Supervised_learning) fashion) the three types of wines
based on the results of the `13` chemical analysis included in the data set.

As it is customary in machine learning, in the chapter we will refer to our data by the matrix $X$
(_also know as the **feature matrix**_, ed.) of size $[178 \times 13]$, samples $\times$ features;
while the list of target classes of each sample is represented by the vector $y$, having $178$ 
entries in in our data).

Using this data set brings many advantages. (1) We don't need to worry about preparing the data: all
[`data sets`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets) in
`scikit-learn` are ready-to-use, with clear distinction between _features_ and _targets_.
(2) It is fairly _small_ (i.e. `178` samples and `13` features), so it is easy to load, and to manipulate
in the browser. (3) It is _simple but not easy_: the data set has a few subtleties that make it an interesting
use case from a machine learning perspective.

---
**to review / check if to keep**

In simpler terms, we are hoping to automatically create a function `sommelier(x)` that
would receive a vector `x` of `13` measurements (i.e. the _features_), and would return in output the _label_ $y$
of the corresponding wine type, i.e. `class_0`, `class_1`, or `class_2` as referred in the data set.
To do so, we would need to _train_ our algorithm by providing several examples of `x`s, along with the
corresponding and the expected $y$s (i.e. the type of wines).

Exercise **XX** will be specifically devoted to create our _classifier function_.

---


## Exercise 1 - A first look data

In this first exercise, we will begin with a simple use case: _investigating the class distribution in our data,
and the correlation between the `13` features_.

> ✋ **Before proceeding**: let's create a copy of our `template.html`, and rename it as
> `1_data_distribution.html`. In the new file, let's also change the text within the `<title>`
> tag accordingly:
> ```html
> <title>Wine dataset: A first look at the data</title>
> ```

The number of samples in the data that belong to each class is generally referred to as the
[class distribution](https://en.wikipedia.org/wiki/Multiclass_classification).
If samples in each classes are not equally distributed, we say that the data set is
[imbalanced](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data).
Analysing the class distribution in the data is always very important, as this may affect the performance of
machine learning models. if no further counter-measure is considered.

To calculate class distribution it would just be necessary to count the number of occurrences of each value in the
vector $y$ of targets. To do that, we can use the
[`bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html) function included in Numpy.

We will visualize our class distribution as a
[bar plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html) using the
[Matplotlib](https://matplotlib.org/stable/index.html) library.

> 💡 Please have a look at Chapter 2 for more examples of PyScript and Data Visualization.

First, we need to add both Numpy, and Matplotlib to our list of Python dependencies in `<py-config>`.

```html
<py-config>
  packages = ["scikit-learn", "numpy", "matplotlib"]
</py-config>
```

Then, we will create a new `<div>` element where we are aiming to display the class distribution bar plot.
In order to uniquely identify this element, we could set the `id="class_distribution"` attribute:

```html
<div id="class_distribution"></div>
```
We can place this element anywhere within the `<body>` tag, e.g. right after the `<py-script>` tag.

Now, it's time to write some Python code. First, we need to import the `wine` dataset from `scikit-learn`,
and extract the array of targets `y`. We can use the array `y` as input to the `np.bincount` function:

```python

import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine()
y = wine.target
class_count = np.bincount(y)
```

Now, we need to create our class distribution barplot for the Wine data set.
We can use the `target_names` attribute
included in the `wine` data object to gather the name of each class, and use them as labels
on the $x$-axis.

We will be using colors picked from the
[`plt.cm.PiYG`](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
(_it's going to be wines, after all_. ed.), and we will annotate each bar in the plot
with the total number of counts
(using [`axis.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html)).

The plot will be written into the target `<div>` element using the PyScript
[`display`](https://docs.pyscript.net/2022.12.1/reference/API/display.html) function.

```python
shades_of_red = plt.cm.PuRd(np.linspace(0.5, 0.7, len(class_count)))
fig, ax = plt.subplots(figsize=(5, 5))

plt.title("Wine Dataset: class distribution")
bars = plt.bar(wine.target_names, class_count, color=shades_of_red)
plt.ylim([0, max(class_count) + 5])

# Loop through the bars and add annotations
for bar in bars:
  height = bar.get_height()
  ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
              xytext=(0, 1), textcoords="offset points", ha='center', va='bottom')
display(fig, target="class_distribution")
```

The second part of this exercise requires to analyse the correlation between the `13` features.
In other words, what we want to consider each pair of features, and visualize in a scatter plot how much
the values of one variable affect the other, with respect to the multiple classes.

We can use the
[`scatter_matrix`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html)
function available in `pandas.plotting` to automatically generate the plots for all the `78`
(i.e. `13` $\times$ `12`) feature combinations.

To do so, we would need to add `pandas` to our list of dependecies:

```html
<py-config>
  packages = ["scikit-learn", "numpy", "matplotlib", "pandas"]
</py-config>
```

Similarly, we can create a new placeholder `<div>` element to host the scatter matrix plot generated.

```html
<div id="scatter_matrix"></div>
```

To load the feature matrix `X` as `pandas.DataFrame` (_instead of the default `numpy.ndarray`_, ed.)
we can use the `as_frame=True` parameter of the
[`load_wine`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)
function. Similarly, the `return_X_y=True` parameter guarantees that the `load_wine` function will only return
the `(features, targets)` tuple, with no additional metadata.

Let's write the following Python code within a new `<py-script>` tag:

```python
from pandas.plotting import scatter_matrix

X, _ = load_wine(as_frame=True, return_X_y=True)

n_features = X.shape[1]
fig, ax = plt.subplots(n_features, n_features, figsize=(12, 12))
_ = scatter_matrix(X, ax=ax, c=y, cmap=plt.cm.PiYG)
display(fig, target="scatter_matrix")
```

## Exercise 2 - Interactive feature exploration

In the first exercise, we have explored class distribution, and feature correlation in our dataset.
In particular, with just a few lines of Python code, we have gathered simple statistics on our data,
and visualised them directly in the browser thanks to PyScript.

> 💡 We have indeed done more than that! We have actually moved into the browser the **same** lines of code
> we would have written into a normal Python module, or an interactive Jupyter notebook to perform the same task!
> In other words, we did not have to change our (pre-existing?) Python code to adjust to the new computational
> environment (i.e. _the browser_, ed.)

In particular, we leveraged on the `pandas.plotting.scatter_matrix` function to automatically generate all the
combinations of features, and visualize all the corresponding scatter plots into a single _big_ picture.
That was indeed very easy to achieve, but admittedly, it wasn't that useful.

This time we will try to come up with a solution that would exploit the fact that we are performing our
analyses in the browser, where _things are supposed to be interactive_
(_and **this** is when PyScript starts to shine!_, ed.).

So, here is the plan: instead of generating a single picture with all the correlations at once, we will
replace it with two dropdown menus where we could select the two features we want to look at.
As soon as we make a selection, a new **scatter plot** will be generated, showing the two selected variables.

> ✋ **Before proceeding**: let's create a copy of our `template.html`, and rename it as
> `2_interactive_feature_exploration.html`. In the new file, let's also change the text within the `<title>`
> tag accordingly:
> ```html
> <title>Wine dataset: Interactive Feature Exploration</title>
> ```

To make things more fun

**NOTE**: The text needs to be completed, but the final solution in the template is done!
It is possible to open it in the browser to see where we're going with this exercise.


## Exercise 3 - 

