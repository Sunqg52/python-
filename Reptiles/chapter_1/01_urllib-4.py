import http.cookiejar, urllib.request

filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)			# 储存为LWP格式
handler = urllib.request.HTTPCookieProcessor(cookie)	# 构建handler
opener = urllib.request.build_opener(handler)			# 构建一个opener
response = opener.open('http://www.baidu.com')			# 使用open打开
cookie.save(ignore_discard=True, ignore_expires=True)

# 使用已保存的cookie进行访问
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
