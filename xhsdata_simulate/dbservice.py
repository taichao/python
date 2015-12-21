# coding: utf-8
import mysql.connector,time,random,uuid, datetime

class DBService:
    def __connect(self):
        config={'host':'rdsqswhmjfiys87frepua.mysql.rds.aliyuncs.com',
                'user':'xhsdata',
                'password':'xhs_data',
                'port':3306 ,#默认即为3306
                'database':'xhs_data',
                'charset':'utf8'#默认即为utf8
                }
        try:
            cnn=mysql.connector.connect(**config)
            return cnn
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))

    def executeQuery(self,sql,data = None):
        cnn  = self.__connect()
        try:
            cursor = cnn.cursor()
            if data is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql,data)
            row = cursor.fetchall()
            return row
        finally:
            if cursor:
                cursor.close()
            if cnn:
                cnn.close()


    def executeUpdate(self,sql,data):
        cnn  = self.__connect()
        try:
            cursor = cnn.cursor()
            cursor.execute(sql,data)
            cnn.commit()
        finally:
            if cursor:
                cursor.close()
            if cnn:
                cnn.close()


    def create_user(self,client_id = None):
        user_id = int(time.time() * 1000)
        name = user_id
        province_list = [ '上海', '云南', '内蒙古', '北京', '台湾', '吉林', '四川', '天津', '宁夏', '安徽', '山东', '山西', '广东', '广西', '新疆', '江苏', '江西', '河北', '河南', '浙江', '海南', '湖北', '湖南', '澳门', '甘肃', '福建', '西藏', '贵州', '辽宁', '重庆', '陕西', '青海', '香港', '黑龙江' ]
        provice = province_list[ random.randint(0,len(province_list) -1) ]
        create_date = time.strftime('%Y-%m-%d %T',time.localtime(time.time()))
        channel_list = ["3001","3002","3003"]
        user_channel = channel_list[random.randint(0,2)]
        if client_id is None:
            client_id = str( uuid.uuid1() )
        else:
            client_id = str(client_id)
        sql = """
            INSERT INTO `xhs_data`.`test_mob_user`
            (`user_id`,
            `name`,
            `province`,
            `create_date`,
            `user_channel`,
            `client_id`)
            VALUES
            (
            %s,%s,%s,%s,%s,%s
            )
        """
        data = (user_id,name,provice,create_date,user_channel,client_id)
        self.executeUpdate(sql,data)

    def get_user(self, client_id = None):
        if client_id is None:
            sql = "SELECT user_id,client_id FROM xhs_data.test_mob_user order by rand() limit 1"
            data = None
        else:
            sql = "SELECT user_id,client_id FROM xhs_data.test_mob_user where client_id=%s"
            data = (client_id,)
        rows = self.executeQuery(sql,data)
        if len(rows) > 0:
            return rows[0]

    def get_user_forfile(self,day,hour):
        sql = """
            SELECT user_id,name,sex,age,province,create_date,user_channel
            FROM xhs_data.test_mob_user
            where date_format(create_date,'%Y%m%d') = '{day}' and hour(create_date) = {hour}
            """
        sql = sql.format(day=day,hour=hour)
        print(sql)
        cnn  = self.__connect()
        try:
            cursor = cnn.cursor()
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is not None:
                return row
            else:
                print("get_user_error")
        finally:
            cursor.close()
            cnn.close()



    def get_area(self):
        id = random.randint(1,1700000)
        sql = "select ip,country,province,city,county from sh_ip_factory where id=%d" % id
        res = self.executeQuery(sql)
        return res


    def create_client_id(self):
        client_id = uuid.uuid1();
        sql = "insert into test_mob_device values(%s,%s)"
        today = datetime.datetime.today()
        data = (str(client_id), today)
        self.executeUpdate(sql,data)
        return client_id

    def get_client_info(self):
        sql = "select client_id from xhs_data.test_mob_device order by rand() limit 1"
        sql = """
         select a.client_id,b.user_id from xhs_data.test_mob_device a
         left join xhs_data.test_mob_user b on a.client_id = b.client_id
          order by rand() limit 1
        """
        rows = self.executeQuery(sql)
        if len(rows) > 0:
            return rows[0]

