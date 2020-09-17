from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from utils import example_func_one

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['LOG_FILE'] = 'application.log'

# if not app.debug:
#     import logging
#     logging.basicConfig(level=logging.INFO)
#     from logging import FileHandler,Formatter
#     file_handler=FileHandler(app.config.get('LOG_FILE'))
#     app.logger.addHandler(file_handler)
#     file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

if not app.debug:
    import logging
    _logger=logging.getLogger(__file__)
    logging.basicConfig(level=logging.INFO,format=('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(_logger)



@app.route("/")
def home():
    app.logger.info("I am about to launch index.html")
    app.logger.warning("This is a test warning message to check logging functionality")
    the_name = example_func_one("say my name")
    return render_template("index.html")
