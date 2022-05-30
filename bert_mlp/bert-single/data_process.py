'''
处理所有的bert_single文件，生成三个文件，分别是train, dev和test.tsv，每一个文件的组成格式是id sentence target aspect label
'''

first_name_all = ['loc1','loc2']
second_name_all = ['general','price','safety','transit']
# first_name_all = ['loc1']
# second_name_all = ['general']
import csv
with open('train.tsv','w',newline='') as f2:
    tsv_writer = csv.writer(f2, delimiter='\t')
    for first_name in first_name_all:
        for second_name in second_name_all:
            path = first_name+'_'
            path+=second_name
            path+='/train.tsv'
            with open(path,'r') as f:
                for line in f.readlines():
                    line = line.strip().split('\t')
                    # print(line)
                    #['99', 'theres a great shop in location - 1 tesco , believe it or not', 'None']
                    id = line[0]
                    sentence = line[1]
                    label = line[2]
                    # reform sentence
                    sentence = sentence.split(' - ')
                    # print(sentence)
                    temp_sentence = ''
                    for i in sentence:
                        temp_sentence+=i
                    # print(temp_sentence)
                    if first_name== 'loc1':
                        target = 'location1'
                    else:
                        target = 'location2'
                    aspect = second_name
                    tsv_writer.writerow([id,temp_sentence,target,aspect,label])


