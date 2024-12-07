from plotnine import *
import pandas as pd

data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 1, 3, 5]
})

#Create a plot object by specifying the data and aesthetic mappings using ggplot():
#ggplot() initializes the plot and defines the aesthetics (how the data maps to visual properties).
#geom_point() adds the layer for creating a scatter plot.
#labs() sets the plot title and axis labels.

gg = (
    ggplot(data, aes(x='x', y='y')) +
    geom_point() +
    labs(title="Scatter Plot Example", x="X-axis", y="Y-axis")
)
#To display the plot, simply print the gg object:
print(gg)
