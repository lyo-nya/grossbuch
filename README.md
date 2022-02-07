## About the app
This is a toy accounting flask app, that has the bare minimum functionality.
It assumes, that there is only one user, who can:
  - Create and update his price list.
  - Use price list to create and update orders.
  - Generate invoices for orders.

To provide the user with this functionality I utilize three types of objects:

**Price tags** are characterized by job type, job title, measurement unit, and price.
They can be added, removed, or modified by the user. Note that currently none of the characteristics is assumed unique.

**Orders** have the following characteristics: client, description, and creation date.
It is only guaranteed, that the creation date is not empty, since it is set automatically.
Each order can (though does not have to) include a list of order items.
Just like price tags, orders can be added, removed, or modified by the user.

**Order items**, as the name suggests, only exist within orders.
They are generated from price tags by setting quantity.
Each order can only include one item for each price tag.
Once added, the item cannot be edited but can be removed.
While an item is being created, price is editable to allow for [first-degree price discrimination](https://en.wikipedia.org/wiki/Price_discrimination).

These types are translated into tables in the SQL database of your choice (I only checked that with [sqlite3](https://www.sqlite.org/index.html) and [porstgresql](https://www.postgresql.org/)),
thanks to [SQLAlchemy](https://www.sqlalchemy.org/).
Basically, the only purpose of this app is to manage rows in this database.

To make it more user-friendly, I used [UiKit 3](https://getuikit.com/) to style pages.
Also, the app not only generates invoices but prints them to PDFs, using [Flask-WeasyPrint](https://pythonhosted.org/Flask-WeasyPrint/).
Finally, all pages of the app require authorization, which is now realized with secret keyword.

## Project structure
Building this project, I tried to comply with developers [guidelines](https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/).
This means, that all application code is within the `grossbuch` folder,
while setup script, which in my case is named `run.py` is in the root directory.

Contrary to guidelines, `/instance` was not put into `.gintignore` on the initial commit,
to give a sense of what minimal app configuration can look like.

Apart from `instance`, the root folder also contains `Procfile`, that is required by [Heroku](https://heroku.com/) to serve the app,
`requirements.txt` file, that contains all pip packages, that are required to run the app,
`data` folder, that contains example raw data file and `fill_pricelist.py` script,
that can be used to pass raw data to the database. Currently, it can only fill `pricetags` entries,
but one can extend it to perform insertions into any other table. 

```
├── data              # Raw data
├── grossbuch         # App code
├── instance          # Default configuration folder
├── fill_pricelist.py # Insertion script
├── Procfile          # Configuration for Heroku
├── requirements.txt  # List of required pip packages
└── run.py            # Run script
```

The layout of the app itself is described in the corresponding [README](https://github.com/lyo-nya/grossbuch/tree/master/grossbuch).

## Deployment
To deploy this app, three steps should be made:
1. Run `pip install -r requirements.txt` in your terminal emulator.
2. Set variables in `instance/config.py`.
3. Deploy
    - If you wish to test it out on your machine, you simply type `./run.py` and press enter.
    This will start flask built-in server.
    - I deployed this app on [Heroku](https://heroku.com/), for you to do the same,
    it suffices to just clone this repository and push it to the Heroku server.
    Note that in this case, you need to set up a remote SQL server.
4. Optionally, you can run `./fill_pricelist.py <path-to-your-csv>` if you already have a price list.
This script assumes, though, that your file has the same structure as `data/raw.csv`.

### TODO
- [ ] Form validation
- [ ] Updatable columns
- [ ] Add some comments maybe
