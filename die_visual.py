import pygal
from die import Die

# 创建一个D6
die = Die()

# 掷N次骰子 将结果存储在一个list中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化

# 直方图
hist = pygal.Bar()
# 直方图标题
hist.title = 'Result of rolling one D6 1000 times'
# 直方图X轴标签
hist.x_labels = ['1', '2', '3', '4', '5', '6']
# 直方图X轴标题
hist.x_title = 'Result'
# 直方图Y轴标题
hist.y_title = 'Frequency of Result'

# 将值添加到图表中
hist.add('D6', frequencies)
# 保存为SVG文件 注意 只能保存为SVG文件
hist.render_to_file('die_visual.svg')
