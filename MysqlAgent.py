# -*- coding:utf-8 -*-
__author__ = 'yang.tian'
'''
初始化数据库，创建数据库连接代理，并执行需要执行的sql
'''
import MySQLdb
import logging


class MysqlAgent():
    def __init__(self, host, db, port, user, password):
        """
        连接数据库，并获得游标
        :param host: 地址
        :param db: 数据库
        :param port: 端口号
        :param user: 用户名
        :param password:密码
        """
        self.conn = MySQLdb.connect(host=host, user=user, passwd=password, db=db, port=port, charset='utf8')
        self.cur = self.conn.cursor()

    def do_sql(self, type, sql):
        '''
        根据sql是否需要返回数据，进行不同的处理
        :param type: sql是否需要返回数据Y：表示需要，N：表示不需要
        :param sql: 需要执行的sql语句
        :return:
        '''
        if type == 'Y':
            logging.info("该sql需要返回数据，执行_sql_with_return_data")
            self._sql_with_return_data(sql)
        elif type == 'N':
            logging.info("该sql不需要返回数据，执行_sql_without_return_data")
            self._sql_without_return_data(sql)
        else:
            logging.info('sql的类型输入有，请检查！')
        #self.cur.close()
        self.conn.commit()
        #self.conn.close()

    def _sql_with_return_data(self, sql):
        '''
        执行需要返回数据的sql
        :param sql:
        :return:
        '''
        logging.info("执行_sql_with_return_data")
        value = self.cur.execute(sql)
        return value

    def _sql_without_return_data(self, sql):
        '''
        执行不需要返回数据的sql
        :param sql:
        :return value：需要返回的数据
        '''
        logging.info("执行_sql_without_return_data")
        self.cur.execute(sql)




