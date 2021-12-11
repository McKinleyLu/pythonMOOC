# 列表中元素数据类型可以不同
import numpy as np
from numpy.core.fromnumeric import partition

# 定义一个ndarray数组
# 轴：数据的维度
# 秩：维度的个数(轴的个数 || 行的个数)
a = np.array([1,2,3,4])
print(a**2)
print(a.ndim,a.shape,a.size,a.dtype,a.itemsize)
# intc == C语言中的int类型


# 创建ndarrray数组
#(1)
lists = [1,2,3,1]
x = np.array(list)
#使用创建函数
x = np.arange(10)
y = np.ones((2,3,4),np.intc)
z = np.zeros(2,np.intc)
a = np.eye(6)
b = np.full((2,3),10)
ans = np.linspace(1,10,4)
anss = np.linspace(1,10,4,endpoint=False)
print(anss)
#数组维度以及元素类型变换
print(y)
k = y.astype(np.float32)
print(k)
# 数组转换成列表
p = k.tolist()
print(p)
print(np.full((3,2,3),5,dtype=np.intc))
# 数组的切片与索引  注意 : 与 ， 的区别
a = np.array((1,2,3,3,4))
# 步长一维切片
print(a[0:4:2])
# 二维数据获取方式
a = np.arange(24).reshape(2,3,4)
print(a)

print(a[:,:,3])
print('\n')
# 步长二维切片
print(a[:,:,::2])


# 数组与标量之间的运算
print(np.sqrt(a))
a = [[2,3,0],[1,3,4]]
b = [1,2,4]
a = np.array(a)
b = np.array(b)
print("===========")
print(a*b)
print(np.maximum(a,b))