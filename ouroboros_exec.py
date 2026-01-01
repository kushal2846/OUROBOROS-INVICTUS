import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

# Set the backend for matplotlib to 'Agg' to prevent display and save to file
matplotlib.use('Agg')

# Generate data for a complex 3D spiral
# Use a high number of points for smoothness
n_points = 2000
theta = np.linspace(-4 * np.pi, 4 * np.pi, n_points)

# Define a more complex radius and z-component
# Radius varies sinusoidally to create a varying thickness/amplitude
r_base = 1.5
r_mod = 0.5 * np.sin(2 * theta)
r = r_base + r_mod

# x and y coordinates of the spiral
x = r * np.cos(theta)
y = r * np.sin(theta)

# z coordinate, also with a sinusoidal modulation for added complexity
z_base = theta * 0.5
z_mod = 1.0 * np.cos(3 * theta)
z = z_base + z_mod

# Create a figure and a 3D subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Map a scalar array (e.g., theta values) to colors using the 'cool' colormap
# We'll use the 'theta' values to color the spiral
colors = cm.cool(theta / theta.max())

# Plot the 3D spiral.
# The `color` parameter in plot_surface or plot depends on the type of plot.
# For plot, we can pass a list of colors (one for each segment) or use a colormap on a scatter plot.
# To plot as a continuous line with varying color, we can iterate through segments.
# A more efficient way is to use scatter with the C parameter or LineCollection.
# For simplicity with plot, we can just map the entire line to a single color,
# or for a more 'gradient' look, use a scatter plot.
# Let's use a scatter plot for clear colormapping based on Z or theta.
ax.scatter(x, y, z, c=theta, cmap='cool', marker='o', s=10, alpha=0.7)

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Complex 3D Spiral with \'cool\' Colormap')

# Add a color bar
cbar = fig.colorbar(ax.collections[0], ax=ax, pad=0.1)
cbar.set_label('Spiral Progression (Theta)')

# Save the plot to 'plot.png'
plt.savefig('plot.png')

# Print a confirmation message to stdout
print("Complex 3D spiral plot saved to plot.png")