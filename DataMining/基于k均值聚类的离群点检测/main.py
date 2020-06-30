"""
    @Author:sumu
    @Date:2020-05-25 11:00
    @Email:xvzhifeng@126.com

"""


# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt
import operator
import time

INF = 9999999.0

def loadDataSet(fileName, splitChar='\t'):
    """
    输入：文件名
    输出：数据集
    描述：从文件读入数据集
    """
    dataSet = []
    with open(fileName) as fr:
        for line in fr.readlines():
            curline = line.strip().split(splitChar)
            fltline = list(map(float, curline))
            dataSet.append(fltline)
    return dataSet

def createDataSet():
    """
    输出：数据集
    描述：生成数据集
    """
    dataSet = [[0.0, 0.0],
               [1.0, 0.0],
               [3.0, 1.0],
               [8.0, 8.0],
               [9.0, 10.0],
               [10.0,7.0],
               [10.0,1.0]]
    dataSet1 = [[0.0,0.0],
                [1.0,2.0],
                [3.0,1.0],
                [8.0,8.0],
                [9.0,10.0],
                [10.0,7.0]]
    dataSet2 = [[0.0,0.0],
                [1.0,1.0],
                [1.0,2.0],
                [9.0,1.0],
                [10.0,2.0],
                [10.0,10.0],
                [11.0,10.0]]
    return dataSet2

def distEclud(vecA, vecB):
    """
    输入：向量A, 向量B
    输出：两个向量的欧式距离
    """
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet, k):
    """
    输入：数据集, 聚类个数
    输出：k个随机质心的矩阵
    """
    # n = shape(dataSet)[1]
    # print(n)
    # centroids = mat(zeros((k, n)))
    # print(centroids)
    N = []
    for i in range(k):
        N.append(dataSet[i])
    centroids = mat(N)
    # for j in range(n):
    #     minJ = min(dataSet[:, j])
    #     rangeJ = float(max(dataSet[:, j]) - minJ)
    #     centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids

def kMeans(dataSet, k, centroids,distMeans=distEclud, createCent=randCent):
    """
    输入：数据集, 聚类个数, 距离计算函数, 生成随机质心函数
    输出：质心矩阵, 簇分配和距离矩阵
    """
    m = shape(dataSet)[0]   # 行的数目
    print("行数",m)
    clusterAssment = mat(zeros((m, 2)))
    print("clusterAssment",clusterAssment)
    # 第1步 初始化centroids
    #centroids = createCent(dataSet, k)

    print("质心",centroids)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        # 遍历所有的样本（行数）
        for i in range(m): # 寻找最近的质心
            minDist = INF
            minIndex = -1
            # 遍历所有的质心
            # 第2步 找出最近的质心
            for j in range(k):
                # 计算该样本到质心的欧式距离
                distJI = distMeans(centroids[j, :], dataSet[i, :])
                print("质心",centroids[j,:],"点",dataSet[i, :],"欧式距离",distJI)
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j

            # 第 3 步：更新每一行样本所属的簇
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist**2
        # 第 4 步：更新质心
        for cent in range(k): # 更新质心的位置
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]  # 获取簇类所有的点
            if len(ptsInClust) != 0:
                centroids[cent, :] = mean(ptsInClust, axis=0)  # 对矩阵的行求均值
        print("质心new",centroids)
    return centroids, clusterAssment

def plotFeature(dataSet, centroids, clusterAssment):
    m = shape(centroids)[0]
    fig = plt.figure()
    scatterMarkers = ['s', 'o', '^', '8', 'p', 'd', 'v', 'h', '>', '<']
    scatterColors = ['blue', 'green', 'yellow', 'purple', 'orange', 'black', 'brown']
    ax = fig.add_subplot(111)
    for i in range(m):
        ptsInCurCluster = dataSet[nonzero(clusterAssment[:, 0].A == i)[0], :]
        markerStyle = scatterMarkers[i % len(scatterMarkers)]
        colorSytle = scatterColors[i % len(scatterColors)]
        ax.scatter(ptsInCurCluster[:, 0].flatten().A[0], ptsInCurCluster[:, 1].flatten().A[0], marker=markerStyle, c=colorSytle, s=90)
    ax.scatter(centroids[:, 0].flatten().A[0], centroids[:, 1].flatten().A[0], marker='+', c='red', s=300)

def main():
    #dataSet = loadDataSet('testSet2.txt')
    #dataSet = loadDataSet('788points.txt', splitChar=',')
    k = 3
    dataSet = createDataSet()
    centroids = randCent(dataSet,k)
    print("初始质心：",centroids)
    dataSet = mat(dataSet)
    #print(dataSet)

    resultCentroids, clustAssing = kMeans(dataSet, k,centroids)
    print('*******************')
    print(resultCentroids)
    print('*******************')
    print(clustAssing)
    plotFeature(dataSet, resultCentroids, clustAssing)

if __name__ == '__main__':
    main()
    plt.show()