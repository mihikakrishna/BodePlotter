import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
df = pd.read_csv("./data.csv")

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Frequency vs Magnitude
ax1.semilogx(df['frequency'], df['magnitude_db'], marker='o', linestyle='-')
ax1.set_xlabel('Frequency (rad/s)')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title('Frequency vs Magnitude')
ax1.grid(True, which="both", ls="--")

# Frequency vs Phase
ax2.semilogx(df['frequency'], df['phase_degrees'], marker='o', linestyle='-', color='orange')
ax2.set_xlabel('Frequency (rad/s)')
ax2.set_ylabel('Phase (degrees)')
ax2.set_title('Frequency vs Phase')
ax2.grid(True, which="both", ls="--")

plt.tight_layout()
plt.show()
