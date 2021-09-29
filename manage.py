from flask_script import Manager
from miniblog import create_app

from miniblog.scripts.db import InitDB, DropDB

if __name__ == "__main__":
    manager = Manager(create_app)
    manager.add_command('init_db', InitDB())
    manager.add_command('drop_db', DropDB())
    manager.run()
