import numpy as np
import matplotlib.pyplot as plt

def projectile_euler(B, D, v0, m, x0, y0, dt):
    """Simulates projectile motion using the Euler Method."""
    g = 9.81
    vx, vy = v0 * np.cos(D), v0 * np.sin(D)
    x_list, y_list = [x0], [y0]
    
    i = 0
    while y_list[i] >= 0:
        v_curr = np.sqrt(vx**2 + vy**2)
        
        # current velocity determines next position
        new_x = x_list[i] + vx * dt
        new_y = y_list[i] + vy * dt
        
        # current forces determine next velocity
        vx = vx - dt * ((B/m) * v_curr * vx)
        vy = vy - dt * g - dt * ((B/m) * v_curr * vy)
        
        x_list.append(new_x)
        y_list.append(new_y)
        i += 1
    return np.array(x_list), np.array(y_list)

def projectile_midpoint(B, D, v0, m, x0, y0, dt):

    # it simulates projectile motion using the RK2 Midpoint Method
    g = 9.81
    vx, vy = v0 * np.cos(D), v0 * np.sin(D)
    x_list, y_list = [x0], [y0]
    
    i = 0
    while y_list[i] >= 0:
        v_curr = np.sqrt(vx**2 + vy**2)
        
        # 1. half-step velocities
        vxm = vx - 0.5 * dt * ((B/m) * v_curr * vx)
        vym = vy - 0.5 * dt * g - 0.5 * dt * ((B/m) * v_curr * vy)
        
        # 2. update position and velocity using the midpoint values
        new_x = x_list[i] + vxm * dt
        new_y = y_list[i] + vym * dt
        vx = vx - dt * ((B/m) * v_curr * vxm)
        vy = vy - dt * g - dt * ((B/m) * v_curr * vym)
        
        x_list.append(new_x)
        y_list.append(new_y)
        i += 1
    return np.array(x_list), np.array(y_list)


# parameters for the Figure 1, comparing difference between Euler and Midpoint methods
v0 = 10 
angle = np.radians(60) 
B = 0.0
m = 1.0
dt = 0.1

# calculate trajectories for both methods
x_e, y_e = projectile_euler(B, angle, v0, m, 0, 0, dt)
x_m, y_m = projectile_midpoint(B, angle, v0, m, 0, 0, dt)

# calculate exact values
t_max = (2 * v0 * np.sin(angle)) / 9.81
t_exact = np.linspace(0, t_max, 100)
x_exact = v0 * np.cos(angle) * t_exact
y_exact = v0 * np.sin(angle) * t_exact - 0.5 * 9.81 * t_exact**2

# plotting to compare the methods
plt.figure(figsize=(9, 6))

# plotting for Euler 
plt.plot(x_e, y_e, 'o--', color='gray', markerfacecolor='none', label='Euler')

# plotting for Midpoint
plt.plot(x_m, y_m, 's-', color='black', markerfacecolor='none', markersize=4, label='Midpoint')

# plotting for exact solution
plt.plot(x_exact, y_exact, color='black', linewidth=1.5, label='Exact')

# formatting the plot
plt.title('Projectile Motion: Different Calculation Schemes')
plt.xlabel('Position (m)')
plt.ylabel('Height (m)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlim(0, 10)
plt.ylim(0, 5)

plt.show()