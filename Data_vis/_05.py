import csv
from datetime import datetime
import matplotlib.pyplot as plt

"""
%A：星期几  %m：用数表示的月份          %Y：四位的年份  %H：24小时制的小时数   
%B：月份名  %d：用数表示的月份中的某一天  %y：两位的年份  %I：12小时制的小时数  
%M：分钟数  %p：am或pm
%S：秒数
"""

# 处理CSV文件格式
filename = "data/sitka_weather_2018_simple.csv"

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)		#next函数返回文件的下一行

	# 从文件中获取日期和最高温度

	dates,highs, lows = [], [], []				
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')

		# 处理数据缺失情况,直接忽略
		try:
			high = int(row[5])
			low = int(row[6])
		except ValueErrot:
			print(f"Missing date for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

#print(highs)

'''
#打印文件头及其位置
#使用enumerate()获得每个元素的索引及其值
for index, column_header in enumerate(header_row):
	print(index,column_header)
'''

#根据最高温度绘制图表
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig,ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)	#alpha:指定颜色透明度
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
ax.set_title("2018年每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()			# 绘制倾斜的日期标签
ax.set_ylabel("温度（F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()




