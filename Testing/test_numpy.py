import numpy as np
import matplotlib.pyplot as plt

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['Wawati TC']  # 設置為娃娃體
plt.rcParams['axes.unicode_minus'] = False  # 防止負號顯示異常

# 生成愛心形狀的數據
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# 創建圖表
plt.figure(figsize=(6, 6))
plt.fill(x, y, color="red")  # 填充為紅色
plt.axis("equal")  # 確保比例一致
plt.axis("off")    # 隱藏坐標軸
plt.title("誓死效忠可琦安", fontsize=16)

# 顯示圖表
plt.show()