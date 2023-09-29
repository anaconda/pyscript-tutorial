## Your browser is your most ubiquitous computing platform

Python is nowadays the most popular programming language, according to the
[TIOBE](https://www.tiobe.com/tiobe-index/) and the
[PYPL](https://pypl.github.io/PYPL.html) programming community indices, 
and the data science domain is where Python finds its broader adoption.

Web browsers, on the other hand, are the most ubiquitous software.
Any computer, smartphone, or device with internet access integrates
a web browser.

Therefore, having the possibility to leverage on the full scale of Python 
computing capabilities, along with its huge ecosystem of packages, directly in the browser, 
would potentially open up to completely new scenarios.

At the very core of Python's number crunching abilities lies [NumPy](https://numpy.org).

In this chapter, we will explore whether and how it could be possible to 
`import numpy as np` in the browser.

> 💡 Why importing Numpy would be a game changer ?
>
> Being able to import NumPy in our PyScript app would be extremely important mainly
> for two reasons. From a mere programmatic and technical perspective, this would
> open up to the possibility of _importing_ "external" packages in our Python code
> running in the browser. By "external" we refer to any generic package that
> is **not** part of the Python Standard library.
> Secondly, if we would be able to bring NumPy in the browser,
> we would immediately unlock unprecedented (numerical) capabilities for the web environment,
> e.g. _operator overloading_, _typed multidimensional arrays_ (i.e. `NDArray`), _threads_,
> [`SIMD`](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data).


**NOTE for future-self & reviewer: Missing reference here, in case remove//add later**
> If you are interested in learning more about how PyScript can be used to develop
> rich web apps for Data Science and Machine Learning, please read module `XXX`


### ⏳ Get Ready



Let's start by creating a simple HTML page template, similarly to what we did 
in the [Get Ready](../01_python_in_the_browser/python_in_the_browser.md#⏳-get-ready)
section of our first PyScript app.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PyScript meets NumPy</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://pyscript.net/snapshots/2023.09.1.RC1/core.css" />
        <script type="module" src="https://pyscript.net/snapshots/2023.09.1.RC1/core.js"></script>
    </head>
    <body>
        <script type="py">
            # Add your code here
        </script>
    </body>
</html>
```

Let's save this template as a **new** file, named `pyscript_meets_numpy.html`.

> 💡 In addition to the PyScript core module, this time we will also import the PyScript CSS 
> (i.e. Cascading Stylesheet),
> namely `core.css`. This asset defines the display rules of custom PyScript components.

### 🧑‍💻 Hands on: Importing NumPy

First thing, let's write some Python code that uses NumPy, and what a better example than the
[_first one_](https://numpy.org/doc/stable/user/quickstart.html#an-example) gathered from the
official NumPy [documentation](https://numpy.org/doc/stable)?

```python
# Adapted from https://numpy.org/doc/stable/user/quickstart.html#an-example
from pyscript import display

import numpy as np

a = np.arange(15).reshape(3, 5)
display(f"NDArray a: \n{a}")
# Expected:
# array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14]])
display(f"a.shape: {a.shape}")
# Expected:
# (3, 5)
display(f"a.ndim: {a.ndim}")
# Expected: 2
display(f"a.dtype.name: {a.dtype.name}")
# Expected: 'int64'
display(f"type(a): {type(a)}")
# Expected <class 'numpy.ndarray'>
b = np.array([6, 7, 8])
display(f"b: {b}")
# Expected: array([6, 7, 8])
display(f"type(b): {type(b)}")
# Expected: <class 'numpy.ndarray'>
```

> 🧑‍💻 Let's now write the code from the snippet above within the `<script type="py">` tag
> in the `pyscript_meets_numpy.html` file.
>
> **Note**: If you are not super familiar with NumPy syntax, I would strongly encourage you
> to take your time to write that snippet of code one line at a time (as opposed to a quick and blunt 
> Copy&Paste).
> In this way, you would get the opportunity to also _read_ the code, while also familiarizing with
> NumPy's API.

The above code snippet is simply trying to allocate two `numpy.ndarray`
[objects](https://github.com/leriomaggio/python-data-science/blob/main/numpy/images/ndarray.png),
and display some of their properties (e.g. `shape`, `ndim`).

If we now save the file again, and we try to open in the browser like we did before...💥

You should get the Python [Traceback](https://docs.python.org/3/library/traceback.html) as the one
reported below:

```bash
Traceback (most recent call last):
  File "/lib/python311.zip/_pyodide/_base.py", line 468, in eval_code
    .run(globals, locals)
     ^^^^^^^^^^^^^^^^^^^^
  File "/lib/python311.zip/_pyodide/_base.py", line 310, in run
    coroutine = eval(self.code, globals, locals)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<exec>", line 5, in <module>
ModuleNotFoundError: The module 'numpy' is included in the Pyodide distribution, but it is not installed.
You can install it by calling:
  await micropip.install("numpy") in Python, or
  await pyodide.loadPackage("numpy") in JavaScript
See https://pyodide.org/en/stable/usage/loading-packages.html for more details.
```

First thing to highlight from this example: **Error Handling**.

PyScript is giving direct access to the Python traceback in the browser.
This is indeed a huge deal, as clear _error reporting_ is a crucial part in coding. 
This also perfectly ties with the
major improvements in error handling introduced in Python 3.11 
(See [PEP657](https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-pep657)).

The most relevant part of the traceback is contained in the last five lines:

```bash
ModuleNotFoundError: The module 'numpy' is included in the Pyodide distribution, but it is not installed.
You can install it by calling:
  await micropip.install("numpy") in Python, or
  await pyodide.loadPackage("numpy") in JavaScript
See https://pyodide.org/en/stable/usage/loading-packages.html for more details.
```

PyScript (and then of course, Pyodide) is reporting (line `1`) that our code is trying to import a `numpy` module that
cannot be found because (A) it is not part of the Pyodide distribution
(i.e. the _Python Standard library on WASM_, ed.), and (B) it is **not installed**!
It then continues (Lines `3-5`) showing how to _install_ a package using Pyodide APIs.

The first important take-away message is that only the Python Standard Library
is available by default, when using PyScript/Pyodide.
To use any other package, one would need to load them separately.

Luckily, Pyodide supports the installation of external packages using
[`micropip`](https://micropip.pyodide.org/en/v0.2.2/project/usage.html#installing-packages-with-micropip),
and PyScript has direct
[integration](https://micropip.pyodide.org/en/v0.2.2/project/micropip-in-other-projects.html#pyscript) with `micropip`.

In fact, PyScript provides a special `<py-config>` tag that is specifically designed to configure your PyScript app.
One thing you can do with the `<py-config>` tag is to declare package dependencies.

To declare the dependencies in our PyScript app we would just need to include the `packages` directive within the 
new `<py-config>` tag:

```html
<py-config>
  packages = ["numpy"]
</py-config>
```

> 💡 Similarly to the `<script type="py">` tag, also the `<py-config>` tag supports loading
> the configuration directives from external resources, via `src`.
> Configuration files can use either [TOML](https://learnxinyminutes.com/docs/toml/) or
> [JSON](https://www.freecodecamp.org/news/what-is-json-a-json-file-example/) syntax.
> The TOML format is the default, and we will be using this throughout the course, as it is
> (a) less verbose than JSON; (b) more intuitive and easier to write; (c) it is the same
> format used to specify 
> [packages metadata](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) 
> (i.e. `pyproject.toml`).

Let's add the `<py-config>` reported above to our `pyscript_meets_numpy.html` file right after the `<body>` tag, and save it.

> ✅ This example is now complete! Let's open the `pyscript_meets_numpy.html` local file in the browser.

<a name="2_output"></a>

Now everything should be working as expected! 🎉
You should be able to see the output of the code on your page thanks to the use of the `display` function:

```
NDArray a:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
a.shape: (3, 5)
a.ndim: 2
a.dtype.name: int32
type(a): <class 'numpy.ndarray'>
b: [6 7 8]
type(b): <class 'numpy.ndarray'>
```

### ⚙️ How it works: 📦 Pyodide Packaging, Micropip, and WASM

As briefly mentioned, the `<py-config>` tag can be used to declare the
dependencies for our PyScript app.
This tag directly maps to the underlying Pyodide mechanism to install external packages, namely `micropip`.

At this point, you should be wondering if _any_ package in the Python ecosystem could be imported
in the browser. If that was really the case: well done indeed! 👏
That is a genuine good question at this point!

The short answer to that question though is: _Not quite!_.

Please remember that the last layer in our reference multi-layered architecture we introduced in
[Exercise 1](#⚙️-13-how-it-works) is WASM, which is the ultimate target of our computation.
And from a Python-packaging perspective, WASM would be no different than other target compile
architectures, e.g. `x86` vs `arm`.

> 💡 The key focus here is on the **instruction set**, and not on any specific hardware
> architecture, despite the two concepts sometimes tend to be paired together, and so
> confused as the same thing (e.g. `arm` instruction set maps to ARM/ARM-based processors).

However, **not all Python packages** require a target architecture. This is only the case
of packages with external C dependencies
(i.e. part of their code base include external C/C++ libraries).

**Pure Python packages** on the other hand can run on every CPU architecture/instruction set
(i.e. [`none-any`](https://packaging.python.org/en/latest/specifications/binary-distribution-format/?highlight=%22none-any%22#installing-a-wheel-distribution-1-0-py32-none-any-whl)), and therefore 
they can also run on WASM!!

So, we are indeed capable of _loading_ **any** pure Python package in our PyScript application!

> 💡 There's more!
> In the `packages` directive in `<py-config>` we can either specify the name of a package,
> or include directly the URL of the Python wheel we want to install.
> If a name is specified, the underlying Pyodide/micropip will be automatically searching for
> the package name on PyPi and download it!

And what about non-pure Python packages?
Moreover, **the majority** of Python packages for numerical and scientific computing have external
C-dependencies to boost the performance, `numpy` included!!How did that work?

The good news is that `Pyodide` has a very _long_ [list of packages](https://pyodide.org/en/0.23.2/usage/packages-in-pyodide.html) already included in the distribution which have been already
compiled for the `WASM32` target!.
This list includes a lot of the _most popular_ Packages in the PyData stack, like `scipy`, `pandas`,
`scikit-image`, `scikit-learn`, `matplotlib`.

So what _really_ happened when we included the `packages = ["numpy"]` in our `<py-config>` specification,
was that underneath Pyodide was **loading** the pre-built `numpy` package included in the distribution.

> 🎮 In order to understand better what is actually happening under the hood, let's try to _refresh_ the page, 
> and look at the messages in the JavaScript console. 
>
> The relevant (`log`) messages you should be seeing in the console are:
>
```bash
[pyscript/pyodide] importing pyscript
[pyscript/pyodide] Found packages in configuration to install. Loading micropip...
[pyscript/pyodide] pyodide.loadPackage: micropip
[pyscript/pyodide] Loading micropip, packaging
[pyscript/pyodide] Loaded packaging, micropip
[pyscript/pyodide] pyodide loaded and initialized
[pyscript/main] Python ready!
[pyscript/main] Setting up virtual environment...
[pyscript/main] Packages to install:  ['numpy']
[pyscript/main] Fetching urls:
[pyscript/pyodide] micropip install numpy
[pyscript/main] Fetched all paths
[pyodide.asm.js:9] Loading numpy
[pyodide.asm.js:9] Loaded numpy
```

### 🎁 Wrap up

We explored how it is possible to include external (Python)
dependencies into our PyScript application. In particular, we learnt how to
`import numpy as np` in our code.

Importing NumPy is the first (and very important) step towards being able to
create Python data apps directly in the browser.

To do so, we introduced the new `<py-config>` tag that PyScript provides, along
with the corresponding `packages = [...]` directives to include packages.

### 🥡 Take away lessons

- PyScript allows the declaration of dependencies via the `<py-config>` special tag.
- The `<py-config>` tag directly integrates with `micropip.install` module of Pyodide to
install external dependencies.
- Any pure Python package can be _installed_ and used in the browser.
- Python packages with external C-dependencies (e.g. `numpy`) can only be used if there exist corresponding
Python wheels packages targeting the `wasm32` instruction set.
- Pyodide includes a very long list of [supported packages](https://pyodide.org/en/stable/usage/packages-in-pyodide.html), 
built-in within the Python distribution.
- This list of Pyodide packages includes the majority of the most popular Python packages in the scientific stack.>
