# -*- coding: UTF-8 -*-

import pymysql
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Diff:
    def __init__(self):
        print("start to connect databases!!!")

        self.test_host="192.168.12.35"
        self.test_port=3306
        self.test_user="root"
        self.test_passwd="123456"
        self.test_dbname="wz"

        self.online_host = "192.168.12.35"
        self.online_port = 3306
        self.online_user = "root"
        self.online_passwd = "123456"
        self.online_dbname="school"


    def get_data(self, env, sql):
        if env == "test":
            zentao = dict(host=self.test_host, port=self.test_port, user=self.test_user, passwd=self.test_passwd, db=self.test_dbname, charset='utf8')
            conn = pymysql.connect(**zentao)
        else:
            zentao = dict(host=self.online_host, port=self.online_port, user=self.online_user, passwd=self.online_passwd, db=self.online_dbname, charset='utf8')
            conn = pymysql.connect(**zentao)

        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()  # 搜取所有结果
        cur.close()
        conn.close()
        return results

    # 把返回的嵌套元素转换为列表
    def to_list(self, result):
        r_list = []
        print(result)
        for t in result:
            print(t)
            r_list.append(t[0])
        return r_list

    # test_table 里面有的 online_table没有
    def comp(self, test_table, online_table):
        ret = [i for i in test_table if i not in online_table]
        return ret

    # test_table online_table 都有的
    def both_list(self, L1, L2):
        both = [i for i in L1 if i in L2]
        return both

    def result(self, test, online):
        test_have = self.comp(test, online)

        online_have = self.comp(online, test)
        if len(test_have) + len(online_have) != 0:
            print("test环境有的table,online环境没有: \r\n")
            for i in test_have:
                print(" ", i)
            print("\r")
        print("online环境有的table,test环境没有: \r\n")
        for i in online_have:
            print(" ", i)

    def column_result(self, table_name, test, online):
        test_have = self.comp(test, online)
        online_have = self.comp(online, test)
        if len(test_have) + len(online_have) != 0:
            print("\r")
            print(" ", table_name, "表：test环境有的字段,online环境没有: \r\n")
            for i in test_have:
                print(" ", i)
            print("\r")
            print(" ", table_name, "表：online环境有的字段,test环境没有: \r\n")
            for i in online_have:
                print(" ", i)

    def export_table_structure(self, env, table_name):
        mysqldump_commad_params = {}
        mysqldump_commad_params['dumpcommad'] = 'mysqldump --no-data'
        if env == "test":
            mysqldump_commad_params['server'] = self.test_host
            mysqldump_commad_params['user'] = self.test_user
            mysqldump_commad_params['password'] = self.test_passwd
            mysqldump_commad_params['port'] = self.test_port
            mysqldump_commad_params['db'] = self.test_dbname
        else:
            mysqldump_commad_params['server'] = self.online_host
            mysqldump_commad_params['user'] = self.online_user
            mysqldump_commad_params['password'] = self.online_passwd
            mysqldump_commad_params['port'] = self.online_port
            mysqldump_commad_params['db'] = self.online_dbname

        file_name = """%s_have_%s.sql""" % (env, table_name)
        path = os.path.join(base_dir, 'sql', env, file_name)
        mysqldump_commad_sql = """%s -h%s -u%s -p%s -P%s %s %s > %s""" % (
        mysqldump_commad_params['dumpcommad'],
        mysqldump_commad_params['server'],
        mysqldump_commad_params['user'],
        mysqldump_commad_params['password'],
        mysqldump_commad_params['port'],
        mysqldump_commad_params['db'],
        table_name,
        path
        )
        # 必须切换到创建sql的文件夹下，才能执行命令！！！
        sql_file_path = os.path.join(base_dir, 'sql', env)
        if not os.path.exists(sql_file_path):
            os.makedirs(sql_file_path)
        os.chdir(sql_file_path)
        print(mysqldump_commad_sql)
        result = os.system(mysqldump_commad_sql)
        if result == 0:
            print("""----------- 导出 %s 表结构成功！------------""" % (table_name))
        else:
            print("""----------- 导出 %s 表结构失败！------------""" % (table_name))

    # print mysqldump_commad_sql
    def drop_more_comment(self, file_path):
        os.chdir()


if __name__ == '__main__':
    diff = Diff()
    diff.get_data("test","show tables")

    test_table_list = diff.to_list(diff.get_data('test', "show tables"))
    online_table_list = diff.to_list(diff.get_data('online', "show tables"))
    both_have_t = diff.both_list(test_table_list, online_table_list)
    print("----------------- 比较两个database的table差异 begin --------------------------")
    print("\r")
    # 调用比较结果函数
    diff.result(test_table_list, online_table_list)
    print("\r")
    print("----------------- 比较两个database的table差异 end --------------------------")
    print("\r\n")
    print("共有表个数：", both_have_t.__len__())
    print("共有表：", both_have_t)
    print("\r")
    print("----------------- 比较共有表的字段差异 begin --------------------------")
    print("\r")
    for i in range(0, len(both_have_t)):
        test_field_sql = "SELECT column_name FROM information_schema.columns WHERE Table_name= '%s' and table_schema = '%s'" % (
            both_have_t[i], diff.test_dbname)
        test_field = diff.to_list(diff.get_data("test", test_field_sql))
        online_field_sql = "SELECT column_name FROM information_schema.columns WHERE Table_name= '%s' and table_schema = '%s'" % (
            both_have_t[i], diff.online_dbname)
        online_field = diff.to_list(diff.get_data("online", online_field_sql))
        print(i + 1, both_have_t[i])
        diff.column_result(both_have_t[i], test_field, online_field)
    print("\r")
    print("----------------- 比较共有表的字段差异 end --------------------------")
    print("\r\n")
    print("----------------- 导出 表结构 begin -------------------------------")
    # 导出表结构sql
    print("----------------- 导出 test 环境有的表，而 online 环境没有的表 ----------")
    test_have = diff.comp(test_table_list, online_table_list)
    for table_name in test_have:
        diff.export_table_structure('test', table_name)
    print("\r\n")
    print("----------------- 导出 online 环境有的表，而 test 环境没有的表 ----------")
    online_have = diff.comp(online_table_list, test_table_list)
    for table_name in online_have:
        diff.export_table_structure('online', table_name)
    print("----------------- 导出 表结构 end -------------------------------")
