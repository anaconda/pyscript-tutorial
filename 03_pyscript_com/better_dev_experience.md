## A "dice roll" to improve your development experience in the browser

When using PyScript, writing Python in the browser is as easy as including your Python code
within the `<script type="py">` tag.
Whilst this is more than acceptable when working on _simple_ examples to familiarize with the
new platform, this can easily become an issue when working on much more complicated apps.

Moreover, you might have noticed that there is a complete lack of support from code editors
nor any syntax highlighting when (_suddenly_, ed.) injecting Python code into HTML tags.

🙌 No worries! PyScript got you sorted! Both the `<script type="py">` and the `<py-config>` tags
support the `src` attribute, similar to what one would normally do when importing
[JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) code.

### ⏳ Get Ready

Let's create again an HTML skeleton template which already includes PyScript, namely:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PyScript Dice</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@pyscript/core/dist/core.css">
        <script type="module" src="https://cdn.jsdelivr.net/npm/@pyscript/core"></script>
    </head>
    <body>
        <script type="py">
            <!-- Add your Python code here -->
        </script>
    </body>
</html>
```

Now let's save this new file as `pyscript_dice.html`.
The name should be self-explanatory of what we are trying to achieve in this section.

> ✅ That is all we needed to do to get ready! We are ready to move on to the hands-on part!

### 🧑‍💻 Hands on: Playing with random, and web events

In this Section, we are about to create an interactive app to roll some dice with Python and PyScript.
In particular, we want to specify how many dice (i.e., _number of rolls_) we want to generate, and what is
the number of sides each dice should have.

To do so, let's first modify our HTML template to include these input components.
Let's add the following HTML tags immediately after the PyScript tag:
```html
<div id="roll">
    <label for="n_rolls">Number of Dice rolls (1-100)</label>
    <input type="number" id="n_rolls" min="10" max="100" />

    <label for="n_sides">Number of Dice sides (4-12)</label>
    <input type="number" id="n_sides" min="4" max="12" step="2" />

    <button id="droll_btn">Roll</button>
    <div id="outcome">
    </div>
</div>
```

In our app, we have simply added two `<input type="number">` to include the number of rolls we want to perform, 
and to select the number of sides our dice will have (from `4` to `12`, in our app).

The idea behind the app we are about to build is quite simple.
First, whenever we would be clicking on the button `Roll`, we would like to read the values specified in the two
`input` elements, and roll dice accordingly. The result of each outcome should be added as an HTML list (e.g. `<ul></ul>`)
within the `<div id="outcome">` element. Alternatively, if we would ask for a roll with a wrong, or incomplete input,
and error message should be shown, instead.

Let's now write the Python code to write the logic of what we want to achieve:

```python
from random import randint
from pyscript import when, document


def to_int(value: str) -> int:
    """Simple function to cast a string to an int, in a BAFTP fashion."""
    try:
        int_v = int(value)
    except ValueError:
        return 0
    else:
        return int_v


@when("click", "#droll_btn")
def dice_roll():
    # Select the two input elements
    n_rolls_el = document.querySelector("#n_rolls")
    n_sides_el = document.querySelector("#n_sides")

    n_rolls = to_int(n_rolls_el.value)
    n_sides = to_int(n_sides_el.value)

    if not n_rolls or not n_sides:
        result = "<span style='color:red'>Please check input values</span>"
    else:
        rolls = [f"<li>{randint(1, n_sides)}</li>" for _ in range(n_rolls)]
        result = f"<ul>{''.join(rolls)}</ul>"

    # Select outcome Element
    outcome_el = document.querySelector("#outcome")
    outcome_el.innerHTML = result  # modify innerHTML property

```

Before investigating all the details of our code, let's first try to bluntly copy and paste the code
directly into the HTML template.

The content of the `pyscript_dice.html` file should look like the following:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PyScript Dice</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@pyscript/core/dist/core.css">
        <script type="module" src="https://cdn.jsdelivr.net/npm/@pyscript/core"></script>
    </head>
    <body>
        <script type="py">
            <!-- Add your Python code here -->
            from random import randint
            from pyscript import when, document


            def to_int(value: str) -> int:
                """Simple function to cast a string to an int, in a BAFTP fashion."""
                try:
                    int_v = int(value)
                except ValueError:
                    return 0
                else:
                    return int_v


            @when("click", "#droll_btn")
            def dice_roll():
                # Select the two input elements
                n_rolls_el = document.querySelector("#n_rolls")
                n_sides_el = document.querySelector("#n_sides")

                n_rolls = to_int(n_rolls_el.value)
                n_sides = to_int(n_sides_el.value)

                if not n_rolls or not n_sides:
                    result = "<span style='color:red'>Please check input values</span>"
                else:
                    rolls = [f"<li>{randint(1, n_sides)}</li>" for _ in range(n_rolls)]
                    result = f"<ul>{''.join(rolls)}</ul>"

                # Select outcome Element
                outcome_el = document.querySelector("#outcome")
                outcome_el.innerHTML = result  # modify innerHTML property

        </script>
    </body>
</html>
```

We can arguably conclude that even with a simple examples like the one we are working on,
embedding the Python code directly into the HTML is not ideal, let alone dealing with
code indentation with complete lack of support by the editor.

Let's now modify the HTML code so that everything currently enclosed within the PyScript tag
would be moved and loaded from external files, namely `main.py` using the `src` attribute.

> 💡 Similarly to the `<script type="py">` tag, also the `<py-config>` tag supports loading
> the configuration directives from external resources, via `src`.
> Configuration files can use either [TOML](https://learnxinyminutes.com/docs/toml/) or
> [JSON](https://www.freecodecamp.org/news/what-is-json-a-json-file-example/) syntax.
> The TOML format is the default, and we will be using this throughout the course, as it is
> (a) less verbose than JSON; (b) more intuitive and easier to write; (c) it is the same
> format used to specify [packages metadata](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) (i.e. `pyproject.toml`).

> 💡 Writing your Python code in the `main.py` file will immediately trigger the code support from your editor
> (e.g. syntax highlighting, linting, etc.) as it would be treated as a normal Python file.
> Who cares that this will later be used within a PyScript app.

The final result of the `pyscript_dice.html` file should be as follows:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PyScript Dice</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@pyscript/core/dist/core.css">
        <script type="module" src="https://cdn.jsdelivr.net/npm/@pyscript/core"></script>
    </head>
    <body>
        <script type="py" src="./main.py"></script>
        <div id="roll">
            <label for="n_rolls">Number of Dice rolls (1-100)</label>
            <input type="number" id="n_rolls" min="10" max="100" />

            <label for="n_sides">Number of Dice sides (4-12)</label>
            <input type="number" id="n_sides" min="4" max="12" step="2" />

            <button id="droll_btn">Roll</button>
            <div id="outcome">
            </div>
        </div>
    </body>
</html>
```

> 💡 If you are already familiar with web development, and web standard, you may have probably
> noticed already the similarity with loading JavaScript modules using the same `src`` attribute.


If we now try to open the `pyscript_dice.html` as local HTML file in your browser, something interesting
is going to happen.

Let's open up the JavaScript Console to get additional clues, as always.

> Access to fetch at 'file:///.../main.py' from origin 'null' has been blocked by **CORS** policy: Cross origin requests are only supported for
> protocol schemes: http, data, isolated-app, chrome-extension, chrome, https, chrome-untrusted.

As a matter of facts, loading resources from unknown (`null`) origins when loading local files in the browser
is in violation of the [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (Cross Origin Resource Sharing)
policy of the browser. To be clear, the **same** would have happened if we would have tried to load some local
JavaScript or CSS file.

To circumvent this issue, we need to serve the "external" resource (i.e. `main.py`) as an asset via an HTTP server.

The quickest way to do this locally would be spawning an http server using Python directly, with its built-in
[`http`](https://docs.python.org/3/library/http.server.html) module:

1. Open a Terminal / Command Line / Power Shell (Windows Users);
2. Move to the location where the HTML file `pyscript_dice.html` lives on your hard drive;
3. Run `python -m http.server`.

On this note, it is worth noticing that you would need to have a working Python Distribution installed on
your computer in order to run the above command, and spawn the local server.

If that's not the case, you could consider downloading [Anaconda Distribution](https://www.anaconda.com/download).

> 💡 At this point, it is worth mentioning **another** quite crucial feature of using PyScript and Python in the browser.
> So far we were not using nor relying _at all_ on any local Python distribution (if any!)
> to run the examples. The Python interpreter that runs in the browser on WASM is automatically downloaded
> by PyScript (i.e. `core.js`) when loading the HTML page.
> Therefore, it means that _any_ PyScript app can be easily distributed, without requiring users to install and configure
> Python on their computers!
>
> In other words: PyScript apps are **self-contained**.

> 💡 Another important lesson we can derive from the previous example is that we would not
> need much infrastructure to _deploy_ a PyScript application. Anything that would simply be
> able to serve HTML pages (e.g. [GitHub Pages](https://pages.github.com/)) would do.

If you were able to spawn the local server via Python
(_or using any other HTTP server of your choice instead_, ed.) you should now see the app loading and
fully working!

You can now insert the numbers in the input (e.g., 3 rolls, of 6-sides die), click on _Roll_, and random
dice outcome will appear! 🎉

### ⚙️ How it works: CORS, FFI, and DOM

It's now finally time to dive into the details of our code, to learn how this simple 
PyScript app works.

First, let's get the simple (pure) Python function `to_int` out of the way.
The only relevant thing to mention about it is that it is a function that attempts
an hard-casting to an integer of a (possibly empty) string value.
This is achieved using a `BAFTP` (i.e. _Better Ask Forgiveness Than Permission_) fashion, attempting a conversion and catching any `ValueError` exception that
may rise. This programming pattern is generally preferable over a series of `if`-clauses.

The `dice_roll` Python function is the core of our logic.
First, we use the `when` decorator provided by PyScript (see the `import` statement on `Line 2`) which
allows to easily mark a Python function as an event handler.
In this case we are marking the `dice_roll` function as the handler for the `click` (i.e., `on_click`)
event for the button `#droll_btn`.

Secondly, we are using the `document` object (again, imported from PyScript), which allows
direct access to the DOM. In fact, this `document` object is part of the `FFI` (_Foreign Function
Interface_) that PyScript provides to seamlessly interact with the JavaScript interpreter
in the browser, and the DOM of the current document. In particular, this `pyscript.document`
In our example, we have used `document` to select the `<input>` elements on the page, and gather
their values (via the `.value` attribute).
Finally, the outcome of the dice rolls is dynamically injected in the web page via the `innerHTML`
attribute of the target `<div id="outcome">`.

### 🎁 Wrap up

In this example we learnt how to use PyScript to create a simple interactive web app for dice rolls.
By doing so we discovered two new PyScript elements, namely `when` and `document`.
The former is used as a decorator to convert any Python function as an event handler, while the
latter provides access to the DOM to select and manipulate the content of the current document.

We also learnt a very important best practice when developing with Python in browser:
_keeping Python and HTML separated in different files_ improves the coding experience,
enabling the support of your editor.
This is achieved via the `src` attribute supported by the PyScript `<script type="py">` tag.

In this way, we could rely on full support from our code editor (syntax highlighting,
code indentation) when we write Python code (_as we would normally do_, ed.), that will be later
used within our PyScript app. The same applies for configuration directives with the `<py-config>`
tag. However, in order to load these "external" local resources, we need to serve the app with an
HTTP server (e.g. `python -m http.server` for local development, or `GitHub Pages`).


Moreover, writing an external Python module would also help in making the code more
maintainable, as it would normally be when developing generic Python applications.
However, the simplicity in getting started and the natural ease of use of PyScript now
meets the "complications" of Web standards.

To be clear, CORS policy restriction do exist for a very good
[security reason](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)!

Nonetheless, we would be needing to set up and run an Http server to work with PyScript.

Luckily, there is an alternative and **better** way to develop, distribute, and share your PyScript apps: 
[PyScript.com](https://pyscript.com).


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

In this section, we have been working to create exactly the same structure on our local computer.
With PyScript.com, you can have all that with just one click, and _you are ready to go!_.

The integrated editor has full support for both HTML/JavaScript and Python programming.
By simply clicking the **Run** button, you can immediately see a Preview of how your 
PyScript application would look like!.

PyScript.com is indeed easy to use, and absolutely perfect to get started with
PyScript as it completely lowers the barrier to set up your coding environment and infrastructure.

> 💡 From now on, we will be using directly PyScript.com to work on the exercises, 
> using this [template](https://bit.ly/pyscript-template-ch-1)
> So please [sign up](https://pyscript.com) to create your account.


### 🥡 Take away lessons

- PyScript tags `<script type="py">` and `<py-config>` can leverage on their `src` attribute to load external resources.
- Using external `main.py` and/or `pyscript.toml` enables better development experience when working with PyScript.
- This would keep HTML and Python resources separated, and would leverage on the full support of
your code editor.
- The `<py-config>` tag supports TOML (default) and JSON formats.
- Loading local files when loading external resources violates CORS browser policy.
- An HTTP server is required to workaround the CORS issue.
- Deploying a PyScript app does not require much infrastructure - just serving HTML pages. No server-side technology!
- (last but not least) PyScript **does not** require to have Python installed on your computer!
- **PyScript apps are self-contained**:
  - You can distribute your HTML PyScript app without requiring users to install anything on their end.
  Not even Python!.
  - The `<py-config>` tag configures the PyScript app, including external dependencies to be downloaded
  and installed.
