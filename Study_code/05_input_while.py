# 使用input()函数判断用户是否成年，input函数的返回值为字符串类型，可以使用int进行强制转换
age = input("how old are you: ")
age = int(age)
if age >= 18:
	print("已成年")
else:
	print("未成年")

 

# while：1.设置标志（true或false） 2.break彻底退出循环 3.continue退出本次循环重新判定


# 使用while在列表间移动用户
unconfirmed_user = ['sunqg','sunqw']	#未验证用户
confirme_user = []		#已验证用户
while unconfirmed_user:
	current_user = unconfirmed_user.pop()
	confirme_user.append(current_user)
print(confirme_user)

# 使用while查找并删除
while 'sunqg' in confirme_user:
	confirme_user.remove('sunqg')
print(confirme_user)



# 使用while填充字典
phones = {}

pollint_active = True

while pollint_active:
	phone_name = input("\n 请输入手机品牌：")
	phone_price = input("\n 请输入手机价格：")

	phones[phone_name] = phone_price

	repeat = input("是否继续输入？(y/n)")
	if repeat == 'n':
		pollint_active = False

print(phones)



