import requests
from pyquery import PyQuery as pq
from lxml import etree


headers = {
	'Host': 'https://github.com',
	'Origin': 'https://github.com',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}
login_url = 'https://github.com/login'
