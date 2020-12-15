import random
import math


class Individual:
    def __init__(self, tsp):
        self.__name, self.__comment, self.__tsp_type, self.__num, self.__edge_type, self.__nodes = tsp.get_info()

    def get_random_result(self):
        rand = [i for i in range(self.__num)]
        random.shuffle(rand)
        rand.append(rand[0])
        dis = 0
        for i in range(self.__num):
            x1, y1 = self.__nodes[rand[i]][0], self.__nodes[rand[i]][1]
            x2, y2 = self.__nodes[rand[i+1]][0], self.__nodes[rand[i+1]][1]
            dis += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return dis
