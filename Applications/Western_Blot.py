# Load the data
import pandas as pd
url = "https://raw.githubusercontent.com/ProteintechLab/Statistics/main/blot_quant.csv"
df = pd.read_csv(url)

# Pivot the data
blot_quant = df.pivot(index=['Area', 'Group',], columns = 'Wavelength', values= 'Intensity').reset_index()
blot_quant.columns.name = None
blot_quant.columns = ['Area', 'Group', 'W700', 'W800']

# Calculate the normalised ratio
blot_quant['norm_ratio'] = blot_quant['W800'] / blot_quant['W700']

# Summary statistics
blotmean = blot_quant.groupby("Group").agg(
    mean_ratio = ("norm_ratio", "mean"), 
    sd_ratio = ("norm_ratio", "std")
).reset_index()

# T Test between Groups
from scipy import stats

group1 = blot_quant[blot_quant['Group'] == 1]['norm_ratio']
group2 = blot_quant[blot_quant['Group'] == 2]['norm_ratio']
test_result = stats.ttest_ind(group1, group2)
print(f"T-test p-value: {test_result.pvalue:.5f}")

# Display results
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.figure(figsize=(6,5))

sns.barplot(
    data = blotmean, 
    x = "Group", 
    y = "mean_ratio", 
    palette = ['#66b3ff', '#cce6ff'], 
    edgecolor = "black", 
    errcolor = "black", 
    capsize=.1
)

# Manually adding error bars using the standard deviation
plt.errorbar(
    x = range(len(blotmean)), 
    y = blotmean['mean_ratio'],
    yerr = blotmean['sd_ratio'],
    fmt = 'none', 
    c = 'black', 
    capsize=5
)

plt.ylim(0,1)
plt.title("Western Blot Normalised Ratio by Group")
plt.ylabel("W800 / W700 Ratio")
plt.tight_layout()
plt.show()
