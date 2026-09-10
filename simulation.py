import numpy as np
import plotly.express as px

# basic parameters
L = 2.5 # wheelbase (m)
v = 5 # speed (m/s)
def delta(t):
    # steering angle (rad)
    if t < 2:
        return 0
    else:
        return 0.17
dt = 0.01 # timestep (s)
total_sim_time = 60

def simulate(L, v, delta, dt, total_sim_time):
    x = [0]
    y = [0]
    psi = [0]

    steps = int(total_sim_time / dt)

    for n in range(steps):
        t = n * dt
        steering_angle = delta(t)

        x.append(x[n] + v * np.cos(psi[n]) * dt)
        y.append(y[n] + v * np.sin(psi[n]) * dt)
        psi.append(psi[n] + (v / L) * np.tan(steering_angle) * dt)

    return x, y, psi

x, y, psi = simulate(L, v, delta, dt, total_sim_time)

print("x values:")
print(x[:10])
print("y values:")
print(y[:10])
print("psi values:")
print(psi[:10])
print(f"Final position: x = {x[-1]:.2f}, y = {y[-1]:.2f}, psi = {psi[-1]:.2f}")

fig = px.line(x=x, y=y)
fig.update_layout(template="plotly_white")
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.show()