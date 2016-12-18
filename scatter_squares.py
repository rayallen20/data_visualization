# data visualization -- 绘制散点图
import matplotlib.pyplot as plt

# 每个点的X坐标值
x_values = [1, 2, 3, 4, 5]

# 每个点的Y坐标值
y_values = [1, 4, 9, 16, 25]

# s=200 设置点的尺寸大小
plt.scatter(x_values, y_values, s=200)

# 设置图表标题 并给坐标轴加上标签

# 标题
plt.title("Square Numbers", fontsize=24)
# X轴标签
plt.xlabel("Value", fontsize=24)
# Y轴标签
plt.ylabel("Square of Value", fontsize=24)

# 设置坐标轴上的字体大小
# which参数:major 显示主刻度 minor 显示次刻度 both 主次刻度都显示
# labelsize 设置字号
plt.tick_params(axis='both', which='major',  labelsize=14)

plt.show()

"""
scatter(X值,Y值) 在坐标系中绘制一个点
"""

"""
scatter(所有点的X坐标值list, 所有点的Y坐标值list, s=num) 在坐标系中绘制多个点
"""