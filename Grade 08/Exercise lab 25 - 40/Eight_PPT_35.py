"""
Ex 35.

Create an array with the letters "A" through "D". Make this the X values. Now create a array with 4 random numbers and make it the Y values. Create a corresponding bar graph with these X and Y values.
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.array(["A", "B", "C", "D"])
Y = np.array([12, 3, 15, 6])

plt.bar(X, Y)