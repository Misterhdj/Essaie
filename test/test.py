import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Creating vectors X and Y
x = np.linspace(-20, 20, 1000)
y = x ** 2
 
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(x, y)
 
# Show the plot
plt.show()
