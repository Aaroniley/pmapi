from requests_html import HTMLSession
session = HTMLSession()
url = 'https://oversea.cnki.net/kdoc/download.aspx?filename=DhjdFt2dFZTS4dkSmZEbuZXeDhHZtVHeBtWdChDbol2NsNUYwQDbS1UYMhFaUd2YwhTcWdVcvZFaRV3RyN3LOdUTndXToFFT5pmcBdEUhxGNq5Wd0BDVJB1cOpmQkZEezFjSTJjavE2Yz4ENPdWd0ElZnlHc2kjU&tablename=CMFD201901&dflag=downpage&cflag=pdf&uid=WEEvREcwSlJHSldSdmVqM1BLUWdMWjJpb0lGOExKTm5CalMvZmNUTG9rOD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&t=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjI5MjU4IiwidGltZXN0YW1wIjoxNjAxMzcwNTIxLCJub25jZSI6IlVPNHc1MEp5QkIifQ.zoytREUuxkBOHQKTNQBP0TAp3xc6ySBwA46gy7PfK3c&lang=en'

r = session.get(url)
table = r.html.find('table')
print(len(table))
result_list = table[0].find('tr > td>a')
url = []
for result in result_list:
    url.append(result.attrs['href']+'\n')
print(url)
with open('urls.txt', 'w') as f:
    f.writelines(url)
# import requests
# url = 'https://oversea.cnki.net/kdoc/download.aspx?filename=DhjdFt2dFZTS4dkSmZEbuZXeDhHZtVHeBtWdChDbol2NsNUYwQDbS1UYMhFaUd2YwhTcWdVcvZFaRV3RyN3LOdUTndXToFFT5pmcBdEUhxGNq5Wd0BDVJB1cOpmQkZEezFjSTJjavE2Yz4ENPdWd0ElZnlHc2kjU&tablename=CMFD201901&dflag=downpage&cflag=pdf&uid=WEEvREcwSlJHSldSdmVqM1BLUWdMWjJpb0lGOExKTm5CalMvZmNUTG9rOD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&t=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBpZCI6IjI5MjU4IiwidGltZXN0YW1wIjoxNjAxMzcwNTIxLCJub25jZSI6IlVPNHc1MEp5QkIifQ.zoytREUuxkBOHQKTNQBP0TAp3xc6ySBwA46gy7PfK3c&lang=en'
# # url = 'http://t.dianping.com/deal/22752400'
# header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#           'Accept-Encoding': 'gzip, deflate',
#           'Accept-Language': 'zh-CN,zh;q=0.9',
#           'Cache-Control': 'max-age=0',
#           'Connection': 'keep-alive',
#           'Cookie': 'Ecp_ClientId=1200929153302203864; Ecp_session=1; cnkiUserKey=958039ad-a253-da18-2c97-6d742000020b; UM_distinctid=174d8d1937b30a-0b9fe0511f459-7e647b65-1fa400-174d8d1937cd9c; ASPSESSIONIDQCRQASTD=AGFNDHBBFCDNPAFLIDLBCOJO; eng_k55_id=123106; CNZZDATA1279278444=1494805179-1601365218-https%253A%252F%252Fwww.cnki.net%252F%7C1601365218; ASP.NET_SessionId=mc3ougnd1kz53sympdkeq0gc; CurrSortField=Publication+Date%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); CurrSortFieldType=desc; _pk_ses=*',
#           'Host': 't.dianping.com',
#           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
#           }
# a = requests.get(url, headers=header)
# print(a.text)
