import numpy as np
import plotly.express as px

# basic parameters
L = 2.5 # wheelbase (m)
v = 5 # speed (m/s)
delta = 0.17 # steering angle (radians)
dt = 0.01 # timestep (s)
total_sim_time = 60

steps = int(total_sim_time / dt)

x = [0]
y = [0]
psi = [0]

n = 0

for n in range(steps):
    x.append(x[n] + v * np.cos(psi[n]) * dt)
    y.append(y[n] + v * np.sin(psi[n]) * dt)
    psi.append(psi[n] + (v / L) * np.tan(delta) * dt)

print("x values:")
print(x[:10])
print("y values:")
print(y[:10])
print("psi values:")
print(psi[:10])
print("Final position: x = {:.2f}, y = {:.2f}, psi = {:.2f}".format(x[-1], y[-1], psi[-1]))

fig = px.line(x=x, y=y)
fig.update_layout(template="plotly_white")
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.show()

# actual radius
R = L / np.tan(delta)
print(f"Turning radius: R = {R:.2f} m")

# estimated radius from simulation
distance_travelled = 0

for n in range(len(x) - 1):
    dx = x[n + 1] - x[n]
    dy = y[n + 1] - y[n]
    distance_travelled += np.sqrt(dx**2 + dy**2)

estimated_R = distance_travelled / (psi[-1] - psi[0])
print(f"Estimated turning radius from simulation: R = {estimated_R:.2f} m")