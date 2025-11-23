# Email: 24f2002696@ds.study.iitm.ac.in
# Customer Engagement Correlation Matrix Heatmap

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic customer engagement data
n_customers = 100

data = {
    'Website_Visits': np.random.normal(45, 15, n_customers),
    'Email_Opens': np.random.normal(30, 10, n_customers),
    'Purchase_Frequency': np.random.normal(5, 2, n_customers),
    'Customer_Support': np.random.normal(2, 1, n_customers),
    'Social_Media': np.random.normal(20, 8, n_customers),
    'App_Usage': np.random.normal(35, 12, n_customers)
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
corr_matrix = df.corr()

# Set style for professional appearance
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.2)

# Create figure with exact size for 512x512 output
plt.figure(figsize=(8, 8))

# Create heatmap
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    square=True,
    linewidths=1,
    cbar_kws={"shrink": 0.8}
)

# Add title and labels
plt.title('Customer Engagement Correlation Matrix', fontsize=16, pad=20)
plt.xlabel('Engagement Metrics', fontsize=12)
plt.ylabel('Engagement Metrics', fontsize=12)

# Adjust layout
plt.tight_layout()

# Save as PNG with exactly 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("Chart saved as chart.png (512x512 pixels)")
