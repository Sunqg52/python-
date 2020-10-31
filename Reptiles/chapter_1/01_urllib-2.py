from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

"""
使用强大的handler来处理问题
常用的headler类：
	HTTPDefaultErrorHandler: 用于处理HTTP响应错误，错误会抛出HTTPError的异常
	HTTPRedirctHandler: 用于处理重定向
	HTTPCookieProcessor: 用于处理cookies
	ProxyHandler: 用于设置代理，默认代理为空
	HTTPPasswordMgr: 用于管理密码， 他维护了用户名和密码的表
	HTTPBasicAuthHandler: 用于管理认证，如果一个链接打开时需要认证，可以用它来解决认证问题

还有一个重要的类就是OpenerDirector.....这个类时什么意思，，很抽象，，，表达不出来。。。。
"""

username = "用户名/邮箱"
password = "密码"
# 登录页面的url 本程序运行完成后 刷新即可登入
url = "https://github.com/login?return_to=%2Fjoin%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home"

p = HTTPPasswordMgrWithDefaultRealm()			# 实例化对象
p.add_password(None, url, username, password)	# 添加用户名密码
auth_handler = HTTPBasicAuthHandler(p)			# 构建处理验证的handler
opener = build_opener(auth_handler)				# 构建一个opener

try:
	result = opener.open(url)					# 利用opener打开链接
	html = result.read().decode('utf8')
	print(html)									#获取到了验证后页面的内容
except URLError as e:
	print(e.reason)