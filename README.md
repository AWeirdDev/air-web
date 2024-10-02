# 🛫 air_web

A lightweight package for crawling the web with the minimalist of code.

```python
from air_web import get

# Crawl example.com and convert to Markdown
get("https://example.com")
```

## 🤨 Why & how
This is proof that web crawling can be done simply and at the highest level of API. No need to install the required 102 dependencies for one feature, no need to create a lot of class instances in order to get something up and running. With a simple `get()`, you get almost everything from the Internet.

`air_web` uses PyO3 as backend, utilizing the `html2text` crate for the `to_markdown` function, as well as some `.pyi` code to get everything typed nicely.

For the Python side, I used `primp` for browser fingerprint impersonation and `selectolax` for selecting HTML nodes.

## 🧐 Redirectors
Redirectors are used to redirect the HTML selector to one specific node to tidy up the results. For example, if the page has navbars, we can select the main content part to skip it through (if the nav isn't important).


```python
@redirector
def my_redirector(node):
  return ok(node.css_first("main"))
```

## 📖 Docs

### <kbd>def</kbd> get()

```python
def get(
    url: str,
    *,
    redirectors: List[Redirector] = [],
    ok_codes: list[int] = [],
    **kwargs,
) -> str: ...
```

Sends an HTTP GET request to the specified website and returns the Markdown result.

**Args**:
- `url` (str): The URL to fetch.
- `redirectors` (list\[Redirector]): A list of redirectors for indexing into or manipulating specific nodes before converting the HTML to Markdown. See reference.
- `ok_codes` (list\[int]): A list of OK codes indicating the success status. Even if provided custom ones or not, the code `200` is always on the list.

