# Django Project "Blog"
This repository demonstrates various capabilities of Django by implementing a blog application. The core functionality is built using custom models, views, and templates, which can be found in the blog/ directory.

##Setup
1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create and activate a virtual environment:

```
python -m venv my_env

# On Windows:
my_env\Scripts\activate

# On macOS and Linux:
source my_env/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Database Setup
This project is configured to use PostgreSQL, but you can switch to SQLite if preferred.

1. For PostgreSQL, update the following in mysite/settings.py:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
    }
}
```
2. For SQLite, modify mysite/settings.py:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

3. Apply migrations:

```python
python manage.py makemigrations blog
python manage.py migrate
```

4. (Optional) Load sample data:

```python
python manage.py loaddata mysite_data.json
```

## Environment Variables
Create a .env file in the project root and add the following:

```
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=your_default_email@example.com

# If using PostgreSQL:
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
```

Update mysite/settings.py to use these variables:

```python
from decouple import config

# Email configuration
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

# Database configuration (if using PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
    }
}
```

## Running the Project
```
python manage.py runserver
```
Visit `http://127.0.0.1:8000/blog` in your browser to view the blog.

## Project Structure
The main Post model in blog/models.py defines the data structure for blog posts. Other models enhance the blog's functionality.

Feel free to explore the code and make modifications as needed!
