import numpy as np
import matplotlib.pyplot as plt




arr = np.identity(20)*255


plt.imshow(arr, cmap='gray')
plt.show()