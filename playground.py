import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation

import time


arr = np.identity(50)*255


while True:
    plt.imshow(arr, cmap='gray')
    plt.show()
    # time.sleep(0.5)
    arr = ((arr==0)*255)
    plt.cla()