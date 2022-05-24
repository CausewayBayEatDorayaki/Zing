# 10 0.40
# 20 0.59
# 30 0.70
# 40 0.78
# 80 0.95

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import make_interp_spline


def smooth_xy(lx, ly):
    """数据平滑处理
    :param lx: x轴数据，数组
    :param ly: y轴数据，数组
    :return: 平滑后的x、y轴数据，数组 [slx, sly]
    """
    x = np.array(lx)
    y = np.array(ly)
    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = make_interp_spline(x, y)(x_smooth)
    return [x_smooth, y_smooth]


def compression_rate():
    # plt.title("double number", fontsize=24)
    plt.xlabel("BMC DEPTH", fontsize=30)
    plt.ylabel("COMPRESSION RATE(%)", fontsize=30)

    x = [0,   10, 20, 40, 60, 80, 100, 200, 500, 1000]
    y = [100, 59, 44, 29, 25, 23,  21,   19,   17.6,   17]
    xy = smooth_xy(x, y)
    # plt.scatter(x, y, s=20) #s为点的大小
    plt.plot(x, y, linestyle='solid', linewidth=1, marker='.', markersize=15, label='RBPS')
    plt.tick_params(labelsize=30)  # 调整坐标轴数字大小
    plt.legend(prop={'size': 30})  # plt.legend( prop = {'size':17})   图例字体大小
    # plt.legend()
    plt.show()


def node_number():
    # plt.title("double number", fontsize=24)
    plt.xlabel("BMC DEPTH", fontsize=30)
    plt.ylabel("NODES", fontsize=30)

    x = [0, 10, 20, 40, 60, 80,     100, 200, 500, 1000]
    y = [0, 22, 48, 68, 88, 108,    128, 228, 528, 1028]  # RBPS
    z = [0, 37, 109, 229, 349, 469, 589, 1189, 2989, 5989]  # BMC

    # x = [0, 10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
    # y = [0, 22, 44, 80, 118, 117, 157, 228, 192, 2079, 2079, 2079]  # RBPS
    # z = [0, 37, 109, 372, 808, 1237, 1914, 2766, 3652, 89553, 111693, 133833]  # BMC

    # x = [0, 10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
    # y = [0, 22, 44, 80, 118, 117, 157, 228, 192, 2079, 2079, 2079]  # RBPS
    # z = [0, 37, 109, 372, 808, 1237, 1914, 2766, 3652, 89553, 111693, 133833]  # BMC

    # xy = smooth_xy(x, y)
    # plt.scatter(x, y, s=20) #s为点的大小

    plt.plot(x, y, linestyle='solid', linewidth=1, marker='.', markersize=15, label='RBPS')
    plt.plot(x, z, linestyle='--', linewidth=1, marker='.', markersize=15, label='BMC')
    plt.tick_params(labelsize=30)  # 调整坐标轴数字大小
    plt.legend(prop={'size': 30})
    plt.show()


if __name__ == '__main__':
    #compression_rate()
    node_number()
