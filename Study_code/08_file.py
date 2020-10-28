# with(自动关闭)  rstrip():去除多余空白行
# 在open函数中添加参数：r读取文件  w覆盖原有文件，写入新内容 a在原文件内容上添加新内容 r+读写模式
# 异常 try-except-esle
file_path = '/home/sunqg/test.txt'

def read_file(file_path):
	# 读取
	try:
		with open(file_path) as file_info:
			for line in file_info:
				print(line.rstrip())
	except FileNotFoundError:
		print("你要打开的文件不存在")
	else:
		print("已打开")

def write_file(file_path, *contents):
	# 写入
	try:
		with open(file_path, 'w') as file_info:
			for content in contents:
				file_info.write(content)
	except: FileNotFoundError:
		pass #不显示错误

def add_file(file_path, *contents):
	#附加
	with open(file_path, 'a') as file_info:
		for content in contents:
			file_info.write(content)


'''
sent_0 = "I love programming.\n"
sent_1 = "I love python.\n"

add_file(file_path,sent_0,sent_1)
read_file(file_path)
'''