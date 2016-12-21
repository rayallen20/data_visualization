import pygal
from die import Die

# 创建1个D6 和 1个D10
die1 = Die()
die2 = Die(10)

# 掷N次骰子 将结果存储在一个list中
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)


# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)


# 对结果进行可视化

# 直方图
hist = pygal.Bar()
# 直方图标题
hist.title = 'Result of rolling a D6 and a D10 50,000 times'
# 直方图X轴标签
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
# 直方图X轴标题
hist.x_title = 'Result'
# 直方图Y轴标题
hist.y_title = 'Frequency of Result'

# 将值添加到图表中
hist.add('D6 + D10', frequencies)
# 保存为SVG文件 注意 只能保存为SVG文件
hist.render_to_file('different_dice.svg')
