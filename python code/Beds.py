import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
df = pd.read_csv("Data/Beds.csv")

# Filter Data
df = df[df['LOCATION'].isin(["GBR", "IRL"])]  # Missing closing parenthesis here
df = df[df['TIME'] == 2021]
df = df[df['SUBJECT'] == "TOT"]

# Create a bar plot with different colors for 'GBR' and 'IRL'
plt.figure(figsize=(8, 6))
sns.set(style="whitegrid", palette="muted")
ax = sns.barplot(x='LOCATION', y='Value', data=df, hue='LOCATION', ci="sd", capsize=0.2, errwidth=1.5)
plt.xlabel('Country')
plt.ylabel('Beds per 1000 inhabitants')
plt.title('Bed Data for GBR and IRL in 2021')

# Add data labels above the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height() + 0.1),
                ha='center', va='center', fontsize=12, color='black')

# Show the plot and save it as a PNG file
plt.ylim(0, 10)  # Adjust the Y-axis limit
plt.savefig('beds_hse_vs_nhs.png')
plt.show()
