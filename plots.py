import numpy as np
import matplotlib.pyplot as plt

def projectile_midpoint(B, D, v0, m, x0, y0, dt):
    g = 9.81
    
    # initial velocities based on launch angle D
    vx0 = v0 * np.cos(D)
    vy0 = v0 * np.sin(D)
    
    # creating lists to store trajectory data
    x, y = [x0], [y0]
    vx, vy = [vx0], [vy0]
    
    i = 0
    # loop until the projectile hits the ground 
    while y[i] >= 0:
        v_current = np.sqrt(vx[i]**2 + vy[i]**2)
        
        # calculate Midpoint Velocities 
        vxm = vx[i] - 0.5 * dt * ((B/m) * v_current * vx[i])
        vym = vy[i] - 0.5 * dt * g - 0.5 * dt * ((B/m) * v_current * vy[i])
        
        # calculate full step velocities
        new_vx = vx[i] - dt * ((B/m) * v_current * vxm)
        new_vy = vy[i] - dt * g - dt * ((B/m) * v_current * vym)
        
        # update positions using midpoint velocities 
        new_x = x[i] + vxm * dt
        new_y = y[i] + vym * dt
        
        # append results to the list
        vx.append(new_vx)
        vy.append(new_vy)
        x.append(new_x)
        y.append(new_y)
        
        i += 1
        if i > 1e5: break # safety break to prevent infinite loops in case of errors. 
        # breaks the loop if i > 100,000 times

    return np.array(x), np.array(y)

# simulation parameters
m = 1.0           # mass (kg)
dt = 0.01         # time step (s)
v0_list = [5, 6, 7, 8, 9, 10]
angles = [30, 35, 40, 45, 50, 55]

# creating a figure with 4 subplots to show the different scenarios`` 
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# 1. different launch angles with no drag (B=0)
for a in angles:
    x_p, y_p = projectile_midpoint(0, np.radians(a), 10, m, 0, 0, dt)
    axs[0, 0].plot(x_p, y_p, label=f'{a}°')
axs[0, 0].set_title("Projectile Motion: Different Launch Angles")
axs[0, 0].set_xlabel("Position (m)")
axs[0, 0].set_ylabel("Height (m)")
axs[0, 0].legend()

# 2. different launch speeds with no drag (B=0)
for v in v0_list:
    x_p, y_p = projectile_midpoint(0, np.radians(30), v, m, 0, 0, dt)
    axs[0, 1].plot(x_p, y_p, label=f'{v} m/s')
axs[0, 1].set_title("Projectile Motion: Different Launch Speeds")
axs[0, 1].set_xlabel("Position (m)")
axs[0, 1].set_ylabel("Height (m)")
axs[0, 1].legend()

# 3. different launch angles with drag (B=0.1)
B_low = 0.1
for a in angles:
    x_p, y_p = projectile_midpoint(B_low, np.radians(a), 10, m, 0, 0, dt)
    axs[1, 0].plot(x_p, y_p, label=f'{a}°')
axs[1, 0].set_title(f"Different Launch Angles w/ Drag")
axs[1, 0].set_xlabel("Position (m)")
axs[1, 0].set_ylabel("Height (m)")
axs[1, 0].legend()

# 4. different launch speeds with drag (B=1.0)
B_high = 1.0
for v in v0_list:
    x_p, y_p = projectile_midpoint(B_high, np.radians(45), v, m, 0, 0.01, dt)
    axs[1, 1].plot(x_p, y_p, label=f'{v} m/s')
axs[1, 1].set_title(f"Different Launch Speeds w/ Drag")
axs[1, 1].set_xlabel("Position (m)")
axs[1, 1].set_ylabel("Height (m)")
axs[1, 1].legend()

for ax in axs.flat:
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_ylim(bottom=0)

plt.show()