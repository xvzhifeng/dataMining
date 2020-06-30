"""
    @Author:sumu
    @Date:2020-05-24 23:02
    @Email:xvzhifeng@126.com

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


def find_Min(M):
    """
    找到距离最小的下标
    :param M:
    :return: 返回距离最小的坐标和最小的距离
    """
    min = 1000
    x = 0; y = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i != j and M[i][j] < min:
                min = M[i][j];x = i; y = j
    return (x, y, min)



#算法模型：
def AGNES(dataset, dist, k):
    """
    :param dataset: 数据坐标
    :param dist:计算机距离的函数
    :param k:族的个数
    :return:聚类集合

    1.将数据集中的每个样本初始化为一个簇，并放入集合C中。计算任意两个集合之间的距离，并存到M中。
    2.设置当前聚类数目q = m。
    3.当q大于k时执行如下步骤：
        3.1找到距离最近的两个集合Ci和Cj, 将Ci和Cj合并。并赋值给Ci。
        3.2在集合C中将Cj删除，更新Cj+1到Cq的下标。
        3.3删除M的第j行和第j列。更新M的第i行和第i列。
        3.4q = q-1
    4.返回聚类集合C

    """
    #初始化C和M
    C = [];M = []
    # 初始化把每一个样本点分成一个族
    for i in dataset:
        Ci = []
        Ci.append(i)
        #print(Ci)
        C.append(Ci)
        #print(C)
    # 计算出样本点间距离
    for i in C:
        Mi = []
        for j in C:
            Mi.append(dist(i, j))
            #print(Mi)
        M.append(Mi)
        #print(M)
    # 用于存储当前有多少个族
    q = len(dataset)
    #合并更新
    while q > k:
        x, y, min = find_Min(M)
        C[x].extend(C[y])
        C.remove(C[y])
        M = []
        for i in C:
            Mi = []
            for j in C:
                Mi.append(dist(i, j))
            M.append(Mi)
        q -= 1
    return C

if __name__ == "__main__":
    # 加载算法模型进行分族
    C = AGNES(dataload(), dist_avg, 2)
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
    #draw(C)



