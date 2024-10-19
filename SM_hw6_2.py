import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定義參數
Ep = 4
Ed = 0
tpd = 1.6
a = 1
ga = 2 * np.pi / a

# 定義 b
b = - (Ep + Ed)  # 可以根據需要調整
kx = ga * np.linspace(-0.5, 0.5, 100)  # 減少點數以提高繪圖效能
ky = ga * np.linspace(-0.5, 0.5, 100)

# 定義 c(kx, ky) 函數
def c(kx, ky):
    return Ep * Ed - 4 * tpd**2 * (np.cos(kx * a / 2)**2 + np.cos(ky * a / 2)**2)

# 計算 c 的值
C = c(kx[:, np.newaxis], ky[np.newaxis, :])

# 計算二次方程的根
with np.errstate(invalid='ignore'):
    x1 = (-b + np.sqrt(b**2 - 4 * C)) / 2
    x2 = (-b - np.sqrt(b**2 - 4 * C)) / 2

# 繪製 3D 圖形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 繪製根 x1 的 3D 曲面
KX, KY = np.meshgrid(kx, ky)
ax.plot_surface(KX/np.pi*a, KY/np.pi*a, x1, cmap='Blues', alpha=0.6)

# 繪製根 x2 的 3D 曲面
ax.plot_surface(KX/np.pi*a, KY/np.pi*a, x2, cmap='Reds', alpha=0.6)

# 繪製平面 x3 = Ep
X_plane, Y_plane = np.meshgrid(kx, ky)
Z_plane = np.full(X_plane.shape, Ep)  # 創建一個常數平面
ax.plot_surface(X_plane/np.pi*a, Y_plane/np.pi*a, Z_plane, color='green', alpha=0.3)

# 添加標註
ax.text(0, 0, np.max(x1) * 0.9, '3rd band', color='blue', fontsize=12, ha='center')
ax.text(0, 0, np.min(x2) * 1.1, '1st band', color='red', fontsize=12, ha='center')
ax.text(0, 0, Ep + 0.2, '2nd band)', color='green', fontsize=12, ha='center')

ax.set_title('CuO2 band structure')
ax.set_xlabel(r'kx($\pi/a$)')
ax.set_ylabel(r'ky($\pi/a$)')
ax.set_zlabel('Energy (eV)')

plt.show()
