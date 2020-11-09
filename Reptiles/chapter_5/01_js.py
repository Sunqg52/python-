from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

# 动态渲染页面的爬取



'''
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriber.Sarari()
'''

browser = webdriver.Chrome()	# 初始化： 声明浏览器对象

try:
	browser.get('https://www.baidu.com')	# 访问页面

	input = browser.find_element_by_id('kw')	#查找节点
	input.send_keys('python')
	input.send_keys(Keys.ENTER)

	wait = WebDriverWait(browser, 10)
	wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

	print(browser.current_url)
	print(browser.get_cookies())
	print(browser.page_source)		# 输出源码
finally:
	browser.close()
