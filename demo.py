# -*- coding:utf-8 -*-
_author_ = 'sky'

import MySQLdb
from MysqlAgent import MysqlAgent
from GetData import GetData
from DealWithData import WriteDataToMysql


w_instance = WriteDataToMysql('sz000656').write_data_to_sql()


