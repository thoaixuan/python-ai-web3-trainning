
# How to run Project

---
Make new env ```python3 -m venv env```

Install package: ```pip install beautifulsoup4 requests```

---
```get()``` method performs an HTTP GET request to the specified URL.

```response.content``` will contain HTML document produced by the server, and ```html.parser``` specifies the parser the library will use.
> Return all ```<a>``` elements with an href attribute, and we will filter.
