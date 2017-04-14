import numpy as np
import matplotlib.pyplot as plt
score = np.random.randn(10000)*10+50

## normal script
count = 0
for point in score:
    if int(point)+1 > 72: count += 1
print count

## using numpy 
print len(np.where(score > 72)[0])