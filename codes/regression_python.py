#### Regression in Python

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import os 
import seaborn as sns


os.listdir("../Datasets")

# Importing dataset 
dt = pd.read_csv("../Datasets/ecommerce-customers.csv")

# Checking the data set 
dt.info()
print(dt.describe())

# Making the plots with Time on App and Yearly Amount Spent 

# ...existing code...
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(dt['Time on Website'], dt['Yearly Amount Spent'], marker='o', alpha=0.7)
ax.set_xlabel('Time on Website')
ax.set_ylabel('Yearly Amount Spent')
ax.set_title('Time on Website vs Yearly Amount Spent')
fig
# ...existing code...
fig, ax = plt.subplots(figsize=(8, 6))
sns.regplot(
    x="Time on Website",
    y="Yearly Amount Spent",
    data=dt,
    ax=ax,
    scatter_kws={"alpha": 0.7, "s": 40},
    line_kws={"color": "red"}
)
ax.set_xlabel("Time on Website")
ax.set_ylabel("Yearly Amount Spent")
ax.set_title("Time on Website vs Yearly Amount Spent (with linear fit)")
fig

# Checking the correlation 
print(
    np.corrcoef(dt['Time on Website'], dt['Yearly Amount Spent'])
)

# There isn't correlation with Time on Website and Yearly Amont Spent

#### Checking the spent and the Time on App
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(dt['Time on App'], dt['Yearly Amount Spent'], 
    marker='o', alpha=0.7, color = 'green')
ax.set_xlabel('Time on App')
ax.set_ylabel('Yearly Amount Spent')
ax.set_title('Time on App vs Yearly Amount Spent')
fig
fig, ax = plt.subplots(figsize=(8,6))
sns.regplot(
    x = "Time on App",
    y = "Yearly Amount Spent", 
    data = dt, 
    ax=ax,
    scatter_kws={"alpha": 0.7, "s": 40},
    line_kws={"color": "green"}
)
ax.set_xlabel("Time on App")
ax.set_ylabel("Yearly Amount Spent")
ax.set_title("Time on App vs Yearly Amount Spent (with linear fit)")
fig

# Checking the correlation 
np.corrcoef(dt['Time on App'], dt['Yearly Amount Spent'])

# ...existing code...
# Hexbin jointplot: Time on App vs Length of Membership
g = sns.jointplot(
    x="Time on App",
    y="Length of Membership",
    data=dt,
    kind="hex",
    height=8,
    color="blue",
    marginal_kws=dict(bins=30, fill=True)
)
g.suptitle("Time on App vs Length of Membership (hexbin)", y=1.02)
# ...existing code...

# Making the pairplot 
sns.pairplot(data=dt)

# Checking the correlation matrix 
numeric_dt = dt.select_dtypes(include='number')
corr = numeric_dt.corr()

# plot masked heatmap
fig, ax = plt.subplots(figsize=(10, 8))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    square=True,
    cbar_kws={"shrink": 0.8},
    ax=ax
)
ax.set_title("Correlation matrix (Pearson) — numeric columns")
fig

# return the correlation DataFrame
corr
# ...existing code...
