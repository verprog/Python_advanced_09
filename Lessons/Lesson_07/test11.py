import config
import MySQLdb
import MySQLdb.cursors as mc
import _mysql_exceptions

DictCursor = mc.DictCursor
SSCursor = mc.SSCursor
SSDictCursor = mc.SSDictCursor
Cursor = mc.Cursor


class Cursor(object):
    def __init__(self, cursorclass=Cursor, host=config.HOST, user=config.USER, passwd=config.PASS, dbname=config.MYDB,
         driver=MySQLdb, ):
        self.cursorclass = cursorclass
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.driver = driver
        self.connection = self.driver.connect(host=host, user=user, passwd=passwd, db=dbname, cursorclass=cursorclass)
        self.cursor = self.connection.cursor()


    def __iter__(self):
        for
        item in self.cursor:
        yield item


    def __enter__(self):
        return self.cursor


    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback() else:
            self.connection.commit()
        self.connection.close()


with Cursor() as cursor:
    print(cursor)
    connection = (cursor.connection)
print(connection)