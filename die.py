from random import randint

class Die:
    """本类用于表示一个骰子"""

    def __init__(self, num_sides=6):
        """骰子缺省设置为6面"""
        self.num_sides = num_sides

    def roll(self):
        """
        返回一个位于1和骰子面数之间的随机数
        :return: int 位于1和骰子面数之间的随机数
        """
        return randint(1, self.num_sides)
