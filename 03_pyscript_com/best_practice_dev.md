## Interactive Apps and FFI

When using PyScript, writing Python in the browser is as easy as including your Python code
within the `<script type="py">` tag.
Whilst this is more than acceptable when working on _simple_ examples to familiarize with the
new platform, this can easily become an issue when working on much more complicated apps.

Moreover, you might have noticed that there is a complete lack of support from code editors
nor any syntax highlighting when injecting Python code directly into HTML tags.

🙌 No worries! PyScript got you sorted! Both the `<script type="py">` and `<script type="mpy">`
tags support the `src` attribute to specify the URL to a Python file, similarly to what we would
normally do when importing [JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) code.

For this reason, the default structure of a PyScript app on pyscript.com includes three separated assets, 
namely `index.html`, `main.py`, and `pyscript.toml`, for HTML, Python, and app configurations, respectively.
This favors best development practice, with a clear separation of concerns (_and technologies_, ed.), along
with maximizing code editor's support for a better development experience.

In this chapter, we are about to create an interactive app to roll some dice with Python and PyScript.
In particular, we want to specify how many dice (i.e., _number of rolls_) we want to generate, and what is
the number of sides each dice should have.
This will be the opportunity to learn how to program the interactivity (e.g. `on_click`) in our apps, and
what features PyScript provides to integrate with the DOM, and 
JavaScript [event handling](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events).

### ⏳ Get Ready

To get starter, let's **duplicate** our PyScript App 
[template](https://pyscript.com/@leriomaggio/pyscript-app-template/latest)
by clicking on the "Clone Project <svg viewBox="0 0 32 32" width="1.2em" height="1.2em" class="-rotate-90 text-base sm:text-sm"><path fill="currentColor" d="M26 18a3.996 3.996 0 0 0-3.858 3H17V11h5.142a4 4 0 1 0 0-2H17a2.002 2.002 0 0 0-2 2v4H9.858a4 4 0 1 0 0 2H15v4a2.002 2.002 0 0 0 2 2h5.142A3.993 3.993 0 1 0 26 18Zm0-10a2 2 0 1 1-2 2a2.002 2.002 0 0 1 2-2ZM6 18a2 2 0 1 1 2-2a2.002 2.002 0 0 1-2 2Zm20 6a2 2 0 1 1 2-2a2.002 2.002 0 0 1-2 2Z"></path></svg>" button.
The clone project is a feature offered by pyscript.com to fork an existing app, and bring its copy into your 
own dashboard, so you can start working on it, independently.

Once done, let's first rename the app as "PyScript Dice", and let's modify it's metadata accessible via the 
gear icon on the top-right toolbar.
Feel free to write any short description to your app, such as:
> An interactive App to roll dice with PyScript and Micropython.

Click on the **Update** button to save project's settings.

Now, please open the `index.html` file, and update the `<title>` tag with a more appropriate
`PyScript Dice`.

> ✅ That is all we needed to do to get ready! We are ready to move on to the hands-on part!

### 🧑‍💻 Hands on: Playing with random, and web events

First, we setup our HTML page with all the required components, and then we will move to
program the core logic in Python.

First, let's modify from the template the default Python interpreter by switching to
MicroPython.
This is how the `<script>` tag should look like:

```html
<script type="mpy" src="./main.py"></script>
```

> 💡 Why using Micropython in this app ?
> 
> _Well, why not ?_ In this app, we won't need any specific feature Pyodide provides,
> and Micropython is blazing fast (and lighter to download).
> Instead, this will be an amazing opportunity to showcase how the PyScript platform seamlessly 
> supports the two interpreters by allowing the **same** code to run equally on both interpreters.
> 

Right after the `<script type="mpy">` tag, let's add the following HTML elements:

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

We have two `<input type="number">`, to include the number of rolls we want to perform, 
and to select the number of sides our dice will have (from `4` to `12`, in our case), and a 
`Roll` `<button>` to start rolling.
The outcome generate - by Python, of course - will be added to the document as an HTML list
(e.g. `<ul></ul>`), displayed within the `<div id="outcome">` tag.
Alternatively, a misconfiguration in the values of the input (e.g. incomplete inputs)
would result in an error message, instead.

Let's now write the Python code in `main.py`:

```python
from random import randint
from pyscript import document


def to_int(value: str) -> int:
    """Simple function to cast a string to an int, in a BAFTP fashion."""
    try:
        int_v = int(value)
    except ValueError:
        return 0
    else:
        return int_v


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

Finally, we need a way 



You can now insert the numbers in the input (e.g., 3 rolls, of 6-sides die), click on _Roll_, and random
dice outcome will appear! 🎉

### ⚙️ How it works: the `document` object, and the `@when` decorator

It's now finally time to dive into the details of our code, to learn how this simple 
PyScript app works.

First, let's get the simple (pure) Python function `to_int` out of the way.
The only relevant thing to mention about it is that it is a function that attempts
an hard-casting to an integer of a (possibly empty) string value.
This is achieved using a `BAFTP` (i.e. _Better Ask Forgiveness Than Permission_) fashion, 
attempting a conversion and catching any `ValueError` exception that
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

PyScript.com is a **free** and flexible coding environment specifically designed to get
started and work with PyScript.
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

We have been working to create exactly the same structure on our local computer.
With PyScript.com, you can have all that with just one click, and _you are ready to go!_.

The integrated editor has full support for both HTML/JavaScript and Python programming.
By simply clicking the **Run** button, you can immediately see a Preview of how your 
PyScript application would look like!.

PyScript.com is indeed easy to use, and absolutely perfect to get started with
PyScript as it completely lowers the barrier to set up your coding environment and infrastructure.

> 💡 From now on, we will be using directly PyScript.com to work on the exercises, 
> using this [template](https://pyscript.com/@leriomaggio/pyscript-template/latest)
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

### 🔍 Web Development and CORS

If you were to open the `index.html` file as a local HTML on your file system, something interesting would happen.
Let's open up the JavaScript console to get additional clues, as always.

> Access to fetch at 'file:///.../main.py' from origin 'null' has been blocked by **CORS** policy: Cross origin requests are only supported for
> protocol schemes: http, data, isolated-app, chrome-extension, chrome, https, chrome-untrusted.

As a matter of facts, loading resources from unknown (`null`) origins when loading local files in the browser
is in violation of the [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (Cross Origin Resource Sharing)
policy of the browser. To be clear, the **same** would have happened if we would have tried to load some local
JavaScript or CSS file.

CORS are a built-in mechanisms in the browser to protect the runtime by avoiding to load resources 
(also referred to as _assets_, in web terminology) from untrusted resources, or resources outside the execution sandbox.

To circumvent this issue, we need to serve the "external" `main.py` as an asset via an HTTP server.

The quickest way to do this locally for development purposes would be spawning an http server 
using Python directly, and its built-in
[`http`](https://docs.python.org/3/library/http.server.html) module:

1. Open a Terminal / Command Line / Power Shell (Windows Users);
2. Move to the location where the HTML file `index.html` lives on your hard drive;
3. Run `python -m http.server`.

Once you are able to spawn the local server (either via Python or using any other HTTP server of your choice) 
you should now see the app loading and fully working!

The derived take away lesson from this is that PyScript app would not
need much infrastructure to run, and yet having access or setting up an HTTP development server 
would still be required.
Another important benefit of using pyscript.com is that the whole development infrastructure is provided 
as a service, so we can concentrate on the part we enjoy the most: coding!