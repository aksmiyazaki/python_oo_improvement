from os import chdir
chdir('/home/aksmiyazaki/git/python_oo_improvement/etl_python/code')

import sqlite3


class DatabaseService:
    __instance = None
    __conn = None

    @staticmethod
    def get_instance():
        if DatabaseService.__instance is None:
            DatabaseService()
        return DatabaseService.__instance

    def initialize_database_conn(self, database_name):
        try:
            self.__conn = sqlite3.connect(database_name)
        except Exception as e:
            print(e)
            raise

    def execute_insert(self, sql, must_commit = False):
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
        self.__conn.commit()

    def execute_select(self, sql):
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
        if DatabaseService.__instance is not None:
            raise Exception("DatabaseService is a singleton class. Try GetInstance instead of constructing a new object.")
        else:
            DatabaseService.__instance = self
