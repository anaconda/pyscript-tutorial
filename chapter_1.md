# Chapter 1 - Getting Started with PyScript

In this chapter, we will get our bearing with the many features PyScript provides to create
rich web applications using Python in the browser.

Working on the multiple exercises in this chapter will be our opportunity to discover a bit more
about _how_ PyScript works, and _why_ PyScript is so revolutionary for Python and Data Science
applications.

<!-- Before we start, a tip for developing code in PyScript. We will open the html page in the browser often to check the result. If something does not work as expected, we can bring up the JavaScript Console to see the error messages. If you are using Chrome (which is recommended in this tutorial), you can open it via the menu `View > Developer > JavaScript Console` -->

Exercises featured in this Chapter:

1. [Your first lines of Python in the browser are "bigger on the inside"](#exercise-1---your-first-lines-of-python-in-the-browser-are-bigger-on-the-inside)
2. []()

---
## Exercise 1 - Your first lines of Python in the browser are "bigger on the inside".

In this exercise, we will work on the simplest example ever one could
think of to write our _first few_ lines of Python in HTML.

### ⏳ 1.1 Get Ready

To get started with this exercise, we would need a Code Editor of
choice that supports syntax highlighting for HTML
(e.g. Visual Studio Code or Vim).

Let's create a skeleton of a [generic HTML page](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics). 
Feel free to copy and paste the one reported below:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Get Started with PyScript</title>
        <meta charset="utf-8">
        <!-- ADD PyScript Here -->
    </head>
    <body>
        <!-- Add PyScript tag and Python code here -->
    </body>
</html>
```

Let's save this file as `first_pyscript_app.html`.
Let's now move onto writing some Python in this HTML page.

### 🧑‍💻 1.2 Writing your first PyScript App

The first thing we need to do, is to actually integrate PyScript into our HTML page.
We will do so by replacing the first placeholder comment 
(i.e. `<!-- ADD PyScript Here -->`) with the following two lines:

```html
<link rel="stylesheet" href="https://pyscript.net/releases/2023.05.1/pyscript.css" />

<script defer src="https://pyscript.net/releases/2023.05.1/pyscript.js"></script>
```

> 💡 Believe it or not, these are the **only** two lines to enable Python in the browser.
> No installation, and not further configuration is needed to get started!

The first `link` tag is necessary to integrate the PyScript 
[CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) (i.e. Cascading Stylesheet). 
which defines the display rules of certain PyScript components.

The `<script>` tag is finally importing `pyscript.js` which is when the magic finally happens.

Now it's finally time to write _some Python_!

Let's replace the second placeholder comment in the template (i.e. `<!-- Add PyScript tag and Python code here -->`) with
the following code:

```html
<script type="py">
    import sys
    print(f"Running Python {sys.version} in the Browser!")
</script>
```

> ✅ This example is complete! Now let's save the `first_pyscript_app.html` and open the local file into the browser.

If everything works correctly, you should be now looking at a blank page, with a black rectangle positioned
at the bottom of the page reporting the following line:

```
Running Python 3.11.2 (main, May  3 2023, 04:00:05) [Clang 17.0.0 (https://github.com/llvm/llvm-project df82394e7a2d06506718cafa347b in the browser!
```

The first thing to notice is that we are indeed running **Python 3.11.2** in the browser.
So this is neither a "special" nor a "surrogate" version of Python.
It is [_standard_](https://pyodide.org/en/stable/usage/wasm-constraints.html#python-standard-library) Python 3,
running in the browser.

The reason for the black rectangle - which may look strange at first - is because PyScript automatically redirect the 
output of every `print` call into a special element, named `<py-terminal>`.

> 💡 The [`<py-terminal>`](https://docs.pyscript.net/latest/reference/plugins/py-terminal.html#py-terminal) is a special
> _plug-in_, enabled by default in PyScript, that specifically serves the purpose to capture all the output on
> `stderr` and `stdout` so that it does not get lost within the rest of the text the HTML page may contain
> (_not certainly the case in this exercise 😄_, ed.).


> 💡 Also, you may have noticed that the address bar in your browser reports something like
> `file://<path on your local hard drive>/first_pyscript_app.html`.
> This means that the browser is loading an HTML from your local hard drive. In other words, no server is
> required to open the web page.

### ⚙️ 1.3 How it works

PyScript brings into the HTML a new special tag (i.e. `<script type="py">`) that will be interpreted by browser
(and integrated into the [`DOM`](https://developer.mozilla.org/en-US/docs/Glossary/DOM)) as a special
HTML tag where Python code will be expected.

And indeed there is some Python code, and we have already discussed that's pure Python 3 that one would
normally write into a general app running on your computer. So _how_ does that work really ?

![PyScript General Architecture](https://anaconda.cloud/api/files/31ea07ba-dadc-4d18-b79e-d309328762d0)

PyScript is currently built on [Pyodide](https://pyodide.org), which is a "port" of the CPython interpreter
compiled to [WebAssembly](https://webassemly.org) (`WASM`)
via
[Emscripten](https://emscripten.org/).

In a nutshell, WASM is a binary instruction format for stack-based virtual machines that is designed
as a portable compilation target for multiple programming languages.
WASM allows to run code written in multiple languages with near-native performance, and the huge
implication of this is that any modern browser rendering engines natively support WASM instruction sets.

We will dive more into the details of this architecture as soon as we will
work on the other exercises in this Chapter.

> ⚪️..🔵..⚫️..🔴 Connecting the dots:
> Thanks to Pyodide, which brings the CPython interpreter to WASM,
> we are allowed to run Python code directly into the browser at near-native performance!
> PyScript builds on top of Pyodide, abstracting from most of the low-level details, and
> making the whole development experience in the browser way more pleasant and easy
> to get started with!

> 💡 The version of Python running in the browser is linked to the version of the 
> CPython interpreter supported by Pyodide.
> In this course, we are using `PyScript 2023.05.1` which builds on top of 
> [`Pyodide 0.23.2`](https://pyodide.org/en/stable/usage/packages-in-pyodide.html) 
> that runs `Python 3.11.2`.

#### `<script type="py"> = <py-script>`

If you have already worked with previous versions of PyScript, or you have seen some examples on PyScript apps on the internet, 
you might have noticed the new special tag
`<script type="py">` that we used in our example, instead of the more common `<py-script>`
[custom element](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements).

The `PyScript 2023.05.1 release` - the one we are using in this course - has introduced the new
`<script type="py">` as a **synonym** for `<py-script>`. Reason for using the new synonym are manifold.

`TL;DR`: Using `<script type="py">` would solve issues with your Python code containing HTML reserved
characters, such as `<`, or `>`.

_Extended Explanation_:

Custom elements, namely HTML `tags` that are not part of the HTML
[Namespace](https://developer.mozilla.org/en-US/docs/Glossary/Namespace) (e.g. `<py-script>`) are
treated by the browser like any other _displayable_ elements: their content is parsed as text, and
displayed on the screen as normal text, unless special _style rules_ impose differently.
In case of the `<py-script>` element, these rules are indeed part of
the `pyscript.css` file mentioned above.
Furthermore, there are some characters which are reserved in HTML (e.g. `<` or `>` or `&`).
Therefore, if any of those characters is present in a text, they are automatically replaced by
their corresponding [`HTML Entities`](https://developer.mozilla.org/en-US/docs/Glossary/Entity).

As a consequence, if your Python code contains any `<` or `>`, for example, those would be converted in their
corresponding entities (i.e. `&lt;` and `&gt;`, respectively) which do not make any sense in Python,
so generating issues in how the page is displayed, or even how the code is executed.
Using the new `<script type="py">` would do the trick.

### 🎁 1.4 Wrap up

In this chapter we have worked on our first example of PyScript app that runs Python in the browser.

To quickly recap, we started from a pretty standard `HTML` page template in which we added two lines
(i.e. `<link rel="stylesheet" href".../pyscript.css">` and `<script defer src=".../pyscript.js"`)
tho integrate PyScript, along with the new `<script type="py">` tag where Python code can be embedded.
Our Python code just prints the version of the Python interpreter we are currently running, and the output
is automatically redirected to a new `<py-terminal>` custom element in the page.

The whole example itself was really simple and not at all complicated (from a mere coding perspective).
Nonetheless there were lots of interesting details we started to unravel as soon as we started digging
a little bit more into the details, and _how_ PyScript actually works. And we have barely started to
scratched the _surface_! This is why this title of this exercise mentions that those two simple
lines of Python code in the browser are indeed like the [TARDIS](https://en.wikipedia.org/wiki/TARDIS):
they are _bigger on the inside_.

#### 🥡 Take away lessons

- PyScript requires no installation, nor configuration to get started.
- PyScript provides a new HTML tag `<script type="py">` where Python code can be embedded.
- PyScript supports standard Python 3 in the browser.
- PyScript builds on top of Pyodide, that is a Python distribution running on WASM.
- WASM is a special instruction set designed to be a portable compilation target for multiple languages.
- All modern Web Browser can run WASM along with JavaScript in their rendering engine.

---

## Exercise 2 - There can be no data app without NumPy

Over the years, [NumPy](https://numpy.org) has become more and more a
[very central gem](https://data-apis.org/array-api/latest/) in
the whole Python ecosystem for data science and numerical computing.
It is so much so, that to date there hardly can be any python apps involving any
form of numerical computation that is not importing `numpy as np` at some point.

Therefore, we could never claim to be creating a data app with PyScript if we
wouldn't have the possibility to `import numpy as np` in our Python code
in the browser as well.

> 💡 Why importing Numpy would be a game changer ?
>
> Being able to import NumPy in our PyScript app would be so important mainly
> for two reasons. From a mere programmatic and technical perspective, this would
> open up to the possibility of _importing_ "external" packages in our Python code
> running in the browser. By "external" we merely refer to any generic package that
> is **not** part of the Python Standard library.
> Secondly, if we would be able to bring NumPy in the browser,
> we would immediately unlock unprecedented (numerical) capabilities for the web environment,
> e.g. _operator overloading_, _typed multidimensional arrays_ (i.e. `NDArray`), _threads_,
> [`SIMD`](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data).

### ⏳ 2.1 Get Ready

Let's start by creating a simple HTML page template, similarly to what we did in [Exercise 1](#⏳-11-get-ready):

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PyScript meets NumPy</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://pyscript.net/releases/2023.05.1/pyscript.css" />
        <script defer src="https://pyscript.net/releases/2023.05.1/pyscript.js"></script>
    </head>
    <body>
        <script type="py">
            # Add your code here
        </script>
    </body>
</html>
```

Let's save this template as a **new** file, named `pyscript_meets_numpy.html`.

### 🧑‍💻 2.2 Importing NumPy

First thing, let's write some Python code that uses NumPy, and what a better example than the
[_first one_](https://numpy.org/doc/stable/user/quickstart.html#an-example) gathered from the
official NumPy [documentation](https://numpy.org/doc/stable)? 

```python
# Adapted from https://numpy.org/doc/stable/user/quickstart.html#an-example
import numpy as np

a = np.arange(15).reshape(3, 5)
print(f"NDArray a: \n{a}")
# Expected:
# array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14]])
print(f"a.shape: {a.shape}")
# Expected:
# (3, 5)
print(f"a.ndim: {a.ndim}")
# Expected: 2
print(f"a.dtype.name: {a.dtype.name}")
# Expected: 'int64'
print(f"type(a): {type(a)}")
# Expected <class 'numpy.ndarray'>
b = np.array([6, 7, 8])
print(f"b: {b}")
# Expected: array([6, 7, 8])
print(f"type(b): {type(b)}")
# Expected: <class 'numpy.ndarray'>
```

> 🧑‍💻 Let's now write the code from the snippet above within the `<script type="py">` tag
> in the `pyscript_meets_numpy.html` file.
>
> **Note**: If you are not super familiar with NumPy syntax, I would strongly encourage you
> to take your time to write that snippet one line at a time (as opposed to quick and blunt Copy&Paste).
> In this way, you would get the opportunity to also _read_ the code, while also familiarising with
> NumPy's API.

The above code snippet is simply trying to allocate two `numpy.ndarray`
[objects](https://github.com/leriomaggio/python-data-science/blob/main/numpy/1_intro_numpy.ipynb),
and print some of their property (e.g. `shape`, `ndim`).

If we now save the file again, and we try to open in the browser like we did before...💥

You should get the Python [Traceback](https://docs.python.org/3/library/traceback.html) as the one
reported below:

```python
Traceback (most recent call last):
  File "/home/pyodide/pyscript/_internal.py", line 104, in run_pyscript
    result = eval_code(code, globals=__main__.__dict__)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/lib/python311.zip/_pyodide/_base.py", line 468, in eval_code
    .run(globals, locals)
     ^^^^^^^^^^^^^^^^^^^^
  File "/lib/python311.zip/_pyodide/_base.py", line 310, in run
    coroutine = eval(self.code, globals, locals)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<exec>", line 2, in <module>
ModuleNotFoundError: The module 'numpy' is included in the Pyodide distribution, but it is not installed.
You can install it by calling:
  await micropip.install("numpy") in Python, or
  await pyodide.loadPackage("numpy") in JavaScript
See https://pyodide.org/en/stable/usage/loading-packages.html for more details.
```

First thing to highlight from this example: **Error Handling**: PyScript is giving direct
access to the Python traceback in the browser, similarly to what would have happened for a standard desktop application.
This is indeed a huge deal, as clear _error reporting_ is a crucial part in coding, and this is also one of the
major improvements introduced in Python 3.11 (See [PEP657](https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-pep657)).

The most relevant part of the traceback is contained in the last five lines:

```python
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

The first important take-away message we can conclude from this example is that only the Python standard library
is available by default, when using PyScript/Pyodide. To use other packages, one would need to load them separately.

Luckily, Pyodide supports the installation of external packages using
[`micropip`](https://micropip.pyodide.org/en/v0.2.2/project/usage.html#installing-packages-with-micropip),
and PyScript has direct
[integration](https://micropip.pyodide.org/en/v0.2.2/project/micropip-in-other-projects.html#pyscript) with `micropip`.

In fact, PyScript provides a special `<py-config>`
[tag](https://docs.pyscript.net/latest/reference/elements/py-config.html) that can be used to declare dependencies
for PyScript applications (_along with setting and configuring general metadata_, ed.).

To [declare the dependencies](https://docs.pyscript.net/latest/reference/elements/py-config.html#dependencies-and-packages)
in our PyScript application we would just need to add the `packages` directive within the new `<py-config>` tag:

```html
<py-config>
  packages = ["numpy"]
</py-config>
```

Let's add the `<py-config>` reported above to our `pyscript_meets_numpy.html` file, and save it.

> ✅ This example is now complete! Let's open the `pyscript_meets_numpy.html` local file in the browser.

<a name="2_output"></a>

Now everything should be working as expected! 🎉
You should be able to see the `<py-terminal>` output on the bottom of your page showing the expected output
from our code, namely:

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

### ⚙️ 2.3 How it works

As briefly mentioned in the previous section, the `<py-config>` tag can be used to declare the
dependencies for our PyScript application.
This tag directly maps to the underlying Pyodide mechanism to install external packages, namely `micropip`.

#### 📦 Pyodide Packages, Micropip, and WASM

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

In fact, let's try to _refresh_ our solution page, but **this time**, let's open the JavaScript console.
On Google Chrome: `View >> Developer >> JavaScript Console` and then hit the Refresh button in your browser.

The relevant (`log`) messages you should be seeing in the console are:

```
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
pyodide.asm.js:9 Loading numpy
pyodide.asm.js:9 Loaded numpy
```

> 🤖 Use the (JavaScript) Console, Luke!
> The JavaScript console included in almost every modern browser is a very useful tool when working
> in the web. Similarly, it is an invaluable source of information when we work with PyScript.
> I could not recommend it more to use it when working on PyScript projects!

### 🎁 2.4 Wrap up

In this exercise we have been exploring how it is possible to include external (Python)
dependencies into our PyScript application. In particular, we explored how to
`import numpy as np` in our code.

Importing NumPy is the first (and very important) step towards being able to
create Python data apps directly in the browser.

To do so, we introduced the new `<py-config>` tag that PyScript provides, along
with the corresponding `packages = [...]` directives to include packages.

#### 🥡 Take away lessons

- PyScript allows the declaration of dependencies via the `<py-config>` special tag.
- The `<py-config>` tag directly integrates with `micropip.install` module of Pyodide to
install external dependencies.
- Any pure Python package can be _installed_ and used in the browser.
- Python packages with external C-dependencies (e.g. `numpy`) can be used only if there exist corresponding
Python wheels packages targeting the `wasm32` instruction set.
- Pyodide includes a very long list of automatically supported packages, built-in with the distribution.
  - This list includes the majority of the most popular Python packages in the scientific stack.

---
## Exercise 3 - A better development experience in the browser

When using PyScript, writing Python in the browser is as easy as including our Python code 
within the `<script type="py">` tag.
Whilst this is more than acceptable when working on _simple_ examples to familiarise with the
new platform, this can easily become an issue when we are working on much more complicated code.

Moreover, you might have noticed that there is a complete lack of support from the code editor,
nor any syntax highlighting.

🙌 No worries! PyScript got you sorted! Both the `<script type="py">` and the `<py-config>` tags
support the `src` attribute, similar to what one would normally do when importing
[JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) code.

### ⏳ 3.1 Get Ready

Let's duplicate the last version of the previous `pyscript_meets_numpy.html` file and let's save this new
copy as `pyscript_src_attribute.html`. The name should be self-explanatory of what we are trying to
achive in this exercise.

Let's now modify the HTML code so that everything currently enclosed within the two PyScript tags 
would be moved and loaded from external files, namely `main.py`, and `pyscript.toml` for
the configuration part (_these files can also have different names_, ed.).

> 💡 Writing your Python code in the `main.py` file will immediately trigger the code support from your editor
> (e.g. syntax highlighting, linting, etc.) as it would be treated as a normal Python file.
> Who cares that this will later be used within a PyScript app.

> 💡 The `<py-config>` [tag](https://docs.pyscript.net/latest/reference/elements/py-config.html#py-config) supports
> either the [TOML](https://learnxinyminutes.com/docs/toml/) or the 
> [JSON](https://www.freecodecamp.org/news/what-is-json-a-json-file-example/) formats.
> The TOML format is the default, and we will be using this throughout the course, as it is
> (a) less verbose than JSON; (b) more intuitive and easier to write; (c) it is the same
> format used to specify [packages metadata](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) (i.e. `pyproject.toml`).

The final result of the `pyscript_src_attribute.html` file should be something similar to:

```html
<!DOCTYPE html>
<html lang="en">

    <head>
        <title>PyScript meets NumPy</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://pyscript.net/releases/2023.05.1/pyscript.css" />
        <script defer src="https://pyscript.net/releases/2023.05.1/pyscript.js"></script>
    </head>

    <body>
        <py-config src="./pyscript.toml"></py-config>
        <script type="py" src="./main.py"></script>
    </body>

</html>
```

### 🧑‍💻 3.2 Web Security, and CORS

If you are already familiar with web development, and web standard you should
already see where this is going.

If we try to open the `pyscript_src_attribute.html` as local HTML file in your browser, you
should be seeing a **blank page** like nothing is working anymore!

This is **expected**, don't worry! Let's open up the JavaScript Console again to see if there
is any additional clue there.

Haha! Indeed there is:


```log
Access to XMLHttpRequest at 'file:///.../pyscript.toml' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, isolated-app, chrome-extension, chrome, https, chrome-untrusted.
```

As a matter of facts, loading resources from unknown (`null`) origins when loading local files in the browser
is in violation of the [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (Cross Origin Resource Sharing)
policy of the browser. To be clear, the **same** would have happened if we would have tried to load some local
JavaScript or CSS file.

To circumvent this issue we should run an [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP) server
that would serve the resources, instead.

The quickest way to do this would be to spawn an http server using Python and its
[`http`](https://docs.python.org/3/library/http.server.html) module:

1. Open a Terminal / Command Line / Power Shell (Windows Users);
2. Move to the location where the HTML file `pyscript_src_attribute.html` lives on your hard drive;
3. Run `python -m http.server`.

On this note, it is worth noticing that you would need to have a working Python Distribution installed on
your computer in order to run the above command, and spawn the local server.

If that's not the case, you could consider downloading [Anaconda Distribution](https://www.anaconda.com/download).

> 💡 Another HUGE "side-effect" of using PyScript and Python in the browser.
> So far we were not using nor relying _at all_ on any local Python distribution (if any!)
> to run the examples. The Python/Pyodide distribution was automatically downloaded by PyScript
> (i.e. `pyscript.js`) when loading the HTML page.
> Therefore, it is not just you open the HTML, write Python and it just works. The "app" can
> also be distributed without requiring anyone to necessarily have Python installed on their computer!
> In other words: PyScript apps are **self-contained**.

If you were able to spawn the local server via Python
(_or using any other HTTP server instead, e.g. nginx_, ed.) you should now see the app loading and
executing as normal, with the same output in the `<py-terminal>` as in 
<a href="#2_output">Exercise 2</a>:

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

> 💡 Another important lesson we can derive from the previous example is that we would not
> need much infrastructure to _deploy_ a PyScript application. Anything that would simply be
> able to serve HTML pages (e.g. [GitHub Pages](https://pages.github.com/)) would do.

### 🎁 3.3 Wrap up

In this example we learnt that it is best practice (as well as a better development experience)
to separate HTML from Python files, leveraging on the `src` attribute the PyScript `<script type="py">`
tag supports. In this way, we could rely on full support from our code editor (syntax highlighting,
code indentation) when we write Python code (_as we would normally do_, ed.), that will be later
used within our PyScript app. The same applies for configuration directives with the `<py-config>`
tag. However, in order to load these "external" local resources, we need to serve the app with an
HTTP server (e.g. `python -m http.server` for local development, or `GitHub Pages`).

#### 🥡 Take away lessons

- PyScript tags `<script type="py">` and `<py-config>` can leverage on their `src` attribute to load external resources.
- Using external `main.py` and `pyscript.toml` enables better development experience when working with PyScript.
  - keeping also HTML and Python separated;
  - leveraging on your code editor support for Python coding.
- The `<py-config>` tag supports TOML (default) and JSON formats.
- Loading local files when loading external resources violates CORS browser policy.
- An HTTP server is required to workaround the CORS issue.
- Deploying a PyScript app does not require much infrastructure - just serving HTML pages.
  - No server-side technology!
- (last but not least) PyScript **does not** require to have Python installed on your computer!
- **PyScript apps are self-contained**
  - You can distribute your HTML PyScript app without requiring users to install anything on their end.
  Not even Python!.
  - The `<py-config>` tag configures the PyScript app, including external dependencies to be downloaded
  and installed.

### 💫 3.4 There is a Better way 🐇

This exercise was absolutely great to learn some best practice of working on PyScript apps:
_keeping Python and HTML separated in different files_ improves the coding experience,
enabling the support of your editor.
Moreover, writing an external Python module would also help in making the code more
maintainable, as it would normally be when developing generic Python applications.

However, the simplicity in getting started and the natural ease of use of PyScript now
meets the "complications" of Web standards.

To be clear, CORS policy restriction do exist for a very good
[security reason](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)!

Nonetheless, we would be needing to set up and run an Http server to work with PyScript.

Luckily, there is an alternative and **better** way: the PyScript bunny way 🐇

#### Introducing [PyScript.com](https://pyscript.com)! 💫

 PyScript.com is a **free** and flexible coding platform specifically designed to get started and
 work with PyScript. The platform is generally available **for free** as a software service.

 Once you log in you do get access to your **Dashboard** where all your apps will reside.
 Moreover, you do have access to public _Trending_ and _Featured_ apps to get inspiration of
 what you can do with PyScript apps.

 To create a new PyScript app, you can click on the
 <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
  <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
</svg> on the left toolbar.

This will create a new **template** for your PyScript app ready to get started with!
This template contains a `main.py` to host your main Python code, a `pyscript.toml` for
configurations, and `index.html` containing the actual HTML of your app.

Does that remind you anything ? 😊

In this exercise, we have been working to create exactly the same structure on our local computer.
With PyScript.com, you can have all that with just one click, and _you are ready to go!_.

The integrated editor has full support for both HTML/JavaScript and Python programming, and by
simply clicking the **Save & Run** button, you can save all your changes to your files, and
immediately see a Preview of how your PyScript application would look like!.

PyScript.com is indeed pretty easy to use, and absolutely perfect to get started with
PyScript as it completely lowers the barrier to set up your coding environment.

> 💡 From now on, we will be using directly PyScript.com to work on the exercises, 
> using this [template](https://bit.ly/pyscript-template-ch-1)
> So please [sign up](https://pyscript.com) to create your account.

> 🤓 In case, please also consider to become a Founder, to further support the PyScript project!

---

## Exercise 4 - Our first data app on PyScript.com

In this exercise we will be working on our first data app hosted on
[PyScript.com](https://pyscript.com). 
While we will dive into our implementation, exploring new _features_ of PyScript itself, 
we will also discover new capabilities offered by PyScript.com.

### ⏳ 4.1 Get Ready

Getting started this time will be super quick, because we will entirely leverage PyScript.com
features. In fact, you can **Copy** the reference [template](https://bit.ly/pyscript-template-ch-1)
project, by clicking on the **Copy Project**, and automatically transfer the project into
your own dashboard. When that is done, you are ready to code!

> 💡 You might have noticed that before importing the project into your dashboard, the whole
> app was in _read-only_ mode. You can work on the only only after the app has been duplicated
> and imported in your own Dashboard.

From now on, the checklist of things to do to get started with our app development for 
the exercises will be essentially the same.

#### Three simple steps to get started

1. Open the `index.html` and fill in the `<title>` tag with an appropriate name.
  - You might also want to rename your App, accordingly.
2. Open the `pyscript.toml` file (selected from the File chooser menu on the left)
and replace all the configuration [metadata](https://docs.pyscript.net/latest/reference/elements/py-config.html#supported-configuration-values).
  -  Please also add any dependency your app may need using `packages = [...]`.
3. Open the `main.py` file and start coding! 🎉

For this exercise specifically, let's name the app: "My first Data App", also in the `<title>` tag, and the `name`
property in `pyscript.toml`. 

In this exercise we will be using [`pandas`](https://pandas.pydata.org/), a very popular Python package for data
analysis and manipulation. Let's add the following line at the end of the `pyscript.toml` file:

```toml
# ... all app metadata here

packages = ["pandas", ]
```

We are all set, and ready to start coding!

### 🧑‍💻 4.2 Pandas in the browser, with Pyodide support

If you are already familiar with Pandas, you would certainly agree that one of the most
popular functions offered by the library is `read_csv`: an utility function to read
data in CSV (Comma Separated Value) format into `pandas.DataFrame` object.

> 💡 Pandas has become very popular in the Python data lore because it first
> introduced the `DataFrame` object into pythonic namespaces, borrowed from the
> more popular Data Frame structure in the R language.

The [`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html?#pandas.read_csv)
function accepts a long list of parameters (_to support multiple data scenarios_, ed.), but first 
of all, it requires a URL to the original data file to read from.

In this exercise, we will be loading the [`brain_size.csv`](https://scipy-lectures.org/_downloads/brain_size.csv)
file, available at the following link from [SciPy Lectures](https://scipy-lectures.org/):

```
https://scipy-lectures.org/_downloads/brain_size.csv
```

This is how the data looks like: 

```
"";"Gender";"FSIQ";"VIQ";"PIQ";"Weight";"Height";"MRI_Count"
"1";"Female";133;132;124;"118";"64.5";816932
"2";"Male";140;150;124;".";"72.5";1001121
"3";"Male";139;123;150;"143";"73.3";1038437
"4";"Male";133;129;128;"172";"68.8";965353
"5";"Female";137;132;134;"147";"65.0";951545
```

In this case, the separation character is `;`.

The Pyodide Python API offers a method to `fetch` a given URL synchronously: 
[`pyodide.http.open_url`](https://pyodide.org/en/stable/usage/api/python-api/http.html#pyodide.http.open_url)


> 💡 Internally `pandas.read_csv` relies on [`requests`](https://requests.readthedocs.io/en/latest/)
> to effectively download the target data file. Requests however does not immediately work
> with Pyodide since `requests.get` is a _synchronous_ blocking call, whilst Pyodide stack is
> entirely _asynchronous_.

So the plan would be to download the data file with `open_url` and pass it to pandas `read_csv` function:

```python
from pyodide.http import open_url
import pandas as pd

DATA_URL = "https://scipy-lectures.org/_downloads/brain_size.csv"

df = pd.read_csv(open_url(DATA_URL), sep=";", na_values=".", index_col=0)
```

Let's now do some grouping and averaging using 
[`pandas.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) function, and
let's print the resulting Data Frame using the 
[`to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html)
utility method.

Before we dive into the remaining part of the code, let's create a new `<div id="data"></div>`
element tag in the `index.html` file. This will be the target element where 

```python

from pyscript import Element, HTML

gender_avg = df.groupby("Gender").aggregate("mean")
Element("data").write(HTML(gender_avg.to_html()))
```

The complete code listing is reported below: 

```python
from pyodide.http import open_url
import pandas as pd
from pyscript import Element, HTML

DATA_URL = "https://scipy-lectures.org/_downloads/brain_size.csv"

df = pd.read_csv(open_url(DATA_URL), sep=";", na_values=".", index_col=0)

gender_group = df.groupby("Gender").aggregate("mean")
Element("data").write(HTML(gender_group.to_html()))
```


### ⚙️ X.3 How it works

### 🎁 X.4 Wrap up

#### 🥡 Take away lessons

---

## Exercise X - 

### ⏳ X.1 Get Ready

### 🧑‍💻 X.2 

### ⚙️ X.3 How it works

### 🎁 X.4 Wrap up

#### 🥡 Take away lessons

## Exercise 2 - Python REPL

Now, let's try to add a Python REPL in the webpage. If you want to keep the work of the previous exercises, feel free to make a copy. Now I will assume we just reuse the `hello_world.html` and continue from there.

Now below the `</py-script>` tag. Add a pair of tags like this:

```html
<py-repl>
</py-repl>
```

This will create a Python REPL on the webpage. Let's look at the browser to find out. If you are on a new file, open that file with a browser, otherwise you can just refresh to see the new changes.

Now by seeing the REPL, you can try to code Python in it. Try printing the time now from the REPL? Then click on the green arrow or press `shirt + enter`.

You can also add Python code between the the tags `<py-repl>` and `</py-repl>`, but they won't get executed right away like the previous exercise. They will be added to the REPL and you have to run them with the green arrow or press `shirt + enter`.

Now try adding the following line between the `<py-repl>` and `</py-repl>` tags:

```python
print(datetime.now()) # press shirt + enter to run
```

and refresh the page.

What if I want to keep the result of the previous REPL and have a new one after I executed the old one. You can activate that creature by adding `auto-generate="true"` inside the `<py-repl>` tag like this:

```html
<py-repl auto-generate="true">
```

Now save and refresh again to see the changes.

---

## Exercise 3 - Async

Remember we can print out the time but it does not update automatically? If we want to do so we need to do a bit of async code. Don't worry if you are not familiar with async code, we will do it here together and you can look deeper into [async code in Python](https://docs.python.org/3/library/asyncio.html) later if you are interested.

Now, let's go to the `hello_world.html` and use it as a starting point. If you had a copy of exercise 1, make a copy of it and we can start form there. If you are continuing form the last exercise, just delete the `<py-repl>` and `</py-repl>` tags and anything between them, we will start from there.

We need to modify the code inside the `<py-script>` and `</py-script>` tags pair. But first, we need to add a div element as `output` for the output, after the `<py-script>` and `</py-script>` tags pair, add this:

```html
<div id=output></div>
```

Then, we need to change our code, first, we need to import asyncio after importing datetime.

```python
from datetime import datetime
import asyncio
```

We can keep the first print statement but for the time itself, we need to update it, so, we will have to write into the div element `output` as `print` statement does not allow us to rewrite it.

```python
Element("output").write(str(datetime.now()))
```

Note that we have to convert `datetime.now()` into string as it is done automatically by the `print` statement but not he `wirte` method here.

Now, let's create an async function (or it is called coroutine) to make it looping over and over again. An async function (coroutine) is just like a function but with `async` in front of the `def`, like this:

```python
async def tick():
```

In this function, it want it to run and never end, so we:

1) use a while `True` loop;
2) then we do the `.write` into `output` (the line above) and finally;
3) sleep for a second before the next iteration

just like this:

```python
async def tick():
    while True:
      Element("output").write(str(datetime.now()))
      await asyncio.sleep(1)
```

Now we have our `tick`, we just need to put it in the PyScript event loop so it is running in the background non-stop. But before, remember the PyScript loader? The spinning thing when PyScript is loading. If we just put our `tick` in the event loop technically PyScript is never finish executing and the spinning will not go away. So we have to tell it to stop.

```python
pyscript_loader.close()
```

Then now we can put `tick` into the event loop:

```python
pyscript.run_until_complete(tick())
```

Did you follow? If you are not sure here is all the code within the `<py-script>` and `</py-script>` tags pair:


```python
from datetime import datetime
import asyncio
print("The time now is:")
async def tick():
    while True:
      Element("output").write(str(datetime.now()))
      await asyncio.sleep(1)
pyscript_loader.close()
pyscript.run_until_complete(tick())
```

When you are done, save and refresh (or open the file) and see the async magic happened.

---


---

## Exercise 5 - Loading a file

Most of the time, when using Pandas, we will load in a csv for data analysis. To load a hosted csv from a url, we can do so with the `open_url` method provided by Pyodide. Let's put this line above the `import pandas as pd` line:

```python
from pyodide.http import open_url
```

We will load the [ice cream data](https://github.com/Cheukting/pyscript-ice-cream/blob/main/bj-products.csv) which is hosted on GitHub as `df`.

> The ice cream data is originally from Kaggle [Ice Cream Dataset](https://www.kaggle.com/datasets/tysonpo/ice-cream-dataset)

> Files need to be hosted on a server. To do it locally, a local server need to be started. The easiest way is to use the `http` module in Python: `python -m http.server`

Replace the two lines below `import pandas as pd` with this:

```python
df = pd.read_csv(open_url("https://raw.githubusercontent.com/Cheukting/pyscript-ice-cream/main/bj-products.csv"))
```

To sum up, the code between the `<py-script>` and `</py-script>` tags pair should look like this:

```python
from pyodide.http import open_url
import pandas as pd
df = pd.read_csv(open_url("https://raw.githubusercontent.com/Cheukting/pyscript-ice-cream/main/bj-products.csv"))
df
```

Now opening the html file in a browser again or refresh the page if you already have it opened. Now we will see the dataset being loaded in full. From here we can do all the operations which Pandas offer, for example, to show only the head (first 5 rows) of the data, replace the last `df` with `df.head()` and refresh.

---

## Exercise 6 - Data analysis with Pandas

In the last exercise, we can do Pandas analysis with the ice cream data. What if we want the user to be able to do it without changing the html file? We can do it with the `<py-repl>`.

Let's delete the last line with `df` or `df.head()` and put the following under the `</py-script>`:

```
<py-repl>
# ice cream data pre-loaded as df
df.head()
</py-repl>
```

Now refresh the page (or open it) and see that instead of the DataFrame, there is a REPL for you to do the Pandas operation with `df`. You can now try running `df.head()` by pushing `shift + enter`. After that, try changing the `df.head()` to other operations like:

* `df.tail()` to show the tail of the data set,
* `df[['name']]` to get all the names of the ice creams, or
* `df.query("rating > 4 and rating_count > 100")` for the best rated ice creams

---

This concludes Chapter 1 of this workshop. To continue learning how to create data visualisation and interactive elements, please go to [Chapter 2](/chapter_2/chapter_2.md)
