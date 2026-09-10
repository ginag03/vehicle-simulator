from simulation import simulate
import numpy as np

# basic parameters
L = 2.5 # wheelbase (m)
v = 5 # speed (m/s)
dt = 0.01 # timestep (s)
total_sim_time = 60

#  test 1: correct turning radius
def constant_delta(_t):
    # steering angle (rad)
    return np.deg2rad(10)  # constant steering angle of 10 degrees

x1, y1, psi1 = simulate(L, v, constant_delta, dt, total_sim_time)

# actual radius
R = L / np.tan(constant_delta(0))
print(f"Turning radius: R = {R:.2f} m")

# estimated radius from simulation
distance_travelled = 0

for n in range(len(x1) - 1):
    dx = x1[n + 1] - x1[n]
    dy = y1[n + 1] - y1[n]
    distance_travelled += np.sqrt(dx**2 + dy**2)

estimated_R = distance_travelled / (psi1[-1] - psi1[0])
print(f"Estimated turning radius from simulation: R = {estimated_R:.2f} m")

error = abs(R - estimated_R)

assert error < 0.1, (
    f"Turning radius error too large: {error:.4f} m"
)

print(f"TEST PASSED: The estimated turning radius is within acceptable error bounds.\nerror = {error:.4f}")

# test 2: straight line motion
def zero_delta(_t):
    # steering angle (rad)
    return 0.0  # no steering

x2, y2, psi2 = simulate(L, v, zero_delta, dt, total_sim_time)

max_y_error = np.max(np.abs(y2))
max_psi_error = np.max(np.abs(psi2))

expected_x = v * total_sim_time
x_error = abs(x2[-1] - expected_x)

tolerance = 1e-10

assert max_y_error < tolerance, (
    f"Straight line motion error too large in y: {max_y_error:.4f}"
)

assert max_psi_error < tolerance, (
    f"Straight line motion error too large in psi: {max_psi_error:.4f}"
)

assert x_error < tolerance, (
    f"Straight line motion error too large in x: {x_error:.4f}"
)

print(f"TEST PASSED: Straight line motion is within acceptable error bounds.\nmax_y_error = {max_y_error:.4e}, max_psi_error = {max_psi_error:.4e}, x_error = {x_error:.4e}")