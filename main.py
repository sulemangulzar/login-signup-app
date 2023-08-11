from database import database
from models import Person

database.connect()
database.create_tables([Person])

option = input("1. Login\n2. Signup\n")
if option == "1":
    username = input("Enter your username: ")
    person = Person.get_or_none(username=username)
    if person == None:
        print(f"The username '{username}' doesn't exist. Please sign up.")
    else:
        print(f"{person.name} is {person.age} years old.")
elif option == "2":
    username = input("Enter your username: ")
    person = Person.get_or_none(username=username)
    if person == None:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        person = Person.create(
            username=username,
            name=name,
            age=age,
        )
    else:
        print(f"The username '{username}' is already taken.")
