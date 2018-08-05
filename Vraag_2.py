from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

expansion = int(input("Input your expansion (any integer number): "))
sq_signal = [0]*expansion

sample = int(input("Input your sample (any integer number): "))
size = int(input("Input graph size (any integer number): "))
sq_fourier = [0]*sample
t = np.linspace(-size, size, sample, endpoint=False)

plt.xlim(-size, size)
plt.ylim(-2, 2)
plt.title("Vraag 2 / Question 2")
plt.xlabel("Tyd / Time")
plt.ylabel("Amplitude")

print("Please wait while yor graph is being generated...")

square = signal.square(2*np.pi*t)

for a in range(1, len(sq_signal)):
    sq_signal[a-1] = ((2*(1-np.cos(a*np.pi)))/(a*np.pi))*np.sin(a*2*np.pi*t)

for a in range(0, len(sq_signal)-1):
    for b in range(0, len(sq_fourier)-1):
        sq_fourier[b] = sq_fourier[b]+sq_signal[a][b]

plt.plot(t, square)
plt.plot(t, sq_fourier)
plt.show()
