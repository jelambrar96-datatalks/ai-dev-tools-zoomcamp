Todo Django App
================

This is a minimal Django TODO application supporting:

- Create, edit and delete TODOs
- Assign due dates
- Mark TODOs as resolved (toggle completed)

Quick start
-----------

1. Create a virtualenv and activate it (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make migrations and migrate the database:

```bash
# export a secure secret and disable debug
export DJANGO_SECRET_KEY='replace-with-a-very-secret-value'
export DJANGO_DEBUG='False'
python manage.py migrate
```

4. Create a superuser (optional, to access admin):

```bash
python manage.py createsuperuser
```

5. Run the dev server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ to view the todo list. Admin is at /admin/.

Notes and next steps
--------------------

- For production you must set DEBUG=False and provide a secure SECRET_KEY.
- Add tests, pagination, filtering, and user ownership/authentication as next improvements.
