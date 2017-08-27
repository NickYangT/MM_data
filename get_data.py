# -*- coding:utf-8 -*-
_author_ = 'sky'
"""
调用东方财富网的数据接口获取数据，返回一个dict
"""

import requests
import re
import logging

class GetData(object):
    def __init__(self):
        code = raw_input()
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
            return self.parser(data)
        except:
            logging.info('输入的code有误，或者不存在，请重新输入')

    def parser(self, data):
        """
        将获得的数据转换成dict
        股票代码:code, 涨停价:high_price, 跌停价:low_price, 现价:now_price
        偏离值:zhangfu, 今天最低:lowest_price, 今天最高:highest_price 偏离幅度:add_percent
        成交量:change_num, 今日开盘价:start_price, 昨日收盘价:end_price, 成交额:changed_value
        量比:QRR, 换手率:change_percent, 市盈率:Price_earnings_ratio, 市净率:PBV
        外盘数:buy, 内盘数:sell, 委比:The_Committee, 委差:Commission, 获取时间:date
        :param data: 出入的list
        :return: dicts
        """
        dicts = {}
        dicts['name'] = data[2]
        dicts['code'] = self.code_num
        dicts['high_price'] = data[23]
        dicts['low_price'] = data[24]
        dicts['now_price'] = data[25]
        dicts['zhangfu'] = data[27]
        dicts['lowest_price'] = data[32]
        dicts['highest_price'] = data[30]
        dicts['add_percent'] = data[29]
        dicts['change_num'] = data[31]
        dicts['start_price'] = data[28]
        dicts['end_price'] = data[34]
        dicts['changed_value'] = data[35]
        dicts['QRR'] = data[36]
        dicts['change_percent'] = data[37]
        dicts['Price_earnings_ratio'] = data[38]
        dicts['buy'] = data[39]
        dicts['sell'] = data[40]
        dicts['PBV'] = data[43]
        dicts['The_Committee'] = data[41]
        dicts['Commission'] = data[42]
        dicts['date'] = data[49]
        return dicts
if __name__ == '__main__':
    data = GetData().request_data()
    print '\033[1;34;40m {0}'.format(data)
