# -*- coding:utf-8 -*-
_author_ = 'sky'
'''
数据处理，写数据到数据库
'''
from MysqlAgent import MysqlAgent
from GetData import GetData

class WriteDataToMysql(object):
    def __init__(self, code):
        self.dicts = GetData(code).request_data()
        print self.dicts

    def write_data_to_sql(self):
        symbol = '"{0}"'.format(self.dicts['Symbol'])
        gpname ='"{0}"'.format(self.dicts['name'])
        LastTrade = self.dicts['LastTrade']
        Changes = self.dicts['Changes']
        Chg = self.dicts['Chg']
        Bid = self.dicts['Bid']
        Ask = self.dicts['Ask']
        PrevClose = self.dicts['PrevClose']
        Opens = self.dicts['Opens']
        Volume = self.dicts['Volume']
        Turnover = '"{0}"'.format(self.dicts['Turnover'])
        The_Committee = self.dicts['The_Committee']
        Commission = self.dicts['Commission']
        date = '"{0}"'.format(self.dicts['date'])
        sql_create_table = """
            CREATE TABLE  IF not exists Share_Main_Data (
                id INT(10) NOT NULL primary key AUTO_INCREMENT,
                Symbol VARCHAR(20) NOT NULL COMMENT "代码",
                gpname VARCHAR(255) NOT NULL COMMENT "名称",
                LastTrade FLOAT NOT NULL COMMENT "最新价",
                Changes FLOAT NOT NULL COMMENT "涨幅",
                Chg FLOAT NOT NULL COMMENT "涨幅率",
                Bid INT (20) NOT NULL COMMENT "卖出",
                Ask INT (20) NOT NULL COMMENT "买入",
                PrevClose FLOAT COMMENT "昨收",
                Opens FLOAT NOT NULL COMMENT "今开",
                Volume INT NOT NULL COMMENT "成交量",
                Turnover VARCHAR(20) NOT NULL COMMENT "成交额",
                The_Committee FLOAT NOT NULL COMMENT"委比",
                Commission INT(10) NOT NULL COMMENT "委差",
                date TIMESTAMP NOT NULL COMMENT "创建时间")
        """

        sql_insert_data = '''
                  insert into  Share_Main_Data values(null , {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13});
        '''.format(symbol, gpname, LastTrade, Changes, Chg, Bid, Ask, PrevClose, Opens, Volume, Turnover, The_Committee, Commission, date )
        instance = MysqlAgent(host='localhost', db='polls', port=3306, user='root', password='123456')
        #instance.cur
        #instance.do_sql('N', sql_create_table)
        instance.do_sql('N', sql_insert_data)

