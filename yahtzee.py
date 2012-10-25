class Yahtzee(object):

    def __init__(self, *args):
        self.dice = args[0:5]

    @staticmethod
    def _count_like(num, dice):
        total = 0
        for i in dice:
            if i == num:
                total += 1
        return total

    @staticmethod
    def _count_equal(size, dice):
        result = []
        for i in range(6,0,-1):
            if Yahtzee._count_like(i, dice) == size:
                result.append(i)
        return result

    def fours(self):
        num = 4
        return Yahtzee._count_like(num, self.dice) * num

    def fives(self):
        num = 5
        return Yahtzee._count_like(num, self.dice) * num

    def sixes(self):
        num = 6
        return Yahtzee._count_like(num, self.dice) * num

    @staticmethod
    def chance(*args):
        return sum(args)

    @staticmethod
    def yahtzee(dice):
        for i in range(1, 7):
            if dice.count(i) == len(dice):
                return 50
        return 0

    @staticmethod
    def ones(*args):
        num = 1
        return Yahtzee._count_like(num, args) * 1

    @staticmethod
    def twos(*args):
        num = 2
        return Yahtzee._count_like(num, args) * 2

    @staticmethod
    def threes(*args):
        num = 3
        return Yahtzee._count_like(num, args) * 3

    @staticmethod
    def score_pair(*args):
        for i in range(6, 0, -1):
            if Yahtzee._count_like(i, args) == 2:
                return 2 * i
        return 0

    @staticmethod
    def two_pair(*args):
        retur = 0
        for i in range(6, 0, -1):
            if Yahtzee._count_like(i, args) == 2:
                if retur:
                    return retur + 2 * i
                else:
                    retur = 2 * i
        return 0

    @staticmethod
    def four_of_a_kind(*args):
        for i in range(6, 0, -1):
            if Yahtzee._count_like(i, args) == 4:
                return 4 * i
        return 0

    @staticmethod
    def three_of_a_kind(*args):
        for i in range(6, 0, -1):
            if Yahtzee._count_like(i, args) == 3:
                return 3 * i
        return 0

    @staticmethod
    def smallStraight(*args):
        return (sorted(args) == [1,2,3,4,5]) * 15

    @staticmethod
    def largeStraight(*args):
        return (sorted(args) == [2,3,4,5,6]) * 20

    @staticmethod
    def fullHouse(*args):
        three = Yahtzee._count_equal(3,args)*3
        two = Yahtzee._count_equal(2,args)*2
        if three and two:
            return sum(three+two)
        return 0
