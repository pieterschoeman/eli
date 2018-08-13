import numpy as np
import matplotlib.pyplot as plt

# Details of the graph
print("Sine Wave")

# Graph options
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.title("Sine Wave\nFourier Series Approximation: Number Of Components: 1")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

t = np.linspace(-2, 2, 500, endpoint=False)

# User feedback
print("Please wait while yor graph is being generated...")

# Create the square wave (with numpy)
origional = np.sin(2*np.pi*t)
fourier = np.sin(2*np.pi*t)

plt.plot(t, origional, label='Signal')
plt.plot(t, fourier, label='Fourier Series Approximation')
plt.legend()
plt.show()
