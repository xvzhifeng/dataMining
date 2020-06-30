"""
    @Author:sumu
    @Date:2020-05-24 23:34
    @Email:xvzhifeng@126.com

"""

"""
聚类算法层次分裂之DIANA

算法思想：

输入：n个对象，终止条件簇的数目k

输出：k个簇，达到终止条件规定簇数目

1、将所有对象当成一个初始簇
2.for(i=1;i≠k;i++) do begin
3.在所有簇中挑选出具有最大直径的簇C
4.找出C中与其它点平均相异度最大的一个点P并把P放入splinter group，剩余的放在old party中
5.repeat
6.在old party中找出到最近的splinter group中的点的距离不大于到old party中最近点的距离的点，并将该点加入splinter group
7.until没有新的old party的点被分配给spilnter group
8。spilnter group和old party为被选中的簇分裂成的2个簇与其它簇一起组成新的簇集合
9、end
"""



import math




def dataload():
    """
    加载并生成原始数据
    :return: 处理好的数据点的坐标
    """
    data= """ 'A',0,2,'B',0,0,'C',1.5,0,'D',5,0,'E',5,2 """

    #数据处理 dataset是5个样本（x，y）的列表
    a = data.split(',')
    dataset = [(float(a[i]), float(a[i+1])) for i in range(1, len(a)-1, 3)]
    return dataset



def dist(a, b):
    """
    计算欧几里得距离,a,b分别为两个元组
    :param a:
    :param b:
    :return:
    """
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))

#dist_min
def dist_min(Ci, Cj):
    return min(dist(i, j) for i in Ci for j in Cj)
#dist_max
def dist_max(Ci, Cj):
    return max(dist(i, j) for i in Ci for j in Cj)
#dist_avg
def dist_avg(Ci, Cj):
    return sum(dist(i, j) for i in Ci for j in Cj)/(len(Ci)*len(Cj))





#算法模型：
def DIANA(dataset, dist, k):
    """
    :param dataset: 数据坐标
    :param dist:计算机距离的函数
    :param k:族的个数
    :return:聚类集合

    """
    #初始化C和M
    C = [];M = []
    # 初始化把每一个样本点分成一个族
    for i in dataset:
        Ci = []
        Ci.append(i)
        C.append(Ci)
    # 计算出样本点间距离
    for i in C:
        Mi = []
        for j in C:
            Mi.append(dist(i, j))
        M.append(Mi)
    oldParty = [];sliterGroup = []

    # 找到平均相异度最大的点并保存其下标
    sum = 0
    index = 0
    for i in range(len(M)):


        sum1 = 0
        for j in range(len(M[i])):
            sum1 += M[i][j]
        if sum1 > sum:
            sum = sum1
            index = i
    #print(index)
    # 初始化sliterGroup和oldParty
    for i in range(len(C)):
        if i == index:
            sliterGroup.append(i)
        else:
            oldParty.append(i)
    #print(sliterGroup,oldParty)
    # 用于存储当前有多少个族
    q = len(dataset)
    #合并更新
    temp = 1000
    index1 = 1000
    index = 1000
    while q > k:
        for i in oldParty:
            for j in sliterGroup:
                if temp > M[i][j]:
                    temp = M[i][j]
                    index = i
        if index != index1:
            sliterGroup.append(index)
            oldParty.remove(index)
            index1 = index
        else:
            N = [];N1 = [];N2 = []
            for i in range(len(C)):
                if sliterGroup.__contains__(i):
                    N1.append(C[i])
                else:
                    N2.append(C[i])
            N.append(N1)
            N.append(N2)
            C = N
        q = len(C)
    return C

if __name__ == "__main__":
    # 加载算法模型进行分族
    C = DIANA(dataload(), dist_avg, 2)
    # 替换坐标点为编号
    s = str(C)
    s = s.replace('(0.0, 2.0)', 'A')
    s = s.replace('(0.0, 0.0)', 'B')
    s = s.replace('(1.5, 0.0)', 'C')
    s = s.replace('(5.0, 0.0)', 'D')
    s = s.replace('(5.0, 2.0)', 'E')
    # 输出最后的结果
    print("分类好的族：")
    print(s)
   # draw(C)



