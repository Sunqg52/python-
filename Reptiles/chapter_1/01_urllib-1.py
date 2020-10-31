from urllib import request, parse, error
import socket

#使用urllib进行简单的爬取
"""
urllib主要包含四个模块：
	request: 模拟发送请求
	error: 处理异常
	parse: 提供了URL的处理方法
	robotparser: 用于识别网站的robot.txt文件

urlopen() 方法：
	class urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, 
		capath=Node, cadefault=False, context=None, 
		)     默认使用GET方式请求

Request方法：
	class urllib.request.Request(url, data=None, headers={}, 
		origin_req_host=None, unverifiable=False, method=None
		)


参数含义：
	url:请求信息  必选参数
	data: 附加数据 可选参数
	headers: 请求头（能通过修改User-Agent让我们伪装成浏览器）
	origin_req_host：请求方的host名称或IP地址
	unverifiable: 权限验证
	method: 用于指示请求的方式(GET/POST)
"""
"""
#添加data参数，添加后请求方式转为POST,若是自己留编码格式的内容，即bytes类型，则需要通过bytes()方法转化
#添加timeout参数。timeout参数用于设置超时时间，即超过这个时间还没响应的话就报错。若不指定则使用全局默认时间。单位为秒
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
try:
	response = urllib.request.urlopen('https://httpbin.org/post', data=data, timeout=5)
except urllib.error.URLError as e:
	if isinstance(e.reason, socket.timeout):
		print("响应超时！")
else:
	print(response.read())
"""
"""
response = urllib.request.urlopen('https://www.csdn.net/?spm=1011.2124.3001.4476')
print(response.read().decode('utf-8'))   # 返回的是一个网页
print(type(response))


返回的是一个 HTTPResponse 对象
这个对象包含：
	read() readinto() getheader(name) getheaders() fileno() 等方法
	以及msg verson status reason debuglevel closed等属性
通过这些方法和属性我们可以对HTML对象进行操作

print(response.status)					# 响应的状态码
print(response.getheaders())			# 响应的头信息
print(response.getheader('Server'))		# 获取服务器名称
"""



"""
# 使用Request方法
url = 'https://httpbin.org/post'
headers = {
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
dict = {
	'name': 'sunqg'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)

print(response.read().decode('utf8'))
"""