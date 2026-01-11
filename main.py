import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

print("Loading data...")
try:
    df = pd.read_csv('customer.csv')
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)

print("Original Data Shape:", df.shape)
print("Missing values before cleaning:\n", df.isnull().sum())

if 'Work_Experience' in df.columns:
    df['Work_Experience'] = df['Work_Experience'].fillna(df['Work_Experience'].median())
if 'Family_Size' in df.columns:
    df['Family_Size'] = df['Family_Size'].fillna(df['Family_Size'].median())

df.dropna(subset=['Age', 'Spending_Score'], inplace=True)
print("Data Shape after cleaning:", df.shape)


print("\nFeature Engineering...")
spending_map = {'Low': 1, 'Average': 2, 'High': 3}
df['Spending_Score_Num'] = df['Spending_Score'].map(spending_map)

features = ['Age', 'Work_Experience', 'Family_Size', 'Spending_Score_Num']
X = df[features]


print("\nNormalizing features...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


print("\nDetermining optimal K (Elbow Method)...")
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.grid(True)
plt.savefig('elbow_plot.png')
print("Elbow plot saved as 'elbow_plot.png'")

optimal_k = 4
print(f"Applying K-Means with K={optimal_k}...")

kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)


print("\nVisualizing Clusters...")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Spending_Score_Num', hue='Cluster', palette='viridis', style='Cluster', s=100)
plt.title(f'Customer Segments (K={optimal_k})')
plt.xlabel('Age')
plt.yticks([1, 2, 3], ['Low', 'Average', 'High'])
plt.ylabel('Spending Score')
plt.legend(title='Cluster')
plt.savefig('cluster_plot.png')
print("Cluster plot saved as 'cluster_plot.png'")


print("\nCluster Insights:")
numeric_cols = ['Age', 'Work_Experience', 'Family_Size', 'Spending_Score_Num']
insights = df.groupby('Cluster')[numeric_cols].mean()
print(insights)

print("\nCluster Counts:")
print(df['Cluster'].value_counts())
