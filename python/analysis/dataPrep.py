__author__ = 'Arul'

import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize


def read_data(inputFile):
    with open(inputFile) as f:
        data = json.load(f)
        return json_normalize(data)

def pushNotification(list1):
    strMsg = ''.join("Please use the app "+str(list1[1]))
    strMsg = strMsg.replace("'","")
    print strMsg
    return strMsg

def getLowUsageAppUser(data):
    #print len(data)
    data_low = data.ix[data.AppProperUsageCount == min(data['AppProperUsageCount'])]

    for i in data_low.index:
        list1 = (str(i)).replace("'","").split(',')
        pushNotification(list1)

def addFeatures(data):

    # Adding usage count related information
    df_properUsageCount =  data[data.use_time > 100].groupby('device')[['use_time']].count()
    df_properUsageCount.columns = ['ProperUsageCount']
    df_totalUsageCount = data.groupby('device')[['use_time']].count()
    df_totalUsageCount.columns = ['TotalUsageCount']
    df_avg_properUsageTime =  data[data.use_time > 100].groupby('device')[['use_time']].mean()
    df_avg_properUsageTime.columns = ['AverageProperUsageTime']
    df_avg_totalUsageTime = data.groupby('device')[['use_time']].mean()
    df_avg_totalUsageTime.columns = ['AverageTotalUsageCount']

    result = df_properUsageCount.join(df_totalUsageCount)
    result = result.join(df_avg_properUsageTime)
    result = result.join(df_avg_totalUsageTime)
    result.to_csv("../data/agg.data")

    # Adding time related features - for future learning
    df_app_device_properUsageCount = data[data.use_time > 100].groupby(['device','app_name'])[['use_time']].count()
    df_app_device_properUsageCount.columns = ['AppProperUsageCount']
    df_app_device_totalUsageCount = data.groupby(['device','app_name'])[['use_time']].count()
    df_app_device_totalUsageCount.columns = ['AppTotalUsageCount']
    df_avg_app_device_properUsageTime = data[data.use_time > 100].groupby(['device','app_name'])[['use_time']].mean()
    df_avg_app_device_properUsageTime.columns = ['AppProperUsageTime']
    df_avg_app_device_totalUsageTime = data.groupby(['device','app_name'])[['use_time']].mean()
    df_avg_app_device_totalUsageTime.columns = ['AppTotalUsageTime']

    result = df_app_device_properUsageCount.join(df_app_device_totalUsageCount)
    result = result.join(df_avg_app_device_properUsageTime)
    result = result.join(df_avg_app_device_totalUsageTime)
    result['index'] = result.index
    getLowUsageAppUser(result)
    return result


def main():
    inputFile = '../data/data.json'
    data = read_data(inputFile)

    data_mod = addFeatures(data)
    #data.to_csv("../data/data1.csv",index=False)

if __name__ == "__main__":
    main()

