# To launch flask with https

First you need to install ```pyopenssl```
```python
$pip install pyopenssl
```

Then you can launch the web app as https
```python
$ flask run --cert=adhoc
```

If you are launching from within the script
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
```