import numpy as np
import matplotlib.pyplot as plt

# constants
G = 6.6743e-11
m_sun = 1.9891e30
dt = 3600 # time step in seconds
N = int(10e5)  # number of steps

# initial conditions
x0, y0 = 1.5e11, 0
vx0_list = [0, -10e3, -20e3, -25e3]
vy0_list = [15e3, 20e3, 25e3, 30e3]
vy0_const = 29.8e3  # initial vy 

# initialize arrays 
x = np.zeros((N + 1, 4))
y = np.zeros((N + 1, 4))
vx = np.zeros((N + 1, 4))
vy = np.zeros((N + 1, 4))

# setting initial states, unlike MATLAB, index of python array = 0
x[0, :] = x0
y[0, :] = y0
vy[0, :] = vy0_const

# simulation
for j in range(4):
    vx[0, j] = vx0_list[j]

    for i in range(N):
        r = ((x[i, j] ** 2) + (y[i, j] ** 2)) ** (1/2)
        ax = -G * m_sun * x[i, j] / (r**3)
        ay = -G * m_sun * y[i, j] / (r**3)


        vx[i + 1, j] = vx[i, j] + ax*dt
        vy[i + 1, j] = vy[i, j] + ay*dt

        x[i + 1, j] = x[i, j] + vx[i + 1, j] * dt
        y[i + 1, j] = y[i, j] + vy[i + 1, j] * dt


plt.figure(figsize=(10, 8))
plt.title('Planet Motion: Varying Initial Horizontal Velocity')
plt.xlabel('Position x (m)')
plt.ylabel('Position y (m)')

for i in range(4):
    plt.plot(x[:, i], y[:, i], label=f'vx0: {vx0_list[i]} m/s')

plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()


