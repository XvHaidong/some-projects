from requests_html import HTMLSession
import pandas as pd
from lxml import etree
session = HTMLSession()
url = 'https://www.jianshu.com/p/85f4624485b9'
r = session.get(url)


sel = 'body > div.note > div.post > div.article > div.show-content > div > p:nth-child(4) > a'

sel = 'body > div.note > div.post > div.article > div.show-content > div > p > a'

sel = '#__next > div._21bLU4._3kbg6I > div > div._gp-ck > section:nth-child(1) > article > p > a'
def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext, mylink))
        return mylist
    except:
        return None
results = r.html.find(sel)

tree = etree.HTML(url)
print(tree)
for link in tree.xpath("//@href"):
    print('*****************************',link)
# print(get_text_link_from_sel(sel))
# print(results[0].text)
# df = pd.DataFrame(get_text_link_from_sel(sel))
# df.columns = ['text','link']
# df.to_csv('output.csv', encoding='gbk', index=False)
# print(results[0].text)
