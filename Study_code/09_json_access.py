import json
# 在加载空的json文件时会出现错误

# 使用json存取数据，需要先import json.  存储：json.dump()    加载：json.load()

#存取用户名字
file_path = '/home/sunqg/user.json'
'''
usernames = ["sunqg", "sunqw"]
with open(file_path,'w') as f:
	json.dump(usernames,f)
'''
def get_username():
	"""如果存储了用户名字就获取"""
	try:
		with open(file_path) as f:
			username = json.load(f)
	except FileNotFoundError:
		#return None
		print("文件未找到，打开失败！")
	else:
		return username


def get_new_name():
	"""提示用户输入用户名"""
	getname = input("what's you name: ")
	with open(file_path, 'a') as f:
		json.dump(user,f)
	return getname

def greet_user():
	"""问候用户并指出名字"""
	username = get_username()
	if username:
		print(f"Welcome back! {username}")
	else:
		username = get_new_name()
		print(f"We will remeber your name when you come back, {username}")

greet_user()

