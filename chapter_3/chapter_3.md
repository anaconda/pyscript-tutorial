# Chapter 3 - Interactive Machine Learning Apps with PyScript

In this chapter, we will explore how PyScript enables the creation of interactive
Machine Learning (`ML`) applications in the browser.

## Before we start

Before starting to dive into our exercises, let's clarify what are the prerequisites for this chapter.
In other words, what are _the things that you need to know already_, or more precisely,
_what I will be assuming you know already_.

Well, the good bit here is that _no specific prior knowledge about machine learning_ is necessary
to work on the exercises. 😊

Each exercise will include enough explanations to understand
what we are working on, along with references to external resources
(_whenever necessary_, ed.) to further expand on specific topics.
If you already have a general understanding of how machine learning works, that would be more than enough to get started.

We will be using `scikit-learn` for our machine learning code, along with
[`numpy`](https://numpy.org/) and [`pandas`](https://pandas.pydata.org/) to load and process the data.
Threfore, if you are already familiar with those packages it will be a **big plus**.

The more we will dive into the multiple exercises in this chapter, the more we will be focusing on combining the interactivity
of Javascript with Python machine learning code running in the browser.

> 💡 _This  is indeed one of the super powers that `PyScript` provides_ 🦸.

Therefore I would assume that you are already familiar with how **PyScript** works, and with HTML, Javascript,
and the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).

If that would not be the case, I would highly recommend going through the exercises included in [Chapter 1](/chapter_1/)
prior working on this chapter. Those could be a fantastic refresher, and/or a great way to get started with PyScript and HTML/DOM.
Moreover, in [Chapter 2](/chapter2) you could also find examples of PyScript applications for Data Visualization.

## Getting Started

Similarly to what we have been doing in other chapters, we will be starting from a basic PyScript
[template](/chapter_3/template.html) that we will incrementally modify as long as we work on our exercises.
The template is indeed very simple, and it just includes [`scikit-learn`](https://scikit-learn.org/stable/) in the
list of the required packages in the `<py-config>` directive.
It also uses a specific **runtime** (see [`runtime.toml`](./runtime.toml)) that imports the latest major release
of [Pyodide]https://blog.pyodide.org/posts/0.23-release/)

> 🔎 **Notes for Visual Studio Code**
> If you are using Visual Studio Code (VSCode) as your editor of choice to work on the exercises, this tutorial
> includes a quick and easy way to create your templates. Just type `ml-template` into an **empty**
> HTML file, and the whole template will be automatically generated for you in a second.
> The template will also includes `placeholders` to quickly customize your new template by filling into
> the necessary fields (e.g. title, packages, external modules, and so on).
> You can use the `tab` key on your keyboard to jump from one placeholder to another.

The default templates also includes a section in `<py-config>` to include external Python modules (i.e. `[[fetches]]`).

We will be using external Python modules to write our machine learning code to be included in our PyScript
apps as external dependencies. There are many advantages for doing so:
(1) separate modules favour a better [_separation of concerns_](https://en.wikipedia.org/wiki/Separation_of_concerns),
leading to a better software design that would be easier to maintain and evlove. (2) It will be easier to re-use code
through multiple exercises without any _copy & paste_ nor [duplicate](https://en.wikipedia.org/wiki/Duplicate_code).
code. (3) Last but not least, writing Python code in `.py` files is a way better development experience than
writing Python snippets into HTML fragments (_regardless of the level of support you would get from your code editor_, ed.).

Therefore, we will be following these _rule of thumb_ to decide where to write our code for the exercises:

1. Any "pure" (machine learning) Python code that does not require any interaction with the Javascript or the DOM, will
be written into reusable **external Python modules**, added to the app as a dependency via the `<py-config>` tag.

2. All the PyScript-specific python code of our apps will be written directly within the `<py-script>` tag **only if**
that is limited to a few [LOC](https://en.wikipedia.org/wiki/Source_lines_of_code)s.

    2.1 Otherwise, the code will be written into a **separate** Python module, referenced in the
  `<py-script>` tag by the `src` attribute:
  ```html
  <py-script src="exercise_code.py"></py-script>
  ```

## Preamble: Every ML journey starts with the data 🍷

> Every journey in machine learning starts with the data!

Indeed **data** in machine learning have a very crucial role: they represent the foundation of our learning strategy!
We are planning to program our algorithms (i.e. ML models) to learn from the data, which would normally require a lot
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

As it is customary in machine learning, in the chapter we will refer to our data as $X$, that is a
two dimensional array (i.e. a [matrix](https://en.wikipedia.org/wiki/Matrix_(mathematics)))
of size $[178 \times 13]$.
The first dimension corresponds to the total number of _samples_ (`178`), while the second dimension
refers to the number of _features_, i.e. the `13` chemical analysis collected from all the `178` samples
in the dataset.

The list of the target class (i.e. _type of wine_, ed.) for each sample is represented by the vector $y$
of size $178$.

Using this data set has many advantages.

(1) We don't need to worry about preparing the data: all
[`data sets`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets) in
`scikit-learn` are ready-to-use, with clear distinction between _features_ and _targets_.

(2) The whole dataset is fairly _small_, both in terms of dimension (i.e. disk space) and of
[dimensionality](https://en.wiktionary.org/wiki/dimensionality).
Therefore this dataset will be easy to load in memory, and to manipulate in the browser environment.

(3) Nonetheless working with this dataset will be _simple but not trivial_: the data contains a few
subtleties that will make it an interesting use case from a machine learning perspective.

---
*NOTE: KEEP FOR NOW - to be moved into the exercise working on the actual classifier**

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

> ✋ **Before proceeding**: let's create a new file called `1_data_distribution.html`.
> You could either copy `template.html`, and simply rename it or, if you're using VSCode,
> just type `ml-template` and the template will automatically appear.
>
> In the new file, let's also change the text within the `<title>`
> tag accordingly:
> ```html
> <title>PyScript ML: A first look at the Wine data set.</title>
> ```
> In VSCode, just hit the `tab` key to move the focus to the next step: python packages.

The number of samples in the data that belong to each class is generally referred to as the
[class distribution](https://en.wikipedia.org/wiki/Multiclass_classification).
If samples in each classes are not equally distributed, we say that the data set is
[imbalanced](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data).

Analysing the class distribution in the data is always very important, as this may affect the performance of
machine learning models, if no further counter-measure is considered.

To calculate class distribution it would just be necessary to count the number of occurrences of each value in the
vector $y$ of targets, for each target/class.
To do that, there is a simple function in `numpy` that we can use:
[`bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html).

Once we have the class counts, we can visualize our class distribution as a
[bar plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html) using the
[Matplotlib](https://matplotlib.org/stable/index.html) library.

> ❗️ Please have a look at Chapter 2 for more examples of PyScript and Data Visualization.

So, the first thing we need to do is to add both `numpy`, and `matplotlib` to our list of Python dependencies in `<py-config>`.

```html
<py-config>
  packages = ["scikit-learn", "numpy", "matplotlib"]
</py-config>
```

Then, we need to work on the code to generate the bar plot of our class distribution. This will presumably be "just" Python code
using `numpy` and `matplotlib`. At this stage, PyScript won't be used until the very end when we will need to add the plot to the
page. Therefore, let's put this function in a separate Python module named `data_distribution.py` to include in our config via
the `fetches` directive.

At this point, your `<py-config>` tag should look like this:
```html
<py-config src="runtime.toml">
    packages = ["scikit-learn", "numpy", "matplotlib"]

    [[fetch]]
    files = ["./data_distribution.py"]
</py-config>
```


will create a new `<div>` element where we are aiming to display the class distribution bar plot.
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

