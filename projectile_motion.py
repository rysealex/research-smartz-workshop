import numpy as np
import matplotlib.pyplot as plt

def projectile_midpoint(B, angle_rad, v0, m, x0, y0, dt, t_final=100):
    g = 9.81
    # Initialize arrays
    num_steps = int(t_final / dt)
    t = np.linspace(0, t_final, num_steps)
    
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)
    vx = np.zeros(num_steps)
    vy = np.zeros(num_steps)
    
    # Initial conditions
    x[0], y[0] = x0, y0
    vx[0] = v0 * np.cos(angle_rad)
    vy[0] = v0 * np.sin(angle_rad)
    
    for i in range(num_steps - 1):
        # Current velocities
        v_total = np.sqrt(vx[i]**2 + vy[i]**2)
        
        # Midpoint step (RK2 approximation)
        # 1. Calculate accelerations at start
        ax = -(B/m) * v_total * vx[i]
        ay = -g - (B/m) * v_total * vy[i]
        
        # 2. Predict state at half-step
        v_mid_x = vx[i] + ax * (dt/2)
        v_mid_y = vy[i] + ay * (dt/2)
        v_mid_total = np.sqrt(v_mid_x**2 + v_mid_y**2)
        
        # 3. Calculate acceleration at midpoint
        ax_mid = -(B/m) * v_mid_total * v_mid_x
        ay_mid = -g - (B/m) * v_mid_total * v_mid_y
        
        # 4. Update full step
        vx[i+1] = vx[i] + ax_mid * dt
        vy[i+1] = vy[i] + ay_mid * dt
        x[i+1] = x[i] + v_mid_x * dt
        y[i+1] = y[i] + v_mid_y * dt
        
        # Stop if projectile hits the ground
        if y[i+1] < 0:
            return x[:i+2], y[:i+2]
            
    return x, y

# --- Parameters ---
B = 1.0 # Drag constant
m = 1.0 # Mass (kg)
v0_list = [5, 6, 7, 8, 9, 10] # Launch speeds (m/s)
y0 = 0.01 # Launch height (m)
x0 = 0 # Launch location (m)
dt = 0.01 # Time step size (s)
launcha = np.array([30, 35, 40, 45, 50, 55]) # Array of different launch angles (degrees)
D = np.radians(launcha) # Conversion of launch angles to radians

plt.figure(figsize=(10, 6))

# Loop and plot
for i in range(len(v0_list)):
    px, py = projectile_midpoint(B, D[0], v0_list[i], m, x0, y0, dt)
    plt.plot(px, py, label=f'Speed: {v0_list[i]} m/s')

# --- Formatting ---
plt.title('Projectile Motion: Different Launch Speeds w/ Drag')
plt.suptitle(f'B = {B}', fontsize=10)
plt.xlabel('Position (m)')
plt.ylabel('Height (m)')
plt.xlim(0, 2)
plt.ylim(0, 0.5)
plt.legend()
plt.grid(True)
plt.show()