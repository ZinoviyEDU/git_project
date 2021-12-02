## Flask microframework practice 

`````@app.route(’/’)````` is a Python decorator, that sets a URL for triggering internal function. 

In this project 6 decorators and functions were implemented:
* ```@app.route('/requirements/')```\
    Reads file 'requirements.txt' and returns data. A template to render HTML for better display was applied. Handles IOError.
* ```@app.route('/generate-users/<int:number>')```\
    Randomly generates users (name and email). ```<int:number>``` is a parameter that regulates the number of users. Used 'faker' library. A template to render HTML for better display was applied.
* ```@app.route('/mean/')```\
    Process the CSV file 'hwo5.csv' and returns data. Used 'CSV' library. Handles IOError.
* ```@app.route('/space')``` \
Displays the number of astronauts in the orbit. Used 'requests' library.
* ```@app.route('/base58encode/<string>')``` \
Encodes input string ```<string>``` in base58 format. Used 'base58' library
* ```@app.route('/base58decode/<encoded_string>')``` \
Decodes base58 format string ```<encoded_string>``` to original string. Used 'base58' library.

Used libraries: "Flask, Faker, render_template, requests, base58, CSV."\
Linting tool - Flake8.