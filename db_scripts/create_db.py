import sqlite3
import os


class DatabaseManager:
    def __init__(self):
        """
        Initialize the DatabaseManager class.
        Sets up the project directory and database folder, and checks if the database exists.
        """
        self.project_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..', '..', 'main.py')))
        self.db_folder = os.path.join(self.project_dir, 'db')
        self.db_path = os.path.join(self.db_folder, 'investments.db')
        self.db_exists = os.path.exists(self.db_path)
        self.check_db_exists()

    def check_db_exists(self):
        """
        Check if the database exists. If not, create a new database.
        """
        if not self.db_exists:
            self.create_database()
        else:
            print("Database already exists")

    def create_database(self):
        """
        Create the SQLite database and required tables if they do not exist.
        """
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # SQL statements to create tables
        create_info_table = """
        CREATE TABLE IF NOT EXISTS Info (
            Cash INTEGER,
            EUR REAL,
            USD REAL
        );
        """
        create_portfolio_current_table = """
        CREATE TABLE IF NOT EXISTS Portfolio_current (
            ISIN TEXT(30),
            Asset_class TEXT(100),
            Asset TEXT(100),
            Currency TEXT(3),
            Percent REAL,
            HUF_invested INTEGER
        );
        """
        create_portfolio_suggested_table = """
        CREATE TABLE IF NOT EXISTS Portfolio_suggested (
            ISIN TEXT(30),
            Portfolio_type TEXT(100),
            Asset_class TEXT(100),
            Asset TEXT(100),
            Currency TEXT(3),
            Percent REAL,
            HUF_invested INTEGER
        );
        """
        create_sell_table = """
        CREATE TABLE IF NOT EXISTS Sell (
            ISIN TEXT(30),
            Portfolio_type TEXT(100),
            Asset_class TEXT(100),
            Asset TEXT(100),
            Currency TEXT(3),
            Units REAL,
            Done INTEGER
        );
        """
        create_buy_table = """
        CREATE TABLE IF NOT EXISTS Buy (
            ISIN TEXT(30),
            Portfolio_type TEXT(100),
            Asset_class TEXT(100),
            Asset TEXT(100),
            Currency TEXT(3),
            HUF_to_invest INTEGER,
            Done INTEGER
        );
        """

        # Execute SQL statements to create tables
        cursor.execute(create_info_table)
        cursor.execute(create_portfolio_current_table)
        cursor.execute(create_portfolio_suggested_table)
        cursor.execute(create_sell_table)
        cursor.execute(create_buy_table)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print("Database and tables created successfully.")
        return True
