# Load libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load excel file
file = "https://raw.githubusercontent.com/ProteintechLab/Statistics/main/TNF%20ELISA.xlsx"
xls = pd.ExcelFile(file)

# Read standards and metadata
standard_meta = pd.read_excel(xls, sheet_name = 0, usecols="A:B", nrows = 9)
standard_vals = pd.read_excel(xls, sheet_name=0, usecols= "A:C", nrows = 9)

# Cleaning up column names
standard_meta.columns = ["Row", "Conc"]
standard_vals.columns = ["Row", "rep1", "rep2"]

# Merge OD values with known concentrations
standards = pd.merge(standard_meta, standard_vals, on="Row")

# Calculate OD from replicates
standards["MeanOD"] = standards[["rep1", "rep2"]].mean(axis=1)
print(standards)

# Plot standard curve
plt.figure(figsize=(8,5))
sns.scatterplot(data=standards, x = "Conc", y = "MeanOD", s = 100, color = "darkblue")

sns.regplot(data = standards, x = "Conc", y = "MeanOD", scatter = False, ci = None, color = "Red")

plt.title("ELISA Standard Curve")
plt.xlabel("Concentration (pg/mL")
plt.ylabel("Mean Absorbance (OD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("elisa_standard_curve.png", dpi = 600)
plt.show()

# Fit a linear model 

from sklearn.linear_model import LinearRegression
import numpy as np

# Set up input X = OD and output Y = concentration
X = standards["MeanOD"].values.reshape(-1,1)
y = standards["Conc"].values

# Train the regression model to find the best fit line
model = LinearRegression()
model.fit(X, y)

# Extract the slope and intercept from the model
slope = model.coef_[0]
intercept = model.intercept_

print(f"Standard Curve Equation: Concentration = {slope:.5f} * OD + {intercept:.5f}")

