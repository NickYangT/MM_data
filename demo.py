# -*- coding:gb2312 -*- 
_author_ = 'sky'
import re
code ='sh002601'
code_header = re.split('\d{6}', code)[0]
print code_header
code_num = re.split('[sz]|[sh]', code)[2]
print code_num
