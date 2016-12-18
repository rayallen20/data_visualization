# data visualization
import matplotlib.pyplot as plt

# 输入值
input_values = [1, 2, 3, 4, 5]

# 输出值
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

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

"""
确切地讲: input_values为输入值 values为输出值 即:我输入了1 希望得到1 输入2 希望得到4 以此类推
而不需要程序自己假设 程序的假设就是按照输出值list的key值排序 即:我输入0 希望得到1 我输入1 希望得到4
即:每个点的X值 为输入值 Y值 为输出值
"""