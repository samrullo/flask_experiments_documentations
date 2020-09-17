from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from utils import example_func_one
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['LOG_FILE'] = 'application.log'
app.config['SECRET_KEY']="mysecret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dev.sqlite"

db = SQLAlchemy(app)
admin = Admin(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    def __repr__(self):
        return f"<User {self.username}>"

db.create_all()
admin.add_view(ModelView(User, db.session))

if not app.debug:
    import logging

    _logger = logging.getLogger(__file__)
    logging.basicConfig(level=logging.INFO,
                        format=('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(_logger)


@app.route("/")
def home():
    app.logger.info("I am about to launch index.html")
    app.logger.warning("This is a test warning message to check logging functionality")
    the_name = example_func_one("say my name")
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)