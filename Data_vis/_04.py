from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
	def __init__(self,num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)

die = Die()		# 6面骰子
die_1 = Die(10) # 10面骰子

# 掷几次骰子并将结果存储在同一个列表中
results = []
for roll_num in range(1000):
	result = die.roll() + die_1.roll()
	results.append(result)
#print(results)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die.num_sides	# 存储可能出现的点数
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)

# 对结果进行可视化
# Plotly不能直接接受函数range() 的结果，使用list函数将其转换为列表
x_values = list(range(2, max_result + 1)) 
data = [Bar(x=x_values, y=frequencies)]			#使用Bar函数生成条形图

x_axis_config = {'title': '结果', 'dtick':1}		# 使用ditck设置刻度间距
y_axis_config = {'title': '结果的频率'}

# 函数layout返回一个指定图表布局和配置的对象
my_layout = Layout(title='掷 1000次的结果',
	xaxis=x_axis_config, yaxis=y_axis_config )

# 使用offline.plot函数，需要一个包含数据和布局对对象的字典 以及图表保存位置为d6.html
offline.plot({'data': data, 'layout':my_layout}, filename='d6_d10.html')
