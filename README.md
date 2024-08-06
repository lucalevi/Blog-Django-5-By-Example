# Django Project "Blog"

This repository shows some of the possibilities that you can have using Django. Namely, a blog is being created using dedicated models, views and templates which can be seen in the blog/ folder.

The model is based on several models, where the most important is the Post model, which controls the whole data structure of the blog posts of the project.

Ad fore the database, you can find a mysite_data.json attached with a dump of the database, you can load this dump by executing `python manage.py loaddata fixture.json` in the main folder, where also the `manage.py` file is located.
Remember to do so after having executed the usual migrations, keeping the database structure in sync with the Django models.  (Locate yourself in the terminal in the same folder as the `manage.py` file.)
```bash
python manage.py makemigrations blog
python manage.py migrate
```

The project is set for use 
