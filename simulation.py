import numpy as np
import plotly.express as px

# basic parameters
L = 2.5 # wheelbase (m)
v = 5 # speed (m/s)
def steering_input(t):
    # steering angle (rad)
    if t < 2:
        return 0.0
    elif t < 5:
        return np.deg2rad(10)
    else:
        return 0.0
dt = 0.01 # timestep (s)
total_sim_time = 60

def simulate(L, v, steering_input, dt, total_sim_time):
    x = [0]
    y = [0]
    psi = [0]

    steps = int(total_sim_time / dt)

    for n in range(steps):
        t = n * dt
        steering_angle = steering_input(t)

        x.append(x[n] + v * np.cos(psi[n]) * dt)
        y.append(y[n] + v * np.sin(psi[n]) * dt)
        psi.append(psi[n] + (v / L) * np.tan(steering_angle) * dt)

    times = [n * dt for n in range(len(x))]

    return x, y, psi, times

x, y, psi, times = simulate(L, v, steering_input, dt, total_sim_time)

print("x values:")
print(x[:10])
print("y values:")
print(y[:10])
print("psi values:")
print(psi[:10])
print(f"Final position: x = {x[-1]:.2f}, y = {y[-1]:.2f}, psi = {psi[-1]:.2f}")

# plot 1: vehicle trajectory
fig1 = px.line(x=x, y=y, title="Vehicle trajectory")
fig1.update_yaxes(scaleanchor="x", scaleratio=1)
fig1.update_layout(template="plotly_white")
fig1.show()

# plot 2: steering angle over time
steering = [steering_input(t) for t in times]

fig2 = px.line(x=times, y=steering, title="Steering angle over time", labels={"x": "Time (s)", "y": "Steering angle (rad)"})
fig2.update_layout(template="plotly_white")
fig2.show()