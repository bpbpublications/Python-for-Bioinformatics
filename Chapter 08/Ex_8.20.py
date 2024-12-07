import matplotlib.pyplot as plt
# Prepare data
Dinucleotide = ['AT', 'GC', 'AA']
Count = [10, 15, 12]
# Create a figure and axes
fig, ax = plt.subplots()
# Plot the horizontal bar chart
ax.barh(Dinucleotide, Count)
# Customize the plot
ax.set_xlabel('Count')
ax.set_ylabel('Dinucleotide')
ax.set_title('Bar Plot')
# Display the plot
plt.show()
