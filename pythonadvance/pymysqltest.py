#-*- coding: utf-8 -*-
import pymysql

conn=pymysql.connect(host='192.168.1.111',user='root',passwd='1234',db='zmap_empi',charset='utf8')

cur=conn.cursor()
query='select count(*)  from zmap_r_patient_empi_jb'

cur.execute(query)
result = cur.fetchall()  # result为tuple类型，记录存放是((),(),...()) 这样的形式


for i in result:
    print i