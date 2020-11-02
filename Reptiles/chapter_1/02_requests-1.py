import requests
import re

"""
# r = requests.get('http://www.baidu.com/')
# r = requests.post('http://www.baidu.com/post')
# r = requests.put('http://www.baidu.com/put')
# r = requests.delete('http://www.baidu.com/delete')
# r = requests.head('http://www.baidu.com/get')
# r = requests.options('http://www.baidu.com/get')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
"""

"""
# 构建一个简单的GET请求
import requests

r = requests.get('http://httpbin.org/get')
print(r.text)
"""


# 利用params参数进行构造
data = {
	'name': 'germey',
	'age': 22
}

r = requests.get("http://httpbin.org/get", params=data)		# 此时返回的时json格式的字符串

# 利用headers参数添加浏览器标识
headers = {
	'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101Firefox/4.0.1'
}

r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?qusetion_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(r.text)


'''
r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
	f.write(r.content)
'''

#利用file参数来添加文件
files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)