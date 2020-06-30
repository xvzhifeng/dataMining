"""
    @Author:sumu
    @Date:2020-05-25 00:39
    @Email:xvzhifeng@126.com

"""


import math
import numpy as np



def loadData():
    """
    初始化数据
    :return: 数据字典
    """
    data = {1:(3,1),2:(2,1),3:(4,2),4:(3,2),5:(2,2),
            6:(1,2),7:(2,3),8:(2,4),9:(3,5),10:(2,5),
            11:(1,5),12:(2,6)}
    return data

def solveData(data):
    """
    数据处理
    :param data: 原始数据
    :return: 处理后的数据
    """
    dataset = []
    for i in range(len(data)) :
        dataset.append(data[i + 1])
    return dataset


def dist(a, b):
    """
    计算欧几里得距离,a,b分别为两个元组
    :param a:
    :param b:
    :return:
    """
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))

#算法模型
def DBSCAN(D, e, Minpts):
    """
    DBSCAN算法模型
    :param D: 处理后的数据
    :param e: 半径
    :param Minpts: 范围的点的个数
    :return:
    """
    #初始化核心对象集合T,聚类个数k,聚类集合C, 未访问集合P,
    T = set(); k = 0; C = []; P = set(D)
    for d in D:
        if len([ i for i in D if dist(d, i) <= e]) >= Minpts:
            T.add(d)
    #开始聚类
    while len(T):
        P_old = P
        o = list(T)[np.random.randint(0, len(T))]
        P = P - set(o)
        Q = []; Q.append(o)
        while len(Q):
            q = Q[0]
            Nq = [i for i in D if dist(q, i) <= e]
            if len(Nq) >= Minpts:
                S = P & set(Nq)
                Q += (list(S))
                P = P - S
            Q.remove(q)
        k += 1
        Ck = list(P_old - P)
        T = T - set(Ck)
        C.append(Ck)
    return C




if __name__ == "__main__":
    # 初始化数据
    data = loadData()
    # 调用算法
    C = DBSCAN(solveData(data), 1, 4)
    # 利用数据字典，转换输出的结果
    data = dict(zip(data.values(), data.keys()))
    N = []
    for i in C:
        Ni = []
        for j in i:
            Ni.append(data[j])
        N.append(Ni)
    print("分好的各族编号：")
    print(N)