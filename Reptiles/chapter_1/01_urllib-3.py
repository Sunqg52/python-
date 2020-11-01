from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


# 搭建了一个代理运行在9743端口上
procxy_handler = ProxyHandler({
	'http': 'http://127.0.0.1:9743',
	'https': 'http://127.0.0.1:9743'
	})

opener = build_opener(procxy_handler)

try:
	response = opener.open('https://www.baidu.com')
	print(response.read().decode('utf-8'))
except URLError as e:
	print(e.reason)