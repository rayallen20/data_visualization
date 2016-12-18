# data visualization
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# 设置图表标题 并给坐标轴加上标签

# 标题
plt.title("Square Numbers", fontsize=24)
# X轴标签
plt.xlabel("Value", fontsize=24)
# Y轴标签
plt.ylabel("Square of Value", fontsize=24)

# 设置坐标轴上的字体大小 axis='both' 即X Y两轴同时生效
plt.tick_params(axis='both', labelsize=14)

# 显示图表
plt.show()

"""
plot(list):绘制图形的方法
show(): 打开matplotlib查看器 显示 plot() 绘制的图形
"""

"""
目前有一个问题:
squares = [1, 4, 9, 16, 25]
设置的Y值确实是 1 4 9 16 25 但是对应的X值 是从0开始的 即描绘出的点 是
(0,1) (1,4) (2,9) (3,16) (4,25)
而我们想要的是
(1,1) (2,4) (3,9) (4,16) (5,25)
"""