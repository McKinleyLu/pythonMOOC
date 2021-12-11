# CSV存储
import numpy as np
from numpy.core.fromnumeric import reshape
from numpy.random.mtrand import choice
from numpy.testing import print_assert_equal 
# np.savetxt(frame,array,fmt,delimiter)  可以生成不止CSV格式的文件
# np.loadtxt(frame,dtype=np.float,delimilter,unpack)
# 只能读取一、二维数据
#--------------------#
a = np.arange(100).reshape(10,10)
# 写
np.savetxt('a.csv',a,fmt='%d',delimiter=',')
# 读
b = np.loadtxt('a.csv',dtype=np.int64,delimiter=',',unpack=False)

#------------------------------------
# a.tofile(frame,sep="",format = '')
# np.fromfile(frame,dtype,count = -1 ,sep='')...
a = np.arange(20).reshape(2,2,5)
# 写
a.tofile("b.dat",sep="-",format="%s")
# 读  失去了原数组维度信息    count = -1 代表读取文档全部内容
b = np.fromfile("b.dat",dtype=np.int8,sep=',')


#----------------------------------------
#np.save(frame,array)  np.savez(frame,array)
#np.load(frame)
# 可以保留数组的维度和变量信息
a = np.arange(20).reshape(2,5,2)
np.save('saves.npy',a)
b = np.load('saves.npy')
print(b)


print("-------numpy随机数函数子库-------")
#numpy随机数函数子库
np.random.seed(10)
n1 = np.random.rand(1,2,3)   #0-1均匀分布 ， 生成shape为(1,2,3)的数组
n2 = np.random.randn(1,2,3)
n3 = np.random.randint(10,20,(1,2,3))

a = np.arange(20).reshape(4,5)
print(a)
print("---------")
np.random.shuffle(a)                     
print(a)
np.random.permutation(a)
print(a)
a = np.arange(10)
newarray = np.random.choice(a,(2,3),replace=False)   #a必须为一维数组
print(newarray)



print("=========分布随机函数===========")
# 均匀分布
a = np.random.uniform(1,10,(2,3))
print(a)
# 正态分布
a = np.random.normal(2,3,(2,3))
print(a)
# 泊松分布
a = np.random.poisson(0.5,(2,3))
print(a)


print("======numpy统计函数=========")
# axis = 1为行(二维数组)
a = np.arange(10).reshape(2,5)
print(a)
sum = np.sum(a)
print(sum)
sumaxis = np.mean(a,axis=1)   
print(sumaxis)
ave = np.average(a,axis=0,weights=[2,3])
print(ave)

print(a)
print(np.max(a),np.argmax(a))
print(np.ptp(a),np.median(a))


print("========梯度函数=========")
# 梯度:连续值之间的斜率
a = [12,25,35,8,12,56,9]
print(a)
print(np.gradient(a))

c = np.random.randint(20,60,(3,4))
print(c)
