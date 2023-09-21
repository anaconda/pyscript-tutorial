## PyScript and _the_ Python in the Browser.

One of the very first questions I asked myself when I heard about _Python in the Browser_ for the
first time was:"Ok that sounds cool, but what do you mean by 'Python'? What kind of Python are we
talking about?".

In retrospect, I am still very convinced that this is a very fair question to ask.
This is a completely new technology. We as Python developers are very used to see our favorite language
as a technology living and nurturing best in the _back-end_.
But with PyScript, we are now saying that Python can also be a technology for the _front-end_ too.
So asking what kind of Python we are indeed running in the browser opens up to understanding a bit
more in details how this new platform actually works.

In this section, we will work on a very simple app to try to answer this question.
We will try to understand what version of Python is running in the browser, and what are its 
differences with the standard Python interpreter running on the local machine.

### ⏳ Get Ready

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

### 🧑‍💻 Hands on: Writing your first PyScript App

The first thing we need to do, is to actually include the main PyScript assets into 
your our HTML page.

We will do so by replacing the first placeholder comment
(i.e. `<!-- ADD PyScript Here -->`) with the following line:

```html
<script type="module" src="https://pyscript.net/snapshots/2023.09.1.RC1/core.js"></script>
```

The `<script>` tag imports the `core.js` JavaScript
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

The very first thing we have discovered is that the Python `print` function in PyScript does not work in the way you might have expected,
i.e., it is not supposed to be used to write textual content into `HTML`. We will refine, and expand more on this in a second.

Let's focus now instead on the version of Python we have obtained: **Python 3.11.2**. So this is neither a "special" nor a "surrogate"
version of the Python interpreter, but instead standard Python 3.11 running in the browser.

As already mentioned, the `print` Python function works as a logger in the console, and cannot be used to modify the content of the HTML
page. Although this is indeed quite reasonable (and perhaps even expected), let's keep in mind that a web page
is indeed a structured document. So even determining where in the document the text should be added, is not trivial.
For this reason, PyScript provides an easy function to manipulate the page
[`DOM`](https://developer.mozilla.org/en-US/docs/Glossary/DOM) (Document Object Model) named `display`.

Let's change our Python code, so that we can show the Python version directly in the web page:

```html
<script type="py">
    import sys
    from pyscript import display


    display(f"Running Python {sys.version} in the Browser!")
</script>
```

If you now save the `first_pyscript_app.html` and refresh the page in the browser, you should be seeing the Python version
displayed directly in the document.

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


### EXTRA 🔍 `<script type="py">` vs `<py-script>`

If you have already worked with previous versions of PyScript,
or you have seen some examples on PyScript apps on the internet, you might have noticed the new special tag
`<script type="py">` that we used in our example, instead of the more "classic" `<py-script>` one.

The `PyScript 2023.09.1` release has introduced the new
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
