# data visualization -- 绘制散点图
import matplotlib.pyplot as plt

# 每个点的X坐标值
x_values = list(range(1, 1001))

# 每个点的Y坐标值
# 下边这个是遍历一个list并将每个value改变后赋值给另外一个list的每个value一种简写
y_values = [x**2 for x in x_values]

# s=200 设置点的尺寸大小
# edgecolors = 'none' 删除数据点的边缘那圈黑色
# c=(红, 绿, 蓝) 其中 每个值均为0~1之间的小数值
# 或 c='red' 直接指定颜色
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)

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

# 设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

"""
scatter(X值,Y值) 在坐标系中绘制一个点
"""

"""
scatter(所有点的X坐标值list, 所有点的Y坐标值list, s=num) 在坐标系中绘制多个点
"""

"""
axis(X轴最小值, x轴最大值, y轴最小值, y轴最大值)
"""