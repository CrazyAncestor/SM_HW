import numpy as np
import matplotlib.pyplot as plt

E0 = 1
a = 1
ga = 2 * np.pi / a

# 定义势能函数
def potential_energy(kx, ky):
    return 2 * E0 - 2 * E0 * (np.cos(kx * a) + np.cos(ky * a))

# 创建网格
kx = ga * np.linspace(-0.5, 0.5, 1000)
ky = ga * np.linspace(-0.5, 0.5, 1000)
KX, KY = np.meshgrid(kx, ky)

# 计算势能值
Z = potential_energy(KX, KY)

# 绘制等能量线
plt.contour(KX / (np.pi * a), KY / (np.pi * a), Z, levels=20, cmap='Blues')
plt.colorbar(label='Energy level (E0)')
plt.title('2D Constant Energy Lines')
plt.xlabel(r'kx($\pi/a$)')
plt.ylabel(r'ky($\pi/a$)')
plt.grid()
plt.axis('equal')

# 绘制路径
path_x = [0, 1, 1]
path_y = [0, 0, 1]
plt.plot(path_x, path_y, color='red', marker='o', label='Path')

# 添加标注
plt.text(0, -0.1, r'$\Gamma$', fontsize=12, ha='center')
plt.text(1, -0.1, r'M', fontsize=12, ha='center')
plt.text(1, 1.1, r'W', fontsize=12, ha='center')

plt.legend()

# 显示图形
plt.show()

# 计算路径上的能量
k_values = []
energy_values = []

# 从 (0,0) 到 (ga/2,0)
for kx in np.linspace(0, ga / 2, 100):
    energy = potential_energy(kx, 0)
    k_values.append(kx)
    energy_values.append(energy)

kxf = k_values[-1]
# 从 (ga/2,0) 到 (ga/2,ga/2)
for ky in np.linspace(0, ga / 2, 100):
    energy = potential_energy(ga / 2, ky)
    k_values.append(kxf + ky)
    energy_values.append(energy)

# 绘制 k vs. Energy plot
plt.figure()
plt.plot(np.array(k_values) / (np.pi * a), energy_values, marker='o', color='blue')
plt.title('k vs. Energy Plot')
plt.xlabel(r'Path k($\pi/a$)')
plt.ylabel('Energy (E0)')
plt.grid()

# 添加标注和垂直线
plt.axvline(x=0, color='gray', linestyle='--')
plt.axvline(x=1, color='gray', linestyle='--')
plt.axvline(x=2, color='gray', linestyle='--')

plt.text(0, max(energy_values) * 0.9, r'$\Gamma$', fontsize=12, ha='center')
plt.text(1, max(energy_values) * 0.9, r'M', fontsize=12, ha='center')
plt.text(2, max(energy_values) * 0.9, r'W', fontsize=12, ha='center')

plt.show()
