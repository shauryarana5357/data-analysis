import numpy as np

# --- Task 1: Weather Data Analysis (NumPy) ---

# Generate 30 random daily temperatures (°C) between 15 and 45
np.random.seed(42)
temperatures = np.random.uniform(15, 45, 30)
print("Daily Temperatures (°C):\n", temperatures)

# Statistical measures
print("\nMean      :", np.mean(temperatures))
print("Median    :", np.median(temperatures))
print("Std Dev   :", np.std(temperatures))

# Normalize between 0 and 1: (x - min) / (max - min)
norm_temps = (temperatures - temperatures.min()) / (temperatures.max() - temperatures.min())
print("\nNormalized Temperatures:\n", norm_temps)

# Reshape into 5x6 matrix (5 weeks, 6 days each)
temp_matrix = temperatures.reshape(5, 6)
print("\nTemperature Matrix (5x6):\n", temp_matrix)

# Transpose
transposed = temp_matrix.T
print("\nTransposed Matrix (6x5):\n", transposed)

# Generate a synthetic rainfall dataset of same shape
rainfall = np.random.uniform(0, 20, (5, 6))
print("\nRainfall Matrix (5x6):\n", rainfall)

# Matrix addition
added = temp_matrix + rainfall
print("\nTemperature + Rainfall:\n", added)

# Element-wise multiplication
multiplied = temp_matrix * rainfall
print("\nTemperature × Rainfall:\n", multiplied)
