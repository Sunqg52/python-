import matplotlib.pyplot as plt
from random import choice

#随即漫步

class RandomWalk:
	def __init__(self,num_points=5000):
		self.num_points = num_points

		# 设置起始位置
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		""" 设置随即漫步包含所有的点"""

		# 不断漫步直到达到制定的长度,及决定本次一共要走多少步
		while len(self.x_values) < self.num_points:

			# 决定方向及距离
			x_direction = choice([1,-1])		# 向右走或向左走

			x_distance = choice([0,1,2,3,4])	# 通过choice函数决定要走的步数
			x_step = x_direction * x_distance	# 确定要走的方向以及步数

			y_direction = choice([1, -1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance

			# 不能原地踏步
			if x_step == 0 and y_step == 0:
				continue

			# 计算下一个点的x值和y值  将列表中的最后一个值与走的步数相加
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)


while True:
	rw = RandomWalk(50000)
	rw.fill_walk()
	# print(f"{rw.x_values} \n {rw.y_values}")

	plt.style.use('classic')
	fig,ax = plt.subplots(figsize=(10,6),dpi=128)   #通过dpi传递分辨率 使用figsize更改大小

	point_numbers = range(rw.num_points)		#暂存漫步点
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
	edgecolors='none', s=15)

	# 突出起点和终点
	ax.scatter(0,0,c='green',edgecolors='none',s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=1)

	# 隐藏坐标轴
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)


	plt.show()

	keep_running = input("Make another walk? (y/n)")
	if keep_running == 'n':
		break

