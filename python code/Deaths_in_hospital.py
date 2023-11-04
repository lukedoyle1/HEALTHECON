import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the Excel file and sheet name (or index)
excel_file = "Data/Deaths per 100,00.xlsx"
sheet_name = 1  # 0-based index, 0 for the first sheet, 1 for the second sheet

# Import Data from the second sheet of the Excel file
df = pd.read_excel(excel_file, sheet_name, engine="openpyxl")

# Convert the 'UK' and 'IRL' columns to numeric, handling errors
df['UK'] = pd.to_numeric(df['UK'], errors='coerce')
df['IRL'] = pd.to_numeric(df['IRL'], errors='coerce')

# Calculate column averages after converting to numeric
UK_avg = df['UK'].mean()
IRL_avg = df['IRL'].mean()

# Create a bar plot with the same style
plt.figure(figsize=(8, 6))
sns.set(style="whitegrid", palette="muted")
ax = sns.barplot(x=['UK', 'IRL'], y=[UK_avg, IRL_avg], palette="muted" , ci="sd", capsize=0.2, errwidth=1.5)
plt.xlabel('Country')
plt.ylabel('Averages')
plt.title('Averages of UK and IRL in 2021')

# Add value labels above the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height() + 20),
                ha='center', va='center', fontsize=12, color='black')

plt.ylim(0, 250)  # Adjust the Y-axis limit
plt.savefig('UK_IRL_Deathsper100k_plot.png')