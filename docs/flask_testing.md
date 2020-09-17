# Flask-Test

First to be able to run ```$flask test``` command

```python
@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)
```

It is useful to define a ```BaseTestCase``` 
and subclass it for individual tests
```python
from flask_testing import TestCase
from application import create_app,db
from application.auth.models import User

class BaseTestCase(TestCase):
    def create_app(self):
        app=create_app('test')
        return app

    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com",username="admin", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
```

To test FlaskForms we need to make sure to set
```app.config['WTF_CSRF_ENABLED']=False```

```python
class RegisterFormTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        user = User(email="test@test.com", username="testuser")
        self.app.config['WTF_CSRF_ENABLED']=False

    def test_validate_success_register_form(self):
        form = RegisterForm(email="nohbus.veollurma@gmail.com", username="myusername", password="mysecret", confirm_password="mysecret")
        self.assertTrue(form.validate())

```