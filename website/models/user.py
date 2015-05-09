from flask.ext.security import UserMixin, RoleMixin
from .core import db


class Role(db.Model, RoleMixin):

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(30), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean())

role_user = db.Table(
    'role_user',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
