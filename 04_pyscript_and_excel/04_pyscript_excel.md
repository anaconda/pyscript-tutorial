## Reading Excel (`.xls`) files with PyScript

In this chapter we will work on a PyScript app to read Excel
files in the browser. This will be our opportunity to dive into
very interesting features of PyScript.
In particular, we will learn ho to use local Python modules,
and how to issue `HTTP` `fetch` requests in Python
(e.g., to download our Excel workbook data file) and what are the
implications with respect to _synchronous_ vs _asynchronous_ I/O calls.

### ⏳ Get Ready

We will use PyScript.com to develop our app, as it provides the easiest
and quickest way to get started with coding, without having to worry
at all about the infrastructure (i.e. the HTTP server).
You would simply need to _clone_ the app template
available [here](https://pyscript.com/@leriomaggio/pyscript-template/latest), 
and in bring it in your own dashboard, and you are ready to go.

That said, if you still wish to work locally on your machine, 
just bear in mind that all the code we will develop has to run
on a HTTP server to circumvent CORS restrictions.

Your `index.html` file should look like this:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>----INSERT YOUR TITLE HERE----</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <link rel="stylesheet" href="https://pyscript.net/snapshots/2023.09.1.RC1/core.css" />
    <script type="module" src="https://pyscript.net/snapshots/2023.09.1.RC1/core.js"></script>
</head>
<body>
    <script type="py" src="./main.py" config="./pyscript.toml"></script>
</body>
</html>
```

Let's set the title of our page as _Read Excel files in the browser_, and also add the 
`<div id="excel_table"></div>` HTML tag right after the PyScript element. 

This tag will act as a placeholder where the Excel sheet read from the
input workbook will be displayed, formatted as an HTML table.

### 🧑‍💻 Hands on

To better organize our code, this time we are going to keep our `main.py` module
as slim as possible, and instead rely on other Python modules to implement the core
functionalities we need (_similar to what we would have done, if we were developing this app 
outside the browser_, ed.).

Therefore, to develop our app we are going to proceed somewhat backwards: we will start 
with the code in the `main.py` to understand where we are heading to with our app,
and then we will start filling in the missing pieces (i.e., modules) to make the code run.

```python
from pyscript import document
from data import load
from formatting import to_html_table

DATA_URL = "https://raw.githubusercontent.com/leriomaggio/pyscript-fetch-resources/main/sample_workbook.xls"


def main(data_url: str = DATA_URL, target_sheet: str = "Data"):
    xl_sheet = load(data_url, sheet_name=target_sheet)
    html_table = to_html_table(xl_sheet)
    target_div = document.querySelector("#excel_table")
    target_div.innerHTML = html_table


main()
```

The processing pattern is pretty straightforward: 
1. we load the data (i.e. `xl_sheet`) from a given URL;
2. we format the excel sheet into an HTML table;
3. we inject the generated HTML into our page using PyScript.


### ⚙️ How it works

### 🎁 Wrap up

### 🥡 Take away lessons