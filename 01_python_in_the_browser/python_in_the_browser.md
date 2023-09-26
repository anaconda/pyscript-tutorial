## PyScript and _the_ Python in the Browser.

One of the very first questions I asked myself when I heard about _Python in the Browser_ was:
"What _kind of_ Python is actually running in the browser ?"
In other words, I was very curious to understand what was behind this technology, and what
were its capabilities.

In retrospect, I am still very convinced that those are very fair questions.
This is a completely new paradigm for Python programming.
We, as Python developers, are very used to see our favorite language
as a technology living and nurturing best in the _back-end_, when it comes to
web development.
But with PyScript, we are now foreseeing Python as a technology for the _front-end_ too.
Therefore, asking ourselves what kind of Python we are running in the browser opens up to
explore an entire new landscape (and stack) of web technologies that you may or may not have
heard of.

In this section, we will work on a very simple app trying to answer that question,
unveiling a bit of the technology that is enabling Python in the browser.
By doing so, we will first check what version of Python is running in the browser, and 
what are (if any) the differences with the standard Python interpreter running on our 
local machine.

### ⏳ Get Ready

To get started. let's open our code editor, and create a skeleton of a generic HTML page.

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

### 🧑‍💻 Hands on: Writing your first PyScript App

The first thing we need now is to include the main PyScript assets into 
our HTML page.

We will do so by replacing the placeholder comment
`<!-- ADD PyScript Here -->` with the following line:

```html
<script type="module" src="https://pyscript.net/snapshots/2023.09.1.RC1/core.js"></script>
```

The `<script>` tag imports the `core.js` JavaScript
[module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), which 
effectively enables PyScript in our application.

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

> 🆕 If you worked with PyScript classic, you may have noticed the use of 
> `<script type="py">` instead of the custom `<py-script>` custom tag.
> There is a dedicated paragraph at the end of this section that explains the
> differences in more details. Please see [here](#script-typepy-vs-py-script).

If everything works correctly, you should be now looking at a blank page! 😁
I know this is probably not something you were expecting. You were perhaps expecting to 
see the string printed on the page. But I promise you: everything is in order.

So where the `print` output went ?
To see it, you need to open the JavaScript Console in your Browser 
(on Chrome: `View > Developer > JavaScript Console`).
In the console, you should be now seeing the message we were looking for, and similar to:

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

Let's focus now instead on the _version_ of Python, i.e. **Python 3.11.2**.
As a matter of facts, the Python we are running in the browser is neither a "special" nor 
a "surrogate" version of the language. But rather standard Python `3.11` running in the 
browser. This is indeed amazing, as potentially the full capabilities of the language
can now be used in the browser!

It is now time to focus on the `print` Python function. This function in PyScript works as a 
logger in the console (i.e. similar to `console.log` in JavaScript), and cannot be used in any way
to change the content of the HTML page.
Let's keep in mind that a web page is indeed a structured document, with its own object model:
the [`DOM`](https://developer.mozilla.org/en-US/docs/Glossary/DOM), Document Object Model. 
So determining where in the document the content should be added, is not trivial.

> 🆕 If you have worked with previous versions of PyScript, you may have noticed a difference here.
> In PyScript classic, the output every `print` call is automatically redirected to a 
> custom element, called 
> [`<py-terminal>`](https://docs.pyscript.net/latest/reference/plugins/py-terminal.html#py-terminal). 
> `<py-terminal>` is a special _plug-in_ in PyScript classic that specifically served the 
> purpose to capture all the output on `stderr` and `stdout`. Currently plug-ins are not
> yet supported in the latest version of PyScript, and so neither is `<py-terminal>`.

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

If you now save the `first_pyscript_app.html` and refresh the page in the browser, 
you should be seeing the Python version displayed directly in the document.

> 💡 You may have noticed that the address bar in your browser reports something like
> `file://<path on your local hard drive>/first_pyscript_app.html`.
> This means that the browser is loading an HTML resource from your local hard drive. 
> In other words, no server is needed to open our web app.

### ⚙️ How it works

PyScript brings introduces a new special tag (i.e. `<script type="py">`) that is ultimately interpreted 
by browser as a special element where Python code will be expected.

And indeed there is some Python code, and we have already discussed that's pure Python 3 that one would
normally write into a general app running on your computer. So _how_ does that work really ?

In the figure below, there is a high-level representation of the PyScript general architecture. 
In the remainder of this Section, we will try to understand
what's the role of these components, and how they relate to each other.

![PyScript General Architecture](https://github.com/pyscript/docs/blob/main/docs/assets/images/platform.png)

On the top level there is the `User Code` leveraging the features of PyScript, which represents the next 
layer in the architecture. 
The PyScript platform then communicates directly to the Python interpreters compiled to **Web Assembly** (`WASM`), 
via [`Emscripten`](https://emscripten.org/docs/index.html).

The default interpreter used by PyScript is [**Pyodide**](https://pyodide.org), 
that is a "port" of the standard CPython interpreter to WASM.

In a nutshell, WASM is a binary instruction format that is designed as a portable compilation target 
for multiple programming languages.
Any code compiled to WASM can run with near-native performance. 

But the most important implication of this architectural choice could be better appreciated if we just add this last piece to our puzzle:

> 💡 "Any modern web browser natively embeds a WASM engine".

In other words, any web browser is able to run any WASM executable within their sand-boxed environment.
And therefore, thanks to PyScript and Pyodide, we are able to run standard CPython (_literally_) into
the browser!

> 💡 The version of Python running in the browser is therefore tighten to the version of the
> Python interpreter PyScript is using. 
> In this section, we are using `PyScript 2023.09.1` that uses `Pyodide 0.23.4`, corresponding to `Python 3.11.2`. 
> Older versions of Pyodide correspond to older versions of the Python interpreter.

We will dive more into the details of this architecture as soon as we will
work on the other sections in the module.

### 🎁 Wrap up

In this section we developed out first PyScript app, which was indeed really simple, and not at all 
complicated (from a mere coding perspective).
Nonetheless this example offered lots interesting insights on _how_ PyScript actually works, and its
architectural design.

To quickly recap, we started from a pretty standard `HTML` page template in which we added the PyScript
core JavaScript module, along with our Python code within a new `<script type="py">` custom tag.
Using the `pyscript.display` function, we showed the Python version we were running, leading
the way to explore a bit more which are the key components that enables Python in the browser.

By default, PyScript works in conjunction with Pyodide, a port of the standard CPython
interpreter that is compiled via Emscripten to run on WebAssembly (WASM).
WASM is a binary instruction format that is designed as a portable compilation target.
WebAssembly is designed to complement and run alongside JavaScript: using the WebAssembly JavaScript APIs,
you can load WebAssembly modules into a JavaScript app and share functionality between the two.

PyScript leverages on these technologies under the hood, and abstracts most of
their low-level details, providing a whole new development experience in the browser, 
and easy to get started with!

In our exercise app, we have discovered the new `display` PyScript function to simply add and show
content in our HTML page.

### 🥡 Take away lessons

- PyScript requires no installation, nor configuration to get started.
- PyScript provides a new HTML tag `<script type="py">` where Python code can be embedded.
- PyScript supports standard Python 3 in the browser.
- PyScript works by default with Pyodide, that is a Python distribution running on WASM.
- WASM is a special instruction set designed to be a portable compilation target for multiple languages.
- All modern Web Browser can run WASM along with JavaScript in their rendering engine.
- The Python `print` function is to be used for mere logging information in the JavaScript console.
- PyScript provides a `display` function to add content to the HTML.


### `<script type="py">` vs `<py-script>`

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
