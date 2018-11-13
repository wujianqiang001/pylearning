# -*- coding:utf-8 -*-
import pymysql
'''
连接数据库
'''

#打开数据库链接
db = pymysql.connect(host="10.112.43.35",user="root",
    password="Hny618gAIDpA8gCN",db="lebizhong",port=3307,charset='utf8')

# 使用cursor()方法获取操作游标
#游标是系统为用户开设的一个数据缓冲区，存放SQL语句的执行结果
cur = db.cursor()

sql = "select * from goods_category"
try:
    #执行sql语句
    cur.execute(sql)
    #获取查询的所有记录
    result = cur.fetchall()   #fetchall() 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
    for i in result:
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
except Exception as e:
    raise e
finally:
    #关闭连接
    db.close()