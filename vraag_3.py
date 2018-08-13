from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# Details of the graph
print("Square Wave 10% Duty Cycle")

# The expansion
expansion = int(input("Input your expansion (any integer number eg. 5): "))
sq_signal = [0]*expansion

# Input options
sample = int(input("Input your sample (any integer number eg. 500): "))
size = float(input("Input graph size x -> -x to +x (any float number eg. 3): "))
sq_fourier = [0]*sample
t = np.linspace(-size, size, sample, endpoint=False)

# Graph options
plt.xlim(-size, size)
plt.ylim(-2, 2)
plt.title("Square Wave 10% Duty Cycle\nFourier Series Approximation: Number Of Components: "+str(expansion))
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# User feedback
print("Please wait while yor graph is being generated...")

# Create the square wave (with scipy)
square = signal.square(20*np.pi*t)

for a in range(1, len(sq_signal)):
    sq_signal[a-1] = ((2*(1-np.cos(a*np.pi)))/(a*np.pi))*np.sin(a*20*np.pi*t)

for a in range(0, len(sq_signal)-1):
    for b in range(0, len(sq_fourier)-1):
        sq_fourier[b] = sq_fourier[b]+sq_signal[a][b]

plt.plot(t, square, label='Signal')
plt.plot(t, sq_fourier, label='Fourier Series Approximation')
plt.legend()
plt.show()
