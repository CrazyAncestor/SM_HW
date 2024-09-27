import numpy as np
import matplotlib.pyplot as plt

#  Define potential function
def U1(x,a,V):
    return -8*V*np.cos(np.pi * x/a) -6*V*np.cos(2 * np.pi * x/a)
def U2(x,a,V):
    return -8*V*np.cos(2 * np.pi * x/a) -6*V*np.cos(8 * np.pi * x/a)
def U3(x,a,V):
    return -8*V*np.cos(3 * np.pi * x/a) -6*V*np.cos(5 * np.pi * x/a)
def U4(x,a,V):
    return -8*V*np.cos(4 * np.pi * x/a) -6*V*np.cos(6 * np.pi * x/a)

# Define the period
a = 1  # You can change this to any value
V = 1

# Create an array of x values
x = np.linspace(0, 4 * a, 1000)  # Plotting over multiple periods

# Calculate the corresponding y values for sine and cosine
POT1 = U1(x,a,V)
POT2 = U2(x,a,V)
POT3 = U3(x,a,V)
POT4 = U4(x,a,V)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, POT1, label='U1(x)', color='blue')
plt.plot(x, POT2, label='U2(x)', color='orange')
plt.plot(x, POT3, label='U3(x)', color='red')
plt.plot(x, POT4, label='U4(x)', color='green')

# Customize the plot
plt.title('Periodic Functions with Period a')
plt.xlabel('x')  # Use 'a' in x label
plt.ylabel('Potential (V)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# Set x-ticks in terms of 'a'
x_ticks = np.arange(0, 5 * a + 1, a)
plt.xticks(x_ticks, [f'{int(t/a)}a' for t in x_ticks])  # Format ticks as multiples of 'a'

#plt.yticks(np.arange(-1, 2, 0.5))
plt.grid()
plt.legend()
plt.xlim(0, 4 * a)
#plt.ylim(-1.5, 1.5)

# Show the plot
plt.show()
