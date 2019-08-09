import sys
import baostock as bs
import pandas as pd
import os
import com.dateUtils as du
import numpy as np

#### 登陆系统 ####
print("-----登陆系统：")
lg = bs.login(user_id="anonymous", password="123456")
while True:
    print("-----请输入要查询的股票代码：")
    code = input()
    #### 登出系统 ####
    if (code == 'exit'):
        break
    #### 获取沪深A股估值指标(日频)数据 ##### peTTM    动态市盈率# psTTM    市销率# pcfNcfTTM    市现率# pbMRQ    市净率
    rs = bs.query_history_k_data_plus(code,"date,pbMRQ,peTTM",start_date=du.getTenYearsAgoTime(), end_date=du.getYesterDayTime(),frequency="d", adjustflag="3")
    #### 打印结果集 ####
    result_list = []
    while (rs.error_code == '0') & rs.next():result_list.append(rs.get_row_data())
    result2 = pd.DataFrame(result_list, columns=rs.fields,dtype=np.float)
    print(result2.dtypes)
    result2 = result2.sort_values(by='pbMRQ',ascending=False)
    result2 = result2.reset_index(drop=True)
    #### 结果集输出到csv文件 ####
    my_file = "/Users/mfhj-dz-001-068/pythonData/pe_"+code+"_data.csv";
    if os._exists(my_file):
        #删除文件
        os.remove(my_file)

    result2.to_csv("/Users/mfhj-dz-001-068/pythonData/pe_"+code+"_data1.csv", encoding="gbk", index=False)

print("-----登陆系统：")
bs.logout()