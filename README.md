# About project...

Application app.py can be accessed at http://127.0.0.1:5000/
Activated by 'flask run' from bash-console / cmd

Endpoints:
```
/requirements
provides info on virtual environment requirements

/generate-users/<XX>
generates and displays XX fake names and emails (XX is an integer provided by user)

/mean
provides an info on mean weight and height using provided .csv-file

/space
provides info on astronauts that are currently in space (names and craft name)

/base58encode/<string_to_encode>
encodes string to base58-string (<string_to_encode> is  string provided by user)

/base58decode/<string_to_decode>
decodes from base58-string to string (<string_to_decode> is string provided by user)

```
