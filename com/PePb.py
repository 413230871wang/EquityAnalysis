import sys
import baostock as bs
import pandas as pd
import os
import numpy as np
import com.dateUtils as du

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
    rs = bs.query_history_k_data_plus(code,"date,peTTM,pbMRQ",start_date=du.getTenYearsAgoTime(), end_date=du.getYesterDayTime(),frequency="d", adjustflag="3")
    #### 打印结果集 ####
    result_list = []
    while (rs.error_code == '0') & rs.next():result_list.append(rs.get_row_data())
    result1 = pd.DataFrame(result_list,columns=rs.fields,dtype=np.float).sort_values(by='peTTM').reset_index(drop=True)
    result2 = pd.DataFrame(result_list, columns=rs.fields,dtype=np.float).sort_values(by='pbMRQ').reset_index(drop=True)
    #获取某个值在集合中的位置
    todayPEIndex = result1[(result1.date==du.getYesterDayTime())].index.tolist()[0]
    todayPBIndex = result2[(result2.date == du.getYesterDayTime())].index.tolist()[0]
    lensPE = len(result1)
    lensPB = len(result2)
    print("PE位置是："+str(todayPEIndex)+",总列数是："+str(lensPE))
    print("PE的分位点是："+str(todayPEIndex/lensPE*100)[:4]+"%")
    print("PB位置是：" + str(todayPBIndex) + ",总列数是：" + str(lensPB))
    print("PB的分位点是：" + str(todayPBIndex / lensPB * 100)[:4] + "%")
    #### 结果集输出到csv文件 ####
    # my_file = "/Users/mfhj-dz-001-068/pythonData/pe_"+code+"_data.csv";
    # if os._exists(my_file):
    #     #删除文件
    #     os.remove(my_file)
    #
    # result1.to_csv("/Users/mfhj-dz-001-068/pythonData/pe_"+code+"_data.csv", encoding="gbk", index=False)

print("-----登陆系统：")
bs.logout()