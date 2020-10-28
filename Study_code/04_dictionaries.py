# 字典：用于存储相关联的信息 类似于键值对数组

alien_0 = {'color' : 'green', 'point' : 5}
print(alien_0['color'])
print(alien_0['point'])

# 添加键值对
alien_0['x_position'] = 5
alien_0['y_position'] = 15
print(alien_0)


# 创建空字典，逐个添加键值对
alien_0 = {}
alien_0['color'] = 'green'
alien_0['point'] = 15
print(f"原字典：{alien_0}")

# 修改键值对
alien_0['color'] = 'red'
print(f"修改后：{alien_0}")

# 删除键值对
del alien_0['color']
print(f"删除后：{alien_0}")

# 获取值
point = alien_0['point']
print(point)

# 使用get()函数来为字典设置默认值
color = alien_0.get('color','No color value assigned')
print(color)


# 例子
sunqg = {'name' : 'sunquangang', 'age' : 21, 'city' : 'chengde'}
print(sunqg)

# 遍历字典
for key, value in sunqg.items():
	print(f"key: {key}\tvalue: {value}")

# 遍历字典中的所有键 同理values()遍历字典中所有的值
for key in sunqg.keys():
	print(key)

# 按顺序遍历字典中的键  将sorted()函数替换为set()可去除所有的重复项
for key in sorted(sunqg.keys()):
	print(key)



# 在列表中存储字典
aliens = []		# 创建一个用于存储外星人的空列表

for aliens_number in range(30):		# 创建30个绿色的外星人
		new_alien = {'color' : 'green', 'point' : 5, 'speed' : 'slow'}
		aliens.append(new_alien)


for alien in aliens[:3]:		# 修改前三个外星人
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['point'] = 10

for alien in aliens[:5]:
	print(alien)

print("...")



# 在字典中存储列表：一个键需要多个值
student_age = [3,4,5,6,7]
student = {'age' : student_age}
print(student_age)


# 在字典中存储字典：信息关联
user = {						#将用户名与用户信息关联
	'sunqg' : {
		'name' : "sunquangang",
		'age' : 21,
	},
	'sunqw' : {
		'name' : 'sunquanwei',
		'age' : 11,
	},
}

for user, user_info in user.items():
	print(f"用户名：{user}\t信息：{user_info}")
