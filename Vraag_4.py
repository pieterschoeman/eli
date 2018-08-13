from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# Details of the graph
print("Sawtooth Wave")

# The expansion
expansion = int(input("Input your expansion (any integer number): "))
sa_signal = [0]*expansion

# Input options
sample = int(input("Input your sample (any integer number eg. 500): "))
size = float(input("Input graph size x -> 0 to +x (any float number eg. 3): "))
sa_fourier = [0]*sample
t = np.linspace(-size, size, sample, endpoint=False)

# Graph options
plt.xlim(0, size)
plt.ylim(0, 2)
plt.title("Sawtooth Wave\nFourier Series Approximation: Number Of Components: "+str(expansion))
plt.xlabel("Time")
plt.ylabel("Amplitude")

# User feedback
print("Please wait while yor graph is being generated...")

# Create the square wave (with scipy)
sawtooth = signal.sawtooth(2*np.pi*t)
for a in range(0, len(sawtooth)-1):
    sawtooth[a] = 0.5*(sawtooth[a]+1)

for a in range(1, len(sa_signal)):
    sa_signal[a-1] = (1j)/(2*np.pi*a)*(np.power(np.e, (1j*a*2*np.pi*t)))+(1j)/(2*np.pi*(-a))*(np.power(np.e, (1j*(-a)*2*np.pi*t)))

for a in range(0, len(sa_signal)-1):
    for b in range(0, len(sa_fourier)-1):
        sa_fourier[b] = sa_fourier[b]+sa_signal[a][b]

plt.plot(t, sawtooth, label="Signal")
plt.plot(t, np.real(sa_fourier)+0.5, label='Fourier Series Approximation')
plt.legend()
plt.show()
