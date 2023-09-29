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
This organization favors best development practice, and maximizes code editor's support for a better 
development experience.

In this chapter, we are about to create an interactive dice roller app. The user can select the number of
dice, and the number of sides on each die, namely a `d4`, `d6`, `d8`, `d12`, and `d20`.
This app will be the opportunity to learn a bit in details how interactions with the browser works
in PyScript (e.g. `on-click`), and what features PyScript provides to integrate with the DOM, and
JavaScript [event handling](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events).

### ⏳ Get Ready

To get starter, let's **duplicate** our PyScript App 
[template](https://pyscript.com/@leriomaggio/pyscript-app-template/latest)
by clicking on the "Clone Project <svg viewBox="0 0 32 32" width="1.2em" height="1.2em" class="-rotate-90 text-base sm:text-sm"><path fill="currentColor" d="M26 18a3.996 3.996 0 0 0-3.858 3H17V11h5.142a4 4 0 1 0 0-2H17a2.002 2.002 0 0 0-2 2v4H9.858a4 4 0 1 0 0 2H15v4a2.002 2.002 0 0 0 2 2h5.142A3.993 3.993 0 1 0 26 18Zm0-10a2 2 0 1 1-2 2a2.002 2.002 0 0 1 2-2ZM6 18a2 2 0 1 1 2-2a2.002 2.002 0 0 1-2 2Zm20 6a2 2 0 1 1 2-2a2.002 2.002 0 0 1-2 2Z"></path></svg>" button.
Cloning a project is a feature offered by pyscript.com to fork an existing app, and bring its copy into 
your own dashboard, so you can start working on it, independently.
In this case, the cloned app will be just the skeleton of the app we are about to create.

Once it's done, let's first rename the new app as "PyScript Dice Roller", and update the metadata in the
settings panel. App settings are accessible by clicking on the gear icon on the top-right toolbar.
Feel free to write any short description to your app. For example:
> An interactive Dice Roller App with PyScript and Micropython.

Click on the **Update** button to save the settings.

Now, please open the `index.html` file, and update the `<title>` tag with a more appropriate
`PyScript Dice Roller`.

> ✅ Perfect! We are now ready to move on to the hands-on part!

### 🧑‍💻 Hands on: Playing with random, and web events

Let's setup our `index.html` page first, with all the required components. We will move to
program the core logic in Python afterwards.

The `<!--  Add HTML TAGS here -->` placeholder can now be replaced with the following HTML:
```html
<h3>Dice Roller</h3>
        <div class="row">
            <div class="col-9">
                <div class="btn-group" role="group" aria-label="Number of Dice Group">
                    <input type="radio" class="btn-check ndice" name="btn-dice" id="btn1" 
                           data-dice="1" autocomplete="off" checked>
                    <label class="btn btn-outline-secondary" for="btn1">1</label>

                    <input type="radio" class="btn-check ndice" name="btn-dice" id="btn2" 
                           data-dice="2" autocomplete="off">
                    <label class="btn btn-outline-secondary" for="btn2">2</label>

                    <input type="radio" class="btn-check ndice" name="btn-dice" id="btn3" 
                           data-dice="3" autocomplete="off">
                    <label class="btn btn-outline-secondary" for="btn3">3</label>

                    <input type="radio" class="btn-check ndice" name="btn-dice" id="btn4"
                           data-dice="4" autocomplete="off">
                    <label class="btn btn-outline-secondary" for="btn4">4</label>

                    <input type="radio" class="btn-check ndice" name="btn-dice" id="btn5" 
                           data-dice="5" autocomplete="off">
                    <label class="btn btn-outline-secondary" for="btn5">5</label>

                    <input type="radio" class="btn-check ndice" name="btn-dice" id="btn10" 
                           data-dice="10" autocomplete="off">
                    <label class="btn btn-outline-secondary" for="btn10">10</label>
                </div>
                <div class="col-3 text-center">
                    <span>Number of Dice</span>
                </div>
            </div>
        </div> <!-- end row -->
        <div class="row" style="margin-top: 20px;">
            <div class="col-12 p-3">
                <div class="btn-group" role="group" aria-label="Die group">
                    <input type="radio" class="btn-check die" name="btn-d" id="btnd4" 
                           data-dice="4" autocomplete="off" checked>
                    <label class="btn btn-outline-warning" for="btnd4">
                        <img src="https://rgbstudios.org/img/projects/other/icon-d4.svg" 
                             alt="d4" class="w-6 h-6 mr-2">
        				d4
                    </label>

                    <input type="radio" class="btn-check die" name="btn-d" id="btnd6" 
                           data-dice="6" autocomplete="off">
                    <label class="btn btn-outline-warning" for="btnd6">
                        <img src="https://rgbstudios.org/img/projects/other/icon-d6.svg" 
                             alt="d6" class="w-6 h-6 mr-2">
        				d6
                    </label>

                    <input type="radio" class="btn-check die" name="btn-d" id="btnd8" 
                           data-dice="8" autocomplete="off">
                    <label class="btn btn-outline-warning" for="btnd8">
                        <img src="https://rgbstudios.org/img/projects/other/icon-d8.svg" 
                             alt="d8">
        				d8
                    </label>

                    <input type="radio" class="btn-check die" name="btn-d" id="btnd12" 
                           data-dice="12" autocomplete="off">
                    <label class="btn btn-outline-warning" for="btnd12">
                        <img src="https://rgbstudios.org/img/projects/other/icon-d12.svg" 
                             alt="d12">
        				d12
                    </label>

                    <input type="radio" class="btn-check die" name="btn-d" id="btnd20" 
                           data-dice="20" autocomplete="off">
                    <label class="btn btn-outline-warning" for="btnd20">
                        <img src="https://rgbstudios.org/img/projects/other/icon-d20.svg" 
                             alt="d20">
        				d20
                    </label>
                </div>
            </div>
        </div> <!-- end row -->
        <div class="row">
            <div class="col-3">
                <button type="button" class="btn btn-primary" id="roll">Roll</button>
            </div>
        </div>
        <div class="row" id="outcome-container" style="opacity: 0;">
            <div class="col-12">
                <div id="outcome"></div>
            </div>
        </div>
```

The listing is quite articulate, so I would recommend hit the `Save` 
button, and then the `Run` button to see the result.
The page contains two series of buttons (i.e. button groups): the first to select
the number of dice we want to roll; the second to choose which die we should be 
rolling. The `Roll` button shown at the bottom of the page will trigger the rolling.
The `<div id="outcome">` element will display the generated result.
The graphics of the button have been gathered from `rgbstudios.com`, emulating
their (much more comprehensive) [dnd-dice](https://rgbstudios.org/projects/dnd-dice) app.

Now onto the Python code! First things first, let's switch interpreter to
**Micropython**:

```html
<script type="mpy" src="./main.py"></script>
```

> 💡 Why using Micropython in this app ?
> 
> _Well, why not ?_ In this app, we won't need any specific feature Pyodide provides,
> and Micropython is blazing fast (and lighter to download).
> Instead, this will be an amazing opportunity to showcase how the 
> PyScript platform seamlessly supports the two interpreters by allowing 
> the **same** code to run equally on both.

Let's now write the Python code in `main.py`:

```python
from random import randint
from pyscript import document

ROLLED = '<span class="badge text-bg-warning">Rolled {n_rolls} D{die}</span>'
ROLL = '<span class="badge text-bg-secondary">Rolls: {rolls}</span>'


# Utility functions
def to_int(value: str) -> int:
    """Simple function to cast a string to an int, in a BAFTP fashion."""
    try:
        int_v = int(value)
    except ValueError:
        return 0
    else:
        return int_v


def select_checked(radio_btns):
    """Return the checked radio button in the group. 
    None otherwise"""
    for btn in radio_btns:
        if btn.checked:
            return btn
    return None


def dice_roll(*args):
    """on-click handler for the Roll button"""
    n_dice_btn = select_checked(document.getElementsByClassName("ndice"))
    die_btn = select_checked(document.getElementsByClassName("die"))
    if die_btn or n_dice_btn is None:
        return

    # Set up rolled badge
    n_dice = to_int(n_dice_btn.getAttribute("data-dice"))
    n_sides = to_int(die_btn.getAttribute("data-dice"))
    rolled_badge = ROLLED.format(n_rolls=n_dice, die=n_sides)

    # generate rolls outcome
    rolls = [str(randint(1, n_sides)) for _ in range(n_dice)]
    roll_badge = ROLL.format(rolls=",".join(rolls))

    # inject outcome in the DOM
    outcome_el = document.querySelector("#outcome")
    outcome_el.innerHTML = f"{rolled_badge} | {roll_badge}"

    # Set max opacity to container to make it visible
    outcome_cont_el = document.querySelector("#outcome-container")
    outcome_cont_el.style.opacity = 1


# Add the dice_roll py-function as event listener
roll_btn = document.querySelector("#roll")
roll_btn.addEventListener("click", dice_roll)

```

> ✅ This completes the app code. Hit `Save` and `Run` to play with it! 🎉

In the next section, we will dissect our code to understand how it works!

### ⚙️ How it works: the `document` object, and JavaScript FFI

The core of our implementation works around the `pyscript.document` object:
```python
from pyscript import document
```

The `document` object is a proxy for the page [`document object`](https://developer.mozilla.org/en-US/docs/Web/API/Document). Its APIs are mapped `1:1` 
with the corresponding JavaScript counterpart (e.g. `document.getElementById`
for both), and can be used in PyScript to access and/or manipulate the `DOM.

For example, in the last two lines of our Python code:
```python
# Add the dice_roll py-function as event listener
roll_btn = document.querySelector("#roll")
roll_btn.addEventListener("click", dice_roll)
```

we first select the `Roll` button tag by its id (i.e. `id=roll`), and then we
invoke its `addEventListener` method to associate to the selected button element
our `dice_roll` (**Python**!) function as handler.
In other words, from now on, every time we will click on the `Roll` button, our
`dice_roll` function will be invoked!

The `pyscript.document` object is part of PyScript's `FFI` (_Foreign Function
Interface_) that seamlessly integrates with the JavaScript interpreter
in the browser. Thanks to the `FFI`, we are able to proxy JavaScript
objects as Python objects (e.g. `roll_btn`), and use Python functions
as JavaScript-equivalent event handlers.

Furthermore, the same FFI can be used regardless of the selected Python interpreter 
we are using, i.e. `pyodide` or `micropython`.

> ⚠️ At the time of writing, a complete feature parity between Pyodide and 
> Micropython FFIs is still in progress.
> PyScript + Pyodide provides the most comprehensive FFI, thanks to direct mapping
> to Pyodide native [one](https://pyodide.org/en/stable/usage/api/python-api/ffi.html).

The `dice_roll` Python function implements the click handler logic.
We first get reference to the `checked` buttons from the two button groups, using the 
`select_checked` utility function. Since all radio buttons in the two groups share the same
CSS class, we can use the `document.getElementsByClassName` function to extract them from
the DOM. Afterwards, the value of the `data-dice` attribute is extracted from the selected
elements, and the rolling is performed.

Finally, the `innerHTML` attribute is used to inject the outcome badges in the `<div id="outcome">`
tag, and the `opacity` style attribute of its container set to `1` to make it visible.

> 💡 For the mere sake of curiosity, please try to change the interpreter from Micropython
> back to the default Pyodide (i.e. `<script type="py"..>`). 
> Everything should still be working the same way, but you will notice a little delay 
> (depending on your internet connection) when running the app on Pyodide. 
> This is mainly due to the fact that the Pyodide interpreter is bigger, and takes a few 
> seconds more to download.

### 🎁 Wrap up

In this example we learnt how to use PyScript to create a simple interactive web app for dice rolls.
By doing so we discovered two new PyScript features: `pyscript.document` object, and JavaScript
FFI. 
The former provides access to the DOM to select and manipulate the content of the current document, 
and the latter provides `1:1` API mapping to the JavaScript counterparts. In the app we have seen
many examples of the DOM access and manipulation capabilities that PyScript FFI makes accessible
via Python code. For example, to select and extract the value of the attributes from the button
elements, as well as using a pure-Python function as a proxy for a JavaScript callable for the 
button `click` event.

Last but not least, the whole example can seamlessly run on **both** Pyodide and **MicroPython** interpreters,
without changing a single line of code, although we decided to use the latter as (a) is faster, and
(b) we did not need any of the _extra_ features provided by Pyodide. In other words, the (subset of the) 
Standard library MicroPython provides was enough to program the core logic of the app.


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

### 🥡 Take away lessons

- PyScript tags `<script type="py">` and `<script type="mpy">` can leverage on their `src` attribute to load external resources.
- Using external `main.py` enables better development experience when working with PyScript.
- This would keep HTML and Python resources separated, and would leverage on the full support of
your code editor.
- Loading local files when loading external resources violates CORS browser policy.
- An HTTP server is required to workaround the CORS issue.
- Deploying a PyScript app does not require much infrastructure - just serving HTML pages. No server-side technology!
- The `pyscript.document` is the object representation of the page's document, to access and manipulate the DOM.
- `document` API proxies `1:1` its JavaScript counterparts (e.g. `document.querySelector`)