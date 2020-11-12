import requests
from pyquery import PyQuery as pq
from lxml import etree

# 模拟登录GitHub 并爬取fellowing的最近动态

class Login(object):
	def __init__(self):
		self.headers = {
			'Host': 'github.com',
			'Origin': 'https://github.com',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
		}
		self.login_url = 'https://github.com/login'
		self.post_url = 'https://github.com/session'
		self.logined_url = 'https://github.com/settings/profile'
		self.session = requests.Session()	# 维持一个会话处理cookies

		self.response = self.session.get(self.login_url, headers=self.headers, allow_redirects=False)
		self.selector = etree.HTML(self.response.text)

	def token(self):
		token = self.selector.xpath('//input[@name="authenticity_token"]/@value')[0]
		return token

	def timestamp(self):
		timestamp = self.selector.xpath('//input[@name="timestamp"]/@value')[0]
		return timestamp

	def timestamp_secret(self):
		timestamp_secret = self.selector.xpath('//input[@name="timestamp_secret"]')[0]
		return timestamp_secret

	def login(self,email, password):
		post_data = {
			'commit': 'Sign in',
			'authenticity_token': self.token(),
			'login': email,
			'password': password,
			'webauthn-support': 'supported',
			'webauthn-iuvpaa-support': 'unsupported',
			'timestamp': self.timestamp(),
			'timestamp_secret': self.timestamp_secret()
		}

		response = self.session.post(self.post_url, data=post_data, headers=self.headers)
		if response.status_code == 200:
			self.dynamics(response.text)
		response = self.session.get(self.logined_url, headers=self.headers)
		if response.status_code == 200:
			self.profile(response.text)

	def dynamics(self, html):
		print(html)
		selector = etree.HTML(html)
		dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
		for item in dynamics:
			dynamics = ' '.join(itme.xpath('.//div[@class="title"]//text()')).strip()

	def profile(self, html):
		selector = etree.HTML(html)
		name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
		email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
		print(name, email)

if __name__=="__main__":
	login = Login()
	login.login(email='2287860193@qq.com', password='5277gang.')