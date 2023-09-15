# Getting Started with PyScript

In this module, we will get our bearings with the many features PyScript provides to create
rich web applications using Python in the browser.

In each section, we will work on a single PyScript app aimed at exploring specific
features, and capabilities offered by the platform.

You are totally free to choose the pace you navigate through content, depending on your
background, your coding skills, or any particular interest in the covered topics.

There will be five sections, each sharing the same content organization:
- ⏳ Get Ready
- 🧑‍💻 Hands on
- ⚙️ How it works
- 🎁 Wrap up
- 🥡 Take away lessons

> 💡 Block-quote paragraph will also be included to highlight specific concepts, or for general remarks.

To work on the apps all that you'd need is a code editor with syntax highlighting, and a Web Browser. 
Any modern we browser would do! So please feel free to use the one you are feeling 
most comfortable with.

I will be using Google Chrome, for the exact same reason. Therefore some references reported
in the text (e.g. to the Web Inspector / JavaScript console) would need to be re-adapted
to your web browser, accordingly.

When you are working on the hands on parts, I would strongly encourage you to _write_ yourself
the code reported in the sections (_unless sometimes differently instructed_), rather than simply
copying and pasting it. This would help you a lot in familiarizing with the code, and the new
technology, especially if you are an absolute beginner.


PyScript has been announced for the first time at [PyCon US 2022](https://youtu.be/qKfkCY7cmBQ?t=561)
by co-creators [Peter Wang](https://www.anaconda.com/leadership/peter-wang), and
[Fabio Pliger](https://www.linkedin.com/in/fabiopliger),[PyScript](https://pyscript.net)
is the new revolutionary platform that brings Python into the browser.


---
## 1. Your first Python in the browser.

As a start, we will work on a very simple app in order to understand
a bit more what version of Python is running in the browser, and what are the differences 
(_if any_, ed.) with the standard Python interpreter.

### 1.1. ⏳ Get Ready

To get started. let's create a skeleton of a generic HTML page.

Feel free to copy and paste in your editor the one reported below:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Get Started with PyScript</title>
        <meta charset="utf-8">
        <!-- ADD PyScript Here -->
    </head>
    <body>
        <!-- Add your Python code here -->
    </body>
</html>
```

Let's save this file as `first_pyscript_app.html`.

Let's now move onto writing some Python in this HTML page.

### 1.2 🧑‍💻 Hands on: Writing your first PyScript App

The first thing we need to do, is to actually include the main PyScript assets into 
your our HTML page.

We will do so by replacing the first placeholder comment
(i.e. `<!-- ADD PyScript Here -->`) with the following line:

```html
<script type="module" src="https://cdn.jsdelivr.net/npm/@pyscript/core"></script>
```

The `<script>` tag imports the `@pyscript/core` JavaScript
[module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), and that effectively
enables PyScript in your application.

> 💡 Believe it or not, that is the **only** single line required to enable Python in the browser.
> No installation, and not further configuration is needed to get started!

Now let's write some Python code!
Where the second placeholder comment is in the template (i.e. `<!-- Add PyScript tag and Python code here -->`)
let's write the following code:

```html
<script type="py">
    import sys
    print(f"Running Python {sys.version} in the Browser!")
</script>
```

> ✅ This example is complete! Now let's save the `first_pyscript_app.html` and open the local file into the browser.

If everything works correctly, you should be now looking at a blank page! 😁
I know this is probably not something you were expecting, but I promise you: everything is in order.

What I would like you to do now, is to open the JavaScript Console in your Browser (on Chrome: `View > Developer > JavaScript Console`).
In the console, you should be now seeing the message we were looking for, and similar to:

```
Running Python 3.11.2 (main, Jul  7 2023, 05:19:00) [Clang 17.0.0 (https://github.com/llvm/llvm-project df82394e7a2d06506718cafa347b in the Browser!
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

In the figure below, there is an high-level representation of the PyScript general architecture,
describing the various components. In the remainder of this Section, we will try to understand
what's the role of these components, and how they relate to each other.

![PyScript General Architecture](https://anaconda.cloud/api/files/31ea07ba-dadc-4d18-b79e-d309328762d0)

On the top level of the architecture, there is indeed PyScript, providing access to
various elements, like "Widgets" and "Custom Tags".
We will talk about some of them more extensively in the following exercises in this Chapter.

PyScript is currently built on **Pyodide**, which is a "port" of the CPython interpreter
that is compiled to **Web Assembly** (`WASM`) via **Emscripten**.

In a nutshell, WASM is a binary instruction format for stack-based virtual machines that is designed
as a portable compilation target for multiple programming languages.
WASM allows to run code written in multiple languages with near-native performance.

However, the real (huge) implication of this architectural choice could be better appreciated if we
add an important piece to our puzzle:

> 💡 "Any modern web browser natively embeds support for WASM instruction sets".

In other words, any browser is able to run any WASM executable within their sand-boxed environment.
And therefore, thanks to native support to WASM, we are able to bring Python (_literally_) into
the browser!

We will dive more into the details of this architecture as soon as we will
work on the other exercises in this Chapter.

Let's pause for a second now. It was certainly a lot to process, with lots of new terms, and terminology.

Let's try to re-connect the dots before moving on, and please feel free to come back to the
following [Section](#⚪️🔵⚫️🔴-connecting-the-dots) any time during this Course, if you feel that
there is still something that "doesn't make sense" in how this whole new technology works.

#### ⚪️..🔵..⚫️..🔴 Connecting the dots:

Let's briefly recap all the components and their role within the
PyScript Architecture.
You can also find the reference links to each of them at the end of the Section.

The current version of **PyScript** builds on top of Pyodide.
**Pyodide** provides a version of the standard CPython interpreter
(e.g. Python 3.11.2) that works directly on WebAssembly (WASM).
WASM is a binary instruction format that is designed as a portable compilation target
for multiple languages.
Pyodide leverages on **Emscripten** to compile Python (i.e. the CPython interpreter)
to WASM.

PyScript leverages on these technologies under the hood, and abstracts most of
their low-level details, providing a whole new development experience in the browser
easy to get started with!

> 💡 The version of Python running in the browser is linked to the version of the
> CPython interpreter supported by the corresponding version of Pyodide.
> In this course, we are using `PyScript 2023.05.1` which builds on top of
> [`Pyodide 0.23.2`](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)
> that runs `Python 3.11.2`.

**Reference Links**:

- [Pyodide](https://pyodide.org)
- [WebAssembly](https://webassemly.org)
- [Emscripten](https://emscripten.org/)

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

Let's add the `<py-config>` reported above to our `pyscript_meets_numpy.html` file right after the `<body>` tag, and save it.

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

### 💫 3.3 There is a Better way 🐇

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

### 🎁 3.4 Wrap up

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
> with Pyodide since `requests.get` is a _synchronous_ blocking call which tries to open a socket to
> establish the connection. And  sockets are currently 
> [not available](https://pyodide.org/en/stable/project/roadmap.html#write-http-client-in-terms-of-web-apis)
> in Pyodide.

So the plan would be to download the data file first, using `open_url` function from Pyodide, and feed the result
directly into the `read_csv` function of Pandas:

```python
from pyodide.http import open_url
import pandas as pd

DATA_URL = "https://scipy-lectures.org/_downloads/brain_size.csv"

df = pd.read_csv(open_url(DATA_URL), sep=";", na_values=".", index_col=0)
```

To finalise our exercise, let's try some _quite standard_ data operations
on the Data Frame do gather some statistics about the data.
For example, we could group our data by `Gender`, using
[`pandas.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) function,
aggregate the result by `mean`, and convert the resulting Data Frame into HTML `<table>` using the
[`to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html)
utility method.

Let's first create a new `div` element tag in the `index.html` file that will contain
the resulting table: `<div id="data"></div>`.

```python
from pyscript import Element, HTML

gender_avg = df.groupby("Gender").aggregate("mean")
Element("data").write(HTML(gender_avg.to_html()))
```

The complete code listing in `main.py` for the exercise is reported below:

```python
import pandas as pd

from pyodide.http import open_url
from pyscript import Element, HTML

DATA_URL = "https://scipy-lectures.org/_downloads/brain_size.csv"

df = pd.read_csv(open_url(DATA_URL), sep=";", na_values=".", index_col=0)

agg_gender = df.groupby("Gender").aggregate("mean")
Element("data").write(HTML(agg_gender.to_html()))
```

### ⚙️ 4.3 How it works

After having configured our dependency for our app in the `pyscript.toml`/`<py-config>`,
we are able to `import pandas as pd` in our code.

The `pyodide.http.open_url` function is the key enabler here to `fetch` data _synchronously_ from
a given URL, and pass the result directly to `pandas.read_csv`. Without the `open_url` function,
the `pandas.read_csv` function would have not worked.

> 💡 Alternatively, we could use [`pyodide-http`](https://github.com/koenvo/pyodide-http)
> This package, automatically included in the list of supported packages in Pyodide, provides patches for 
> `requests` and `urllib` http libraries to make them work in Pyodide.

> 🧑‍💻 Would you like to give it a go ?
> All you would need to do to start using `pyodide-http` is to include it in our list of required `packages`
> (in `pyscript.toml`), and then adding the following two lines to our Python code:
> ```python
> from pyodide_http import patch_requests
> patch_requests()
> ```
> After this, we will be able to normally use `pd.read_csv`, without
> using `pyodide.http.open_url`, instead 😊.

#### _One does not simply run Python in the browser_

At first, this may look like quite a set back from what we've been discussing so far. So far, we have
written in the browser the _same_ Python that would normally work on a CPU. Instead, in this exercise,
we are need to make "adjustments" to port our Python code into the browser.
However, it is very important to emphasise that this is neither a limitation of PyScript, nor of Pyodide.
It is entirely related with how the _web works_, and with built-in sandboxed isolation from all the
low-level details of the Operating System of the browser runtime environment. Let alone, that in the web
_async_ calls are way preferable then _sync_ ones.

Therefore all that we are starting to understand in this exercise is that _sometimes_ we would need to
to adapt our code to be executed in this _new_, and mostly _unexplored_ environment for Pythonistas.
No different than what we would need when porting Python to MicroControllers
(e.g. [MicroPython](https://micropython.org/)).

From this exercise onwards in this tutorial, similar notes and adjustment
to our code will be remarked by the [meme-like](https://imgflip.com/gif/7qptor) title of
_One does not simply run Python in the browser_.

Jokes aside, all these considerations about porting our Python code into the browser will offer
valuable opportunities to dive into details of the new computation platform we are trying to
get along with: the Browser &nbsp; WASM.

The rest of the (Pandas) code in the exercise is pretty standard `pandas` ops on Data Frame and does not deserve
further comments.

What it is worth mentioning instead are the use of those two objects imported from `pyscript`:
[`Element`](https://docs.pyscript.net/latest/reference/API/element.html) and `HTML`.
The former, is a Python abstraction provided by the PyScript high-level API to work with DOM in a very Pythonic way.
`Element` accepts a target (HTML) `id` in its constructor method, which identifies a unique element in the Page,
and gives access to the corresponding element tag. In fact, we could either use `pyscript.Element` or 
`js.document.getElementById()` function to identify and manipulate element tags in the DOM.

> 💡 This is the first time we mention the `js` module to get immediate access to the JavaScript
> interpreter running in the browser. Under the hood, Pyodide is responsible to create this bridge
> connection between Python and JavaScript. In this case, using the `js` module from our Python
> is an example of direct integration of Python with JavaScript (i.e. `Py` ➡️ `JS`).
> Later on in the following Chapters, we will see also examples considering the opposite direction
> of communication (i.e. `Py` ⬅️ `JS`) enabled by PyScript/Pyodide, thus implementing a bi-directional
> channel between the two technologies: `Py` ↔️ `JS`.

One of the methods in the `Element` class is `write` that can be used to add content, of various
mime/type. We are wrapping the output generated by `agg_gender.to_html()` into an
[HTML](https://github.com/pyscript/pyscript/blob/848d77b1c29d4145a3438b832acd4b3b9bf32951/pyscriptjs/src/python/pyscript/_html.py#L10)
instance to would mark the content with `text/html` [`mime/type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types),
rather than the default `text/plain`.

> 💡 It is worth mentioning that the `pyscript` module (and corresponding _global_ namespace)
> are automatically available for our Python code when we work with PyScript.
> In other words, the line `from pyscript import Element, HTML` could be simply omitted, and the
> whole code would continue to work the same way.
> However, it is always good practice to declare imports explicitly in our code, to improve
> readability, and code understanding.

### 🎁 4.4 Wrap up

In this exercise, we have been exploring the use of the `pandas` library with PyScript. Pandas is another
key library in the PyData stack, and another fundamental piece for our Python data apps running in
the browser, with PyScript.
One of the most popular, and widely used function from `pandas` is `read_csv` to read data in CSV format, and
convert them into `pandas.DataFrame` objects. This function can automatically read data hosted on remote URLs
but its underlying implementation is not fully compatible with how PyScript/Pyodide work. Namely `sockets` and
synchronous calls are not supported in Pyodide. Therefore, in our code solution, we used `pyodide.http.open_url`
function to fetch our data synchronously, and feed it into `pandas.read_csv` function.

After some _standard_ data processing involving grouping and averaging of our data, the resulting `DataFrame` has
been written into the HTML page using pyscript high-level Python APIs: `pyscript.Element` and `pyscript.HTML`.

#### 🥡 Take away lessons

- PyScript/Pyodide supports running also `pandas` in the browser.
  - If combined with `numpy` (see Ex. 3), we already have two of the most crucial packages for Data Science in Python.
- `pd.read_csv` requires either `pyodide.http.open_url` to fetch the data, or `pyodide-http` to patch its internals.
  - This is because `sockets` are not supported in Pyodide, so we need to adapt our code to run in the new Web/WASM environment.
- PyScript provides high-level APIs to interact with DOM, e.g. `Element` and `HTML`.
  - `Element` works thanks to the bi-directional bridge PyScript/Pyodide provide between `Py` and `JS`

---

## Exercise 5 - Pythonic `Read-Eval-Print-Loop`, and custom Python modules

In this exercise, we will explore the _third_ of the special [custom elements](https://docs.pyscript.net/latest/reference/index.html#reference)
PyScript provides: `<py-repl>`.

The [`<py-repl>`](https://docs.pyscript.net/latest/reference/elements/py-repl.html) special tag allows users to add a
`REPL` (Read-Eval-Print-Loop) directly into their HTML page, which is able to evaluate multi-line Python code, and display its output.
Similar REPL elements are the foundational blocks on which Jupyter notebooks are build upon. So, chances are that you would be already
familiar with it.

In this exercise, we will see how this tag can be used to directly interact with the Python code available in the browser.
One very good example along these lines is provided by the
[_Using SQLite in PyScript_](https://pyscript.com/view/6fd75ce3-df0a-4384-b255-195e41c4f02f/d9dad5e1-bebd-4fb8-9493-5813063cebcc/latest)
app, available on [PyScript.com](https://pyscript.com).
This app uses the `<py-repl>` to enable the execution of Python code to read from, and write to, an online `sqlite3` database.

While working on the `<py-repl>`, we will also focus on another _important_ feature provided by PyScript: the ability to configure and use
**custom Python modules**.

### ⏳ 5.1 Get Ready

Similarly to what we did for [Exercise 4](#exercise-4---our-first-data-app-on-pyscriptcom),
we need to duplicate the reference project [template](https://bit.ly/pyscript-template-ch-1)
available on PyScript.com, to automatically transfer the project into
our own dashboard. When that is done, you are ready to code!

Please follow the simple [instructions](#three-simple-steps-to-get-started) to customise, and rename the app
accordingly.

### 🧑‍💻 5.2 Learning to Fly, with Python

In this exercise, we will replicate on of the [examples](https://pyscript.net/examples/) available in the
official PyScript documentation, and currently going under the quite anonymous name of `PyREPL2`.

Let's not spoil anything, and let's start working on the exercise 😊.

First thing first, let's add a new custom file to our PyScript.com project, and let's name this file `antigravity.py`.

> 💡 To add a new file to your PyScript app on PyScript.com, just click on the `+` icon located
> on the top-right corner of the resource manager, that is the leftmost pane window in the project editor.

If you know already the popular [xkcd](https://xkcd.com/) comic (i.e. [353](https://xkcd.com/353/)), you may have already
guessed where this is going.

Let's write the following code in the `antigravity.py` module:

```python
import random

from js import DOMParser, document, setInterval
from pyodide.ffi import create_proxy
from pyodide.http import open_url


class Antigravity:
    url = "https://raw.githubusercontent.com/pyscript/pyscript/main/examples/antigravity.svg"

    def __init__(self, target=None, interval=10, append=True, fly=False):
        self.target = (
            document.getElementById(target)
            if isinstance(target, str)
            else document.body
        )
        doc = DOMParser.new().parseFromString(
            open_url(self.url).read(), "image/svg+xml"
        )
        self.node = doc.documentElement
        if append:
            self.target.append(self.node)
        else:
            self.target.replaceChildren(self.node)
        self.xoffset, self.yoffset = 0, 0
        self.interval = interval
        if fly:
            self.fly()

    def fly(self):
        setInterval(create_proxy(self.move), self.interval)

    def move(self):
        char = self.node.getElementsByTagName("g")[1]
        char.setAttribute("transform", f"translate({self.xoffset}, {-self.yoffset})")
        self.xoffset += random.normalvariate(0, 1) / 20
        if self.yoffset < 50:
            self.yoffset += 0.1
        else:
            self.yoffset += random.normalvariate(0, 1) / 20


_auto = Antigravity(append=True)
fly = _auto.fly
```

Please take a moment to read, and digest the above code, but please don't worry about understanding every single details of
what's going. We will explain everything in due course (i.e. in the next section). 
So, please feel free to take a first glance at it _for now_ 😊.

To integrate this module into our app, we could use once again the `<py-config>` tag.
Remember ? The whole idea of the `<py-config>` element is to specify all the dependencies (remote and or local) of our PyScript
project (_somewhat similar to `pyproject.toml`, ed.), so that the whole app will be consistent, and self-contained.
To do so, we can leverage on the [`[[fetch]]`](https://docs.pyscript.net/latest/reference/elements/py-config.html#local-modules)
section in our `pyscript.toml` configuration file.
The list of local modules to import in our app can be specified using the `files` directive:

```toml
# In pyscript.toml
[[fetch]]
files = ["./antigravity.py"]
```

From this moment onwards, we will be able to import and use the `antigravity` module from our Python code.

Let's now add a new `<py-repl>` into our `index.html` page. In particular, let's add the following two lines
in the main `body` tag of the page:

```html
<py-repl auto-generate="true">
  import antigravity
</py-repl>
```

That's it for the coding part of this exercise.

> 💡 You might have noticed that we didn't touch the `main.py` module at all in this exercise.
> It is because the plan will be to write all the code we want for our app directly into the
> PyREPL element. Therefore, you can even decide to remove entirely the `<script>` tag
> from the `index.html`.

Let's now hit the `Save & Run` button to have a preview of what we
have done! 💫

#### Run the app, interactively

The `index.html` page features a fully-working PyREPL element including the line `import antigravity`.
To execute the code, you could either select the REPL and hit `Shift+Enter` on your keyboard, or
moving with your mouse pointer onto the right side of the element. A green triangle/arrow should appear.
You could click there instead.
Once executed, (A) the `antigravity` module is now available into the Python (global) namespace;
(B) the xkcd comic should appear underneath the PyREPL/cell;
(C) a new REPL element should have appeared immediately under the output of the previous one.
This is the effect of using `auto-generate="true"` as attribute to the `<py-repl>` element.

> 💡 So far, nothing extremely surprising about the xkcd comic, if you knew already the easter-egg
> included in the Python Standard Library. If you have no clue of what I am talking about, let's open
> a new Python interpreter, and type:
> ```python
> import antigravity
> ```
> and see what happens! 😉

[**And Now for Something Completely Different**](https://en.wikipedia.org/wiki/And_Now_for_Something_Completely_Different):
In the newly generated REPL, let's now type:
```python
antigravity.fly()
```

And **that** is something entirely new, even for the ester egg 🎉💫.

### ⚙️ 5.3 How it works

The exercise is indeed composed by two parts, focusing on two features provided by PyScript: the new `<py-repl>` custom
element, and the possibility to include local Python modules into our code.

The only things worth mentioning about the `<py-repl>` element is that, as mentioned,
specifying the [`auto-generate`](https://docs.pyscript.net/latest/reference/elements/py-repl.html#auto-generate)
attribute allows to add another `<py-repl>` tag upon execution.
The other thing to point out from our example is that any Python code that we would add within the `<py-repl></py-repl>`
tags will automatically constitute the content of our cell.

> 💡 If you're familiar with Jupyter notebooks format, you might have noticed lots of similarities with the
> PyREPL element. However, despite their similar aspect, they are indeed two completely different things.
> Let's say that PyREPL is a much simpler object, or by contrast that Jupyter notebooks are not just a collection
> of PyREPL. PyScript `<py-repl>` elements would be comparable to _code-cells_ into a Jupyter notebook.
> In fact, they do just support Python code, and it's not currently possible to write
[Markdown](https://www.markdownguide.org/) into a PyScript REPL.

The custom `antigravity.py` module has been integrated into the PyScript app thanks as local module via
the `<py-config>` element.
What the code of the module intends to do is to _replace_ the `antigravity` module from the Standard library,
with one that apparently works exactly the same way. Until we `fly()` 🤓.

> 💡 If you are wondering how Python imports the custom local module, instead of the one
> with the same name from the Standard library, the answer is in how _Name Resolution_ works
> in Python. On this note, I would strongly encourage to follow up on this very interesting topic
> about Python internals by reading [this article](https://www.python.org/download/releases/2.3/mro/)
> from the official Python doc (and parts of Python 2.3 Release Notes) by Michele Simionato,
> Italian Pythonista, and founding member of the Python Italia Association.

The custom `antigravity` module defines a new class, i.e. `Antigravity` which renders the xkcd SVG when
it gets instantiated (see `Antigravity.__init__`).
A new instance is created on `line 43` of the above code, and this is why when we `import antigravity`, the
instance is created, and so the SVG is rendered.

The way how the SVG is added to the document is very interesting. Here we see a concrete example of the
bi-directional communication PyScript and Pyodide enable between Python and JavaScript.
In fact, from our custom Python code, we are able to import, `from js`, `DOMParser`, `document` and `setInterval` (useful later
with the `fly()` method implementation).

The `DOMParser` class (_`DOMParser.new` is the corresponding object_, ed.) parses the SVG and add a new element in the DOM.
The actual SVG object is gathered from remote URL using
the `pyodide.http.open_url` function, similarly to what we did in
[Exercise 4](#🧑‍💻-42-pandas-in-the-browser-with-pyodide-support).

> 💡 JavaScript to Python Syntax Adaptation
>
> The Object instantiation syntax using the `new` operator in **JavaScript**, for example:
>
> ```javascript
> const parser = new DOMParser(...)
> ```
>
> becomes in Python:
>
> ```python
> parser = DOMParser.new(...)
> ```

If you are used to work with JavaScript, and its OOP model, you may have noticed a slight
difference in how the `DOMParser` object is instantiated in the Python code above. 
In fact, `new` is **not** a reserved keyword statement in the Python language, therefore any 
instruction like `new DOMParser` would be valid Python code that works.
However, whenever we manipulating any JavaScript object in our Python code, we are in fact working with 
`pyodide.ffi.JsProxy` instances. `JsProxy` instances exposes a `new` method
([doc](https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.JsProxy.new))
which construct an instance of its corresponding JavaScript object (e.g. `DOMParser.new`).

The last element to highlight from the `Antigravity` class we have implemented regards its `fly` method.
First, we are leveraging on the built-in JavaScript function `setInterval` to repeatedly invoke the
`Antigravity.move` method (i.e. `self.move` in the code example). Thanks to the `pyodide.ffi.create_proxy`
function ([doc](https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.create_proxy))
we are able to feed in to the JavaScript `setInterval` a generic Python callable (method, in this case).

The last two examples (`cerate_proxy` and `JsProxy.new `) are part of the larger built-in **JavaScript Bridge** 
(see [Architecture](#⚪️🔵⚫️🔴-connecting-the-dots)) PyScript and Pyodide provide to seamlessly **integrate** these
two (quite different) technologies.

### 🎁 5.4 Wrap up

In this exercises we have explored two new features provided by PyScript: the ability to load custom Python modules,
in addition to Python packages; and the `<py-repl>` custom element. 
Our custom module (i.e. `antigravity.py`) has been added to the PyScript application via the `<py-config>` tag, 
and its `[[fetch]]` directive.

Thanks to the `<py-repl>` element, we have been able to integrate a REPL into our
HTML page, that is able to interactively process any Python code we would have available in the app runtime namespace.

In our exercise, we started importing our `antigravity` custom module, and then call `antigravity.fly()`.

While exploring in details the code for our `antigravity.py` module, we had the opportunity to witness first-hand
some of the built-in components (i.e. `JsProxy`, `create_proxy`) Pyodide offers to create a bridged integration 
with the JavaScript language into our Python code. This integration is achieved via the `pyodide.ffi` package.

> 💡 FFI: Foreign Function Interface

#### 🥡 Take away lessons

- The `<py-config>` PyScript tag allows to load any Python custom module
  - We would need to add a `[[fetch]]` section to our configuration
  - We would then use the `files = [...]` directive to list the URLs/Paths of our custom modules to load.
- The `<py-repl>` special tag creates a Pythonic REPL into our HTML page
- The REPL can interact with any code available in the runtime namespace
  - We initialised the REPL with the `import antigravity` statement
- The `<py-repl>` supports a `auto-generate="true"` attribute that would immediately
append to the REPL output, a brand new `<py-repl>` element.
- PyScript and Pyodide provide seamless integration of the Python language (i.e. objects, and functions)
with JavaScript via the `pyodide.ffi` package.
