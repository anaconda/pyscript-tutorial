## Your browser is your most ubiquitous computing platform

Python is nowadays the most popular programming language, according to the
[TIOBE](https://www.tiobe.com/tiobe-index/) and the
[PYPL](https://pypl.github.io/PYPL.html) programming community indices; and
the data science domain is where Python finds its broader adoption.

Web browsers, on the other hand, are the most ubiquitous software.
Any computer, laptop, smartphone, or any device with access to the internet integrates
a web browser. Therefore, if we could have the possibility to integrate directly into
the browser Python's numerical processing capabilities, along with its huge ecosystem
and libraries, we would open up to completely new scenarios for data science.

The first thing that comes in mind when thinking to numerical processing with Python is
[NumPy](https://numpy.org). NumPy, namely "Numerical Python", is the core library and
de-facto standard for all data science packages in the scientific Python ecosystem.

In this chapter, we will explore how it could be possible to 
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


### ⏳ Get Ready

To get starter, let's **duplicate** our PyScript App 
[template](https://pyscript.com/@leriomaggio/pyscript-app-template/latest)
by clicking on the "Clone Project <svg viewBox="0 0 32 32" width="1.2em" height="1.2em" class="-rotate-90 text-base sm:text-sm"><path fill="currentColor" d="M26 18a3.996 3.996 0 0 0-3.858 3H17V11h5.142a4 4 0 1 0 0-2H17a2.002 2.002 0 0 0-2 2v4H9.858a4 4 0 1 0 0 2H15v4a2.002 2.002 0 0 0 2 2h5.142A3.993 3.993 0 1 0 26 18Zm0-10a2 2 0 1 1-2 2a2.002 2.002 0 0 1 2-2ZM6 18a2 2 0 1 1 2-2a2.002 2.002 0 0 1-2 2Zm20 6a2 2 0 1 1 2-2a2.002 2.002 0 0 1-2 2Z"></path></svg>" button.

Once it's done, let's rename the new app as "3D voxel plot with NumPy", and then let's 
update the app metadata, accordingly:
> 3D Plotting with NumPy and Matplotlib with PyScript & Pyodide.

Similarly, please update the metadata contained in the `pyscript.toml` file.

In this app, we will demonstrate how it is possible to (dynamically) generate 3D plots using
NumPy and [Matplotlib](https://matplotlib.org/) running in the browser, via PyScript.

> 💡 If you are not familiar with these two Python libraries, don't worry! 
> It is completely fine, and it won't be necessary to have previous experience with these
> packages to work on our app! Also, we will explain in details the crucial parts of our 
> implementation in the How-to section. Let's just say that NumPy and Matplotlib are the
> two most popular, and essential libraries in the Python scientific ecosystem.
> We will see them in action in the browser working in a new way, integrating with the
> interactive and _asynchronous_ nature of the browser environment.

> ✅ Perfect! We are now ready to move on to the hands-on part!

### 🧑‍💻 Hands on: Interactive 3D Voxel Plots

First, let's create the skeleton of our HTML page. To do so, let's replace
the `<!--  Add HTML TAGS here -->` placeholder with the following:
```html
<div class="row">
  <div class="col">
      <h3 class="display-3">3D Plot with PyScript</h4>
      <div id="plot">
          <div></div>
      </div>
  </div>
</div>
<h3 class="display-4">Configure Cube</h3>
<div class="row">
  <div class="col-4 p-3">
      <div class="input-group">
          <label for="x_dim" class="form-label">X:</label>
          <input type="range" class="form-range" min="1" max="15" step="1"
                  value="3" id="x_dim" oninput="this.nextElementSibling.value = this.value" disabled>
          <output class="form-control">3</output>
      </div>
  </div>
  <div class="col-4 p-3">
      <div class="input-group">
          <label for="y_dim" class="form-label">Y:</label>
          <input type="range" class="form-range" min="1" max="15" step="1" 
                  value="3" id="y_dim" oninput="this.nextElementSibling.value = this.value" disabled>
          <output class="form-control">3</output>
      </div>
  </div>
  <div class="col-4 p-3">
      <div class="input-group">
          <label for="z_dim" class="form-label">Z:</label>
          <input type="range" class="form-range" min="1" max="10" step="1" 
                  value="3" id="z_dim" oninput="this.nextElementSibling.value = this.value" disabled>
          <output class="form-control">3</output>
      </div>
  </div>
  <div class="col-6 p-3">
      <div class="input-group mb-3">
          <label for="border_color" class="form-label">Outside Cubes Edge Color:</label>
          <input type="color" name="border_color"  
                  class="form-control form-control-color" 
                  id="border_color" value="#BFAB6E" 
                  title="Choose the color of cubes on the outside edges"
                  disabled
            />
      </div>
      <div class="input-group mb-3">
          <label for="inner_color" class="form-label">Inside Cubes Edge Color:</label>
          <input type="color" name="inner_color"  
                  class="form-control form-control-color" 
                  id="inner_color" value="#7D84A6"
                  title="Choose the color of cubes on the inner edges"
                  disabled
          />
      </div>
  </div>
</div>
<div class="row">
  <div class="col">
      <input class="btn btn-primary" type="button" id="btn_gen" value="Generate Plot" disabled />
      <input class="btn btn-secondary" type="button" id="btn_reset" value="Reset" disabled />
  </div>
</div>
```

At this point, I would recommend to click on the `Save` 
button, and then the `Run` button to see the result.

The content of the page is basically organized in two main sections. On the
top there is the placeholder where the plot will be displayed, once generated
by our Python code (_that we are going to write next_, ed.). This placeholder
is identified by the element with id `plot`: `<div id="plot">...</div>`.
The other part of the page contains several components to configure the 
voxels we want to generate in our 3D plot. In particular, we can choose how
many voxels we will generate per each axis (i.e., `x`, `y`, and `z`), and
the edge colors of voxels on the outside border, and the internal ones.
All the components are automatically set to default values, with `3` cubes
per each axis, and with default colors of the (_old_, ed.) NumPy
[logo](https://commons.wikimedia.org/wiki/File:NumPy_logo.svg).
Now it's time to move to implement the logic in Python.

> 💡 You may have noticed that all the interactive components in our page,
> i.e., slides, color pickers, and buttons, are _disabled_ by default.
> We will discuss this later in the `⚙️ How it works` section.

The first thing we are going to try is to open the `main.py`
and add this simple line of code in the code:

```python
import numpy as np
```

Now, let's **save** and click **Run** to see if that works...💥

You should get the Python [Traceback](https://docs.python.org/3/library/traceback.html) 
as the one reported below:

```bash
Traceback (most recent call last):
  File "/lib/python311.zip/_pyodide/_base.py", line 499, in eval_code
    .run(globals, locals)
     ^^^^^^^^^^^^^^^^^^^^
  File "/lib/python311.zip/_pyodide/_base.py", line 340, in run
    coroutine = eval(self.code, globals, locals)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<exec>", line 1, in <module>
ModuleNotFoundError: The module 'numpy' is included in the Pyodide distribution, but it is not installed.
You can install it by calling:
  await micropip.install("numpy") in Python, or
  await pyodide.loadPackage("numpy") in JavaScript
See https://pyodide.org/en/stable/usage/loading-packages.html for more details.
```

First thing to highlight here is: **Error Handling**.

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

PyScript (and then of course, the Pyodide interpreter that is running on WASM) is reporting (line `1`) that
our code is trying to import a `numpy` module that
cannot be found because (A) it is not part of the Pyodide distribution
(i.e. the _Python Standard library on WASM_, ed.), and (B) it is **not installed**!
It then continues (Lines `3-5`) showing how to _install_ a package using Pyodide APIs.

The first important take-away message is that only the Python Standard Library
is available by default, when using the Pyodide interpreter via PyScript.
To use any other package, one would need to load them separately.

Luckily, Pyodide supports the installation of external packages using
[`micropip`](https://micropip.pyodide.org/en/v0.2.2/project/usage.html#installing-packages-with-micropip),
and PyScript has direct
[integration](https://micropip.pyodide.org/en/v0.2.2/project/micropip-in-other-projects.html#pyscript) with `micropip`.

To declare the dependencies in our PyScript app we would just need to include the `packages` directive within the 
`pyscript.toml` configuration files:

```
packages = ["numpy", "matplotlib"]
```

> 💡 Let's also include `matplotlib` to the list of our packages, as we already know we will 
> require Matplotlib for our app!

> 💡 If we run our PyScript code using the MicroPython interpreter (`<script type="mpy">`)
> the `packages` directive in the configuration will be ignored, as MicroPython currently 
> does not support external packages, or similar technologies like `micropip` in Pyodide.

If we now **save** and **run** our app, the import error will work! 
We will discuss this in more details in the next `⚙️ How it works` 
section.

> 💡 PyScript configurations can use either [TOML](https://learnxinyminutes.com/docs/toml/) or
> [JSON](https://www.freecodecamp.org/news/what-is-json-a-json-file-example/) syntax.
> The TOML format is the default, and we will be using this throughout the course, as it is
> (a) less verbose than JSON; (b) more intuitive and easier to write; (c) it is the same
> format used to specify 
> [packages metadata](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) 
> (i.e. `pyproject.toml`).

A best practice when developing with Python is to organize
your code into multiple modules, namely `.py` files.
Each Python module would contain their own set of functions and objects 
that are logically related, and can be used by other modules via `import`
statements. The same principle can be similarly applied to PyScript apps!

By default, all the apps on pyscript.com include a `main.py` module, which
is automatically referenced by the `<script type="py">` via the `src`
attribute. We would now need to understand how it would be possible to
avoid writing _everything_ inside the `main.py`, but instead modularize
our implementation across multiple `.py` files.

In the case of our app, we would ideally want to keep all the logic to
generate the 3D voxel plot data (using `numpy`), from the code
to manipulate the DOM, and program widgets' interactions (using `pyscript`).

Let's create then a new `cubes.py` module in our PyScript app. To do so,
please click on the "New File" button (identified by a `+` icon in top right
corner of the leftmost editor pane).
If you now click on the file, the `cubes.py` module will appear as a new tab 
in the code editor.

Let's now write the code for our `cubes.py` module:
```python
# cubes.py
import numpy as np
import numpy.typing as npt
from itertools import permutations, combinations_with_replacement
from dataclasses import dataclass


@dataclass
class CubeOpts:
    x: int = 3
    y: int = 3
    z: int = 3
    border_col: str = "#BFAB6E"
    inner_col: str = "#7D84A6"

    @property
    def shape(self):
        return (self.x, self.y, self.z)

    @staticmethod
    def _upscale(data: npt.ArrayLike):
        size = np.array(data.shape) * 2
        data_e = np.zeros(size - 1, dtype=data.dtype)
        data_e[::2, ::2, ::2] = data
        return data_e

    def _mark_borders(self):
        def to_slice(t):
            pos, ax = t
            return ax if ax != ":" else slice(0, self.shape[pos])

        data = np.zeros(self.shape, dtype=bool)
        boundaries = combinations_with_replacement([0, -1], r=2)
        for x1, x2 in boundaries:
            indices = permutations([x1, x2, ":"], r=3)
            for axes in indices:
                x, y, z = tuple(map(to_slice, enumerate(axes)))
                data[x, y, z] = True

        return data

    @staticmethod
    def _get_indices(shape: tuple):
        x, y, z = np.indices(np.array(shape) + 1).astype(float) // 2
        # Shrink the gaps
        x[0::2, :, :] += 0.05
        y[:, 0::2, :] += 0.05
        z[:, :, 0::2] += 0.05

        x[1::2, :, :] += 0.95
        y[:, 1::2, :] += 0.95
        z[:, :, 1::2] += 0.95
        return x, y, z

    def generate_voxels(self):
        # build up the numpy logo
        n_voxels = self._mark_borders()
        facecolors = np.where(n_voxels, "#FFD65DC0", "#7A88CCC0")
        edgecolors = np.where(n_voxels, self.border_col, self.inner_col)
        filled = np.ones(n_voxels.shape)

        # upscale the above voxel image, leaving gaps
        filled = self._upscale(filled)
        fcolors = self._upscale(facecolors)
        ecolors = self._upscale(edgecolors)
        indices = self._get_indices(filled.shape)

        return indices, filled, fcolors, ecolors

```

The first thing we may notice about this module is that it does not have 
any specific PyScript dependency (see `import` statements on the very top).

Therefore, the `cubes.py` module would be no different if we were running
our code in a desktop app instead of the browser!
This is quite an important feature of the PyScript platform to highlight.
And even more so if using the default Pyodide interpreter, thanks to
packages support via `micropip`, and an almost complete port of the Python standard library.

> 💡 You may have noticed that some of the methods in the `CubeOpts` data class
> are named with an initial `_`. If you did, well done!
> These methods are intended to be part of the _internal_ (private) class API
> and so not to be used in code that is not part of the class implementation
> itself. This is a standard convention in Python to differentiate the private
> from the public API of a class. In other languages (e.g., C++ or Java) this
> distinction is clearly marked by dedicated keywords, and language constructs:
> `private` and `public`. Python does not have similar constructs, so the
> distinction is made via naming conventions.
> If you are interested in more conventions, and coding style in Python, I would
> strongly recommend reading [`PEP8`](https://peps.python.org/pep-0008/):
> "Style Guide for Python Code".


The module defines a `CubeOpts` dataclass which encapsulates the parameters
(and default values) for cubes settings, along with the logic to generate the 3D 
voxels, i.e., the `CubeOpts.generate_voxels()` method.

Now, in order to use the `cubes.py` module in our app, we need to _configure_ it within
our app. 

> 🎮 If you are curious, you could first try adding an import statement in `main.py`, 
> e.g., `from cubes import CubeOpts`, and see what happens. Please also remember to keep
> the JavaScript console open.


To add Python modules dependencies for our app, we need to add a new `files` directive
in the `pyscript.toml` file, under the `[[fetch]]` section:

```
packages = ["numpy", "matplotlib"]

[[fetch]]
files = ["./cubes.py"]
```

Please note that there can be multiple `[[fetch]]` sections in the configuration,
each with their own specific rules to configure _any resource_ we wish to
bundle with our app. Please refer to the PyScript [documentation](https://docs.pyscript.net/2023.09.1.RC2/user-guide/#files)
for further details on supported configuration options.

Let's now finish our implementation by writing the `main.py` module:
```python
import matplotlib
from matplotlib import pyplot as plt
from pyscript import when, display, document
from pyodide.ffi import create_proxy
from cubes import CubeOpts

matplotlib.use("agg")


def gather_cube_options() -> CubeOpts:
    """Collect all settings from page and instantiate a new CubeOpts object"""
    x = int(document.getElementById("x_dim").value)
    y = int(document.getElementById("y_dim").value)
    z = int(document.getElementById("z_dim").value)
    border_col = document.getElementById("border_color").value
    inner_col = document.getElementById("inner_color").value
    return CubeOpts(x=x, y=y, z=z, border_col=border_col, inner_col=inner_col)


@when("click", "#btn_gen")
@when("change", "input[type='range']")
def generate_plot():
    cube_opts = gather_cube_options()
    (x, y, z), filled, fcolors, ecolors = cube_opts.generate_voxels()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.voxels(x, y, z, filled, facecolors=fcolors, edgecolors=ecolors)
    ax.set_aspect('auto')
    display(fig, target="plot", append=False)


@create_proxy
def reset_configs(event):
    event.preventDefault()
    default_opts = CubeOpts()
    sliders = document.querySelectorAll("input[type='range']")

    for axis, slider in zip(("x", "y", "z"), sliders):
        def_axis = getattr(default_opts, axis)
        slider.value = def_axis
        slider.nextElementSibling.value = def_axis
    document.getElementById("border_color").value = default_opts.border_col
    document.getElementById("inner_color").value = default_opts.inner_col
    document.getElementById("btn_gen").click()


btn_reset = document.getElementById("btn_reset")
btn_reset.addEventListener("click", reset_configs)


def enable_all_input_components():
    # Enable all input components for interactivity
    input_components = document.querySelectorAll("input")
    for component in input_components:
        component.disabled = False

enable_all_input_components()
```

> ✅ The code of our app is ready. If you hit save, and run it will be working! 🎉

Every time you click on "Generate Plot" button, or interact with the sliders,
a new 3D Voxel plot will be displayed on the page, generated by NumPy and Matplotlib.
If you click on the "Reset" button, all the components are automatically set to their
default values, and the default plot is generated.

It's time now to discuss how the app works, and learn more about some other
new cool features of PyScript.

### ⚙️ How it works: Pyodide Packaging 📦, interactivity, and FFI with Pyodide

First, let's focus on the packages, and the **unique** ability of Pyodide to automatically
install Python packages, and to make them running on WASM.

AS briefly mentioned in the previous section, Pyodide includes a mechanism to install 
external packages called `micropip`.

At this point, you may be wondering if _any_ Python package could be _downloaded_
and imported in the browser. If that was the case: well done indeed! 👏
That is a genuinely good question!

The short answer to that question though is: _Not quite!_.

First, let's remember that the last layer in our multi-layered architecture on which 
the PyScript platform operates ends with `WASM`.
From a mere Python-packaging perspective, WASM would be no different than any other 
target compile architectures, e.g., `x86` or `arm`.

> 💡 The key here is on the **instruction set**, and not on any specific hardware; 
> and admittedly these two concepts sometimes tend to be confused, and treated 
> as the same thing. For example, the `arm` instruction set maps to 
> ARM/ARM-based processors.

However, **not all Python packages** require a target architecture. 
This is only the case of packages with external C dependencies
(i.e. part of their code base include external C/C++ libraries).

Python-only packages can run on every CPU architecture/instruction set
(i.e., 
[`none-any`](https://packaging.python.org/en/latest/specifications/binary-distribution-format/?highlight=%22none-any%22#installing-a-wheel-distribution-1-0-py32-none-any-whl)),
and therefore they can run on `WASM` too!!

So, we are indeed capable of _loading_ **any** Python-only package in our PyScript application!

> 💡 There's more!
> In the `packages` directive of the `pyscript.toml` configuration file we can either 
> include the name of a package we want to use,
> or a URL of the Python wheel we want to install (e.g. from PyPI).
> If a name is specified, the underlying Pyodide/micropip will be automatically searching for
> the package name on PyPI and download it!

And what about other Python packages?
In facts, **the majority** of Python packages for numerical and scientific computing have external
C-dependencies to boost the performance, `numpy`, and `matplotlib` included!! So, how does it work?

The good news is that Pyodide has a very _long_ 
[list of packages](https://pyodide.org/en/stable/usage/packages-in-pyodide.html) already included in the 
distribution, compiled for the `WASM32` target, and ready to use!.
This list includes a lot of (_but it is not limited to_, ed.) the _most popular_ packages
for data science, like `pandas`, `scikit-image`, `scikit-learn`, `numpy`, and `matplotlib`.

So what _really_ happened when we included the `packages = ["numpy", "matplotlib"]` in our configuration
was that underneath Pyodide was **loading** the pre-built `numpy` package included in the distribution.

> 🎮 In order to understand better what is actually happening under the hood, let's try to _refresh_ the page, 
> and look at the messages in the JavaScript console. 
>
> The relevant (`log`) messages you should be seeing in the console are:
>
```bash
Loading numpy, matplotlib, ... matplotlib-pyodide
```

Now, let's focus on the logic of the app, and how PyScript enables some very cool integrations.
First, you may have noticed that all the HTML components are initially disabled, until the app 
finishes loading.
This has been done **on purpose**, since bootstrapping the Pyodide interpreter, plus the
(_not so light_) additional packages we need to download and install (i.e. NumPy and Matplotlib),
would require some extra time.

In fact, if you notice some delay the first time you run the app, it's because of all the downloads 
happening in background. Future executions though will be much faster as the Pyodide interpret
it's downloaded once, and then stored in the browser cache.

Therefore, to improve the user experience of our app, all the components are dynamically enabled
when the rest of our code has run. This is done by the `enable_all_input_components` functions 
defined in `main.py` (lines `51-57`).

At a first glance, the code in the `main` module contains all functions to program the interactivity
of our app. Anything that is instead more related to the actual Python/NumPy logic is demanded to
`cubes` module. As already mentioned, similar distribution of functionalities and responsibilities 
across multiple Python modules is a best development practice for PyScript apps.

The two main functions that control the interactivity of the widgets are `reset_configs`, 
and the `generate_plot`, mapped to the "Reset" button and the "Generate Plot" button, respectively.
These functions have been programmed as event handlers using two alternative methods: the former
adopts **Pyodide-specific** APIs, while the latter uses PyScript (higher-level) APIs. 
These two approaches have been intentionally included in the example to showcase how PyScript 
provides more intuitive and more _pythonic_ APIs over the underlying interpreters.

First, the `reset_configs` function, is decorated by the
[`create_proxy`](https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.create_proxy),
function, imported from the [`pyodide.ffi`](https://pyodide.org/en/stable/usage/api/python-api/ffi.html) package. This function is necessary to convert a Python function into a JavaScript callable
proxy in order to be used as handler in combination with the `addEventListener` function 
(see lines `47-48`)

The `generate_plot` function, on the other hand, adopts the `@when` decorator imported directly
from `pyscript`. This decorator expects the JavaScript event as first parameter (e.g. `click`, or
`change`), and a valid `selector` to be used internally by `document.querySelectorAll`.
In our example we provide the `id` of the "Generate Plot" button (i.e. `#btn_gen`), as well as
a selector for all input widgets of `type=color` (i.e. `input[type="color"]`).
With this simple decorator we abstracted from low-level details in our code (i.e., PyScript will 
automatically create the `JSProxy` callable object for us, as required by Pyodide) a avoided
boilerplates with a much more intuitive solution.

> 💡 At the time of writing, the `when` decorator is only supported with the Pyodide interpreter.
> When this will also become available with MicroPython, using the `@when` decorator would also
> guarantee portability of our app across multiple interpreters.

As a result, every time we click on the "Generate Plot" button, or we interact with any of the
three sliders, the `generate_plot` function will be invoked, which in turn instantiate the
`CubeOpts` instance, plots the generated voxels using `matplotlib` APIs, and add the graph to
the document using the PyScript `display` function. The `append=False` parameter is used so that
each time the old plot will be replaced by the newly generated one.

### 🔍 Runtime Threads, Interactivity, and Blocking Calls

The last thing worth mentioning regards interactivity, and how the execution of the Python code
that runs in the browser really works.

If we try to move the sliders towards the end of their scales (e.g. `x=14`, `y=14`, `z=10`) we will
notice a certain delay from the moment we set the value, and the moment when the plot is finally
displayed.

This is because the code that is running in our browser to generate this enormous amount of 3D
cubes would need **extra time** to complete.
Well, we are just saying that "more computation requires more completion time".
And to be fair, if we would try to run the same code on our desktop (i.e., and not inside the browser), 
it would similarly take some time to generate the plot.
_So far, so good_. Nothing particularly surprising here.
Unless, we would focus on the responsiveness of our app, while our code is running!

Moving the sliders to higher values was indeed just the excuse to make the computation heavier, 
so to highlight the issue.

You may have noticed that the whole page _freezes_ until the plot is generated.
If you haven't noticed that, please try to have a look at the slider widget while the code is running:
it is automatically disabled by the browser, and becomes enabled again when the plot is displayed.

This happens automatically, and it is due to the fact that our Python code gets executed directly in 
the _main thread_, where also the rest of the normal execution of the browser is also happening. 
So the code is serialized in the main thread, and the browser sets itself in busy waiting 
until our code is finished!
This behavior is certainly not ideal!

Luckily the web has solved this issue already, using 
[Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers).

Web Workers are a simple means for any web content to run execution in background threads, without
**blocking** nor interfering with the _main thread_.

This looks **exactly** what we would need to solve our "UI-freeze" issue 🎉.
And now for the _really_ interesting part! If you want your Python script to run in a web worker,
simply add the attribute `worker` to the `<script type="py">` tag:

```html
<script type="py" src="./main.py" config="./pyscript.toml" worker></script>
```

If you **save** and **run** the app after the change, you will notice that the page will
not freeze anymore, as each call to our Python code will be _non-blocking_.

> 💡 Support for Python Web Workers (i.e., web workers that can run Python code) is indeed part of the **new** 
> main features introduced in the latest release of PyScript (along with support for multiple interpreters)!
> An in full PyScript-style, the feature is offered to the user to be _straightforward_ to use, and _simple_
> to understand! All the low-levels, and internal technicalities are handled by the platform itself.

### 🎁 Wrap up

In this Chapter we worked on a PyScript app to dynamically generate 3D voxel plots
using the NumPy and Matplotlib packages.

We explored how it is possible to include external (Python)
dependencies into our PyScript application thanks to the Pyodide
built-in `micropip` feature, as well as custom Python modules.
These are possible thanks to the `packages` and the `files` directives in the `pyscript.toml`
configuration files.

We also learned two alternative ways to program the interactivity with HTML widgets using
either Pyodide low-level APIs, and the PyScript `@when` decorator. Using the `@when`
decorator we could appreciate how PyScript allows to abstract from lower-level
details in our Python code, avoiding useless boilerplate.

Last but not least, we discovered a **new** and very easy option PyScript has introduced
to support Web Workers. We first emphasized the issue of running our (heavy) computation
directly in the main thread, and then we just added the attribute `worker` to the 
`<script type="py">` tag, and that is done!

### 🥡 Take away lessons

- PyScript apps can be modularized by distributing the code across multiple modules (`.py` files).
- Adding custom modules to a PyScript app would be as easy as adding `files=[...]` directive
in the `pyscript.toml` configuration file.
- PyScript also allows to declare (external) dependencies via the `packages` directive.
- The PyScript config tag directly integrates with `micropip.install` module of Pyodide to
install external dependencies.
- Any pure Python package can be _installed_ and used in the browser.
- Python packages with external C-dependencies (e.g. `numpy`) can only be used if there exist corresponding
Python wheels packages targeting the `wasm32` instruction set.
- Pyodide includes a very long list of [supported packages](https://pyodide.org/en/stable/usage/packages-in-pyodide.html), 
built-in within the Python distribution.
- This list of Pyodide packages includes the majority of the most popular Python packages in the pydata stack.
- (At the time of writing) The `packages` directive with the MicroPython interpreter is
simply ignored, as MicroPython does not allow installing external packages.
- PyScript provides the `@when` decorator to be used to automatically transform any Python function
into a JavaScript proxy event handler.
- To program a JS proxy using Pyodide lower-level APIs we need to use `pyodide.ffi.create_proxy`,
and manually attach the handler to the event.
- We expanded on threads, and exacution in the browser, and we learnt how easy is to enable
the execution of our code into Web Workers.
- Web Workers are a simple means for web content to run execution in background threads, without
**blocking** nor interfering with the _main thread_.
- To enable worker execution it would be just needed to add the `worker` attribute to the 
`<script type="py">` element.
