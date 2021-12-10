## What should I do when I need to start Flask?

#### Create and activate virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

#### Install library

```bash
pip install Flask
```

#### Before run (create context)

```bash
export FLASK_APP=main.py
export FLASK_ENV=development
```

#### Run dev-server of Flask

```bash
flask run
```
