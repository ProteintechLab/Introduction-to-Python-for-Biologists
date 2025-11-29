# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the qPCR dataset
url = "https://raw.githubusercontent.com/ProteintechLab/Statistics/main/QPCR.csv"
qpcr = pd.read_csv(url)

# Define columns using variables
gene_cols = ["Gene1", "Gene2"]
housekeeper = "HouseKeepr" # typo in the original dataset

# Calculate delta CT values 
qpcr["Gene1dCT"] = qpcr[gene_cols[0]] - qpcr[housekeeper]
qpcr["Gene2dCT"] = qpcr[gene_cols[1]] - qpcr[housekeeper]

# Choose contral sample using row index 1
control_values = (qpcr.loc[1, "Gene1dCT"], qpcr.loc[1, "Gene2dCT"])

# Calculate delta delta CT = delta CT (sample) - delta CT (control)
qpcr["Gene1ddCT"] = qpcr["Gene1dCT"] - control_values[0]
qpcr["Gene2ddCT"] = qpcr["Gene2dCT"] - control_values[1]

# Calculate relative quantity RQ
qpcr["Gene1RQ"] = 2 ** (-qpcr["Gene1ddCT"])
qpcr["Gene2RQ"] = 2 ** (-qpcr["Gene2ddCT"])

# Creating dictionary of labels to use in the plot
labels = {"Gene1RQ": "Relative Quantity (RQ)", "Group":"Experimental Group"}

# Plot results
plt.figure(figsize = (8,6))

# Boxplot
sns.boxplot(data = qpcr, x = "Group", y = "Gene1RQ", palette= "pastel")

# Stripplot
sns.stripplot(data = qpcr, x= "Group", y = "Gene1RQ", color = "black", jitter = True)

plt.title("Relative Expression of " + gene_cols[0])
plt.xlabel(labels["Group"])
plt.ylabel(labels["Gene1RQ"])
plt.tight_layout()
plt.show()
