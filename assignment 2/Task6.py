import matplotlib.pyplot as plt

# --- Task 6: Line Graph Implementation ---

months      = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [15, 18, 22, 28, 35, 42]

plt.figure(figsize=(8, 5))

# a) Line graph with red color, circle markers, dashed style
plt.plot(months, temperature,
         color='red',
         marker='o',
         linestyle='--',
         linewidth=2,
         markersize=8,
         label='Temperature (°C)')

# b) Axis labels and title
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Readings (Jan–Jun)')

# d) Grid and y-axis limits
plt.grid(True)
plt.ylim(0, 50)

# e) Legend
plt.legend()

plt.tight_layout()
plt.savefig("task6_line_graph.png", dpi=150)
plt.show()
print("Saved: task6_line_graph.png")
