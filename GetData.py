# -*- coding:utf-8 -*-
_author_ = 'sky'
"""
调用东方财富网的数据接口获取数据，返回一个dict
"""

import requests
import re
import logging

class GetData(object):
    def __init__(self, code):
        #code = raw_input()
        self.code_header = re.split('\d{6}', code)[0]
        self.code_num = re.split('[sz]|[sh]', code)[2]


    def request_data(self):
        """
       根据给定的code，获取数据
        :param code: 
        :return: 
        """
        try:
            if self.code_header == "sh":
                url_sh = 'http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id={0}1'.format(self.code_num)
                response = requests.get(url_sh)
            elif self.code_header == "sz":
                url_sz = 'http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id={0}2'.format(self.code_num)
                response = requests.get(url_sz)
            data = eval(response.content.split('(')[1].split(')')[0])['Value']
            return self._parser(data)
        except:
            logging.info('输入的code有误，或者不存在，请重新输入')

    def _parser(self, data):
        """
        将获得的数据转换成dict
        股票代码:Symbol, 涨停价:high_price, 跌停价:low_price, 现价:LastTrade
        偏离值:Changes, 今天最低:lowest_price, 今天最高:highest_price 偏离幅度:Chg
        成交量:Volume, 今日开盘价:Opens, 昨日收盘价:PrevClose, 成交额:Turnover
        量比:QRR, 换手率:change_percent, 市盈率:Price_earnings_ratio, 市净率:PBV
        外盘数:Ask, 内盘数:Bid, 委比:The_Committee, 委差:Commission, 获取时间:date
        :param data: 出入的list
        :return: dicts
        """
        dicts = {}
        dicts['name'] = data[2]
        dicts['Symbol'] = self.code_num
        dicts['high_price'] = data[23]
        dicts['low_price'] = data[24]
        dicts['LastTrade'] = data[25]
        dicts['Changes'] = data[27]
        dicts['lowest_price'] = data[32]
        dicts['highest_price'] = data[30]
        dicts['Chg'] = data[29]
        dicts['Volume'] = data[31]
        dicts['Opens'] = data[28]
        dicts['PrevClose'] = data[34]
        dicts['Turnover'] = data[35]
        dicts['QRR'] = data[36]
        dicts['change_percent'] = data[37]
        dicts['Price_earnings_ratio'] = data[38]
        dicts['Ask'] = data[39]
        dicts['Bid'] = data[40]
        dicts['PBV'] = data[43]
        dicts['The_Committee'] = data[41]
        dicts['Commission'] = data[42]
        dicts['date'] = data[49]
        return dicts



