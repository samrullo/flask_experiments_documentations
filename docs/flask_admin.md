#Flask-Admin

To install

```python
pip install flask-admin
```

Usage

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app=Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI']='sqlite:///dev.sqlite'
app.config['SECRET_KEY']="mysecret"

db=SQLAlchemy(app)
admin=Admin(app,template_mode="bootstrap3")

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25))
    
    def __repr__(self):
        return f"<User {self.username}>"

# this is most straightforward way of adding model view to admin
admin.add_view(ModelView(User,db.session))

if __name__=="__main__":
    app.run(debug=True)
```

If you want to exclude certain columns from your model when 
rendering admin views, use ```column_exclude_list``` property
of the ```BaseModelView```

```python
from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
    column_exclude_list = ['password']
```

If you want to force display the primary key, set ```column_display_pk```
to True. It is False by default

Flask-Admin ModelView has properties such as below to enable or disable
certain CRUD operation on a model

- ```can_create```
- ```can_edit```
- ```can_delete```

If you want to disable any CRUD operation, set one of above
to Falsegit@github.com:samrullo/bsiuzbekistanjapan.git