#!/usr/bin/env python
# coding=utf-8
import pymysql
conn=pymysql.connect(host="localhost",user="admin",password="admin",database="books")
cursor1=conn.cursor()
cursor1.execute("""insert into book_list (id,name,author) values (1,"math","tom")""")
cursor1.execute("""select * from book_list""")
row=cursor1.fetchall()
print(row)
cursor1.close()
conn.close()
