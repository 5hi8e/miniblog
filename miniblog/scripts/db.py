from flask_script import Command
from miniblog import db

class InitDB(Command):
    "create database"
    def run(self):
        db.create_all()
