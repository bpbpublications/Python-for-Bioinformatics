import matplotlib.pyplot as plt
# Prepare data
Dinucleotide = ['AT', 'GC', 'AA']
Count = [10, 15, 12]
# Create a figure and axes
fig, ax = plt.subplots()
# Plot the bar chart for count of Dinucleotide Values
ax.bar(Dinucleotide, Count)
# Customize the plot
ax.set_xlabel('Dinucleotide')
ax.set_ylabel('Count')
ax.set_title('Bar Plot')
# Display the plot
plt.show()
