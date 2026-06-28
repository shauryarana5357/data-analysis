import matplotlib.pyplot as plt

# --- Task 7: Bar Chart and Pie Chart ---

languages = ['Python', 'Java', 'C++', 'JavaScript', 'R']
votes     = [45, 30, 25, 35, 15]
colors    = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#F44336']

# --- a) Horizontal Bar Chart ---
plt.figure(figsize=(8, 5))
plt.barh(languages, votes, color=colors)
plt.xlabel('Number of Votes')
plt.ylabel('Programming Language')
plt.title('Favorite Programming Languages (Survey)')
plt.tight_layout()
plt.savefig("task7_horizontal_bar.png", dpi=150)
plt.show()
print("Saved: task7_horizontal_bar.png")

# --- b & c) Pie Chart with exploded Python slice ---
explode = (0.1, 0, 0, 0, 0)   # explode Python slice

plt.figure(figsize=(7, 7))
plt.pie(votes,
        labels=languages,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',   # show percentages
        startangle=140,
        shadow=True)
plt.title('Programming Language Preference Distribution')
plt.tight_layout()
plt.savefig("task7_pie_chart.png", dpi=150)
plt.show()
print("Saved: task7_pie_chart.png")
