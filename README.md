## Mini-site with Flask and Jinja2
The main python code is in the file `main.py`.\
All templates are in the directory `/templates`.\
Styles and images are in the directory `/static`.\
File `requirements.txt` contains installed libraries.\
File `.flaskenv` is an example of using environment variables.\
File `.flake8` contains linter *flake8* settings.\
File `containers.txt` created by running the ```write_file(data):``` function from  *'main.py'*, and contains data received from contact forms.  
Note `raise Exception("error")` for testing custom error 500 FLASK_ENV=development must be unset.
To unset development mode:

```bash
unset FLASK_ENV
```

### to start Flask:

- Create and activate virtual environment
```bash
virtualenv venv
source venv/bin/activate
```
- Install library
```bash
pip install Flask
```
- Before run (create context)
```bash
export FLASK_APP=main.py
export FLASK_ENV=development
```
- Run dev-server of Flask
```bash
flask run
```
