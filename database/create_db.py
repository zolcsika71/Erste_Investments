import sqlite3
import os


class DatabaseManager:
    def __init__(self):
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.directory_path = os.path.join(self.project_dir, 'database')
        self.db_path = os.path.join(self.directory_path, 'investments.db')
        self.check_structure()

    def create_directory(self):
        print(f"Creating Database directory at: {self.directory_path}")
        os.makedirs(self.directory_path, exist_ok=True)
        print(f"Database directory created at: {self.directory_path}")
        return True

    def create_database(self):

        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # SQL statements to create tables
        create_info_table = """
        CREATE TABLE IF NOT EXISTS Info (
            Cash INTEGER(50),
            EUR REAL(50),
            USD REAL(50)
        );
        """

        create_portfolio_current_table = """
        CREATE TABLE IF NOT EXISTS Portfolio_current (
            ISIN TEXT(30),
            Asset_class TEXT(100),
            Asset TEXT(100),
            Currency TEXT(3),
            Percent REAL(30),
            HUF_invested INTEGER(50)
        );
        """

        create_portfolio_suggested_table = """
        CREATE TABLE IF NOT EXISTS Portfolio_suggested (
            ISIN TEXT(30),
            Portfolio_type TEXT(100),
            Asset_class TEXT(100),
            Asset TEXT(100),
            Currency TEXT(3),
            Percent REAL(30),
            HUF_invested INTEGER(50)
        );
        """

        create_sell_table = """
        CREATE TABLE IF NOT EXISTS Sell (
            ISIN TEXT(30),
            Portfolio_type TEXT(100),
            Asset_class TEXT(100),
            Asset TEXT(100),
            Currency TEXT(3),
            Units REAL(50),
            Done INTEGER(1)
        );
        """

        create_buy_table = """
        CREATE TABLE IF NOT EXISTS Buy (
            ISIN TEXT(30),
            Portfolio_type TEXT(100),
            Asset_class TEXT(100),
            Asset TEXT(100),
            Currency TEXT(3),
            HUF_to_invest INTEGER(50),
            Done INTEGER(1)
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

    def check_structure(self):

        # Check if the directory exists
        if not os.path.exists(self.directory_path):
            print(f"Database directory not found at: {self.directory_path}")
            self.create_directory()
        else:
            print(f"Database directory found at: {self.directory_path}")
            if not os.path.exists(self.db_path):
                print(f"Database not found at: {self.db_path}")
                self.create_database()
            else:
                print(f"Database found at: {self.db_path}")
                return True

