from urllib.parse import urlparse, urlunparse, urlsplit, urlsplit
from urllib.parse import urljoin, urlencode, parse_qs, parse_qsl
from urllib.parse import quote, unquote




"""
# 解析链接
API: urllib.parse.urlparse(urlstring, scheme='', allow_fragments=Ture)
	urlstring: 必填项。 scheme: 默认协议。
	allow_fragments: 选择是否忽略。如果它被设置为False， fragment部分就会就会被忽略
"""
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)

"""
ParseResult(
scheme='http', netloc='www.baidu.com',path='/index.html', 
params='user', query='id=5', fragment='comment')  元组

可以看出urlparse方法将链接拆分成了6个部分：
	scheme：协议， netloc：域名， path：访问路径， 
	params：参数， query： 查询条件， fragment：锚点 

"""


"""
构造链接
urllib.parse.urlunparse()
此函数接受一个可迭代对象，必须传递6个参数！
"""
# data=['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))

"""
urlsplit()
不会单独解析param,将其与path合并
解析链接，但只返回5个结果
"""
"""
urlunsplit()
构造链接，参数长度必须为5
"""

"""
urljoin
提供一个基础链接(base_url)作为第一个参数,将新链接作为第二个参数。
该方法会分析base_url的schme, netloc, path这三个内容对新链接缺失的部分进行补充，返回最后的结果
"""
#print(urljoin('http://www.baidu.com', 'FAQ.html'))
#print(urljoin('http://www.baidu.com', 'https://sunqg.com/FAQ.html'))
#print(urljoin('http://www.baidu.com/about.html', 'https://sunqg.FAQ.html'))


"""
urlcode
常用于构造GET方法，传入一个字典
params = {
	'name': 'germey',
	'age': 22
}
base_url = 'http://www.baidu.com'
url = base_uel+urlencode(params)
print(url)
"""

"""
pares_qs()
将GET参数转化为字典

pares_qsl()
将GET参数转化为元组组成的列表
"""

"""
quote()
将内容转化为URL编码格式

unquote()
将内容进行解码
"""
# keyword = '孙全刚'
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)
# 输出：https://www.baidu.com/s?wd=%E5%AD%99%E5%85%A8%E5%88%9A

# url = 'https://www.baidu.com/s?wd=%E5%AD%99%E5%85%A8%E5%88%9A'
# print(unquote(url))
# 输出：https://www.baidu.com/s?wd=孙全刚





