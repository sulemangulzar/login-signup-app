from peewee import CharField, IntegerField, Model

from database import database


class Person(Model):
    username = CharField(primary_key=True)
    name = CharField()
    age = IntegerField()

    class Meta:
        database = database
