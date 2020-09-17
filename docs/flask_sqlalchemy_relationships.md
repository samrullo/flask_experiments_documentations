# Relationships

Suppose we have a User model and Role model. 
A user can have only one role, while a role can belong to many users.
So the relationship of the Role to User is one to many.

User model is defined as below
```python
class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String)
    ...
    role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))
``` 

Role model is defined as below
```python
class Role(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    permissions=db.Column(db.Integer)
    users=db.relationship("User",backref="role")
```

In some cases we can have one to one relationship.
For instance user enters one record for a post weight, then admin
enters his measurement as a record for each post weight record.
In this case the relationship between user entered post weight
and admin entered post weight is one to one.

In such cases, we can set ```uselist``` parameter of
```db.relationship``` to False

## Many to many relationship

A classic example is students and classes. A student can register with many classes,
and a class will have many students.

We will need to use an association table in this case.
```python
registrations=db.Table("registrations",
                db.Column("student_id",db.Integer,db.ForeignKey("students.id")),
                db.Column("class_id",db.Integer,db.ForeignKey("classes.id")))

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    classes=db.relationship('Class',
                            secondary=registrations,
                            backref=db.backref('students',lazy='dynamic'),
                            lazy='dynamic')

class Class(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
```
