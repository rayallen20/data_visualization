import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要用户选择继续 就重新生成5000个点
while True:

    # 创建一个RandomWalk()实例 并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
