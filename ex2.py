import numpy as np
import matplotlib.pyplot as plt

# normal scrypt
deg = range(0, 360)
rad = []
for theata in deg:
    rad.append(theata/180.0 * np.pi)

# using list comprehension
rad2 = [ theata / 180.0 * np.pi for theata in deg ]