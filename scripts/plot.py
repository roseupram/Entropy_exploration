import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
import matplotlib.cm as cm
from itertools import cycle

def plot_path(x,y,fig_name='path.svg'):
    linewidth=3
    distances = np.sqrt(np.diff(x)**2 + np.diff(y)**2)  # 计算相邻点的距离
    total_distance = np.cumsum(distances)  # 路径的累计距离
    total_distance = np.insert(total_distance, 0, 0)  # 将第一个点的距离设为 0

    # 归一化处理，将路径的累计距离映射到 [0, 1] 范围
    norm = Normalize(vmin=total_distance.min(), vmax=total_distance.max())

    # 创建一个 LineCollection 来绘制渐变路径
    segments = [[(x[i], y[i]), (x[i+1], y[i+1])] for i in range(len(x)-1)]
    lc = LineCollection(segments, cmap=plt.cm.rainbow.reversed(), norm=norm, linewidth=linewidth)

    # 为每个线段设置颜色
    lc.set_array(total_distance[1:])  # 只传递每个段的累计距离，生成渐变效果

    # 创建图形和坐标轴
    fig, ax = plt.subplots()
    ax.add_collection(lc)

    # 设置坐标轴范围
    ax.set_xlim(min(x)-1, max(x)+1)
    ax.set_ylim(min(y)-1, max(y)+1)
    ax.axis('off')

    plt.grid(False)
    plt.savefig(fig_name,format='svg',bbox_inches='tight',pad_inches=0,transparent=True)
    # 显示图形
    plt.show()

folder='../log/best/indoor2/'
traj=pd.read_csv(folder+'dsvp-trajectory.txt',sep=' ',header=None,names=['x','y','z','r','p','yaw','time'])
x1=traj['x']
y1=traj['y']
# plot_path(x1,y1)

# exit()
methods=['dsvp','hphs','tare','ours']
color_cycle=cycle(['#af58ba','#14a2e1','#a6761d','#ff1f5b'])
linewidth=3
fontsize=18
# volumn distance runtime time
# x y z r p y time
plt.figure(figsize=(10,4))
for method in methods:
    label=method.capitalize() if method =='ours' else method.upper()
    data=pd.read_csv(folder+f'{method}-metrics.txt',sep=' ',header=None,names=['volumn','distance','runtime','time'])
    plt.plot(data['time'],data['volumn'],color=next(color_cycle),label=label,linewidth=linewidth)
# print(metric)
# plt.plot(time,distance,label='ours')
plt.xticks(fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.xlabel('Time (s)',fontsize=fontsize)
plt.ylabel(r'volumn ($m^3$)',fontsize=fontsize)
plt.legend(fontsize=fontsize)
plt.savefig('volumn-time.svg',format='svg',bbox_inches='tight',pad_inches=0)
plt.show()