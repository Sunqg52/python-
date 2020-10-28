import matplotlib.pyplot as plt

# 使用scatter()绘制散点图并添加样式
# 自动计算数据 自定义颜色 使用颜色映射 保存图表

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig,ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)	#使用颜色映射

'''
ax.scatter(x_values,y_values, c='red',s=10)  # 自定义颜色
ax.scatter(2,4,s=200)	# 在指定坐标绘制一个点. s:规定点的尺寸
'''

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置表尺刻度的大小
#ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])
ax.ticklabel_format(useOffset = False, style ='plain')   # 防止使用科学计数法


#plt.show()
plt.savefig('squares_plot.png', bbox_inches = 'tight')