import matplotlib.pyplot as plt
import matplotlib
import numpy as np

import matplotlib.gridspec as gridspec

# 对于plot，如果只有一个列表，只代表纵轴
# ply.axis([0,10,0,5])   # x轴起始于0终止于10  y轴起始于0终止于5
plt.subplot(331)  
plt.plot([3,63,53,8,3])
plt.ylabel('Grade')
plt.savefig('test',dpi=600)



# pyplot的绘图区域
#选定区域
plt.subplot(332)   # === plt.subplot(324) 将画布分成三个横轴两个纵轴，分成4个区域
#画图 plot(x,y,format_string,**kwargs)
#format_string 包括颜色字符、风格字符和标记字符
a = np.arange(10)
plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'>-')


# 坐标系中出现中文方法
# 第一种方法，全部的字体都改变了
plt.subplot(333)
matplotlib.rcParams['font.family'] = 'Kaiti'
matplotlib.rcParams['font.size'] = 20
a = np.arange(0.0,5.0,0.02)
plt.ylabel('纵轴:振幅')
plt.xlabel('横轴:时间')
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()
#第二种方法，可以指定改变字体
# 即在中文输出的地方添加fontproperties




a = np.arange(0.0,5.0,0.02)
plt.ylabel('纵轴:振幅',fontproperties="Kaiti",fontsize=15,color='green')
plt.xlabel('横轴:时间',fontproperties="Kaiti",fontsize=15)
plt.plot(a,np.cos(2*np.pi*a),'r--')
# latex   $符号引入latext文法
plt.title(r'正弦实例波 $y = cos(2\pi x)$',fontproperties="Kaiti",fontsize=25)
plt.text(2,1,r'$\mu=100$',fontsize = 15)
plt.axis([-1,6,-2,2])
plt.grid(True)   # 画布为网格
plt.show()




# ======= pyplot子图绘制方法 =======
# 3x3的九块区域，当前选定区域为(1,0)，在列的方向上延申2
plt.subplot2grid((3,3),(1,0),colspan=3)
a = np.array([1,2,3,4,5])
plt.plot(a,'r--')
plt.show()
#也可以使用GridSpec类实现
gs = gridspec.GridSpec(3,3)    # 分成3x3的四个区间
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:-1])
ax3 = plt.subplot(gs[1:,-1])
ax4 = plt.subplot(gs[2,0])
ax5 = plt.subplot(gs[2,1])










