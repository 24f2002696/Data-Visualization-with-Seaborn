# Email: 24f2002696@ds.study.iitm.ac.in
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate data
np.random.seed(42)
n = 100

df = pd.DataFrame({
    'Purchase': np.random.randint(50, 500, n),
    'Visits': np.random.randint(1, 20, n),
    'Time': np.random.randint(5, 60, n),
    'Rating': np.random.uniform(1, 5, n),
    'Engagement': np.random.randint(10, 100, n)
})

# Create correlation heatmap
plt.figure(figsize=(512/64, 512/64), dpi=64)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', square=True, fmt='.2f')
plt.title('Customer Behavior Correlation')
plt.tight_layout()
plt.savefig('chart.png')
plt.close()