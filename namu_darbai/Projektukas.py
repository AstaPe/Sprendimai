# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA  # Added for dimensionality reduction

# Data processing and ML tools
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
from scipy.cluster.hierarchy import dendrogram, linkage
from kneed import KneeLocator
from scipy.spatial.distance import pdist, squareform
from sklearn.neighbors import NearestNeighbors  # Added for DBSCAN tuning

# Filter warnings
import warnings

warnings.filterwarnings("ignore")

# Load and inspect data
df = pd.read_csv('C:/Users/astap/Downloads/Customer_Data.csv')
print("Dataset shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())

# Data preprocessing
if 'ID' in df.columns:
    df.drop('ID', axis=1, inplace=True)

# Handle missing values
numeric_cols = df.select_dtypes(include=np.number).columns
imputer = IterativeImputer(random_state=42)
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

# Remove duplicates
df = df.drop_duplicates()

plt.figure(figsize=(16, 14))  # Increased figure size
ax = sns.heatmap(
    df[numeric_cols].corr(),
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    annot_kws={"size": 10}  # Adjust annotation size
)
plt.title("Feature Correlation Matrix", fontsize=14)

# Rotate x-axis labels and set font size
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=15,  # 45-degree angle
    horizontalalignment='right',
    fontsize=10
)

# Rotate y-axis labels
ax.set_yticklabels(
    ax.get_yticklabels(),
    rotation=0,  # Horizontal
    fontsize=8
)

plt.tight_layout()  # Fix spacing
plt.show()

# Data standardization
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[numeric_cols])

# Create PCA reducer for visualization
pca = PCA(n_components=2)
data_2d = pca.fit_transform(scaled_data)


# Unified plotting function
def plot_clusters(data, labels, title, reducer=None):
    plt.figure(figsize=(8, 6))
    if reducer:
        data = reducer.fit_transform(data)
    sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=labels, palette='viridis', style=labels)
    plt.title(title)
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.show()


# K-Means implementation
def kmeans_analysis(data):
    # Elbow method
    inertias = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)

    # Optimal clusters
    kl = KneeLocator(range(1, 11), inertias, curve='convex', direction='decreasing')
    optimal_k = kl.elbow if kl.elbow else 3

    # Final clustering
    kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42, n_init=10)
    clusters = kmeans.fit_predict(data)

    # Visualization
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, 11), inertias, 'bo-')
    plt.axvline(optimal_k, color='r', linestyle='--')
    plt.title("Elbow Method")

    plt.subplot(1, 2, 2)
    plot_clusters(data, clusters, "K-Means Clusters", pca)

    return clusters, optimal_k


kmeans_clusters, k = kmeans_analysis(scaled_data)


# Agglomerative Clustering
def hierarchical_analysis(data):
    # Dendrogram
    plt.figure(figsize=(15, 7))
    linkage_matrix = linkage(data, 'ward')
    dendrogram(linkage_matrix)
    plt.title("Dendrogram")
    plt.xlabel("Data Points")
    plt.ylabel("Distance")
    plt.show()

    # Auto-determine clusters from dendrogram
    last_merges = linkage_matrix[-10:, 2]
    acceleration = np.diff(last_merges, 2)
    optimal_k = acceleration.argmax() + 2  # Add 2 because of diff and 0-index

    # Clustering
    agg = AgglomerativeClustering(n_clusters=optimal_k)
    clusters = agg.fit_predict(data)

    # Visualization
    plot_clusters(data, clusters, "Agglomerative Clustering", pca)

    return clusters


agg_clusters = hierarchical_analysis(scaled_data)


# DBSCAN Implementation
def dbscan_analysis(data):
    # Parameter tuning using k-distance
    nn = NearestNeighbors(n_neighbors=5)
    nn.fit(data)
    distances, _ = nn.kneighbors(data)
    distances = np.sort(distances[:, -1])

    # Find optimal eps
    kl = KneeLocator(np.arange(len(distances)), distances, curve='convex', direction='increasing')
    eps = distances[kl.elbow] if kl.elbow else 0.3

    # DBSCAN with optimized parameters
    dbscan = DBSCAN(eps=eps, min_samples=10)
    clusters = dbscan.fit_predict(data)

    # Handle noise points
    unique_clusters = np.unique(clusters)
    if -1 in unique_clusters:
        print(f"DBSCAN identified {sum(clusters == -1)} noise points")

    # Visualization
    plot_clusters(data, clusters, "DBSCAN Clustering", pca)

    return clusters


dbscan_clusters = dbscan_analysis(scaled_data)


# Evaluation metrics (optimized)
def evaluate_clustering(data, clusters, algorithm):
    unique_clusters = np.unique(clusters)
    if len(unique_clusters) < 2:
        return None

    metrics = {
        'Silhouette': silhouette_score(data, clusters),
        'Davies-Bouldin': davies_bouldin_score(data, clusters),
    }

    # Optimized Dunn Index calculation
    try:
        if data.shape[1] > 2:
            sample_data = data[np.random.choice(data.shape[0], 1000, replace=False)]  # Subsample
        else:
            sample_data = data

        dist_matrix = squareform(pdist(sample_data))
        cluster_labels = clusters[
            np.random.choice(clusters.size, 1000, replace=False)] if clusters.size > 1000 else clusters

        inter_cluster = []
        intra_cluster = []

        for cluster in unique_clusters:
            mask = cluster_labels == cluster
            if sum(mask) > 1:
                intra = np.max(dist_matrix[mask][:, mask])
                intra_cluster.append(intra)

                other_clusters = [c for c in unique_clusters if c != cluster]
                min_inter = min(np.min(dist_matrix[mask][:, cluster_labels == oc]) for oc in other_clusters)
                inter_cluster.append(min_inter)

        if inter_cluster and intra_cluster:
            metrics['Dunn'] = np.min(inter_cluster) / np.max(intra_cluster)
        else:
            metrics['Dunn'] = np.nan
    except Exception as e:
        print(f"Dunn Index error: {str(e)}")
        metrics['Dunn'] = np.nan

    return pd.DataFrame(metrics, index=[algorithm])


# Compare all methods
results = []
for clusters, name in zip([kmeans_clusters, agg_clusters, dbscan_clusters],
                          ['K-Means', 'Agglomerative', 'DBSCAN']):
    evaluation = evaluate_clustering(scaled_data, clusters, name)
    if evaluation is not None:
        results.append(evaluation)

if results:
    print("\nClustering Performance Comparison:")
    print(pd.concat(results))

# Enhanced analysis
analysis = """
DBSCAN performs the best in terms of Silhouette and Dunn Index.
Agglomerative and K-Means perform similarly with regard to Davies-Bouldin, but DBSCAN shows less separation between clusters.
"""
print(analysis)