from selenium import webdriver
from selenium.webdriver import ActionChains
import time

'''
Selenium是一个自动化测试工具
	1. 可以驱动浏览器执行特定的动作，如下拉、点击、填充表单、模拟点击等
	2. 可以获取浏览器当前呈现的源代码，做到可见即可爬
	3. 支持多种类浏览器，使用get()方法访问页面
	4. 查找节点
		（1）单个节点:find_element_by_id()、find_element_by_name()、find_element_by_xpath()
			find_element_by_link_text()、find_element_by_partial_link_text()、find_element_by_tag_name()
			find_element_by_class_name()、find_element_by_css_selector()
			通用函数：find_element(by, value)

		（2）多个节点(如导航栏)
			find_elements_by_id()、find_elements_by_name()、find_elements_by_xpath()
			find_elements_by_link_text()、find_elements_by_partial_link_text()
			find_elements_by_tag_name()、find_elements_by_class_name()、find_elements_by_css_selector()
			通用函数：find_elements(by, value)

	5.节点交互
	 输入文字：send_keys()、清空文字：clear()、 点击： click()

	6.动作链（用于鼠标拖拽，键盘按键等没有特定执行对象的操作）
	7.执行JavaScript:使用execute_script模拟下拉进度条
	8.获取节点信息
	9. 切换Frame(相当于页面的子页面)
	10. 延时等待（确保节点完全加载）
	11. 前进和后退
	12. Cookies: 对cookies进行添加获取和删除
	13.选项卡管理：可对选项卡进行操作
	14.异常处理
'''
browser = webdriver.Chrome()			
'''
# 从淘宝网获取节点
# browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

# 获取单个节点 搜索框  返回单个WebElement类型
input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first, input_second, input_third)

# 获取多个节点 左侧导航条所有条目	返回列表，每个元素都是WebElement类型
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)

# 通过上面获取的搜索框进行搜索
input_first.send_keys('小米')
time.sleep(1)
input_first.clear()
input_first.send_keys('华为')

button = browser.find_element_by_class_name('btn-search')	# 获取搜索按钮
button.click()
browser.close()



# 动作链（用于鼠标拖拽，键盘按键等没有特定执行对象的操作）
# 执行一个拖拽实例
browser = webdriver.Chrome() 
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()




# 执行JavaScript:使用execute_script模拟下拉进度条
# 下拉知乎进度条并 弹出窗口
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')




"""
获取节点信息:
 通过page_source可以获取到网页源代码，接着便可以使用pyquery等解析库来提取信息了。但是selenium也提供了相关的提取信息的方式
（1）获取属性  get_attribute
（2）获取文本值 get_text或text()
（3）获取id、位置、标签名和大小  id location tag_name
"""
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo.get_attribute('class'))
'''

'''
切换Frame(相当于页面的子页面)
	switch_to.frame()方法来进行切换
'''




'''
延时等待（确保节点完全加载）
（1）隐式等待：在指定时间内进行等待
（2）显式等待：设置最长等待时间  常用
'''


'''
前进和后退
 back() 后退
 forward()  后退
'''



'''
Cookies: 对cookies进行添加获取和删除
'''


'''
选项卡管理：可对选项卡进行操作
'''



'''
异常处理
'''
