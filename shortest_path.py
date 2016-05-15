# -*- encoding:utf-8 -*-
import random
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
global distance_matrix
class Point:
    def __init__(self,X,Y,Q):
        self.X = X
        self.Y = Y
        self.Q = Q
        self.flag = 0

#输入：第几个点，距离矩阵
#输出：第几个点
def min_dis(crrod,distance_matrix):
    min = 30
    poin = crrod
    for j in range(33):
        if (distance_matrix[crrod][j] < min and point[j].flag == 0):
            min = distance_matrix[crrod][j]
            poin = j
    point[poin].flag = 1
    return poin

#判断全部点是否遍历
def is_all():
    flag = False;
    for i in range(33):
        if (point[i].flag == 0):
            flag = True;
    return flag

if __name__ == "__main__":
    #随机生成点33个点
    point = [0 for col in range(33)]
    for i in range(33):
        point[i] = Point(random.randint(1,30),random.randint(1,30),random.uniform(0.2,1.5))

    f1 = plt.figure(1)
    # plt.subplot(211)
    #取前三个点为配送中心
    for i in range(3):
        plt.scatter(point[i].X, point[i].Y,color = 'r')
    #剩余的30个点为需求点
    for i in range(3,33):
        plt.scatter(point[i].X,point[i].Y)


    #构建距离矩阵

    distance_matrix = [[0 for col in range(33)] for row in range(33)]

    for i in range(33):
        for j in range(33):
            distance_matrix[i][j] = math.sqrt((point[i].X - point[j].X)*(point[i].X - point[j].X) + (point[i].Y - point[j].Y)*(point[i].Y - point[j].Y))
            #print distance_matrix[i][j]
    '''
    for i in range(33):
        for j in range(33):
            print distance_matrix[i][j]
    '''
    #寻找最短路径
    point[0].flag = 1
    list_X = [point[0].X]
    list_Y = [point[0].Y]
    print is_all()
    count = 0
    while is_all():
        poin = min_dis(0 ,distance_matrix)
        list_X.append(point[poin].X)
        list_Y.append(point[poin].Y)
        print is_all()
        if count > 40:
            break
        count=count+1
    plt.plot(list_X,list_Y)
    plt.show()









