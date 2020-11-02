from requests.exceptions import RequestException
import requests
import json


def get_one_page(url):
	try:
		headers = {
			'User-Agent': 'Mozilla/5.0 (macintosh; Intel Mac OS X 10_13_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
		}
		response = requests.get(url,headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def write_to_file(content):
	with open("result2.txt", 'a', encoding = 'utf-8') as f:
		print(type(json.dumps(content)))
		f.write(json.dumps(content,ensure_ascii=False) + '\n')


url = 'http://maoyan.com/board/4'
html = get_one_page(url)
results = write_to_file(html)
print(results)

