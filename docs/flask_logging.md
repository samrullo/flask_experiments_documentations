# Flask logging

By default Flask will not log anything for us anywhere, except for
the errors with their stack traces, which are sent to 
the logger.

```python
app.config['LOG_FILE']='application.log'
if not app.debug:
    import logging
    logging.basicConfig(level=logging.INFO)
    from logging import FileHandler
    file_handler=FileHandler(app.config['LOG_FILE'])
    app.logger.addHandler(file_handler)
```

Here we added a configuration parameter to specify the log
file's location. This takes the relative path from the 
application folder, unless an absolute path is explicitly
specified.

```python
@app.route('/')
def home():
    app.logger.info("This is some example log")
    return render_template("index.html")
```

It will be great to know when the issue was logged, with what level, 
which file caused the issue at what line number

```python
import logging
logging.basicConfig(level=logging.INFO)
from logging import FileHandler,Formatter
file_handler=FileHandler(app.config['LOG_FILE'])
app.logger.addHandler(file_handler)
file_handler.setFormatter((Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')))
```

or if we don't want to use FileHandler

```python
import logging
logging.basicConfig(level=logging.info,format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s %(lineno)d]')
logger=logging.getLogger(__file__)
app.logger.addHandler(logger)
```

## Sending error logs to email
```python
RECIPIENTS=['some_receiver@gmail.com']

if not app.debug:
    import logging
    logging.basicConfig(level=logging.INFO)
    from logging import FileHandler,Formatter
    from logging.handlers import SMTPHandler
    file_handler=app.config['LOG_FILE']
    app.logger.addHandler(file_handler)
    mail_handler=SMTPHandler(('smtp.gmail.com',587),'sender@gmail.com',RECIPIENTS,'Error occurred in your application',
                ('sender@gmail.com','gmail_password'),secure=())
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
    for handler in [file_handler,mail_handler]:
        handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))   
```