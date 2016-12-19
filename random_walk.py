from random import choice

class RandomWalk:
    """本类用于生成随机漫步数据"""

    def __init__(self, num_points=5000):
        """
        初始化随机漫步的属性
        :param num_points: int 随机漫步的次数
        """
        self.num_points = num_points

        # 所有的随机漫步都从(0,0)开始
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 如果没有达到指定的次数 继续漫步
        while len(self.x_values) < self.num_points:

            # 本次移动在X轴上方向为右或者左
            x_direction = choice([1, -1])

            # 在该方向上移动0~4个单位
            x_distance = choice([0, 1, 2, 3, 4])

            # 本次移动的X轴坐标
            x_step = x_direction * x_distance

            # 本次移动在Y轴上方向为上还是下
            y_direction = choice([-1, 1])

            # 在该方向上移动 0~4个单位
            y_distance = choice([0, 1, 2, 3, 4])

            # 本次移动的Y轴坐标
            y_step = y_direction * y_distance

            # 如果是原地踏步 则重新开始一次循环
            if x_step == 0 and y_step == 0:
                continue

            # 基于上一个随机漫步点的位置 进行本次移动
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # 将本次移动点的X/Y坐标 加入到list中
            self.x_values.append(next_x)
            self.y_values.append(next_y)
