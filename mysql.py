# -*- coding: utf-8 -*- #
import MySQLdb

conn = MySQLdb.Connect(
                        host = '115.29.52.104',
                        port = 3306,
                        user = 'nebula',
                        passwd = '314159',
                        db = 'one',
                        charset = 'utf8'
                        )
cursor = conn.cursor()
conn.autocommit(False)

sql_insert = "insert into quotations(content) values('test')"
sql_update = "update quotations set content='test_update' where id=3"
sql_delete = "delete from quotations where id>2"


try:
    #cursor.execute(sql_insert)
    #print cursor.rowcount

    cursor.execute(sql_update)
    print cursor.rowcount

    cursor.execute(sql_delete)
    print cursor.rowcount

    conn.commit()
except Exception as e:
    print e
    conn.rollback()
finally:
    cursor.close()
    conn.close()
    


