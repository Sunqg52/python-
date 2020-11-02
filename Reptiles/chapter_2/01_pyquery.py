from pyquery import PyQuery as pq
from requests.exceptions import RequestException
import requests
import json

"""
解析库：pyquery

准备工作,安装pyquery:
	使用python3+pip安装，没有安装pip的需要自行安装
	python3 -m pip install --user pyquery

开始操作：
	1. 传入一个HTML文件来初始化一个PyQuery对象
	（1）字符串初始化 最常用的方法
	（2）URL初始化
	（3）文件初始化

	2. 基本的css选择器： doc('id class 标签名')  返回一个选择器对象

	3. 查找节点：与jQuery中的函数用法完全相同（基于选择器对象进行调用）
	（1）子节点：find()
	（2）父节点：parent()		返回单个父节点
				   parents()	返回所有祖先节点
	（3）兄弟节点：siblings()	默认返回所有兄弟节点，可传参选择特定的节点

	4. 在进行节点选择时可能返回多个节点，我们可以使用items()方法进行遍历

	5. 获取信息（基于选择器对象进行调用）
	（1）获取属性：attr() 只返回一个值，需要进行遍历才能显示出所有值
	（2）获取文本：html() 获取HTML文本（源代码） 只获取一个 需要遍历
                    text()  获取节点内部的纯文本内容，可以获取多个， 将所有内容拼成一个字符串 由空格分离

    7. 节点操作（基于选择器对象进行调用）
    （1）addClass()、removeClass()：class的添加和移除
    （2）attr('name', 'value'): 操作节点的属性
    	html(): 改变节点内容
    	text(): 改变节点内部内容
    （3）remove(): 移除不必要节点



"""
def get_one_page(url):
	try:
		headers = {
			'User-Agent': 'Mozilla/5.0 (macintosh; Intel Mac OS X 10_13_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
		}

		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None


url = 'https://maoyan.com/board/4'
#url = 'https://blog.csdn.net/xsj_blog/article/details/51837570'
html = get_one_page(url)			# 获取网页
doc = pq(html)						# 构建css选择器
# print(doc)						# 获取网页源码	

items = doc('div')				# 获取网页中的ul所有节点

# 获取子节点
lis_a = items.find('a')
lis_a.addClass('sunqg')
lis_a.removeClass('sunqg')
lis2_a = items.children()				# 可加参数

# 获取父节点
# container = lis_a.parent()
# container2 = lis_a.parents()


# # 获取兄弟节点
# bother = items.siblings()

# # 获取信息
# a_href = lis_a.attr('href')

# 输出文本
print(items)

# 遍历
# for a in lis_a:
# 	print(a.attr('href'))