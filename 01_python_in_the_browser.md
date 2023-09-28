## PyScript and _the_ Python in the Browser.

One of the very first questions I asked myself when I heard about _Python in the browser_ was:
"What _kind of_ Python is actually running in the browser, and what can you really do with it ?"
I was very curious to understand what was behind this technology, and what were its capabilities.

In retrospect, I am still very convinced that those the are very fair questions.
This is a completely new paradigm for Python programming.
We, as Python developers, are very used to see our favorite language
as a technology living and nurturing best in the _back-end_, when it comes to
web development.
But with PyScript, we are now foreseeing Python as a tool for the _front-end_ too.
Therefore, asking ourselves what "kind" of Python we are running in the browser opens up to
explore an entire new landscape (and stack) of web technologies that you may or may not have
heard of before.

In this chapter, we will work on a very simple app trying to give an answer to those questions,
unveiling a bit of how Python in the browser works.

To do so, let's simply start by checking what is the _version_ of Python we are running!

### ⏳ Get Ready

First, let's log into PyScript.com to access our dashboard.

Let's create a new PyScript app by clicking on the
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
</svg> on the left toolbar, and rename this app "Get Started with PyScript".

Whenever you create a new PyScript app on PyScript.com, you will be presented with a 
**template** skeleton which contains everything you need to start coding!
In particular, you will find a `main.py` to host your main Python code, a `pyscript.toml` for
app configurations, and an `index.html` containing the HTML skeleton of the app.
We will explore in details the role of these files in the next chapters.

The development environment on pyscript.com is presented as organized in three panes:
a resource navigator, the code editor, and the preview pane.

The integrated code editor has full support for HTML/JavaScript, Python and Markdown files.
You have a **Save** <svg viewBox="0 0 24 24" width="1.2em" height="1.2em" class="text-base sm:text-sm"><path fill="currentColor" d="M21 7v12q0 .825-.587 1.413Q19.825 21 19 21H5q-.825 0-1.413-.587Q3 19.825 3 19V5q0-.825.587-1.413Q4.175 3 5 3h12Zm-9 11q1.25 0 2.125-.875T15 15q0-1.25-.875-2.125T12 12q-1.25 0-2.125.875T9 15q0 1.25.875 2.125T12 18Zm-6-8h9V6H6Z"></path></svg>
button to save your progress - also accessible via the shortcut `Ctrl+s` (or `Cmd+s`, on macOS) - 
and a  **Run** <svg viewBox="0 0 32 32" width="1.2em" height="1.2em" class="text-base sm:text-xs"><path fill="currentColor" d="M7 28a1 1 0 0 1-1-1V5a1 1 0 0 1 1.482-.876l20 11a1 1 0 0 1 0 1.752l-20 11A1 1 0 0 1 7 28Z"></path></svg> button, 
to immediately see a preview of your app running, in the _Preview_ rightmost pane.

Let's open the `index.html` file in our code editor, and _for the sake of this chapter_, 
let's replace its content with the HTML template reported below.

We will try to understand the role of each component in the page, by manually adding them
one at a time.

Here is how the `index.html` should look like:

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

Let's hit the save button, and we are ready to proceed with the hands on exercise.

### 🧑‍💻 Hands on: Writing your first PyScript App

The first thing we need now is to include the main PyScript assets into 
our HTML page.

We will do so by replacing the placeholder comment
`<!-- ADD PyScript Here -->` with the following line:

> ❗️TODO: Update PyScript URL when new will become available

```html
<script type="module" src="https://pyscript.net/snapshots/2023.09.1.RC1/core.js"></script>
```

The `<script>` tag imports the `core.js` JavaScript
[module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), which 
effectively enables PyScript in our app.

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

> ✅ This example is complete! Now let's Save <svg viewBox="0 0 24 24" width="1.2em" height="1.2em" class="text-base sm:text-sm"><path fill="currentColor" d="M21 7v12q0 .825-.587 1.413Q19.825 21 19 21H5q-.825 0-1.413-.587Q3 19.825 3 19V5q0-.825.587-1.413Q4.175 3 5 3h12Zm-9 11q1.25 0 2.125-.875T15 15q0-1.25-.875-2.125T12 12q-1.25 0-2.125.875T9 15q0 1.25.875 2.125T12 18Zm-6-8h9V6H6Z"></path></svg> and Run <svg viewBox="0 0 32 32" width="1.2em" height="1.2em" class="text-base sm:text-xs"><path fill="currentColor" d="M7 28a1 1 0 0 1-1-1V5a1 1 0 0 1 1.482-.876l20 11a1 1 0 0 1 0 1.752l-20 11A1 1 0 0 1 7 28Z"></path></svg> our first PyScript app.

If everything works correctly, you should be now looking at a blank page! 😁
I know this is probably not something you were expecting. You were perhaps expecting to 
see the string printed on the page. But I promise you: everything is in order.

So where the `print` output went ?
To see it, you need to open the JavaScript Console in your Browser 
(on Chrome: `View > Developer > JavaScript Console`).
In the console, you should be now seeing the following message:

```
Running Python 3.11.2 (main, Jul  7 2023, 05:19:00) [Clang 17.0.0 (https://github.com/llvm/llvm-project df82394e7a2d06506718cafa347b in the Browser!
```

> 🎮 The JavaScript console is a very useful tool when working
> in the web. Similarly, it is an invaluable source of information when we work with PyScript.
> I could not recommend it more! And we will end up using and/or referencing a lot 
> of times throughout this module.

The very first thing we learned is that the Python `print` function in PyScript 
does not work in a way you might have expected,
i.e., it is not supposed to be used to write textual content into `HTML`. 
We will refine, and expand more on this soon.

Let's focus now on the _version_ of Python, i.e. **Python 3.11.2**.
As a matter of facts, the Python we are running in the browser is neither a "special" nor 
a "surrogate" version of the language. But rather standard Python `3.11` running in the 
browser. This is quite amazing, as potentially the full capabilities of the language
can now be used directly in the browser!

Let's go back to the `print` function. This function in PyScript is expected to work similarly
to what `console.log` in JavaScript does. It cannot be used in any way
to change the content of the HTML page.
Let's keep in mind that a web page is indeed a structured document, with its own object model:
the [`DOM`](https://developer.mozilla.org/en-US/docs/Glossary/DOM), Document Object Model. 
So determining where in the document the content should be added with _just_ the standard
`print` Python function, is not trivial. We need something a little more flexible, and
sophisticated!

> ❗️TODO: REMOVE - This is still kept in case py-terminal will be re-enabled before release!
---
> 🆕 If you have worked with previous versions of PyScript, you may have noticed a difference here.
> In PyScript classic, the output every `print` call is automatically redirected to a 
> custom element, called 
> [`<py-terminal>`](https://docs.pyscript.net/latest/reference/plugins/py-terminal.html#py-terminal). 
> `<py-terminal>` is a special _plug-in_ in PyScript classic that specifically served the 
> purpose to capture all the output on `stderr` and `stdout`. Currently plug-ins are not
> yet supported in the latest version of PyScript, and so neither is `<py-terminal>`.
----

To add and visualize generic content in the HTML page, PyScript provides an easy-to-use
utility function called `display`.

Let's change our Python code, to use the `display` PyScript function instead of `print`:

```html
<script type="py">
    import sys
    from pyscript import display


    display(f"Running Python {sys.version} in the Browser!")
</script>
```

Let's now save & run our app. The preview pane will refresh, and
you should now be seeing the Python version displayed directly in the document.

### ⚙️ How it works

PyScript introduces a new special attribute for the `<script>` tag (i.e. `type="py"`) that is 
ultimately interpreted by the browser as an element where Python code will be expected.

And indeed there is some pure Python 3 code in the tag we've written. 
So _how_ does that work, really ?

In the figure below, there is a high-level representation of the PyScript general architecture. 
In the remainder of this chapter, we will try to understand
what's the role of these components, and how they relate to each other.

![PyScript General Architecture](https://docs.pyscript.net/2023.09.1/assets/images/platform.png)

On the top level there is the `User Code` leveraging the features of PyScript.
The PyScript platform then communicates directly to the Python interpreters compiled to 
**Web Assembly** (`WASM`), via [`Emscripten`](https://emscripten.org/docs/index.html).

The <u>default</u> interpreter used by PyScript is [**Pyodide**](https://pyodide.org), 
that is a "port" of the standard CPython interpreter to WASM.

In a nutshell, WASM (Web Assembly) is a binary instruction format that is designed 
as a portable compilation 
target for multiple programming languages.
Any code compiled to WASM can run with near-native performance.

But the most important implication of this architectural choice could be better appreciated if we just add this last piece to our puzzle:

> 💡 "Any modern web browser natively embeds a WASM engine".

In other words, any web browser is able to run any WASM executable within their 
sand-boxed environment. And therefore, thanks to PyScript and Pyodide, we are able to run 
standard CPython (_literally_) into the browser!

However, Pyodide **is not** the only interpreter PyScript can integrate with.
[**Micropython**](https://micropython.org/) is also supported.
MicroPython is a lean and very efficient re-implementation of Python 3 that includes
a comprehensive subset of the standard library, compiled to Web Assembly

Switching to the MicroPython interpreter is **very easy**. We just need to change 
the `type="py"` attribute of the `<script>` tag to `type="mpy"`.

Let's quickly change the `type` attribute in our code with `mpy` and let's see what happens:
```html
<script type="mpy">
    import sys
    from pyscript import display


    display(f"Running Python {sys.version} in the Browser!")
</script>
```

When we run the version of our app using MicroPython instead of the default Pyodide, this is 
the output `display` returns:
```
Running Python 3.4.0; MicroPython v1.20.0-297-g5fbb84a77 on 2023-07-13 in the Browser!
```

In conclusion, to answer more precisely to the question

> What version of Python we are running in the browser?

we have learned that it depends on which interpreter PyScript is currently using underneath!
Considering the layers of the architecture, top to bottom, we are using `PyScript 2023.09.1`, 
which uses by default `Pyodide 0.23.4`, corresponding to `Python 3.11.2` running on `WASM`.
Different versions of Pyodide correspond to different versions of the Python interpreter.
Alternatively, if we were using `MicroPython` instead, `Python 3.4.0` is used.

There are clear differences in terms of capabilities (and therefore use cases) between the two
interpreters, which justify the support for both in PyScript.
On one hand, Pyodide brings a full-fledged Python interpreters in the browser, with many
amazing features. On the other hand, the MicroPython interpreter is blazing fast 
(_and faster than Pyodide_, ed.), as it is natively more suited to run on constrained
environments like the browsers, but it is limited in terms of capabilities, 
if compared to Pyodide.
We will explore in details in the next chapters features of both the interpreters.

### 🎁 Wrap up

We developed out first PyScript app, which was indeed really simple, and not at all 
complicated (from a mere coding perspective).
Nonetheless the example offered lots of interesting insights on _how_ PyScript works, and its
architectural design.

To quickly recap, we started from a pretty standard `HTML` page template in which we added 
the PyScript `core.js` JavaScript module, along with our Python code within a new 
`<script type="py">` custom tag.
Using the `pyscript.display` function, we were able to show the Python version running, 
paving the way to understand a bit more in details the key architectural components that enable
Python in the browser.

By default, PyScript works with Pyodide, a port of the standard CPython
interpreter that is compiled via Emscripten to run on Web Assembly (WASM). 
Also the MicroPython interpreter compiled to WASM is supported by PyScript.

WASM is a binary instruction format that is designed as a portable compilation target.
Web Assembly is designed to complement and run alongside JavaScript: 
using the WebAssembly JavaScript APIs, you can load Web Assembly modules into a JavaScript app
and share functionality between the two.

PyScript leverages on these technologies under the hood, and abstracts most of
their low-level details, providing a whole new development experience in the browser, 
and easy to get started with!

### 🥡 Take away lessons

- PyScript.com is the easiest and quickest way to get started with PyScript, without having 
to worry about setting up the coding environment, and the infrastructure (i.e. HTTP server)
- PyScript requires no installation, nor configuration to get started.
- PyScript provides a new HTML tag `<script type="py">` where Python code can be embedded.
- PyScript supports standard Python 3 in the browser.
- PyScript works by default with Pyodide, that is a Python distribution running on WASM.
- In addition, PyScript also supports the MicroPython interpreter enabled via `<script type="mpy">`
- WASM is a special instruction set designed to be a portable compilation target 
for multiple languages.
- All modern web browsers can run WASM along with JavaScript in their rendering engine.
- The Python `print` function is to be used for mere logging information in the JavaScript console.
- PyScript provides a `display` function to add content to the HTML.


### 🔍 `<script type="py">` vs `<py-script>`

If you worked with PyScript classic, you may have noticed the new special tag
`<script type="py">` that we used in our example, instead of the `<py-script>`
custom element.

The new PyScript release inf fact has introduced the new
`<script type="py">` as an alternative for `<py-script>`. 
Reason for using the new tag are manifold.

`TL;DR`: Using `<script type="py">` would solve issues with your Python code containing HTML reserved
characters, such as `<`, or `>`.

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
