#!/usr/bin/env python
# coding=utf-8
import pymysql
import sqlite3
class Db():
    def __init__(self):
        self.conn = sqlite3.connect('data/test.db')
    def creatdb(self):
        print("Opened database successfully")
        c = self.conn.cursor()
        c.execute('''CREATE TABLE COMPANY
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               AGE            INT     NOT NULL,
               ADDRESS        CHAR(50),
               SALARY         REAL);''')
        print("Table created successfully")
        self.conn.commit()
        self.conn.close()

    def insertdb(self,sql):
        c = self.conn.cursor()
        print("Opened database successfully")
        c.execute(sql)
        self.conn.commit()
        print("Records created successfully")
        # self.conn.close()

    def selectdb(self,sql):
        # conn = sqlite3.connect('../data/test.db')
        c = self.conn.cursor()
        print("Opened database successfully")
        cursor = c.execute(sql)
        print("Operation done successfully")
        c = cursor.fetchall()
        self.conn.close()
        return c
if __name__ == "__main__":
    db = Db()
    sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (9, 'Jeny', 22, 'California', 20000.00 )"
    db.insertdb(sql)
    cursor = db.selectdb("SELECT id, name, address, salary  from COMPANY WHERE ID = 9")
    for row in cursor:
       print("ID = ", row[0])
       print("NAME = ", row[1])
       print("ADDRESS = ", row[2])
       print("SALARY = ", row[3], "\n")