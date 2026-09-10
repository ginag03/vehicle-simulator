from simulation import simulate
import numpy as np
import plotly.express as px

# basic parameters
L = 2.5 # wheelbase (m)
v = 5 # speed (m/s)
dt = 0.01 # timestep (s)
total_sim_time = 60

#  test 1: constant steering gives the expected turning radius
def constant_delta(_t):
    # steering angle (rad)
    return np.deg2rad(10)  # constant steering angle of 10 degrees

def test_turning_radius():
    # check if the turning radius is correct
    x, y, psi = simulate(L, v, constant_delta, dt, total_sim_time)

    R = L / np.tan(constant_delta(0))

    distance_travelled = 0
    for n in range(len(x) - 1):
        dx = x[n + 1] - x[n]
        dy = y[n + 1] - y[n]
        distance_travelled += np.sqrt(dx**2 + dy**2)

    estimated_R = distance_travelled / (psi[-1] - psi[0])

    error = abs(R - estimated_R)

    assert error < 0.1, (
        f"Turning radius error too large: {error:.4f} m"
    )

    print(f"TEST PASSED: The estimated turning radius is within acceptable error bounds.\nerror = {error:.4f}")

# test 2: straight line motion gives y and psi close to zero, and x close to v * total_sim_time
def zero_delta(_t):
    # steering angle (rad)
    return 0.0  # no steering

def test_straight_line_motion():
    # check if y and psi remain close to zero
    x, y, psi = simulate(L, v, zero_delta, dt, total_sim_time)

    max_y_error = np.max(np.abs(y))
    max_psi_error = np.max(np.abs(psi))

    expected_x = v * total_sim_time
    x_error = abs(x[-1] - expected_x)

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

def plot_trajectory(x, y, title):
    fig = px.line(x=x, y=y, title=title)
    fig.update_layout(template="plotly_white")
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig.show()

test_turning_radius()
test_straight_line_motion()