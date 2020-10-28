# 使用函数返回字典

def build_preson(frist_name,last_name):
	person = {'first' : frist_name, 'last' : last_name}
	return person
muscian = build_preson('quangang','sun')
print(muscian['first'].title())




# 在函数中修改列表

def project_transfer(not_completed,completed):

	while not_completed:
		current_pro = not_completed.pop()
		print(f"Printing project: {current_pro}")
		completed.append(current_pro)

def show_projuct_transfer(completed):

	print("\n The following models have been printed:")
	for pro in completed:
		print(pro)

not_completed = ['java_web', 'javastript', 'json', 'python']
completed = []

not_completed_copy = not_completed[:]

project_transfer(not_completed_copy,completed)
show_projuct_transfer(completed)





# 传递任意数量的形参：1.形参声明形式为 “*name” 表示元组  2.形参声明形式为 “**name” 表示字典
# 导入模块： import file_name 
# 导入模块中的特定函数： from file_name import function_0, function_1
# 导入模块中的全部函数： from file_name import *
# 给函数起别名： from file_name inport function_0 ad fun
