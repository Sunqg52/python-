from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo

from config import *

# 爬取淘宝商品页

# 无界面模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)


# browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30)
client = pymongo.MongoClient(MONGO_URL)		# 创建链接
db = client[MONGO_DB]	# 创建集合

def index_page(page):
	"""
	抓取索引页
	:para page:页码
	"""
	print(f"正在获取第{page}页\n")
	try:
		url = 'https://re.taobao.com/search_ou?keyword=' + quote(KEYWORD)
		browser.get(url)
		# 判断页码是否大于1 如果是执行跳转  如果不是等待加载
		if page > 1:
			input = wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '#Jumper')))
			submit = wait.until(
				EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_waterfallPagination .pageConfirm')))
			input.clear()
			input.send_keys(page)
			submit.click()
		wait.until(
			EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_waterfallPagination .page-cur'),
				str(page)))
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_waterfallWrapper .item')))
		get_products()
	except TimeoutException:
		index_page(page)

def get_products():
	"""
	提取商品数据
	"""
	print('正在提取...\n')
	html = browser.page_source		# 获取页面的源代码
	doc = pq(html)
	items = doc('#J_waterfallWrapper .item').items()
	for item in items:
		product = {
			'image':item.find('.imgLink img').attr('src'),		# 通过url提取图片
			'price':item.find('.price').text(),
			'title':item.find('.title').text(),
			'shop':item.find('.shopName .shopNick').text(),
			'info':item.find('.moreInfo ul').text()
		}
		print(product)
		save_to_mongo(product)

def save_to_mongo(result):
	"""
	保存至MongoDB
	：param result:结果
	"""
	print('正在存储...\n')
	try:
		if db[MONGO_COLLECTION].insert(result):
			print('存储到MongoDB成功')
	except Exception:
		print('存储到MongoDBs失败')

def main():
	"""
	遍历每一页
	"""
	for i in range(1, MAX_PAGE+1):
		index_page(i)

	browser.close()

if __name__ == '__main__':
	main()