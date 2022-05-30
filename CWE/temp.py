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
import json
import xlrd
import xlsxwriter
'''
对于NVD数据集的分析，2021年漏洞库
'''
#表示次数



low = 0
medium = 0
high = 0
critical = 0

xl = xlrd.open_workbook(r'CWE2.xlsx')
table = xl.sheets()[0]


pathTxt = 'new3.txt'

file = open(pathTxt, 'a', encoding='utf-8')
# todo 添加sheet
# sheet = temp.add_worksheet('sheet1')

list = []
for i in range(0,91):

    data = table.cell(0,i).value
    ID = data
    with open('nvdcve-1.1-2018.json', encoding='utf-8') as f:
        line = json.load(f)
        # d = json.loads(line)
        # name = d['CVE_data_type']
        # print(name)
        # print(type(line['CVE_Items']))
        mylist = line['CVE_Items']#列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；
        # print(len(mylist))

        for item in mylist:
            # pass
            first =item
        # print(first)
            cve = first['cve']
            cwe = cve['problemtype']
            problemtype_data = cwe['problemtype_data']
            description = problemtype_data[0]
            description = description['description']
            if description == []:
                continue
            cweID = problemtype_data[0]['description'][0]['value']
            if cweID == ID:
                impact = first['impact']
                if 'baseMetricV3' in impact:
                    V3 = impact['baseMetricV3']['cvssV3']
                    baseSeverity = V3['baseSeverity']
                    if baseSeverity == 'LOW':
                        low +=1
                    elif baseSeverity == 'MEDIUM':
                        medium +=1
                    elif baseSeverity == 'HIGH':
                        high += 1
                    elif baseSeverity == 'CRITICAL':
                        critical +=1
                    else:
                        pass
        f.close()

    # with open('nvdcve-1.1-2018.json', encoding='utf-8') as f:
    #     line = json.load(f)
    #     # d = json.loads(line)
    #     # name = d['CVE_data_type']
    #     # print(name)
    #     # print(type(line['CVE_Items']))
    #     mylist = line['CVE_Items']  # 列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；
    #     # print(len(mylist))
    #
    #     for item in mylist:
    #         # pass
    #         first = item
    #         # print(first)
    #         cve = first['cve']
    #         cwe = cve['problemtype']
    #         problemtype_data = cwe['problemtype_data']
    #         description = problemtype_data[0]
    #         description = description['description']
    #         if description == []:
    #             continue
    #         cweID = problemtype_data[0]['description'][0]['value']
    #         if cweID == ID:
    #             impact = first['impact']
    #             if 'baseMetricV3' in impact:
    #                 V3 = impact['baseMetricV3']['cvssV3']
    #                 baseSeverity = V3['baseSeverity']
    #                 if baseSeverity == 'LOW':
    #                     low += 1
    #                 elif baseSeverity == 'MEDIUM':
    #                     medium += 1
    #                 elif baseSeverity == 'HIGH':
    #                     high += 1
    #                 elif baseSeverity == 'CRITICAL':
    #                     critical += 1
    #                 else:
    #                     pass
    #     f.close()
    #
    #
    # with open('nvdcve-1.1-2019.json', encoding='utf-8') as f:
    #     line = json.load(f)
    #     # d = json.loads(line)
    #     # name = d['CVE_data_type']
    #     # print(name)
    #     # print(type(line['CVE_Items']))
    #     mylist = line['CVE_Items']  # 列表的每一项是一个CVE条目,而每一个单独的CVE条目又是一个词典；
    #     # print(len(mylist))
    #
    #     for item in mylist:
    #         # pass
    #         first = item
    #         # print(first)
    #         cve = first['cve']
    #         cwe = cve['problemtype']
    #         problemtype_data = cwe['problemtype_data']
    #         description = problemtype_data[0]
    #         description = description['description']
    #         if description == []:
    #             continue
    #         cweID = problemtype_data[0]['description'][0]['value']
    #         if cweID == ID:
    #             impact = first['impact']
    #             if 'baseMetricV3' in impact:
    #
    #                 V3 = impact['baseMetricV3']['cvssV3']
    #                 baseSeverity = V3['baseSeverity']
    #                 if baseSeverity == 'LOW':
    #                     low += 1
    #                 elif baseSeverity == 'MEDIUM':
    #                     medium += 1
    #                 elif baseSeverity == 'HIGH':
    #                     high += 1
    #                 elif baseSeverity == 'CRITICAL':
    #                     critical += 1
    #                 else:
    #                     pass
    #     f.close()
    file.write(ID)
    file.write(',')
    file.write(str(low))
    file.write(',')
    file.write(str(medium))
    file.write(',')
    file.write(str(high))
    file.write(',')
    file.write(str(critical))
    file.write('\n')
    low = 0
    medium = 0
    high = 0
    critical = 0
    # sheet.write_string(i, 0, ID)
    # sheet.write_number
    # sheet.write_string(i, 1, low)
    # sheet.write_string(i, 2, medium)
    # sheet.write_string(i, 3, high)
    # sheet.write_string(i, 4, critical)
    # list.append(low)
    # list.append(medium)
    # list.append(high)
    # list.append(critical)
# xl.close()
# temp.close()
file.close()
# print(list)

