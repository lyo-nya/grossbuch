## App layout
```
├── static                # Styles and pictures (Flask default direcotry)
│  ├── hellothere.jpg     # This picture is shown for unauthorized requests
│  ├── invoice.css        # Styles names represent purpose
│  ├── main.css            
│  └── morocco-blue.png   # Background image
├── templates             # Markdown files (Flask default directory)
│  ├── orders             # Folder with all templates for orders actions
│  │  ├── edit.html
│  │  ├── list.html
│  │  └── new.html
│  ├── pricetags          # Same for pricetags, new and edit are combined here
│  │  ├── edit.html
│  │  └── list.html
│  ├── base.html          # The body of the template
│  ├── invoice.html       # Completely separate template, that is used for printing
│  ├── login.html
│  ├── navbar.html
│  └── unauthorized.html
├── views                 # Module, that contains @app.routes
│  ├── __init__.py        # Initiator, helps to hide all the imports
│  ├── delete_item.py     # This scripts do, what their name implies
│  ├── get_data.py
│  ├── list_items.py
│  ├── login.py
│  ├── print_invoice.py
│  └── show_item.py
├── __init__.py           # App initialization
├── auth.py               # Auth configuration
├── db.py                 # Database configuration
├── models.py             # Database tables definition
└── queries.py            # Collection of queries
```

## Initialization
This app is organized as python module, `__init__.py` file serves the same purpose
as `__init__` method in class definition - creates the instance of the app class.
Also, it imports `views` submodule with its own `__init__.py`, which in this case
is just a convenient way to execute everything within 'views' directory without using
wildcard imports.

In the context of this particular app, views are just a collection of functions 
with `@app.route` decorator, so the main purpose of this submodule is to avoid
walls of code that could have appeared in main `__init__.py` file. Additionally,
it makes directory structure more intuitive.

The intuition here is that app only needs views to run, but each view, in turn,
requires additional functionality. To be more specific, let's observe what some 
particular views do:

`get_data.py` is the route, that other routes call to acquire necessary information.
I needed such interface to receive data for form input options live update.
Naturally, this script imports `queries.py`, that contains what requests to database.
Queries are just strange sentences without database and tables, so 
this script imports both from main modules root, using relative import.
As a result, once `get_data.py` view is imported, database, models and queries 
are imported as well.

`login.py` contains the authorization route. I use [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
plugin, which requires `login_user` function and `User` class. They are both
defined in `auth.py`, that is imported by `login.py`, that renders login form,
generates user instance and passes it to login function.

All the other routes use `get_data.py` to do perform certain actions, such as listing,
editing or deletion of items.

## How to extend
The simplest way to extend this app is to add a new view or modify existing ones.
Actually, this is the required step anyway, since any modifications to other files
without it would just break the functionality.

Certainly, one can just put code directly into main `__init__.py` file and it will
be executed as expected, but I would recommend to avoid this.
Although such code might be functional, it is much less readable and semantic, and,
as a result, less maintainable and extensible.
