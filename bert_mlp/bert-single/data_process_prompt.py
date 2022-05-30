'''
处理所有的bert_single文件，生成三个文件，分别是train, dev和test.tsv，每一个文件的组成格式是sentence,label;  其中sentence是content+aspect+label
'''

first_name_all = ['loc1','loc2']
second_name_all = ['general','price','safety','transit']
# first_name_all = ['loc1']
# second_name_all = ['general']
import csv
with open('test_prompt.tsv','w',newline='') as f2:
    tsv_writer = csv.writer(f2, delimiter='\t')
    for first_name in first_name_all:
        for second_name in second_name_all:
            path = first_name+'_'
            path+=second_name
            path+='/test.tsv'
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
                    temp_sentence = temp_sentence+' '+target+' is about '+aspect+ ' '+'.'+' '+ target
                    if label=='Positive':
                        label=1
                    elif label=='None':
                        label=0
                    else:
                        label=-1
                    tsv_writer.writerow([temp_sentence,label])


