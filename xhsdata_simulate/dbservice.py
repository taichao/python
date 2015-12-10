# coding: utf-8
import mysql.connector,time,random,uuid

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

    def create_user(self):
        user_id = int(time.time() * 1000)
        name = user_id
        province_list = [ '上海', '云南', '内蒙古', '北京', '台湾', '吉林', '四川', '天津', '宁夏', '安徽', '山东', '山西', '广东', '广西', '新疆', '江苏', '江西', '河北', '河南', '浙江', '海南', '湖北', '湖南', '澳门', '甘肃', '福建', '西藏', '贵州', '辽宁', '重庆', '陕西', '青海', '香港', '黑龙江' ]
        provice = province_list[ random.randint(0,len(province_list) -1) ]
        create_date = time.strftime('%Y-%m-%d %T',time.localtime(time.time()))
        channel_list = ["3001","3002","3002"]
        user_channel = channel_list[random.randint(0,2)]
        client_id = str( uuid.uuid1() )
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
        cnn  = self.__connect()
        try:
            cursor = cnn.cursor()
            cursor.execute(sql,data)
            cnn.commit()
        finally:
            cursor.close()
            cnn.close()

    def get_user(self):
        sql = "SELECT user_id,client_id FROM xhs_data.test_mob_user order by rand() limit 1"
        cnn  = self.__connect()
        try:
            cursor = cnn.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                return row
            else:
                print("get_user_error")
        finally:
            cursor.close()
            cnn.close()

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
