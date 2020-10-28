# 列表 for循环

magicians = ['alice','david','carolina']
for magician in magicians:
	print(f"{magician.title()},you are good!")
	print(f"I can't wait to see you next trick, {magician.title()}.\n")
print("thank you, everyone.That was a great magic show!")







# 数值列表 range函数

list = []		
for value in range(1,11):		
	list.append(value**2)

print(f"list: {list}\n")			#输出列表
print(f"list_min: {min(list)}\n")	#输出列表中的最小值
print(f"list_max: {max(list)}\n")	#输出列表中的最大值
print(f"list_sum: {sum(list)}\n")	#输出列表中所有值的和





# 列表解析
# 将range函数生成的值赋给value 再将alue平方 添加进列表list中

list = [value**2 for value in range(1,11)]
print(list)




#使用for循环打印10-20
for value in range(1,21):
	print(f"1~20: {value}")

#打印1到一百万
for value in range(1,1000001):
	print(f"{value}\t")

#对一到一百万操作
list = [value3 for value3 in range(1,1000001)]
print(f"list_min: {min(list)}\n")
print(f"list_max: {max(list)}\n")
print(f"list_sum: {sum(list)}\n")


#3到30能被3整除的数
list = [value for value in range(3,31,3)]
print(list)

#1到10的立方
list = [value**3 for value in range(1,11)]
print(list)


#切片 遍历列表中的前十个数
list = [value for value in range(1,101)]
for value in list[:10]:
	print(f"\t{value}")

#切片 遍历列表中的后十个数
for value in list[90:]:
	print(f"\t{value}")

#切片 遍历列表中的500~600
for value in list[49:60]:
	print(f"\t{value}")

#此处并不是彻底赋值  彻底赋值：list_1 = list
list_1 = list[:]
print(list_1)


#元组：不可改变的列表，用圆括号标识