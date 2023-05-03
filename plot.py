import matplotlib.pyplot as plt
from matplotlib.patches import Circle

player_radius = 0.525

x_right = [5, 5]
y_right = [-34, -5]

x_left = [-5, -5]
y_left = [-34, -5]

shooter_pos = [0, -6]
player_pos = [-8, -37]

fig, ax = plt.subplots(figsize=(8, 8))

ax.add_patch(Circle(player_pos, player_radius))

ax.plot(x_right, y_right, c='b')
ax.plot(x_left, y_left, c='b')
ax.scatter(shooter_pos[0], shooter_pos[1], c='g')
ax.plot([shooter_pos[0], player_pos[0]], [shooter_pos[1], player_pos[1]], c='r')
ax.invert_yaxis()

ax.set_xlim(-12, 12)
ax.set_ylim(0, -40)

plt.show()
