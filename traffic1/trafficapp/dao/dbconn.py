import pymysql
from pymysql.err import DatabaseError
# 数据访问层
class DBConn:
    def __init__(self, 
            server_addr="127.0.0.1", 
            server_port=3306, 
            db_user="root", 
            db_password="1822", 
            db_name="TrafficsDB"):
        # 链接数据库
        self.db = pymysql.connect(host=server_addr,user=db_user,password=db_password,database=db_name,charset='utf8')
    
    def close(self):
        self.db.close()
    
    def insert(self, sql):
        cursor = self.db.cursor()
        try:
            re = cursor.execute(sql)
            self.db.commit()
            # 释放游标
            cursor.close()
            cursor = None
            # 返回insert状态
            return (0, re)
        except DatabaseError as err:
            return err.args   # 返回状态码与错误提示
        except:
            return (-1, "未知错误")
    
    def delete(self, sql):
        # raise Exception("no implimentation！")
        return (0, "删除成功数")
    
    def query(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data  # ((字段1, .....), (......), ......)

# 直接创建一个数据库链接实例
conn = DBConn()
