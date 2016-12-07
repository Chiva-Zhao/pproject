def y(v0y, t):
    g = 9.81  # Acceleration of gravity
    return v0y * t - 0.5 * g * t ** 2


def x(v0x, t):
    return v0x * t


def xy(v0x, v0y, t):
    g = 9.81  # acceleration of gravity
    return v0x * t, v0y * t - 0.5 * g


def xy(t, v0x=0, v0y=0):
    """Compute the x and y position of the ball at time t"""
    g = 9.81  # acceleration of gravity
    return v0x * t, v0y * t - 0.5 * g * t ** 2


initial_velocity_x = 2.0
initial_velocity_y = 5.0
time = 0.6  # Just pick one point in time
print(x(initial_velocity_x, time), y(initial_velocity_y, time))
time = 0.9  # ... Pick another point in time
print(x(initial_velocity_x, time), y(initial_velocity_y, time))

print(xy(initial_velocity_x, initial_velocity_y, time))
x_pos, y_pos = xy(initial_velocity_x, initial_velocity_y, time)
print(x_pos, y_pos)

print(xy(0.6))
print(xy(0.6, v0y=4.0))
print(xy(v0y=4.0, v0x=1.0, t=0.6))
