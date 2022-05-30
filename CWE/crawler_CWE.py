from requests_html import HTMLSession
import pandas as pd
session = HTMLSession()
url = 'https://nvd.nist.gov/vuln/categories'
r = session.get(url)



# print()


# sel = 'body > div.note > div.post > div.article > div.show-content > div > p > a'

# sel = '#__next > div._21bLU4._3kbg6I > div > div._gp-ck > section:nth-child(1) > article > p > a'
def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            # mylink = list(result.absolute_links)[0]
            mylist.append(mytext)
        return mylist
    except:
        return None
sel = '#cweRow-CWE-843'
# sel = '#body-section > div:nth-child(2) > div > div > table > tbody'

results = r.html.find(sel)
# print(results)
# print(results[0].text)
all_str = results[0].text
print(all_str)
first_list = all_str.split('\n')
temp = 0
cwe_list = []
des_list = []
# for i,item in enumerate(first_list):
#     if i==temp:
#         cwe_list.append(item)
#         temp+=3
#     else:
#         des_list.append(item)
#
# des_list2 = []
#
# for i,item in enumerate(des_list):
#     if i%2==0:
#         str = item
#         str+=' '
#     else:
#         str+=item
#         des_list2.append(str)


# print(len(cwe_list))
# print(len(des_list2))
#
# print(cwe_list)
# print(des_list2)
# results = []
# for i,j in zip(cwe_list,des_list2):
#     results.append((i,j))

# print(results[0])

# str = results[0].text
# test_list = str.split('\n')
# print(test_list)
# print(get_text_link_from_sel(sel))
# print(results[0].text)
# df = pd.DataFrame(results)
# df.columns = ['cwe','description']
# df.to_csv('cwe_nvd.csv', encoding='gbk', index=False)
# print(results[0].text)
