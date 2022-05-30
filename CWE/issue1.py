import pandas as pd
df_train = pd.read_csv("train.tsv", header =None, sep="\t", encoding = "UTF-8", quotechar='"')
df_bert_train = pd.DataFrame({'0':df_train[0],'1':df_train[1].replace(r'\n',' ',regex=True)})
df_bert_train.to_csv('train.tsv', sep='\t', index=False, header=False, encoding="UTF-8")


