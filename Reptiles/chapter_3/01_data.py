import requests
from pyquery import PyQuery as pq 

url = 'https://diwx821nvp.feishu.cn/docs/doccnkhLJnc9Bvpb0es70IJafUc'
headers = {
	'User-Agent': 'Mozilla/5.0 (macintosh; Intel Mac OS X 10_13_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
} 

html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('span')
print(items)
# for item in items:
# 	series_name = item.find('span .op-symbol').text()
# 	link = item.find('a').text()
	# print(f"{series_name}")
	# file = open('explore.txt', 'a', encoding='utf-8')
	# file.write('\n'.join([question, author, answer]))
	# file.write('\n' + '=' * 50 + '\n')
	# print(f"{question} \n {author} \n {answer}")
	# file.close()

