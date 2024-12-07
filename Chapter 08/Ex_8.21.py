import matplotlib.pyplot as plt
# Prepare data
data_x_axis = [10, 20, 30, 40, 50]
data_y_axis = [20, 40, 60, 80, 100]
# Create a figure and axes
fig, ax = plt.subplots()
# Plot the scatter plot
ax.scatter(data_x_axis, data_y_axis)
# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Scatter Plot')
# Display the plot
plt.show()
