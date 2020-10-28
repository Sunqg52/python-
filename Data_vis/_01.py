import matplotlib.pyplot as plt

# 绘制一个简单的折线图 subplots()在一张图片中绘制图表
squares = [1,2,4,3,6,74,5,7]
fig, ax = plt.subplots()

# 设置线条粗细并更改标签
ax.plot(squares,linewidth=3)
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=25)
ax.set_ylabel("值的平方", fontsize=15)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=20)
plt.show()
