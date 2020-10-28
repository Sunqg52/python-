import matplotlib.pyplot as plt

# 绘制一个简单的折线图 subplots()在一张图片中绘制图表
input_value = [1,2,3,4,5,6,7]
squares = [1,2,4,6,7,9,11]

# 使用内置样式
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


fig, ax = plt.subplots()

# 设置线条粗细并更改标签input_value, 设置输入值
ax.plot(input_value, squares,linewidth=3)
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)
plt.show()
