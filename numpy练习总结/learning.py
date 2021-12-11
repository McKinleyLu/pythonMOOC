import numpy as np
from numpy.random.mtrand import permutation
#  通过列表创建二维数组
print("=====通过列表创建二维数组=========")
np.array([(1, 2, 3), (4, 5, 6)])  
# 上方数组的秩为 2。第一个维度长度为 2,第二个维度长度为 3。

# 依据自定义函数创建数组
print("=====依据自定义函数创建数组====")
np.fromfunction(lambda i, j: i + j, (3, 3))

# 矩阵乘法运算
print("======矩阵乘法运算=======")
A = np.array([[1,2],
   [3,4]])
B = np.array([[5,6],
           [7,8]])
print(np.dot(A,B))

#矩阵的转置
print("=====矩阵的转置======")
print(A.T)

#矩阵求逆
print("====矩阵求逆=====")
print(np.linalg.inv(A))

# 一维数组索引
print("=====一维数组索引=====")
a = np.array([1,2,3,4,5])
print(a[0:2], a[:-1])

# 二维数组索引
print("=====二维数组索引======")
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(a[0],a[-1])

print("====数组a=====")
a = np.array([[1,2 ,3],
 [4 ,5 ,6],
 [7, 8, 9]])
print(a)
# 二维数组切片（取第 2 列）
print("====二维数组切片（取第 2 列）======")
print(a[:,1])
print("====二维数组切片（取第 2，3 行）=====")
print(a[1:3,:])

print("===展平数组====")
print(a.ravel())

print("==== 数组合并===")
a = np.random.randint(10, size=(3, 3))
b = np.random.randint(10, size=(3, 3))
print(a)
print("===")
print(b)
print("===水平合并=====")
print(np.hstack((a,b)))
print("===垂直合并====")
print(np.vstack((a,b)))

print("======割分数组=======")
print("===原数组===")
print(a)
print("==沿横轴分割数组==")
print(np.hsplit(a,3))
print("==沿纵轴分割数组==")
print(np.vsplit(a,3))

# 数组排序
print("===数组排序===")
a = np.array(([1, 4, 3], [6, 2, 9], [4, 7, 2]))
print(a)
#axis = 0 列    axis = 1 行
print("===返回列最小值====")
print(np.min(a,axis=0))
print("===返回行最大值====")
print(np.max(a,axis=1))
print("==返回每列最大值索引==")
print(np.argmax(a,axis=0))
print("==统计数组各列的中位数==")
print(np.mean(a,axis=0))
print("==统计数组各行的算术平均值==")
print(np.mean(a,axis=1))
print("==统计数组各列的加权平均值==")
print(np.average(a,axis=0))
print("==统计数组各行的方差==")
print(np.var(a,axis=1))
print("==统计数组各列的标准偏差==")
print(np.std(a,axis=0))


# 进阶部分
print("=======================进阶部分=============================")
print("==创建一个 5x5 的二维数组，其中边界值为1，其余值为0==")
a = np.ones((5,5))
print(a)
a[1:-1,1:-1] = 0 
print(a)

print("使用数字 0 将一个全为 1 的 5x5 二维数组包围")
a = np.zeros((5,5))


'''
pad_width是在各维度的各个方向上想要填补的长度,
如（（1，2），（2，2）），
表示在第一个维度上水平方向上padding=1,垂直方向上padding=2,
在第二个维度上水平方向上padding=2,垂直方向上padding=2。
如果直接输入一个整数，则说明各个维度和各个方向所填补的长度都一样。

mode为填补类型，即怎样去填补，有“constant”，“edge”等模式，
如果为constant模式，就得指定填补的值，如果不指定，则默认填充0。
'''



a = np.pad(a, pad_width=1, mode='constant', constant_values=0)
print(a)

print("===创建一个 5x5 的二维数组，并设置值 1, 2, 3, 4 落在其对角线下方===")
a = np.diag(1+np.arange(4), k=-1)
print(a)

print("创建一个 10x10 的二维数组，并使得 1 和 0 沿对角线间隔放置：")
a  = np.zeros((10,10),dtype=int)
a[1::2,::2] = 1
a[::2,1::2] = 1
print(a)

print("创建一个 0-10 的一维数组，并将 (1, 9] 之间的数全部反转成负数：")
a = np.arange(11)
a[(1 < a) & (a <= 9)] *= -1
print(a)

print("找出两个一维数组中相同的元素")
a1 = np.random.randint(0,10,10)
a2 = np.random.randint(0,10,10)
print("a1:",a1)
print("a2:",a2)
np.intersect1d(a1,a2)

print("使用 NumPy 打印昨天、今天、明天的日期")
yesterday = np.datetime64('today','D') - np.timedelta64(1,'D')
today = np.datetime64('today','D')
tomorrow = np.datetime64('today','D') + np.timedelta64(1,'D')
print("yesterday:",yesterday)
print("today",today)
print("tomorrow",tomorrow)

print("===使用五种不同的方法去提取一个随机数组的整数部分===")
a = np.random.uniform(0,10,10)
print(a)
print(a - a % 1)
print(np.floor(a))
print(np.ceil(a) - 1)
print(a.astype(int))
print(np.trunc(a))


