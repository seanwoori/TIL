import sys
sys.stdin = open('input.txt', 'r')

class Rectangle:
    def __init__(self, lst):
        self.st_a = lst[0]
        self.st_b = lst[1]
        self.ed_a = self.st_a + 10
        self.ed_b = self.st_b + 10

    def overlap(self, lst):
        flag = False
        flag_temp = False

        if (lst[0] >= self.st_a) and (lst[0] <= self.ed_a):
            flag_temp = True
        elif (lst[1] >= self.st_b) and (lst[1] <= self.ed_b) and flag_temp == True:
            flag = True
            return flag
        else:
            return flag

