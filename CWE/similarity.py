# #
# import xlsxwriter
#
# pathTxt = 'new.txt'
# temp = xlsxwriter.Workbook(r'total.xlsx')
# file = open(pathTxt, 'r', encoding='utf-8')
# sheet = temp.add_worksheet('sheet2')
# #
# j = 0
# x = 0
# for item in file.readlines():
#     list = item.split(',')
#     sheet.write_string(j,0,list[0])
#     for i in range(1,5):
#         sheet.write_number(j,i,int(list[i]))
#     j = j+1
#
# temp.close()
# file.close()
# # todo 添加sheet
# # sheet = temp.add_worksheet('sheet1')
# # sheet.write_number(0,1,100)
#
# # temp.save()
#
# # temp.close()
# # dict = {'as':'3'}
# # print(dict.has_key('as'))
# # if 'as'in dict:
#     # print(1)

# !/usr/bin/env python
# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


from sklearn import preprocessing

import numpy as np
# 读取原始数据
X = []
#City里边有四种Label的数据
f = open('City.txt',encoding="utf-8")
for v in f:
    X.append([float(v.split(',')[1]), float(v.split(',')[2]),float(v.split(',')[3]),float(v.split(',')[4])])
# 转化为numpy array
#     X.append([float(v.split()[0]),float(v.split()[1])])
X = np.array(X)

min_max_scaler = preprocessing.MinMaxScaler()

X_minMax = min_max_scaler.fit_transform(X)
# print(X_minMax)

# 类簇的数量
n_clusters = 3
# 开始调用函数聚类

#归一化之后
cls = KMeans(n_clusters=3,max_iter=300000).fit(X_minMax)

#没有归一化
cls2 = KMeans(n_clusters=3,max_iter=300000).fit(X)
# 输出X中每项所属分类的一个列表
print(cls.labels_)
print(cls2.labels_)
# 画图
markers = ['>', 'o', '+','x','d']
#
for i in range(n_clusters):
    members = cls.labels_ == i  # members是布尔数组
    # array([False, False, False, False, False, False, False, False, False,
    #    False, False, False, False, False, False, False, False, False,
    #    False, False,  True, False, False, False, False, False, False,
    #    False,  True,  True,  True,  True, False, False,  True,  True,
    #     True, False,  True, False,  True,  True,  True,  True,  True,
    #     True, False, False, False, False,  True,  True,  True, False,
    #    False, False, False,  True,  True,  True,  True,  True,  True,
    #    ...])
    plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i], c='b', alpha=0.5)  # 画与menbers数组中匹配的点

# plt.title('China')
# plt.show()
# print(X)