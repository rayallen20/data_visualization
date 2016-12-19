import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要用户选择继续 就重新生成5000个点
while True:

    # 创建一个RandomWalk()实例 并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 颜色映射 start
    point_numbers = list(range(rw.num_points))
    # 颜色映射 end

    # 其中 c=point_numbers的意思 是指 前边正好有5000个点 所以每个点分配一个颜色的深度
    # c 和 cmap两个参数同时出现时 c为一个list 其中 值较小的 颜色较浅 值较大的 颜色较深
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=1)

    # 着重绘制起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 由于我们希望看到的是点的随机漫步路径 而不是坐标轴 所以设置隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
