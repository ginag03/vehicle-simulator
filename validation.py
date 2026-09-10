from simulation import simulate
import numpy as np

# basic parameters
L = 2.5 # wheelbase (m)
v = 5 # speed (m/s)
def constant_delta(t):
    # steering angle (rad)
    return np.deg2rad(10)  # constant steering angle of 10 degrees

dt = 0.01 # timestep (s)
total_sim_time = 60

x, y, psi = simulate(L, v, constant_delta, dt, total_sim_time)

# actual radius
R = L / np.tan(constant_delta(0))
print(f"Turning radius: R = {R:.2f} m")

# estimated radius from simulation
distance_travelled = 0

for n in range(len(x) - 1):
    dx = x[n + 1] - x[n]
    dy = y[n + 1] - y[n]
    distance_travelled += np.sqrt(dx**2 + dy**2)

estimated_R = distance_travelled / (psi[-1] - psi[0])
print(f"Estimated turning radius from simulation: R = {estimated_R:.2f} m")