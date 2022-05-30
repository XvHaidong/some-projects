import csv
import pandas as pd
import tensorflow as tf
# from sklearn.model_selection import train_test_split

'''
将json文件格式转换成tsv
'''
#将json文件转换为csv文件，提取主要信息

#由于出现了许多转换问题，考虑把class变成0，1,2,3
#以下需要重写这段代码

import json
import csv
from random import shuffle
#表示次数

#
# ['cve_id', 'description', 'description_cleaned',
#  'cvssV2_baseScore', 'class']]
ID = []
description = []
description_cleaned = []
CWE = []
score = []
severity = []

v2_num = 0
with open('../../temp/nvdcve-1.1-2017.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']
            des = cve['description']['description_data'][0]['value']
            description.append(des)
            CWE.append(cwe[0]['value'])
            severity.append(vs)
        if len(temp1)!=0 and len(temp1)!=1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']
                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)

                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2016.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']
            des = cve['description']['description_data'][0]['value']
            description.append(des)
            CWE.append(cwe[0]['value'])


            severity.append(vs)
        if len(temp1)!=0 and len(temp1)!=1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2015.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!=0 and len(temp1)!=1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2014.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!=0 and len(temp1)!=1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2013.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2012.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2011.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2010.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2009.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2008.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']


                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2007.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2006.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2005.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2004.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']
            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2003.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']

            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
            CWE.append(cwe[0]['value'])
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()
with open('../../temp/nvdcve-1.1-2002.json', encoding='utf-8') as f:
    line = json.load(f)
    mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；

    for item in mylist:
        first =item
        cve = first['cve']
        cwe = cve['problemtype']['problemtype_data'][0]['description']
        temp1 = first['impact']
        if len(temp1)==1:
            v2_num+=1
            vs = temp1['baseMetricV2']['severity']
            CWE.append(cwe[0]['value'])
            des = cve['description']['description_data'][0]['value']
            description.append(des)
            severity.append(vs)
        if len(temp1)!= 0 and len(temp1)!= 1:
            score_ = temp1['baseMetricV3']['cvssV3']['baseScore']
            if score_:
                id = cve['CVE_data_meta']['ID']
                CWE.append(cwe[0]['value'])
                vs = temp1['baseMetricV3']['cvssV3']['baseSeverity']

                des = cve['description']['description_data'][0]['value']

                # score.append(score_)
                description.append(des)
                if len(des)==0:
                    print('sfsfs')
                # description_cleaned.append(des)
                severity.append(vs)
                ID.append(id)
    f.close()

#--------------------追加CWE的代码-----------------------------------------------------------------------
set_CWE = set(CWE)
# print(len(set_CWE))
# print(len(CWE))
# print(len(severity))
#len(CWE)和len(severity)一样，下一步读取CWE-description的映射;

with open('cwe_nvd.csv','r',newline='')as f:
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
data = data[1:]
cwe_list = []
for item in data:
    cwe_list.append(item[0])
for i in set_CWE:
    if i not in cwe_list:
        print(i)
#--------------------追加CWE代码--------------------------------------------------------------------------
# # print(len(description))
# # result = [list(item) for item in zip(ID,)]
#
# result = [list(item) for item in zip(severity,description)]
# # shuffle(result)
# train, test = train_test_split(result, test_size=0.1,
#                                                random_state=1773
#                                                )
# train, dev = train_test_split(result, test_size=0.1,
#                                                random_state=1773
#                                                )
# # print(result[0])
# #2018年数据15617，80%训练集，10%验证集，10%测试集
# #12493,1561
# #2002-2017V3和V2共计101753
# # num = len(result)
# # print(num)
#
# with open(r'train.tsv', 'w', newline='') as f:
#     tsv_w = csv.writer(f, delimiter='\t')
#     tsv_w.writerow(['severity','description'])
#     tsv_w.writerows(train)  # 多行写入
# with open(r'dev.tsv', 'w', newline='') as f:
#     tsv_w = csv.writer(f, delimiter='\t')
#     tsv_w.writerow(['severity','description'])
#     tsv_w.writerows(dev)  # 多行写入
# with open(r'test.tsv', 'w', newline='') as f:
#     tsv_w = csv.writer(f, delimiter='\t')
#     tsv_w.writerow(['severity','description'])
#     tsv_w.writerows(test)  # 多行写入
# with open('temp2.csv', 'w', newline='') as csvfile:
#     writer  = csv.writer(csvfile)
#     for row in result:
#         writer.writerow(row)
# print(result[0])
# result = result[:2]
# print(test)
#实际上用的是cvss3的数据
# print(result)

# with open('cvre.csv', 'w', newline='') as csvfile:
#     writer  = csv.writer(csvfile)
#     for row in result:
#         writer.writerow(row)





# train=pd.read_csv('dev_ids.tsv', sep='\t')
# train = csv.reader(train, delimiter="\t")
# result = []
# for row in train:
#     result.append(row)
# print(result)
#
# with tf.gfile.Open(r'test.tsv', "r") as f:
#     reader = csv.reader(f, delimiter="\t")
#     lines = []
#     for line in reader:
#         lines.append(line)
# print(lines[0])
#
# temp1 = lines[1:]
# print(temp1)

# with open(r'file.tsv', 'w', newline='') as f:
#     tsv_w = csv.writer(f, delimiter='\t')
#     tsv_w.writerow(['场景','问题'])
#     tsv_w.writerows(temp1)  # 多行写入

# df_train = pd.read_csv("file.tsv", header =None, sep="\t", encoding = "UTF-8", quotechar='"')
# df_bert_train = pd.DataFrame({'0':df_train[0],
#                   '1':df_train[1].replace(r'\n','',regex=True)})
# df_bert_train.to_csv('file.tsv', sep='\t', index=False, header=False, encoding="UTF-8")
