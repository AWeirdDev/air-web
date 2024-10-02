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

## 📖 Docs

### <kbd>def</kbd> get()

Sends an HTTP GET request to the specified website and returns the Markdown result.

