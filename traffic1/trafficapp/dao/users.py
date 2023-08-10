from trafficapp.dao.dbconn import conn

class UserDAO:
    def  __init__(self):
        super(UserDAO, self).__init__()
    
    def validate(self, user):
        # 数据验证
        sql = F"select count(*) from TUser where u_name='{user}'"
        result = conn.query(sql)
        if result[0][0] > 0: 
            return True
        else:
            return False
        