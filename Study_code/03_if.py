# 使用if的但条件判断

car_list = ['audi', 'bwm', 'subaru', 'toyota']
for car_name in car_list:
	if car_name == 'bwm':
		print(car_name.upper())
	else:
		print(car_name.title())


age_list = [value for value in range(20,31)]



# 使用if进行多条件判断
for age in age_list:
	if (age >= 21) and (age <=25):
		print(f"age: {age}")
	else:
		print("不符合规定！")

for age in age_list:
	if (age <= 23) or (age >= 27):
		print(f"age: {age}")
	else:
		print("不符合规定！")


# 直接使用if进行判断
if '21' in age_list:
	print("true")
else:
	print("false")

if '21' not in age_list:
	print("false")
else:
	print("true")



# 多重判断  此形式为一个整体代码块 一个条件符合后不再执行剩下的判断 若要执行多个代码块可使用2的形式
for age in age_list:
	if (age <= 23):
		print("You admission cost is $2000")
	elif (age > 23) and (age <= 27):
		print("You admission cost is $4000")
	else:
		print("You admission cose is #5000")



# 根据外星人颜色判断玩家得分
alien_color = ['green', 'red', 'yellow']
for death_alien_color in alien_color:
	if death_alien_color == 'green':
		print("get 5 points")
	elif death_alien_color == 'red':
		print("get 10 points")
	elif death_alien_color == 'yellow':
		print("get 15 points")


# 判断列表是否为空
list = []
if list:
	print("not empty")
else:
	print("empty")

	

