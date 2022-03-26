import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm



x = np.arange(-3, 3, 0.001)

plt.plot(x, norm.pdf(x))
plt.title("Normal / Gaussian Distribution")
plt.show()
