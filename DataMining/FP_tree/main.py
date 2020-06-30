import FP_tree.fpgrowth  as fpgrowth
import time

'''simple data'''
# 初始化数据
simDat = fpgrowth.loadSimpDat()
# 初始化每个数据元素出现的次数
initSet = fpgrowth.createInitSet(simDat)
# 构造FPtree
myFPtree, myHeaderTab = fpgrowth.createFPtree(initSet, 3)
#遍历构造好的FP树
myFPtree.disp()

# print (fpgrowth.findPrefixPath('p', myHeaderTab))
# print (fpgrowth.findPrefixPath('m', myHeaderTab))
# print (fpgrowth.findPrefixPath('b', myHeaderTab))
# print (fpgrowth.findPrefixPath('a', myHeaderTab))
# print (fpgrowth.findPrefixPath('c', myHeaderTab))

# 找出所有的频繁项集
freqItems = []
fpgrowth.mineFPtree(myFPtree, myHeaderTab, 3, set([]), freqItems)
# 输出关于m的频繁项集
for x in freqItems:
    if list(x).__contains__('m'):
        print (x)

# suppData = fpgrowth.calSuppData(myHeaderTab, freqItems, len(simDat))
# suppData[frozenset([])] = 1.0
# for x,v in suppData.items():
#     print (x,v)
#
# freqItems = [frozenset(x) for x in freqItems]
# fpgrowth.generateRules(freqItems, suppData)

# '''kosarak data'''
# start = time.time()
# n = 20000
# with open("./data/kosarak.dat", "rb") as f:
#     parsedDat = [line.split() for line in f.readlines()]
# initSet = fpgrowth.createInitSet(parsedDat)
# myFPtree, myHeaderTab = fpgrowth.createFPtree(initSet, n)
# freqItems = []
# fpgrowth.mineFPtree(myFPtree, myHeaderTab, n, set([]), freqItems)
# for x in freqItems:
#     print (x)
# print (time.time()-start, 'sec')

# compute support values of freqItems
# suppData = fpgrowth.calSuppData(myHeaderTab, freqItems, len(parsedDat))
# suppData[frozenset([])] = 1.0
# for x,v in suppData.iteritems():
#     print (x,v)
#
# freqItems = [frozenset(x) for x in freqItems]
# fpgrowth.generateRules(freqItems, suppData)