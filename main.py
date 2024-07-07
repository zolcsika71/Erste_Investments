# imports

from db_scripts.create_db import DatabaseManager
from gui.gui import run_app


if __name__ == '__main__':
    db_manager = DatabaseManager()
    run_app()
