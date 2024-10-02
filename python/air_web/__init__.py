"""The `air_web` module is a lightweight package for crawling the web with the minimalist of code.

Example:

.. code-block:: python

    import air_web

    air_web.get("https://medium.com/p/dca128e0202a")

To learn more, check out the GitHub repo: https://github.com/AWeirdDev/air-web
"""

from .air_web import to_markdown
from .core import get, redirector, redirectors

__all__ = ["to_markdown", "get", "redirector", "redirectors"]
