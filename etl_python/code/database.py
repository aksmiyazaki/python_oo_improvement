import sqlite3
from sqlite3 import IntegrityError


class DatabaseService:
    """
    This class provides a database interation service.
    It allows qurying and executing commands in SQLite database
    It's implemented with a singleton design pattern because its main responsi
    bility is provide a communication channel between the python code and the database.
    """
    __instance = None
    __conn = None

    @staticmethod
    def get_instance():
        """
        Static method that allows users of this service to request an object.
        If it doesn't exists (hasn't been created), it will instantiate an object.
        """
        if DatabaseService.__instance is None:
            DatabaseService()
        return DatabaseService.__instance

    def initialize_database_conn(self, database_name):
        """
        This method initializes the connection with the database.
        Keyword arguments:
        database_name -- a string object with database name. Since we are using
        sqlite, it must be the name of the file (.db).
        """
        try:
            self.__conn = sqlite3.connect(database_name)
        except Exception as e:
            print(e)
            raise

    def execute_insert(self, sql, must_commit = False):
        """
        This method executes an Insert into the database.
        Keyword arguments:
        sql -- a string object with the sql to be executed (insert) into the database
        must_commit -- a bool object that indicates if it is necessary to call
        commit() method after each insert,
        """
        try:
            cur = self.__conn.cursor()
            cur.execute(sql)
            if must_commit:
                self.__conn.commit()
        except Exception as e:
            print(f"[ERROR] Can't insert data:[{sql}]")
            print(e)
            raise

    def commit_changes(self):
        """
        Method that commit changes to the database.
        """
        self.__conn.commit()

    def execute_select(self, sql):
        """
        Method which executes a Select into the database.
        Keyword arguments:
        sql -- a string object with the sql to fetch the data.
        """
        try:
            cur = self.__conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
        except:
            print(f"[ERROR] Can't query data:[{sql}]")
            print(e)
            raise

    def __init__(self):
        """
        Class constructor.
        The whole class works as a singleton (if this method is called twice),
        it will trigger an Exception.
        """
        if DatabaseService.__instance is not None:
            raise Exception("DatabaseService is a singleton class. Try GetInstance instead of constructing a new object.")
        else:
            DatabaseService.__instance = self
